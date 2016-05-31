.. _TR__sql2canopsis:

============
sql2canopsis
============

Connector ``sql2canopsis`` description.

.. contents::
   :depth: 2

-------
Updates
-------

.. csv-table::
   :header: "Author(s)", "Date", "Version", "Summary", "Accepted by"

   "Thomas Gosselin", "2016/04/15", "0.1", "Creation", ""

--------
Contents
--------

.. _TR__Title__Sql:

Sql requests
------------


Sql requests execution
>>>>>>>>>>>>>>>>>>>>>>

The connector executes the request from sampleconf.ini

Event creation
--------------

Event creation
>>>>>>>>>>>>>>

The connector creates events and publishes them in rabbitmq

Class Application
>>>>>>>>>>>>>>>>>

Application class:
~~~~~~~~~~~~~~~~~~

Attributes:

- argparser instance of ArgumentParser
- config instance of ConfigParser from ConfigParser
- engine create_engine from sqlalchemy
- conn connection to sql engine

Methods
~~~~~~~

.. code-block:: python

    def sql_connect(self):
        """
            Method to etablished a connection to the database

            :return: a boolean
        """


    def sql_query(self):
        """
            Method to execute sql query in the database
            :return: a list with differents rows
        """

    def gen_events(self, items):
        """
            Method to generate event
            :param items: sql query results.
            :return: events
        """

    def states_objects(self, info_state):
        """
            Methode to get differents name of things to get states

            :param info_state: a list with tuples

            :return: a list with names
        """

    def not_in(self, name, alist):
        """
            Method to check if an element is in a list

            :param name: an element
            :param alist: a list of element
            :return: a boolean
        """

    def get_state(self, info_state, actualstate):
        """
            Get information to have different values to generate a state

            :param info_state: a list with informations
            :param actualstate: the state before the check

            :return: a state to put in the event
        """

    def state(self, value, minor_min, minor_max, maj_min, maj_max, crit_min,   crit_max):
        """
            Generate a state with informations

            :param value:
            :param minor_min
            :param minor_max
            :param maj_min
            :param maj_max
            :param crit_min
            :param crit_max

            :return: a state 0, 1, 2, 3
        """

    def amqp_publish(self, events):
        """
            Publish an event on amqp

            :param events: an event to publish
            :return: a boolean
        """
