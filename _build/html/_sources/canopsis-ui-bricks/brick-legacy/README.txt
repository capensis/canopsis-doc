Legacy Canopsis Brick
=====================

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

legacy code files

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
    $ ./bin/brickmanager install brick-legacy

Then, you need to enable the brick

::

    $ ./bin/brickmanager enable brick-legacy

You can see enabled bricks

::

    $ su - canopsis
    $ cd var/www
    $ ./bin/brickmanager list
    [u'core', u'uibase', u'monitoring', ..., **u'brick-legacy'**]

Usage
-----

See
`Howto <https://git.canopsis.net/canopsis-ui-bricks/brick-legacy/blob/master/doc/index.rst>`__

Continuous-Integration
----------------------

Tests
~~~~~

The last build was not a full build. Please use the "full-compile" npm
script to make test results show up here.

Lint
~~~~

Tested on commit : 2db547d.

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
| src/compo | component |
| nents/wra | -wrapper  |
| pper/comp | does not  |
| onent.js  | seems to  |
|           | be used   |
|           | anymore,  |
|           | check if  |
|           | it's      |
|           | possible  |
|           | to remove |
|           | this      |
|           | component |
|           |           |
+-----------+-----------+
| src/mixin | remove    |
| s/minimiz | this      |
| ebutton.j | file      |
| s         |           |
+-----------+-----------+

FIXMES
~~~~~~

Additional-info
---------------

Minified version : 21 files (size: 100K) Development version : 35 files
(size: 220K)
