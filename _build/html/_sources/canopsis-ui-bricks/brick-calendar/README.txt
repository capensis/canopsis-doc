Calendar Canopsis Brick
=======================

Index
-----

-  `Description <#description>`__
-  `Content <#content>`__
-  `Installation <#installation>`__
-  `Usage <#usage>`__
-  `Continuous-integration <#continuous-integration>`__
-  `Code-notes <#code-notes>`__
-  `Additional-info <#additional-info>`__

Description
-----------

Calendar widget for Canopsis

Content
-------

Screenshots
-----------

|View0|\ |View1|

Installation
------------

You need to clone the git repository and copy directory to Canopsis path

::

    $ su - canopsis 
    $ cd var/www
    $ ./bin/brickmanager install brick-calendar

Then, you need to enable the brick

::

    $ ./bin/brickmanager enable brick-calendar

You can see enabled bricks

::

    $ su - canopsis
    $ cd var/www
    $ ./bin/brickmanager list
    [u'core', u'uibase', u'monitoring', ..., **u'brick-calendar'**]

Usage
-----

See
`Howto <https://git.canopsis.net/canopsis-ui-bricks/brick-calendar/blob/master/doc/index.rst>`__

Continuous-Integration
----------------------

Tests
~~~~~

The last build was not a full build. Please use the "full-compile" npm
script to make test results show up here.

Lint
~~~~

Tested on commit : bb9bf2b.

+----------+------------------------------------------+--------+
| Target   | Status                                   |  Log   |
+==========+==========================================+========+
|  Lint    | :negative\_squared\_cross\_mark: ERROR   |        |
+----------+------------------------------------------+--------+

Code-Notes
----------

TODOS
~~~~~

+-----------+-----------+
|  File     |  Note     |
+===========+===========+
| src/mixin | REMOVE!!  |
| s/calenda | ---       |
| rsourceev | Actually  |
| entslog.j | needful   |
| s         | to get    |
|           | the       |
|           | customfil |
|           | terlist   |
+-----------+-----------+
| src/mixin | @fdemeule |
| s/calenda | naere     |
| rsourceev | create a  |
| entslog.j | property  |
| s         | on the    |
|           | mixin     |
|           | dict, in  |
|           | order to  |
|           | comment   |
|           | it, and   |
|           | notify    |
|           | the       |
|           | presence  |
|           | of this   |
|           | property  |
|           | to future |
|           | readers   |
+-----------+-----------+

FIXMES
~~~~~~

Additional-info
---------------

Minified version : 7 files (size: 84K) Development version : 19 files
(size: 184K)

.. |View0| image:: https://git.canopsis.net/canopsis-ui-bricks/brick-calendar/raw/master/doc/preview/calendar_overview.png
.. |View1| image:: https://git.canopsis.net/canopsis-ui-bricks/brick-calendar/raw/master/doc/preview/category_creation.png

