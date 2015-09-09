.. _canopsis-doc_setup:


Setup
=====

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

.. note:
	You need to have the same release of libgit2 and pygit2 in order to compile tools

