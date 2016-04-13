.. _ED__CALink:

======
CALink
======

User manual of CALink utility.

.. contents::
   :depth: 2

References
==========

List of referenced functional requirements...

- :ref:`FR::CALink <FR__CALink>`
- :ref:`TR::CALink <TR__CALink>`

Updates
=======

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "David Delassus", "2016/03/15", "0.2", "Document validation", "Florent Demeulenaere"
   "David Delassus", "2016/02/01", "0.1", "Document creation", ""

Contents
========

.. _ED__CALink__Configuration:

Configuration
-------------

The configuration is located in: ``~/etc/calink/calink.conf``.

By default, it contains:

.. code-block:: python

    {
        "CALINK": {
            "commands": [
                "autosup --name calink",
                "crontab -l",
                "pip freeze",
                "webmodulemanager list",
                "supervisorctl status"
            ],
            "logdirs": [
                ".",
                "engines"
            ]
        }
    }


By default:

 - ``dateformat`` is: ``%H:%M:%S %d-%m-%Y``
 - ``workdir`` is: ``$PREFIX/tmp/calink``
 - ``destdir`` is: ``$PREFIX/var/lib/canopsis/calink``

.. _ED__CALink__Usage:

Usage
-----

Just run the command ``calink``, then send the produced archive:

```
$ date
Mon Feb  1 11:09:12 CET 2016
$ calink
$ cd ~/var/lib/canopsis/calink
$ ls
calink-linkdd.beastie.eu-2016-01-29-15:07:11.tar.gz
calink-linkdd.beastie.eu-2016-01-29-15:46:50.tar.gz
calink-linkdd.beastie.eu-2016-01-29-15:48:18.tar.gz
calink-linkdd.beastie.eu-2016-01-29-16:01:05.tar.gz
calink-linkdd.beastie.eu-2016-01-29-17:19:55.tar.gz
calink-linkdd.beastie.eu-2016-01-29-17:23:05.tar.gz
calink-linkdd.beastie.eu-2016-01-29-17:25:08.tar.gz
calink-linkdd.beastie.eu-2016-01-29-17:26:31.tar.gz
calink-linkdd.beastie.eu-2016-02-01-11:09:15.tar.gz
```
