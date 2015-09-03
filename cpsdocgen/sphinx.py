# -*- coding: utf-8 -*-

import subprocess
import os


class SphinxGenerator(object):
    def __init__(self, settings, *args, **kwargs):
        super(SphinxGenerator, self).__init__(*args, **kwargs)

        self.settings = settings

        self.docdir = os.path.join(
            os.getcwd(),
            self.settings.target,
            'doc'
        )

        self.preparecmd = [
            'sphinx-quickstart',
            '-q',
            '-p', self.settings.sphinx_project,
            '-a', self.settings.sphinx_author,
            '-v', self.settings.sphinx_version,
            '-r', self.settings.sphinx_release,
            '--suffix=.rst',
            '--master=index',
            '--makefile',
            self.docdir
        ]

    def __enter__(self):
        print('-- Prepare Sphinx project')
        with open('/dev/null', 'w') as null:
            subprocess.check_call(self.preparecmd, stdout=null, stderr=null)

    def __exit__(self, *args, **kwargs):
        print('-- Update Sphinx configuration (not yet implemented)')
        path = os.path.join(self.docdir, 'conf.py')

