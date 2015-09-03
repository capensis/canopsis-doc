# -*- coding: utf-8 -*-

import json


class Settings(object):
    class fields:
        giturl = 'git.url'
        gituser = 'git.user'
        gitpass = 'git.pass'

        target = 'target'
        global_index = 'index.global'
        namespace_index = 'index.namespace'

        sphinx_theme = 'sphinx.theme'
        sphinx_project = 'sphinx.project'
        sphinx_author = 'sphinx.author'
        sphinx_version = 'sphinx.version'
        sphinx_release = 'sphinx.release'

        repositories = 'repositories'
        repo = 'repo'
        branch = 'branch'
        docdir = 'docdir'

    class defaults:
        giturl = 'https://github.com/'

        target = 'public'

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
    def target(self):
        return self._get_field(Settings.fields.target)

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
