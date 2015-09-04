# -*- coding: utf-8 -*-

from cpsdocgen import Settings
from cpsdocgen import Extractor, Fetch, Push
from cpsdocgen import Templater, SphinxGenerator
from argparse import ArgumentParser

import os


class Application(object):
    def __init__(self, argv, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        parser = ArgumentParser(description='Canopsis Documentation Generator')
        parser.add_argument(
            '-c', '--config',
            nargs=1,
            help='Path to configuration'
        )
        argmap = parser.parse_args(argv)

        if argmap.config:
            confpath = os.path.expanduser(argmap.config[0])

        else:
            confpath = '~/.cpsdocgen.conf'

        self.settings = Settings(confpath)

    def iter_repos(self):
        paths = []

        for namespace in self.settings.namespaces():
            for repo in self.settings.repositories(namespace):
                print('-- Fetch {0}/{1}'.format(
                    namespace,
                    repo[Settings.fields.repo]
                ))

                fetcher = Fetch(self.settings, namespace, repo)
                workdir = fetcher.init_repo()
                paths.append((namespace, repo, workdir))

        return paths

    def iter_paths(self, paths):
        for namespace, repo, path in paths:
            print('-- Extract {0}/{1}'.format(
                namespace,
                repo[Settings.fields.repo]
            ))

            extract = Extractor(self.settings, namespace, repo, path)
            extract.move_files()

    def render_templates(self):
        templater = Templater(self.settings)
        templater.genindex()
        templater.iter_namespaces()

    def __call__(self):
        with SphinxGenerator(self.settings):
            paths = self.iter_repos()
            self.iter_paths(paths)
            self.render_templates()

        if self.settings.target_push:
            push = Push(self.settings)
            repo = push.init_repo()
            commit = push.init_commit(repo)
            push.push_commit(repo, commit)
