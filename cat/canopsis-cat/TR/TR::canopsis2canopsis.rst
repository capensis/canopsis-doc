.. _TR__Script_canopsis2canopsis:

========================
Script canopsis2canopsis
========================

This document specifies the canopsis2canospis script.

----------
References
----------

 - :ref:`FR::Task-Handling <FR__Task>`
 - :ref:`FR::Output-Media <FR__Output>`
 - :ref:`TR::Task-Shell <TR__Task-Shell>`
 - :ref:`TR::Task-File <TR__Task-File>`

-------
Updates
-------

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "Vincent CANDEAU", "2015/10/15", "0.1", "Document creation", ""

--------
Contents
--------

Description
===========

This output media will send bunch of events to remote Canopsis.

Script canopsis2canopsis configuration
======================================

Usage: canopsis2canopsis.sh URL AUTHKEY LIMIT PATHJSON
URL: Remote Canopsis URL (http://canopsis.example.com)
AUTHKEY: Authkey of the account would we receive the event
LIMIT: How many event will be combine and send at one time ( Default: 200 )
PATHJSON: File path where json will be store

Deploy
======

Notification job: task_file
---------------------------

path: "~/tmp/{{timestamp}}_{{rk}}.json"
body: "{{EVT}}"

Scheduled job: task_shell
-------------------------

???????

