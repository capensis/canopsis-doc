# -*- coding: utf-8 -*-

from os import chdir, makedirs, remove, rename
from os.path import isdir, isfile, exists, basename
from json import load
from glob import glob
from subprocess import Popen, PIPE
from shutil import rmtree, move, copy

CONF_FILE = '/opt/canopsis/doc_builder.json'

# constants are json-parsed from CONF_FILE
SPHINX_INDEX = {}
AUTO_LIBS = {}
HTML_INDEX_TITLE = ''
VERSIONS = {}
AUTODOC_DIRECTORY = ''
CONNECTORS = {}
LOG_FILE = ''


class DocBuilder:
    """Contains imperative style methods to build documentation"""

    def __init__(self):
        # Remove previous log in case of rebuilding
        if isfile(LOG_FILE):
            remove(LOG_FILE)

        # Make sure we do not overwrite something
        if exists('doc'):
            self.log(
                'A directory named \'doc\' already exists : aborting procedure')
            quit()
        else:
            self.log('Creating directory \'doc\'')
            makedirs('doc')
            chdir('doc')

    def sphinx_index(self):
        """Get core documentation and remove parts we don't need"""

        self.git_sc(
            SPHINX_INDEX['dir'],
            SPHINX_INDEX['branch'],
            SPHINX_INDEX['repo']
            )
        self.mvrm(SPHINX_INDEX['dir'], '.')
        remove('doc_builder.py')
        remove('doc_builder.json')

    def generate_html_index(self):
        """Insert category titles in the pre-existing html index page"""

        with open('index.html', 'r+') as root_index:
            with open('new_index.html', 'w') as new_index:
                for line in root_index:
                    # We write index in new_index...
                    new_index.write(line)
                    if 'toctree-l1 current' in line:  # ...and insert titles
                        for version in VERSIONS:
                            version_name = version['dir'].replace('doc/', '')
                            new_index.write(HTML_INDEX_TITLE.format(
                                version_name,
                                version_name.capitalize()
                                )
                            )
                        if CONNECTORS:
                            new_index.write(HTML_INDEX_TITLE.format(
                                'connectors',
                                'Connectors'
                                )
                            )
        rename('new_index.html', 'index.html')

    def autodoc(self):
        """Generate rst `hooks` for docstrings in *_AUTODOC dirs"""

        for auto_lib in AUTO_LIBS:
            # Autodocumentation is stored in a temp directory
            # /version/_AUTODOC. Since it is possible to have multiple
            # versions of canopsis to autodocument, we check if the
            # version already has its directory.
            if not isdir(auto_lib['version'] + '_AUTODOC'):
                makedirs(auto_lib['version'] + '_AUTODOC')

            self.git_sc(
                auto_lib['sources'],
                auto_lib['branch'],
                auto_lib['repo']
                )

            for project in glob(auto_lib['packages']):
                if isdir(project):  # ignore isolated files
                    print project
                    self.sphinx_apidoc(
                        project,
                        '{0}_AUTODOC'.format(auto_lib['version'])
                        )
            # we don't need sources anymore
            rmtree(auto_lib['sources'].split('/')[-1])

    def autodoc_index(self):
        """Generate indexes paths for each _AUTODOC dir"""

        for autolib_dir in [d for d in glob('*') if d[-8:] == '_AUTODOC']:
            chdir(autolib_dir)
            auto_index = ('API\n'
                          '===\n\n'
                          '.. toctree::\n'
                          '   :maxdepth: 1\n'
                          '   :titlesonly:\n\n'
                          )

            for rst in glob('*.rst'):  # rst files are in subdirectories
                # modules.rst and canopsis.rst are heavy to read
                if basename(rst) in ['modules.rst', 'canopsis.rst']:
                    remove(rst)
                else:
                    auto_index += '   {0}\n'.format(rst.replace('.rst', ''))
            with open('index.rst', 'w') as index_rst:
                index_rst.write(auto_index)
            chdir('..')

    def make_versions(self):
        """Download, insert autodoc, sphinx-build and rm sources"""

        for version in VERSIONS:
            self.git_sc(
                version['dir'],
                version['branch'],
                version['repo']
                )

            final_directory = version['dir'].split('/')[-1]
            autodoc_tmp_dir = final_directory + '_AUTODOC'
            autodoc_dest_dir = final_directory + AUTODOC_DIRECTORY
            if isdir(autodoc_tmp_dir):
                copy(autodoc_tmp_dir + '/index.rst', autodoc_dest_dir)
                remove(autodoc_tmp_dir + '/index.rst')
                self.mvrm(
                    autodoc_tmp_dir,
                    autodoc_dest_dir
                )

            self.sphinx_build(final_directory)
            # Just extract output from _build and rm sources
            self.mvrmbuild(final_directory)

    def connectors(self):
        """
        Download each connector, format files out of it and build.
        All connectors are one single sphinx-project.
        """

        chdir('connectors')
        connector_index_list = ''  # string to append to the index
        for connector in CONNECTORS:
            self.git_sc(
                connector['dir'],
                connector['branch'],
                connector['repo']
                )

            for rst in glob('doc/*.rst'):
                index_entry = rst[4:-4]  # doc/connector.rst --> connector
                connector_index_list += '   {0}\n'.format(index_entry)
                move(rst, '.')  # mv doc/connector.rst connector.rst

            # images must be in that dir (or will be ignored)
            if exists('doc/img'):
                self.mvrm('doc/img', '_static/images')
            rmtree('doc')  # cleaning

        with open('index.rst', 'a') as connector_index:
            connector_index.write(connector_index_list)

        self.sphinx_build('.')
        self.mvrmbuild('.')  # extract build output and rm sources

        chdir('..')

    def finish(self):
        """Just to say bye"""

        self.log('Process completed')
        self.log('Documentation is available in \'doc\'')

    def log(self, event):
        """Prints an event and records a string in a logfile"""

        with open(LOG_FILE, 'a') as log_file:
            log_file.write(event)
        print(event)

    def cmd(self, *args):
        """Execute a shell command"""

        p = Popen(args, stdout=PIPE)
        return p.communicate()[0]

    def mvrm(self, source, destination):
        """
        Recurent operation in the process. Equivalent to :
        mv sources/* destination && rm -r sources
        """

        for path in glob(source + '/*'):
            move(path, destination)
        rmtree(source)

    def mvrmbuild(self, source):
        """
        Similar to mvrm to extract built doc to the parent dir.
        mv source/_build/* . && rm -r source
        """

        for element in glob(source + '/*'):
            if element != source + '/_build':
                if isdir(element):
                    rmtree(element)
                else:
                    remove(element)
        self.mvrm(source + '/_build', source)

    def git_sc(self, directory, branch, repo):
        """Download a git subdirectory with sparse checkout option"""

        message_str = 'Downloading directory {0} from branch {1} (repo : {2})'
        message = message_str.format(
            directory,
            branch,
            repo
            )
        self.log(message)

        # Sparse checkout `directory` will checkout `directory`/subtree
        # and tree/`directory`/subtree. We create a tmp dir to store
        # what we don't want in an rmtree later.
        makedirs('git_tmp')
        chdir('git_tmp')

        self.cmd('git', 'init')
        self.cmd('git', 'config', 'core.sparsecheckout', 'true')
        with open('.git/info/sparse-checkout', 'w') as sparse_checkout:
            sparse_checkout.write(directory)
        self.cmd('git', 'remote', 'add', '-f', 'origin',
                        'https://github.com/capensis/{0}.git'.format(repo))
        self.cmd('git', 'pull', 'origin', branch)

        # mv my/dir/lastdir lastdir
        final_directory = '../' + directory.split('/')[-1]
        move(directory, final_directory)

        chdir('..')
        rmtree('git_tmp')

    def sphinx_build(self, source_path):
        """sphinx-build -b html source_path source_path/_build"""

        build_path = '{0}/_build'.format(source_path)
        self.log(
            self.cmd('sphinx-build', '-b', 'html', source_path, build_path))

    def sphinx_apidoc(self, source_path, doc_path):
        """sphinx-apidoc command"""

        if not isdir(source_path):
            makedirs(doc_path)
        return self.cmd('sphinx-apidoc', '-o', doc_path, source_path)


def load_conf():
    """Loads configuration from CONF_FILE (json)"""

    with open(CONF_FILE) as conf_file:
        conf = load(conf_file)

    global SPHINX_INDEX
    SPHINX_INDEX = conf['sphinx_index']
    global HTML_INDEX_TITLE
    HTML_INDEX_TITLE = conf['html_index_titles']
    global VERSIONS
    VERSIONS = conf['versions']
    global AUTO_LIBS
    AUTO_LIBS = conf['auto_libs']
    global AUTODOC_DIRECTORY
    AUTODOC_DIRECTORY = conf['autodoc_directory']
    global CONNECTORS
    CONNECTORS = conf['connectors']
    global LOG_FILE
    LOG_FILE = conf['log_file']


if __name__ == '__main__':
    load_conf()
    doc_builder = DocBuilder()

    doc_builder.sphinx_index()
    doc_builder.generate_html_index()
    if AUTO_LIBS:
        doc_builder.autodoc()
        doc_builder.autodoc_index()
    doc_builder.make_versions()
    if CONNECTORS:
        doc_builder.connectors()
    else:
        rmtree('connectors')
    doc_builder.finish()
