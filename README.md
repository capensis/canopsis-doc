Canopsis Documentation Generator
================================

*cpsdocgen* is a tool used to track Canopsis Git repositories, in order to
extract documentation and build it in one Sphinx project.

Requirements
------------

You need to install the following packages before :

 - python-dev
 - libgit2-dev 0.23.3

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


Supported clone/fetch methods:

- HTTPS
- HTTP
- SSH


Example with HTTP/HTTPS:

```json
{
    "git": {
        "url": "https://host",
        "user": "gitlab_user",
        "pass": "user_password"
    }
}
```

Example with SSH, with agent:

```json
{
    "git": {
        "url": "ssh://git@host:port",
        "ssh_pub": null,
        "ssh_priv": null,
        "ssh_passphrase": ""
    }
}
```

Example with SSH, without agent:

```json
{
    "git": {
        "url": "ssh://git@host:port",
        "ssh_pub": "/home/user/.ssh/id_rsa.pub",
        "ssh_priv": "/home/user/.ssh/id_rsa",
        "ssh_passphrase": "passphrase"
    }
}
```

If no passphrase is required, give an **empty string**, not `null`.
