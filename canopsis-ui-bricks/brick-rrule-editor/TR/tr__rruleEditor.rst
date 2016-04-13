.. _tr__rruleEditor:

=====
Canopsis rrule editor
=====

.. contents::
   :depth: 2

References
==========

List of referenced functional and technical requirements...

- `fr__rruleEditor.rst <../ED/fr__rruleEditor.rst>`_
- `ed__rruleEditor.rst <../ED/ed__rruleEditor.rst>`_

Updates
=======


.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "Tristan Carranante", "2016/02/16", "0.1", "Creation", "Florent Demeulenaere"

Contents
========

.. _TR__Title__Task1:

Implementing the Editor
------

Description related to :ref:`desc <FR__rruleEditor.rst>`.

Technical guide
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

This Editor use the library `rrule.js <https://github.com/jkbrzt/rrule>`_ . The rrule Editor will implement all the library options as in the `demo <https://jkbrzt.github.io/rrule/>`. The Editor is composed of three tabs, simple, advanced and Text input. The implementation must have all the options of the demo and use canopsis ui components.

This component aim to simplify the rrule creation. Each Rrule option is rendered in a html input, by selecting several options users can create complex rules without the hassle of learning rrule language. 

RRule.js give tools to transform rrule to human string, with emberjs computed properties this fonctionnality will be simple to implement.

This component use uibase component like the tabuled view.

A simple renderer is included with this brick to display rrules in human language, usefull to shorten rrules in tables and improve readability.