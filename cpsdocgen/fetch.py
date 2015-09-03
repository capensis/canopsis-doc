# -*- coding: utf-8 -*-

from cpsdocgen import Settings

from ConfigParser import ConfigParser
from StringIO import StringIO
import pygit2
import os


class Fetch(object):
    def __init__(self, settings, namespace, repository, *args, **kwargs):
        super(Fetch, self).__init__(*args, **kwargs)

        self.settings = settings
        self.namespace = namespace
        self.repo = repository

    @property
    def repourl(self):
        return '/'.join([
            self.settings.giturl,
            self.namespace,
            '{0}.git'.format(self.repo[Settings.fields.repo])
        ])

    @property
    def repodest(self):
        return os.path.join(
            os.getcwd(),
            self.settings.target,
            'git',
            self.namespace,
            self.repo[Settings.fields.repo]
        )

    @property
    def branch(self):
        return self.repo.get(
            Settings.fields.branch,
            Settings.defaults.branch
        )

    def init_repo(self):
        # initialize repository
        if not os.path.exists(self.repodest):
            print('---- Clone repository')

            # Create and init repository
            os.makedirs(self.repodest)

            repo = pygit2.init_repository(
                self.repodest
            )

            remote = repo.create_remote('origin', self.repourl)

            repo.create_reference(
                'refs/heads/master',
                'refs/remotes/origin/master'
            )

            # edit .git/config to avoid cloning the whole data
            gitconfig = os.path.join(repo.path, 'config')

            with open(gitconfig) as f:
                content = f.readlines()

            bytestr = StringIO(''.join([l.lstrip() for l in content]))

            parser = ConfigParser()
            parser.readfp(bytestr)

            edit = False
            if not parser.has_option('core', 'depth'):
                edit = True

            elif parser.getint('core', 'depth') != 1:
                edit = True

            if edit:
                parser.set('core', 'depth', 1)

                with open(gitconfig, 'w') as f:
                    parser.write(f)

        else:
            print('---- Pull repository')

            # open already existing repository
            repo = pygit2.init_repository(
                self.repodest
            )

            remote = repo.remotes[0]

        # Fetch data from remote
        print('---- Fetch from remote')

        remote.credentials = pygit2.UserPass(
            self.settings.gituser,
            self.settings.gitpass
        )
        remote.fetch()

        rrefname = 'refs/remotes/origin/{0}'.format(self.branch)
        rref = repo.lookup_reference(rrefname)
        trefname = 'refs/heads/{0}'.format(self.branch)

        try:
            repo.lookup_reference(trefname)

        except KeyError:
            repo.create_reference(trefname, rrefname)

        repo.head.set_target(rref.target)

        # Checkout working directory
        repo.checkout_head()

        return repo.workdir
