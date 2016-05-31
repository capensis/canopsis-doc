.. _connectors_sql2canopsis_setup:


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

`connector-sql2canopsis` is based on sqlalchemy toolkit (http://www.sqlalchemy.org/) to query database and kombu lib to publish messages to RabbitMQ.

.. code-block:: bash

    pip install sqlalchemy
    pip install kombu

SQLAlchemy comes with differents dialects (http://docs.sqlalchemy.org/en/latest/dialects/index.html) that need dependencies too.

For Example, if you want to query a MySQL database, you need to install python-mysql lib

.. code-block:: bash

    pip install mysql

Stable version (not published yet):

.. code-block:: bash

    pip install connector-sql2canopsis

Development version:

.. code-block:: bash

    pip install https://git.canopsis.net/canopsis-connectors/connector-sql2canopsis
