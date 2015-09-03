Canopsis Documentation Generator
================================

*cpsdocgen* is a tool used to track Canopsis Git repositories, in order to
extract documentation and build it in one Sphinx project.

Requirements
------------

You need to install the following packages before :

 - python-dev
 - libgit2-dev 0.22.1

Installation
------------

In a virtualenv :

    $ git clone https://git.canopsis.net/canopsis/canopsis-doc.git -b feature-new-docbuilder
    $ cd canopsis-doc
    $ virtualenv-2.7 venv
    $ . ./venv/bin/activate
    $ pip install -r requirements
    $ python setup.py install

How to use
----------

See config example in ``etc/cpsdocgen.conf``.

Then just call :

    $ cpsdocgen -c etc/cpsdocgen.conf
