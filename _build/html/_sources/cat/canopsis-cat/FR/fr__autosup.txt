.. _FR__Autosup:

=======
Autosup
=======

This document describes the autosupervision functionality in Canopsis.

.. contents::
   :depth: 2

References
==========

List of referenced functional requirements:

 - :ref:`FR::Event <FR__Event>`
 - :ref:`FR::Monitoring <FR__Monitoring>`

Updates
=======

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "David Delassus", "2016/03/14", "0.2", "Document validation", "Florent Demeulenaere"
   "David Delassus", "2016/03/08", "0.1", "Document creation", ""

Contents
========

.. _FR__Autosup__Desc:

Description
-----------

The autosupervision utility in Canopsis is used to run *Nagios* checks on the
current node, and produce :ref:`check events <FR__Event__Check>`, using the
:ref:`monitoring feature <FR__Monitoring__Desc>` of Canopsis.
