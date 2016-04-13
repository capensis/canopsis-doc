CaLink
________

Table of contents
------------------------


1. What_

2. How_

   1. Configuration_

      1. info_

      2. files_

      3. commands_

      4. output_

   2. Example_

3. Library_

   1. Adding Informations_

   2. Use_

.. _what:

What
----

CaLink is a tool destined to provide a user with a way to gather all informations of their system.

These informations includes system information, any logs they may have, and output of commands.

The informations are then added to a an archive for an easy sharing.

Everything is configurable.


.. _how:

How
---

Simply run ``calink``

.. _configuration:

Configuration
..............

Four sections are supported

Sections are composed of variables which values should be separated with commas

.. _info:

info
,,,,,,

Here are specified the informations to gather

.. code:: python

          [info]
          system=host,os,version
          resources=loadavg

The variable names will define the key of the JSON document containing the informations:

The informations supported at the moment are :

* uptime
        How long the system has been running

* loadavg
        Load average over 1, 5, and 15mn

        Currently executing kernels scheduling entities

        Number of kernel scheduling entities existing on the system

        PID of the latest created process

* disk
        List of the information of all the partition on the local machine

* ps
        List of all the running processes (with their pid) on the local machine
* cpu
        CPU average, minimum, and maximum
* vmem
        Virtual memory average, minimum, and maximum
* smem
        SWAP memory average, minimum, and maximum
* iostat
        I/O stat average, minimum, and maximum

* host
        Hostname

* os
        OS Name and distribution version

* version
        Version of system


files
,,,,,,

This sections is used to retrieve the list of files to add to the archive

.. code:: python

          [files]
          var_log_dirs=engines,.
          etc_dirs=bar
          etc_files=foo.log


The variable names are used to determine if whole directories or only specific files should be added to the archive and to also determine the path.

The names follow this template

.. code:: python

          $PATH.replace('/', '_')_[dirs|files]=...

A single dot as a value means that the directory specified in the variable name should be retrieved

.. _commands:

commands
,,,,,,,,,,,,

Commands that must be run and added to the archive are listed here

The name of each variable is the label that will be used in the log file

The command should then be written without any delimiter

.. code:: python

          [commands]
          list_root_directory=ls -lha ./

.. _output:

output
,,,,,,

The names of the archive, commands log, and json files should be specified here

.. code:: python

          [output]
          json=CaLink-JSON
          commands=CaLink-commands-log

If nothing is specified, they will have the following format

.. code:: python

         CaLink-$WORKSTATION-$TIMESTAMP[.targ.gz|.json|-commands.log]


.. _example:

Example
........

Here is an example with the configuration above

.. code:: bash

          $ calink
          2014-10-28 22:29:10,591 [MainThread  ] [INFO ]          + Getting host informations
          2014-10-28 22:29:10,636 [MainThread  ] [INFO ]   + Retrieving informations..
          2014-10-28 22:29:10,636 [MainThread  ] [INFO ]          + Getting host informations
          2014-10-28 22:29:10,636 [MainThread  ] [INFO ]          + Getting OS informations
          2014-10-28 22:29:10,647 [MainThread  ] [INFO ]          + Getting version informations
          2014-10-28 22:29:10,647 [MainThread  ] [INFO ]          + Getting I/O stat informations
          2014-10-28 22:29:10,647 [MainThread  ] [INFO ]          + Getting swap memory informations
          2014-10-28 22:29:10,648 [MainThread  ] [INFO ]          + Getting virtual memory informations
          2014-10-28 22:29:10,648 [MainThread  ] [INFO ]          + Getting process informations
          2014-10-28 22:29:10,660 [MainThread  ] [INFO ]          + Getting CPU informations
          2014-10-28 22:29:10,660 [MainThread  ] [INFO ]          + Getting disk informations
          2014-10-28 22:29:10,661 [MainThread  ] [INFO ]          + Getting load average informations
          2014-10-28 22:29:10,662 [MainThread  ] [INFO ]          + Getting uptime informations
          2014-10-28 22:29:10,662 [MainThread  ] [INFO ]   + Creating json file CaLink-workstation-zdibe-1414531750.json
          2014-10-28 22:29:10,702 [MainThread  ] [INFO ]   + Creating commands file CaLink-workstation-zdibe-1414531750-commands.log
          2014-10-28 22:29:10,702 [MainThread  ] [INFO ]          + Executing command ls -lha
          2014-10-28 22:29:10,705 [MainThread  ] [INFO ]   + Getting filepaths
          2014-10-28 22:29:10,705 [MainThread  ] [INFO ]          - get_files: Directory /usr/etc/bar/ not found
          2014-10-28 22:29:10,730 [MainThread  ] [INFO ]          - get_files: File /usr/etc/foo.log not found
          2014-10-28 22:29:10,730 [MainThread  ] [INFO ]   + Creating archive file CaLink-workstation-zdibe-1414531750.tar.gz
          2014-10-28 22:29:10,740 [MainThread  ] [INFO ]          + Adding file /usr/var/log/engines/cleaner.log to the archive
          2014-10-28 22:29:10,741 [MainThread  ] [INFO ]          + Adding file /usr/var/log/engines/filter.log to the archive
          2014-10-28 22:29:10,742 [MainThread  ] [INFO ]          + Adding file /usr/var/log/engines/archiver.log to the archive
          2014-10-28 22:29:10,742 [MainThread  ] [INFO ]          + Adding file /usr/var/log/engines/eventstore.log to the archive
          2014-10-28 22:29:10,742 [MainThread  ] [INFO ]          + Adding file /usr/var/log/calink.log to the archive
          2014-10-28 22:29:10,760 [MainThread  ] [INFO ]          + Adding file /usr/var/log/bar.log to the archive
          2014-10-28 22:29:10,761 [MainThread  ] [INFO ]          + Adding file /usr/var/log/foo.log to the archive
          $ cat CaLink-commands-log-commands.log

          list current directory: ls -lha ./:
          total 40K
          drwxr-xr-x 5 zdibe zdibe 4.0K Oct 24 17:05 .
          drwxr-xr-x 6 zdibe zdibe 4.0K Oct 10 14:28 ..
          -rw-r--r-- 1 zdibe zdibe   37 Oct 24 17:07 CaLink-commands-log-commands.log
          -rw-r--r-- 1 zdibe zdibe  305 Oct 24 17:07 CaLink-JSON.json
          -rw-r--r-- 1 zdibe zdibe  715 Oct 24 17:05 CaLink-workstation-zdibe-1414163113.tar.gz
          drwxr-xr-x 3 zdibe zdibe 4.0K Oct 21 16:01 canopsis
          drwxr-xr-x 2 zdibe zdibe 4.0K Oct 24 17:04 etc
          drwxr-xr-x 2 zdibe zdibe 4.0K Oct 21 16:58 scripts
          -rw-r--r-- 1 zdibe zdibe  270 Oct 21 14:54 setup.py
          $ cat CaLink-JSON.json
          {'resources': {'loadavg': {'average': {'1': 0.3, '15': 0.49, '5': 0.46},
                                                 'entities': {'current': 1, 'total': 390},
                                                  'last_pid': 8912}},
           'system': {'host': 'workstation-zdibe',
                      'os': 'debian-jessie/sid-',
                      'version': 'Linux-3.13-1-amd64-x86_64-with-debian-jessie-sid'},
           'timestamp': '17:05:13 24-10-2014'}


.. _library:

Library
-------

.. _informations:

Adding informations
....................

To support new informations, simply add a function following this template to the CaLink library:

.. code:: python

          def get_NAME_info():
          """
          Returns:
              ...
          """

          return ...

The type of the returned data should be JSON compliant

.. _use:

Using the library
..................

Each informations have the template seen above and can be called outside of the ``calink`` script like so:

.. code:: python

          from canopsis.calink import calink

          print calink.get_host_info()


Or use it to call the ``calink`` utils from elsewhere, in an engine after an event is triggered for example:

.. code:: python

          from canopsis.calink import calink

          import ConfigParser
          config = ConfigParser.ConfigParser()

          output = calink.get_from_section(config, 'output', {})
          calink(config.read(join(sys.prefix, 'etc', 'calink-config.ini')),
                 json_file=output.get('json', None),
                 archive_file=output.get('archive', None),
                 cmd_file=output.get('commands', None))
