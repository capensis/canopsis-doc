# -*- coding: utf-8 -*-

from jinja2 import Template
import os


class Templater(object):
    def __init__(self, settings, *args, **kwargs):
        super(Templater, self).__init__(*args, **kwargs)

        self.settings = settings

    def _tmpl(self, path):
        with open(os.path.expanduser(path)) as f:
            tmpl = Template(f.read())

        return tmpl

    @property
    def globaltmpl(self):
        return self._tmpl(self.settings.global_index)

    @property
    def nstmpl(self):
        return self._tmpl(self.settings.namespace_index)

    def genindex(self):
        print('-- Generate template index')

        path = os.path.join(self.settings.target, 'doc', 'index.rst')
        context = {
            'namespaces': list(self.settings.namespaces())
        }
        out = self.globaltmpl.render(context)

        with open(path, 'w') as f:
            f.write(out)

    def iter_namespaces(self):
        for namespace in self.settings.namespaces():
            print('-- Generate template {0}/index'.format(namespace))

            path = os.path.join(
                self.settings.target,
                'doc', namespace,
                'index.rst'
            )
            context = {
                'namespace': namespace,
                'repositories': list(self.settings.repositories(namespace))
            }

            out = self.nstmpl.render(context)

            with open(path, 'w') as f:
                f.write(out)
