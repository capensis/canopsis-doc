.. _connectors_zabbix2canopsis_use:

Use
===

Configuration
-------------

Create a configuration file sampleconf.ini :

.. code-block:: json

    A revoir

Start / Stop
------------

You need a launcher like supervisord

Then you can configure it with

.. code-block:: bash


Now you can control you connector throught supervisortctl:

Start:

.. code-block:: bash

    supervisorctl start zabbix2canopsis

Stop:

.. code-block:: bash

    supervisorctl stop zabbix2canopsis

Restart:

.. code-block:: bash

    supervisorctl restart zabbix2canopsis   
