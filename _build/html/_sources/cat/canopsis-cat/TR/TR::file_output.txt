.. _TR__File_Output:

=================
File Output Media
=================

This document specifies the File output media.

----------
References
----------

 - :ref:`FR::Task-Handling <FR__Task>`
 - :ref:`FR::Output-Media <FR__Output>`

-------
Updates
-------

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "Vincent CANDEAU", "2015/10/07", "0.1", "Document creation", "Jonathan Labéjof"

--------
Contents
--------

Description
===========

This output media will write an email, configured in its :ref:`task <FR__Task__Job>` configuration.

Task configuration
==================

It **MUST** contain:

 - a path.
 - a body.

Task handling
=============

It **MUST** render the path/body templates with the provided job context as data source.

Test Cases
==========

Case: Everything went good
--------------------------

It **SHOULD** return the following informations:

 - an error code, equal to ``0``.
 - a message explaining that there was no error.


Case: Invalid configuration
---------------------------

If there is a missing field, or an invalid field in the task received, it **SHOULD**
return the following informations:

 - an error code, superior to ``0``.
 - a message explaining the error.

Case: Can't write file
----------------------

It **SHOULD** return the following information:

 - an error code, superior to ``0``.
 - a message explaining the error.
