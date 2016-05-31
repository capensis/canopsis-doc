Compact\_themes Canopsis Brick
==============================

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

Content
-------

Screenshots
-----------

Installation
------------

You need to clone the git repository and copy directory to Canopsis path

::

    $ su - canopsis 
    $ cd var/www
    $ ./bin/brickmanager install compact_themes

Then, you need to enable the brick

::

    $ ./bin/brickmanager enable compact_themes

You can see enabled bricks

::

    $ su - canopsis
    $ cd var/www
    $ ./bin/brickmanager list
    [u'core', u'uibase', u'monitoring', ..., **u'compact_themes'**]

Usage
-----

See
`Howto <https://git.canopsis.net/canopsis-ui-bricks/compact_themes/blob/master/doc/index.rst>`__

Continuous-Integration
----------------------

Tests
~~~~~

The last build was not a full build. Please use the "full-compile" npm
script to make test results show up here.

Lint
~~~~

Tested on commit : 63f712a.

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

Minified version : 4 files (size: 20K) Development version : 2 files
(size: 20K)
