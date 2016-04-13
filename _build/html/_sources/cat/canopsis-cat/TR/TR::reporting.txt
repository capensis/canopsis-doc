=========
Reporting
=========

This document describes the technical requierements of the reporting feature.

.. contents::
   :depth: 2

----------
References
----------

- :ref:`FR::Reporting <FR__Reporting>`
- :ref:`FR::Briefcase <FR__Briefcase>`
- :ref:`FR::TaskHandler <FR__TaskHandler>`

-------
Updates
-------

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "Vincent CANDEAU", "09/10/2015", "0.1", "Creation", "Jonathan Labéjof"

--------
Contents
--------

In order to do this job, we will use a taskhandler that will execute a PhantomJS script.
This script will save a pdf file that will be saved into the briefcase.

Implementation
==============

The implementation is done in a taskhandler named 'taskreporting' (module ``canopsis.engines.task_reporting``).

Metadata
========

The following metadata are provided to the taskhandler:

 - URL: (Default: http://127.0.0.1:8082/)
 - View: View to export
 - User: User account use for export

PDF Exporting
=============

Usage: phantomjs canopsisExport.js server viewName authkey [logLevel] [lang] [fileName]

- **logLevel**: Logging Level [DEBUG, INFO, ERROR, NONE] (Default: NONE)
- **Lang**: Language of the exported View (Default: en)
- **FileName**: name of file (Default: login_viewName_yyyymmddhhiiss.pdf)
