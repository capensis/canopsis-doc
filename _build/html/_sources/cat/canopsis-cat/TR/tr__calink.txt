.. _TR__CALink:

======
CALink
======

This document describes the implentation of the CALink utility.

.. contents::
   :depth: 2

References
==========

List of referenced functional and technical requirements:

- :ref:`FR::CALink <FR__CALink>`

Updates
=======


.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "David Delassus", "2016/03/15", "0.2", "Document validation", "Florent Demeulenaere"
   "David Delassus", "2016/02/01", "0.1", "Document creation", ""

Contents
========

.. _TR__CALink__Configurable:

Implementation
--------------

The implementation **MUST** be done in a configurable, and be provided the following configuration :

 - ``dateformat``: format used to stringify the date (as a ``string``)
 - ``workdir``: directory used to gather informations before archiving (as a ``string``)
 - ``destdir``: directory used to put the TAR archive (as a ``string``)
 - ``commands``: list of commands to execute (as a ``list`` of ``string``)
 - ``logdirs``: list of log directories to include (as a ``list`` of ``string``):
     - each value is within ``$PREFIX/var/log``

The archive **MUST** be named: ``calink-{FQDN}-{DATE}-{TIME}.tar.gz``

.. _TR__CALink__Content:

Archive content
---------------

The archive **MUST** contains:

 - a file named ``info.json`` containing the gathered informations
 - a file named ``commands.log`` containing (for each command):
    - the ran command
    - the command's output (``stdout`` and ``stderr``)
    - the command PID and exit code
 - a folder named ``logs`` containing all gathered logs
