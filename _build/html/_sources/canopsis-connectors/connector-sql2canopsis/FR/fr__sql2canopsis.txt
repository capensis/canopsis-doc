.. _FR__sql2canopsis:

============
sql2canopsis
============

connector-sql2canopsis is a script that execute sql queries and publish resultats to Canopsis/AMQP.

.. contents::
   :depth: 2

Updates
=======

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "Thomas Gosselin", "2016/04/14", "1.0", "Creation", " "

Contents
========

.. _FR__sql2canopsis__Desc:

Description
-----------

Connector-sql2canopsis is a script that execute sql queries and publish results to Canopsis/AMQP.

Each line recovered by the connector will generate an event in canopsis.

Bounds can be parameterized to generate event states.

.. _FR__sql2canopsis__Desc:

Test
----

To realize the functionnal test of sql2canopsis, you have to create a database like explained in the Readme.

In this Database, create a table users:

.. code-block:: sql

	CREATE TABLE IF NOT EXISTS users (name VARCHAR(20),nickname VARCHAR(20), age INTEGER, size INTEGER);

To check all states we can insert 4 people:

.. code-block:: sql

	INSERT INTO users VALUES ('test_one', 'info', 19, 140);
	INSERT INTO users VALUES ('test_two', 'minor', 19, 160);
	INSERT INTO users VALUES ('test_three', 'major', 13, 140);
	INSERT INTO users VALUES ('test_four', 'critical', 2, 230);

Use this sampleconf.ini

.. code-block:: shell

	[database]

	url=yourdatabase://user:password@localhost:3306/base
	query=SELECT * FROM users

	[amqp]

	url=amqp://cpsrabbit:canopsis@localhost:5672/canopsis

	[event]

	connector.constant=edc2canopsis
	connector_name.constant=sql2canopsis
	event_type.constant=check
	source_type.constant=resource
	component.value=name
	resource.value=name
	output.value=age
	age.metrictype=GAUGE
	age.metric.min=18:
	age.metric.maj=15:
	age.metric.crit=5:
	age.metric.value=age
	size.metrictype=GAUGE
	size.metric.min=150
	size.metric.maj=175
	size.metric.crit=200
	size.metric.value=size

When you run this test with  command:

.. code-block:: shell

	python connector-sql2canopsis.py -c sampleconf.ini

4 events are created and sent to canopsis.
Each event has a different state.



