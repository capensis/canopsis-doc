# -*- coding: utf-8 -*-

from cpsdocgen import Settings

from ConfigParser import ConfigParser
from StringIO import StringIO

import os

import pygit2

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
            self.settings.target_folder,
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
        credentials = self.settings.get_git_creds()
        callbacks = pygit2.RemoteCallbacks(credentials=credentials)

        if not os.path.exists(self.repodest):
            print('---- Clone repository')

            # Create and init repository
            os.makedirs(self.repodest)

            # git init
            repo = pygit2.init_repository(
                self.repodest
            )

            # git remote add origin <self.repourl>
            remote = repo.create_remote('origin', self.repourl)

            print('---- Fetch from remote')
            remote.fetch(callbacks=callbacks)

            # git branch master --set-upstream=origin/master
            repo.create_reference(
                'refs/heads/master',
                repo.lookup_reference('refs/remotes/origin/master').target
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

            print('---- Fetch from remote')
            remote.fetch(callbacks=callbacks)

        # prepare merge
        rrefname = 'refs/remotes/origin/{0}'.format(self.branch)
        rref = repo.lookup_reference(rrefname)
        trefname = 'refs/heads/{0}'.format(self.branch)

        try:
            tref = repo.lookup_reference(trefname)

        except KeyError:
            tref = repo.create_reference(
                trefname,
                repo.lookup_reference(rrefname).target
            )

        repo.set_head(tref.target)
        repo.head.set_target(rref.target)

        # git checkout HEAD
        repo.checkout_head()

        return repo.workdir
