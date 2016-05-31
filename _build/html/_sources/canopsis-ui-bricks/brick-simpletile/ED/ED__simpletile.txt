.. _ED__simpletile:

====================
Canopsis Simple Tile
====================

This document describes how to use the Simple Tile in Canopsis.

.. contents::
   :depth: 2

Updates
=======

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "Florent Demeulenaere", "2016/05/31", "0.1", "Document creation", ""

Contents
========
.. _ED__Title__Desc:


Simpletile widget
=================

Overview
--------
whose purpose is to display a metric value with text, icons
The Canopsis Simpletile widget can show a metric in a esthetic way

Create a simpletile in a view
---------------------------------

Inserting a simpletile widget in a canopsis view requires management rights. please refer to the canopsis rights management to know more about this topic.

First, choose a view where the simpletile will be inserted. When done, switch to insert widget edition mode, choose the simpletile in the list and click on it. The specific form for the simpletile is displayed and let input this widget configuration.

Simpletile parameters are explained below.

Simpletile widget configuration
-----------------------------------


.. figure:: ../_static/images/ED/form.png



Options
-------

- **Title** : the widget title
- **Tile icon to use, font-awesome style** : icon to use
- **Title color** : the color title
- **Tile color** : the tile color
- **Use an alternative fancy layout for this widget** : icon is displayed near metric value
- **Unit to display next to the value** : unit, text to display next metric value
- **Display current value as KiB, MiB, GiB ...** : human readable value

Footer
-----

This section allow to set Simpletile footer's options

.. figure:: ../_static/images/ED/footer.png

- **Target of footer's link**
- **Footer Color**
- **Text on link**


Series
------

This section allow to choose series to include into the chart

.. figure:: ../_static/images/ED/series.png


Metrics
-------

This section allow to choose metrics to include into the chart

.. figure:: ../_static/images/ED/metrics.png

Renders
-------

.. figure:: ../_static/images/ED/render1.png
.. figure:: ../_static/images/ED/render2.png
.. figure:: ../_static/images/ED/render3.png
