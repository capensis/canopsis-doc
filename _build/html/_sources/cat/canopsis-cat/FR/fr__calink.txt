.. _FR__CALink:

======
CALink
======

This document describes the CALink functionality in Canopsis.

.. contents::
   :depth: 2

References
==========

List of referenced functional requirements...

Updates
=======

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "David Delassus", "2016/03/15", "0.3", "Document validation", "Florent Demeulenaere"
   "David Delassus", "2016/02/01", "0.2", "Add description", ""
   "David Delassus", "2016/01/29", "0.1", "Document creation", ""

Contents
========

.. _FR__CALink__Desc:

Description
-----------

CALink is an utility used to ease the debug in Canopsis.

It gather informations about the host where it's run and may collect logs.

Gathered informations are:

 - date and uptime
 - Fully Qualified Domain Name
 - Distribution and Kernel version
 - load average
 - CPU/RAM/SWAP/Disk usage
 - Disk I/O stats
 - List of processes
 - output (``stdout`` and ``stderr``) of a list of commands
 - Canopsis logs

All of this informations is then stored in a TAR archive, ready to be sent.
