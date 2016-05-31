Simpletile Canopsis Brick
=========================

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

A widget whose purpose is to display a metric value with text, icons.

Content
-------

Screenshots
-----------

|View0|\ |View1|\ |View2|

Installation
------------

You need to clone the git repository and copy directory to Canopsis path

::

    $ su - canopsis 
    $ cd var/www
    $ ./bin/brickmanager install brick-simpletile

Then, you need to enable the brick

::

    $ ./bin/brickmanager enable brick-simpletile

You can see enabled bricks

::

    $ su - canopsis
    $ cd var/www
    $ ./bin/brickmanager list
    [u'core', u'uibase', u'monitoring', ..., **u'brick-simpletile'**]

Usage
-----

See
`Howto <https://git.canopsis.net/canopsis-ui-bricks/brick-simpletile/blob/master/doc/index.rst>`__

Continuous-Integration
----------------------

Tests
~~~~~

The last build was not a full build. Please use the "full-compile" npm
script to make test results show up here.

Lint
~~~~

Tested on commit : f5f4334.

+----------+------------------------------------------+--------+
| Target   | Status                                   |  Log   |
+==========+==========================================+========+
|  Lint    | :negative\_squared\_cross\_mark: ERROR   |        |
+----------+------------------------------------------+--------+

Code-Notes
----------

TODOS
~~~~~

FIXMES
~~~~~~

Additional-info
---------------

Minified version : 4 files (size: 32K) Development version : 3 files
(size: 36K)

.. |View0| image:: https://git.canopsis.net/canopsis-ui-bricks/brick-simpletile/raw/master/doc/preview/render1.png
.. |View1| image:: https://git.canopsis.net/canopsis-ui-bricks/brick-simpletile/raw/master/doc/preview/render2.png
.. |View2| image:: https://git.canopsis.net/canopsis-ui-bricks/brick-simpletile/raw/master/doc/preview/render3.png

