# -*- coding: utf-8 -*-'

from cpsdocgen import Settings
from shutil import copyfile
import os


class Extractor(object):
    def __init__(self, settings, namespace, repo, path, *args, **kwargs):
        super(Extractor, self).__init__(*args, **kwargs)

        self.settings = settings
        self.namespace = namespace
        self.repository = repo

        self.docpath = os.path.join(path, repo[Settings.fields.docdir])
        staticpath = os.path.join(self.docpath, '_static')
        themespath = os.path.join(self.docpath, '_themes')

        self.docs = [
            (
                root.split(self.docpath)[1].lstrip('/'),
                filename.lstrip('/')
            )
            for root, dirnames, filenames in os.walk(self.docpath)
            for filename in filenames
            if filename.endswith('.rst')
            or root.startswith(staticpath)
            or root.startswith(themespath)
        ]

    @property
    def targetdir(self):
        return os.path.join(
            self.settings.target_folder,
            'doc'
        )

    def move_files(self):
        for root, filename in self.docs:
            srcpath = os.path.join(self.docpath, root, filename)
            dstpath = os.path.join(
                self.targetdir,
                self.namespace,
                self.repository[Settings.fields.repo],
                root,
                filename
            )

            dirname = os.path.dirname(dstpath)

            if not os.path.exists(dirname):
                os.makedirs(dirname)

            copyfile(srcpath, dstpath)
