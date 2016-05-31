.. _connectors_sql2canopsis_use:

Use
===

Configuration
-------------

Create a configuration file sampleconf.ini :

.. code-block:: ini

    [database]
    url=mysql://root:toor@localhost/tickets
    query=SELECT id, title, description, etablissement FROM tickets where status = 1

    [amqp]
    url=amqp://cpsrabbit:canopsis@localhost:5672/canopsis

    [event]
    connector.constant=edc2canopsis
    connector_name.constant=instance1
    event_type.constant=check
    source_type.constant=resource
    component.value=id
    resource.value=etablissement
    output.value=description
    #metrique1.metrictype=GAUGE
    #metrique1.metricvalue=nb

Start / Stop
------------

See http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls to configure urls

Then you can execute it with a predefined configuration:

.. code-block:: bash

    sudo connector-sql2canopsis -c sampleconf.ini

Otherwise, you can go manually:

.. code-block:: bash

    $ python connector-sql2canopsis.py --help
    usage: connector-sql2canopsis.py [-h] [-c CONFIG]

    SQL connector to Canopsis

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            Path to configuration file
