.. _FR__rruleEditor.rst:

========================
Canopsis rrule editor
========================

This document describes the rrule editor features.

.. contents::
   :depth: 2


Updates
=======

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "Tristan Carranante", "2016/02/16", "0.1", "Creation", "Florent Demeulenaere"


Contents
========

.. _FR__Title__Desc:

Description
-----------

This editor provide the ability to visually build and edit a rrule. The default tab allow users to quickly create a simple rrule. The second tab titled "advance" provide tools to build a complex rrule. The last tab allow power users to write their own rrule by hand. A human feedback of the rrule is given by the tool.

Functional test
---------------

the easiest way to test the editor is to go in the ui and settings -> User interface -> Editors, type "rrule" in the left text box and rruleeditor in the right one, hit the plus button and save changes.

Now if you go in the Engines -> Scheduled jobs, click the edit button of the default task tasklinklist, you can see the rrule editor on the second panel in the tab "link list". 

Test every html input, notice the change in the rrule and summary field. Save your rrule, and then modify it. save it again. Notice the renderer change in the scheduled table. Hover the renderer and every field in editor, all should display a message except the "frequency" one.
