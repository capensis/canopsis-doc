# -*- coding: utf-8 -*-

from cpsdocgen import Settings
from redbaron import RedBaron
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
        print('-- Update Sphinx configuration')
        path = os.path.join(self.docdir, 'conf.py')

        with open(path) as f:
            red = RedBaron(f.read())

        self.add_path(red, 'html_theme_path', '_themes')
        self.add_path(red, 'html_static_path', '_static')

        themenode = red.find(
            'assignment',
            target=lambda node: node.value == 'html_theme'
        )

        themenode.value.replace('"{0}"'.format(self.settings.sphinx_theme))

        with open(path, 'w') as f:
            f.write(red.dumps())

    def add_path(self, red, var, basepath):
        pathlistnode = red.find(
            'assignment',
            target=lambda node: node.value == var
        )

        if pathlistnode is None:
            red.append('{0} = []'.format(var))

            pathlistnode = red.find(
                'assignment',
                target=lambda node: node.value == var
            )

        for namespace in self.settings.namespaces():
            for repository in self.settings.repositories(namespace):
                path = os.path.join(
                    namespace, repository[Settings.fields.repo],
                    basepath
                )

                indocpath = os.path.join(self.settings.target, 'doc', path)

                if os.path.exists(indocpath):
                    newval = "'{0}'".format(path)

                    if pathlistnode.value.find('string', value=newval) is None:
                        pathlistnode.value.append(newval)
