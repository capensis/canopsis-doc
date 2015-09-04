# -*- coding: utf-8 -*-

from datetime import datetime
from shutil import copyfile
import pygit2
import os


class Push(object):
    deleted = (
        pygit2.GIT_STATUS_INDEX_DELETED,
        pygit2.GIT_STATUS_WT_DELETED
    )

    added = (
        pygit2.GIT_STATUS_INDEX_MODIFIED,
        pygit2.GIT_STATUS_INDEX_NEW,
        pygit2.GIT_STATUS_WT_MODIFIED,
        pygit2.GIT_STATUS_WT_NEW
    )

    def __init__(self, settings, *args, **kwargs):
        super(Push, self).__init__(*args, **kwargs)

        self.settings = settings

        self.workdir = os.path.join(
            self.settings.target_folder,
            'workdir'
        )

        self.docdir = os.path.join(
            self.settings.target_folder,
            'doc'
        )

    @property
    def repourl(self):
        return '/'.join([
            self.settings.giturl,
            self.settings.target_git
        ])

    def init_repo(self):
        if not os.path.exists(self.workdir):
            print('---- Clone target repository')

            os.makedirs(self.workdir)

            # git init
            repo = pygit2.init_repository(self.workdir)

            # git remote add origin <self.repourl>
            remote = repo.create_remote('origin', self.repourl)
            remote.add_push('+refs/heads/*:refs/remotes/origin/*')

            # git fetch
            remote.credentials = pygit2.UserPass(
                self.settings.gituser,
                self.settings.gitpass
            )

            remote.fetch()

            for branch in ['master', self.settings.target_branch]:
                # git branch <branch> --set-upstream=origin/<branch>
                repo.create_reference(
                    'refs/heads/{0}'.format(branch),
                    repo.lookup_reference(
                        'refs/remotes/origin/{0}'.format(branch)
                    ).target
                )

            # git merge / git checkout HEAD
            rrefname = 'refs/remotes/origin/{0}'.format(
                self.settings.target_branch
            )
            rref = repo.lookup_reference(rrefname)

            repo.head.set_target(rref.target)
            repo.checkout_head()

        else:
            repo = pygit2.init_repository(self.workdir)
            remote = repo.remotes[0]
            remote.add_push('+refs/heads/*:refs/remotes/origin/*')

        return repo

    def init_commit(self, repo):
        # copy documentation to workdir
        abspath = os.path.abspath(self.docdir)
        nskip = len(abspath.split(os.sep))

        for root, dirs, names in os.walk(abspath):
            for fname in names:
                parts = root.split(os.sep)[nskip:] or ['']

                localdir = os.path.join(*parts)
                src = os.path.join(self.docdir, localdir, fname)
                dest = os.path.join(self.workdir, localdir)

                if not os.path.exists(dest):
                    os.makedirs(dest)

                dest = os.path.join(dest, fname)

                copyfile(src, dest)

        # make sure the .git/index file is updated in memory
        repo.index.read()

        # git status
        status = repo.status()

        for fname, flags in status.items():
            # git rm
            if flags in Push.deleted:
                del repo.index[fname]

            # git add
            elif flags in Push.added:
                repo.index.add(fname)

        # Build commit object
        treeid = repo.index.write_tree()

        author = pygit2.Signature(
            self.settings.sphinx_author,
            self.settings.sphinx_email
        )
        committer = author

        refname = 'refs/heads/{0}'.format(self.settings.target_branch)

        try:
            parents = [repo.lookup_reference(refname).target]

        except pygit2.GitError:
            parents = []

        commit = repo.create_commit(
            refname, author, committer,
            'Documentation update {0}'.format(
                str(datetime.now())
            ),
            treeid,
            parents
        )

        # Write changes to .git/index and reload it
        repo.index.write()
        repo.index.read()

        # return object
        return repo[commit]

    def push_commit(self, repo, commit):
        remote = repo.remotes[0]
        remote.credentials = pygit2.UserPass(
            self.settings.gituser,
            self.settings.gitpass
        )

        remote.push([
            'refs/heads/{0}'.format(self.settings.target_branch)
        ])
