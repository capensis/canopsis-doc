# -*- coding: utf-8 -*-

from urlparse import urlparse
import pygit2
import json


class Settings(object):
    class fields:
        giturl = 'git.url'
        gituser = 'git.user'
        gitpass = 'git.pass'

        target_folder = 'target.folder'
        target_git = 'target.git'
        target_branch = 'target.branch'
        target_push = 'target.push'

        global_index = 'index.global'
        namespace_index = 'index.namespace'

        sphinx_theme = 'sphinx.theme'
        sphinx_project = 'sphinx.project'
        sphinx_author = 'sphinx.author'
        sphinx_email = 'sphinx.email'
        sphinx_version = 'sphinx.version'
        sphinx_release = 'sphinx.release'

        repositories = 'repositories'
        repo = 'repo'
        branch = 'branch'
        docdir = 'docdir'

    class defaults:
        giturl = 'https://github.com/'

        target_folder = 'public'
        target_branch = 'master'
        target_push = False

        sphinx_theme = 'sphinx_rtd_theme'

        branch = 'master'
        docdir = 'doc'

    def __init__(self, confpath, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)

        with open(confpath) as f:
            self.config = json.load(f)

    def _get_field(self, fieldname):
        root = self.config
        fields = fieldname.split('.')

        if hasattr(Settings.defaults, fieldname):
            default = getattr(Settings.defaults, fieldname)

        else:
            default = None

        n = len(fields)
        for i in range(n):
            if i < (n - 1):
                root = root.get(fields[i], {})

            else:
                root = root.get(fields[i], default)

        return root

    @property
    def giturl(self):
        return self._get_field(Settings.fields.giturl)

    @property
    def gituser(self):
        return self._get_field(Settings.fields.gituser)

    @property
    def gitpass(self):
        return self._get_field(Settings.fields.gitpass)

    @property
    def target_folder(self):
        return self._get_field(Settings.fields.target_folder)

    @property
    def target_git(self):
        return self._get_field(Settings.fields.target_git)

    @property
    def target_branch(self):
        return self._get_field(Settings.fields.target_branch)

    @property
    def target_push(self):
        return self._get_field(Settings.fields.target_push)

    @property
    def global_index(self):
        return self._get_field(Settings.fields.global_index)

    @property
    def namespace_index(self):
        return self._get_field(Settings.fields.namespace_index)

    @property
    def sphinx_theme(self):
        return self._get_field(Settings.fields.sphinx_theme)

    @property
    def sphinx_project(self):
        return self._get_field(Settings.fields.sphinx_project)

    @property
    def sphinx_author(self):
        return self._get_field(Settings.fields.sphinx_author)

    @property
    def sphinx_email(self):
        return self._get_field(Settings.fields.sphinx_email)

    @property
    def sphinx_version(self):
        return self._get_field(Settings.fields.sphinx_version)

    @property
    def sphinx_release(self):
        return self._get_field(Settings.fields.sphinx_release)

    def namespaces(self):
        repofield = Settings.fields.repositories

        for namespace in self._get_field(repofield):
            yield namespace

    def repositories(self, namespace):
        repofield = Settings.fields.repositories

        for repo in self._get_field(repofield).get(namespace):
            yield repo

    def get_git_creds(self):
        url = urlparse(self.giturl)

        if url.scheme in ['http', 'https']:
            creds = pygit2.UserPass(
                self.gituser,
                self.gitpass
            )

        else:
            creds = pygit2.KeypairFromAgent(self.gituser)

        return creds
