.. _ED__Autosup:

=======
Autosup
=======

This document describes how to use the autosupervision feature in Canopsis.

.. contents::
   :depth: 2

References
==========

List of referenced functional requirements:

 - :ref:`FR::Autosup <FR__Autosup>`
 - :ref:`TR::Autosup <TR__Autosup>`

Updates
=======

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "David Delassus", "2016/03/14", "0.2", "Document validation", "Florent Demeulenaere"
   "David Delassus", "2016/03/08", "0.1", "Document creation", ""

Contents
========

.. _ED__Autosup__Configuration:

Configuration
-------------

Autosupervision configuration is located in ``~/etc/autosup/autosup.conf`` and contains:

.. code-block:: javascript

   {
       "autosup": {
           "commands": [
               "http",
               "mongodb",
               "rabbitmq",
               "rabbitmqalive",
               "rabbitmqconnections"
           ]
       }
   }

.. _ED__Autosup__Running:

Running
-------

The provided script ``autosup`` can takes the following arguments:

 - ``--name <NAME>``: connector's name for produced events
 - ``--amqp``:
    - if present, it will send events to Canopsis directly
    - if not, events will be printed on standard output
