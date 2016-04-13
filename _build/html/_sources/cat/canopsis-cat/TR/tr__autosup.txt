.. _TR__Autosup:

=======
Autosup
=======

This document describes the autosupervision requirements in Canopsis.

.. contents::
   :depth: 2

References
==========

List of referenced functional requirements:

 - :ref:`FR::Autosup <FR__Autosup>`
 - :ref:`FR::Monitoring <FR__Monitoring>`

Updates
=======

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "David Delassus", "2016/03/14", "0.2", "Document validation", "Florent Demeulenaere"
   "David Delassus", "2016/03/08", "0.1", "Document creation", ""

Contents
========

.. _TR__Autosup__Desc:

Description
-----------

The autosupervision feature **MUST** provide:

 - a set of :ref:`monitoring checks <FR__Monitoring__Check>`
 - a configuration file to list commands to execute
 - a script to execute listed commands
