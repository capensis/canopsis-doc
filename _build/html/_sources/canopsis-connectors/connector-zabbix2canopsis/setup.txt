.. _connectors_zabbix2canopsi_setup:


Setup
=====

Requirements
------------

MySQL
*****

Prerequisite :

.. code-block:: bash

    MySQL dev packages (eg. $ apt-get install mysqld-dev)
    Python dev packages (eg. $ apt-get install python-dev)
    $ pip install mysql-python

Database section in conf file :

.. code-block:: ini

    [database]
    url=mysql://user:password@mysql_host/database
    query=sql query (eg. SELECT * from table WHERE criterions)

PgSQL
*****

Prerequisite :

.. code-block:: bash

    PostgreSQL dev packages (eg. $ apt-get install postgresql postgresql-server-dev-all)
    Python dev packages (eg. $ apt-get install python-dev)
    $ pip install psycopg2

Database section in conf file :

.. code-block:: bash

    [database]
    url=postgresql://user:password@postgresql_host/database
    query=sql query (eg. SELECT * from table WHERE criterions)

Oracle
******

Prerequisite :

.. code-block:: bash

    Oracle instant Client and Oracle instant Client SDK
    (Account needed !) You need to download it at http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html
    =>  instantclient-basic-linux
    =>  instantclient-sdk-linux

    Python dev packages (eg. $ apt-get install python-dev)

Define Oracle home var :

.. code-block:: bash

    $ export ORACLE_HOME=/path_to_oracle_instant_client

Symlink lib clntsh 

.. code-block:: bash

    ln -sf libclntsh.so.xx.x libclntsh.so

Finaly, install cx_oracle

.. code-block:: bash

    $ pip install cx_Oracle

Database section in conf file :

.. code-block:: ini

    [database]
    url=oracle://user:password@oracle_host:1521/sid
    query=sql query (eg. SELECT * from table WHERE criterions)

Alternative URL 

.. code-block:: ini

    [database]
    url=oracle+cx_oracle://user:password@tnsname

Install
-------

Connector `tcp2canopsis` must be first installed and configured.

`connector-zabbix2canopsis` is based on sqlalchemy toolkit (http://www.sqlalchemy.org/) to query database and kombu lib to publish messages to RabbitMQ.

.. code-block:: bash

    pip install sqlalchemy
    pip install kombu

SQLAlchemy comes with differents dialects (http://docs.sqlalchemy.org/en/latest/dialects/index.html) that need dependencies too.

For Example, if you want to query a MySQL database, you need to install python-mysql lib

.. code-block:: bash

    pip install mysql

Stable version (not published yet):

.. code-block:: bash

    pip install connector-zabbix2canopsis

Development version:

.. code-block:: bash

    pip install https://git.canopsis.net/canopsis-connectors/connector-zabbix2canopsis

Install Zabbix action
---------------------

Create hostgroup hg_canopsis, all hosts monitored must belong to this hostgroup.

AlertScriptsPath is configued in zabbix_server.conf.
Create action ac_send_canopsis.

.. code-block:: bash

    Configure condition :
    Host group = hg_canopsis
    Configure operation :
    Operation type : remote command
    Execute on : zabbix server
    Command(replace AlertScriptsPath by its value) : "AlertScriptsPath"/send_zab_event2canop.py "{EVENT.DATE}" "{EVENT.TIME}" "{STATUS}" "{TRIGGER.NSEVERITY}" "{TRIGGER.ID}" "{TRIGGER.NAME}" "{HOST.NAME1}" "{ITEM.NAME1}" "{ITEM.VALUE1}" "{HOST.NAME2}" "{ITEM.NAME2}" "{ITEM.VALUE2}" "{HOST.NAME3}" "{ITEM.NAME3}" "{ITEM.VALUE3}" "{HOST.NAME4}" "{ITEM.NAME4}" "{ITEM.VALUE4}" "{HOST.NAME5}" "{ITEM.NAME5}" "{ITEM.VALUE5}" "{HOST.NAME6}"

Create log file :

.. code-block:: bash

    touch /var/log/send_zab_event2canop.log && chown zabbix:zabbix /var/log/send_zab_event2canop.log

Create buffer folder (replace AlertScriptsPath by its value):

.. code-block:: bash

    mkdir "AlertScriptsPath"/connector_buffer  && chown zabbix:zabbix  "AlertScriptsPath"/connector_buffer""

The token must be the same as in connector-zabbix2canopsis.config file
