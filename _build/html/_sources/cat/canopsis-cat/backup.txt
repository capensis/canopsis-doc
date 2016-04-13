Canopsis Backup Utility
=======================

Canopsis's Backup utility provides a command line interface to create backup of the current node.

Description
-----------

This utility is based on:

 * **Burp**: a backup utility using *librsync*
 * **mongodump/mongorestore**: *MongoDB* tools for exporting/importing data

It works in a client/server mode:

 * the client describes what to backup and sends data to the server
 * the server handles deduplication, compression and backup storage

Because of the use of *librsync*, each backup is a diff of the previous backup. Only delta are stored.
But each of those deltas contains all the files, hard-linked (to avoid duplicated content), and so, is virtually a full backup.

Usage
-----

.. code-block::

   $ cpsbackup -h
   Usage: cpsbackup <options>

   Options:
       -e,--export               Backup current node state
       -i,--import [backup id]   Restore last backup, or specific backup
       -l,--list                 List all backups
       -s,--show <backup id>     Show backup's content
       -d,--delete <backup id>   Remove backup
       -h,--help                 Print this help

Example:

.. code-block::

   $ cpsbackup -l
   2015-02-24 11:39:06: burp[29705] before client
   2015-02-24 11:39:06: burp[29705] begin client
   2015-02-24 11:39:06: burp[29705] auth ok
   2015-02-24 11:39:06: burp[29705] Server version: 1.4.30
   2015-02-24 11:39:06: burp[29705] nocsr ok
   2015-02-24 11:39:06: burp[29705] SSL is using cipher: DHE-RSA-AES256-GCM-SHA384 TLSv1.2 Kx=DH       Au=RSA  Enc=AESGCM(256) Mac=AEAD
   Backup: 0000001 2015-02-23 14:24:31 (deletable)
   Backup: 0000002 2015-02-23 14:27:13
   Backup: 0000003 2015-02-23 14:30:25
   Backup: 0000004 2015-02-24 09:33:18

   2015-02-24 11:39:06: burp[29705] List finished ok
   2015-02-24 11:39:06: burp[29705] after client

Configuration
-------------

*Burp* uses **SSL** to encrypt transport on port 4200.
All certificates used are stored in ``etc/ssl``.

Server
++++++

The server configuration is stored in ``etc/backup/server.conf``:

.. code-block:: ini

   address=0.0.0.0
   port=4200
   status_address=127.0.0.1
   status_port=4201
   keep=5

***NB:*** only interesting options are listed above.

 * ``address``: address to bind to
 * ``port``: port to listen on
 * ``status_address``: address to bind to for status interface
 * ``status_port``: port to listen on for status interface
 * ``keep``: number of backup to keep per client

Each client is registered have a configuration file in ``etc/backup/clients`` named after the client's name.

For example, in ``etc/backup/clients/cpsnode`` we have the following:

.. code-block:: ini

   ssl_peer_cn=cpsnode

The only option is the expected common name in the client's supplied certificate.

Client
++++++

The client configuration is located at ``etc/backup/node.conf``:

.. code-block:: ini

   server=127.0.0.1
   port=4200

   include=/opt/canopsis/etc
   include=/opt/canopsis/opt/mongodb/load.d/json_object
   include=/opt/canopsis/opt/mongodb/load.d/rights
   include=/opt/canopsis/var/cache/canopsis/mongodb
   exclude_regex=\.bson\.(pid|lock|state)$
   read_all_fifos=1

***NB:*** only interesting options are listed above.

 * ``server``: address to connect to
 * ``port``: port to connect to
 * ``include``: include folder to backup
 * ``exclude_regex``: exclude a pattern from the backup
 * ``read_all_fifos``: if a backed-up file is a FIFO, it will read the FIFO and backup its content

The two last options are for the *MongoDB* integration with *Burp*.

Functional overview
-------------------

Exporting
+++++++++

First, a FIFO is created for each *MongoDB* collection (listed in ``etc/backup/storage.conf``).
Then, with the help of ``mongodump``, each collection is dumped to its corresponding FIFO.

When *Burp* is launched, it will backup the specified folders, including the previously created FIFOs.

Finally, after the backup, we will check that each ``mongodump`` was successful (or invalidates the backup if not).

No extra-space is required to perform the backup, since the database is backed-up via a FIFO.

Importing
+++++++++

When *Burp* performs a restore, it will write FIFOs content into a file named after the FIFO.

This means that the FIFO created for ``mongodump``, when exporting, will be restored as a regular file by *Burp*.

This also means that you will need extra-space during the restore process.

Finally, when *Burp* has finished to perform the restore, ``mongorestore`` will be called to re-inject the data into the database.

The files used by ``mongorestore`` will be deleted once everything is done.

Miscellaneous
-------------

When Canopsis is configured in HA mode, you should refer to the documentation of
the HAC brick, in order to designate the backup server and client amongs the nodes.