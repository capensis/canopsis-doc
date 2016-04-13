.. _TR__Shell_Output:

==================
Shell Output Media
==================

This document specifies the Shell output media.

References
==========

 - :ref:`FR::Task-Handling <FR__Task>`
 - :ref:`FR::Output-Media <FR__Output>`

Updates
=======

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "David Delassus", "2015/10/06", "0.1", "Document creation", ""

Contents
========

Description
-----------

This output media will execute a shell command, configured in its :ref:`task <FR__Task__Job>` configuration.

Task configuration
------------------

It **MUST** contains:

 - the command to execute

Task handling
-------------

The command will be executed with an extra argument : the provided job context as a JSON string.

Test Cases
----------

Case: Everything went good
~~~~~~~~~~~~~~~~~~~~~~~~~~

It **SHOULD** return the following informations:

 - an error code, equal to ``0``
 - a message explaining that there was no error


Case: Invalid configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If there is a missing field, or an invalid field in the task received, it **SHOULD**
return the following informations:

 - an error code, superior to ``0``
 - a message explaining the error

Case: An error occured during execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It **SHOULD** return the following informations:

 - an error code, superior to ``0``
 - a message explaining the error
