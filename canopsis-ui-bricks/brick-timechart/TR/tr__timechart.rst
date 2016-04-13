.. _TR__Timechart:

=========================
Canopsis Widget Timechart
=========================

.. contents::
   :depth: 2

References
==========

List of referenced functional and technical requirements.

- `FR::timechart.rst <FR__timechart>`_
- ref: tr__periodic_behaviors.rst
- ref: tr__alarms.rst

Updates
=======

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "Florent Demeulenaere", "3/02/2016", "0.1", "Document creation", ""

Description
===========

The timechart widget let the user display one or several metrics in a customizable chart. It is also possible to display periodic behaviors and alarms relative to the selected metrics.

Contents
========

The frontend timechart part is implemented thanks to the C3js library `C3 <http://c3js.org/>`_

Widget main description
-----------------------

This widget will manage charts creation thanks to the configuration given in the creation form. the widget will be composed of a view and a template to render every C3 components.

Sources
-------

Metrics
~~~~~~~

The querybuilder component will let the user to select metrics. The user will have the possibility to group selected metrics to obtain several charts thanks to C3. The whole selection part is located on the widget configuration form. Metrics give related perfdata displayed on the chart. The request to the database to obtain perfdata is performed by the metricconsumer mixin.

Alarms
~~~~~~

Alarms will be requested by an adapter linked to the alarm python brick.
The python brick contains the webservice that serves alarms thanks to the related manager.

Periodic behaviors
~~~~~~~~~~~~~~~~~~

Periodic behaviors are requested thanks to the periodic pehavior manager and displayed in background of charts. If there are multiple charts, the user has only the possibility to display or hide them on every chart in the same time.

Chart options
-------------

Charts options are just attributes to set correctly when we are using C3js components. When charts are instantiate, the user can change some of the options thanks to a dropdown button.

The has the possibility to change the type of curve, and some other options too. To do that correctly, the selected charts will be refresh by calling a specific function in the C3 library: c3.generate().



