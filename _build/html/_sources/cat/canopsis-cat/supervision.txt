Canopsis Supervision
====================

This document describes how we will supervise *Canopsis* services.
It is intended for both **Canopsis** and **Canopsis HA**.

Prerequisite
------------

You will need to fulfill the following requirements :

 * *Canopsis Sakura*, or newer, installed ;
 * **Canopsis CAT** installed ;
 * SSH key of *Canopsis* user known by your supervisor ;
 * the firewall is configured to allow traffic between your supervisor and *Canopsis*.

Functional overview
------------------

The supervision will be done on both *Canopsis* node and your supervisor.
In order to apprehend correctly this document, we need to define some things :

 * a *Canopsis* node is a machine running *Canopsis* ;
 * the services launched on a *Canopsis* node defines its role.

The key to an efficient supervision is to have well-defined roles for each of your
nodes.

It is recommended to consider these roles :

 * standalone : all services are running ;
 * backend : in HA, only databases are running ;
 * middleware : in HA, only the AMQP bus and the engines are running ;
 * frontend : in HA, only the web server is running.

Many nodes can have the same role, when talking about availability, we will consider
the whole cluster instead of a single node.

Technical overview
------------------

The supervision is split in 3 parts :

 * the services supervision :
    * check that each *Canopsis* service is started ;
    * those checks will be executed directly on *Canopsis* node (via SSH) ;
 * the availability supervision :
    * check that *Canopsis* backend, middleware and frontend are available ;
    * with **Canopsis HA**, check that load balancers and virtual IP addresses are available ;
    * with standalone *Canopsis*, this is done by the services supervision ;
 * the hardware supervision :
    * check that every (virtual) machine is healthy.

In this document, we consider that your are using one of those supervisors :

 * Nagios 3.5.X ;
 * Icinga 1.X ;
 * Centreon ;
 * Shinken.

Services supervision
++++++++++++++++++++

In order to make sure *Canopsis* is at least running, we need to check that some
processes are running.

Here is the list of processes that needs to be checked :

 * mongodb : provides database service ;
 * rabbitmq-server : provides AMQP bus for the engines ;
 * webserver : provides the user interface for *Canopsis* ;
 * collectd : collect data about the system to feed *Canopsis* ;
 * every processes from the *amqp2engines* group : provides the engines.

And for **Canopsis HA**, you will need to check :

 * haproxy : provides load balancing on the node ;
 * keepalived : provides virtual IP address on the node.

This is done by executing a special command, provided by a *supervisord* plugin,
which outputs the process status in the format of a *Nagios* plugin.

Availability supervision
++++++++++++++++++++++++

There is only 3 services that provides an interface to the user (or other *Canopsis*
components) :

 * MongoDB : will serve data for the rest of *Canopsis* ;
 * RabbitMQ : will accept events from the user, and deliver them to the rest of *Canopsis* ;
 * Webserver : will serve the user interface through HTTP.

Those interfaces are provided through the virtual IP address (*keepalived*) when
you are using **Canopsis HA**.

The following checks will be executed :

 * check the state of the MongoDB node ;
 * in HA, check the existence of a primary MongoDB node ;
 * check the state of the RabbitMQ node ;
 * in HA, check the state through the virtual IP address ;
 * check the web server node is reachable through HTTP ;
 * in HA, check the web server through the virtual IP address.

Hardware supervision
++++++++++++++++++++

It is recommended (but not mandatory) to check the following aspects of a machine
used as a *Canopsis* node :

 * PING : will check that the machine is reachable over the network ;
 * Load ;
 * Memory ;
 * Disk usage ;
 * Disk I/O ;
 * Network.

You are free to check more things.

Nagios commands
+++++++++++++++

TODO

Example
+++++++

TODO

Example with HA
+++++++++++++++

TODO
