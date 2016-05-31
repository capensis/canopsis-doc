.. _connectors_send-event2canopsis_setup:

`connector-send_event2canopsis` is a script that execute a powershell script and publish an event given as argument to Canopsis/REST API

Setup
=====

Requirements
------------

Requirements :

`connector-send_event2canopsis` is based on Powershell and can be executed by powershell v2.x and >= 3.x
Pay attention, 2 scripts exist depending on powershell's version.

connector-send_event2canopsis for powershell >= 3.x used cmdlet :
* ConvertTo-JSON,
* ConvertFrom-Json,
* Invoke-WebRequest.

To install the connector, just copy the ps1 file into a directory on your windows machine.

.. code-block:: bash

 C:\connector-send_event2canopsis>dir
 Volume in drive C has no label.
 Volume Serial Number is xxx

 Directory of C:\connector-send_event2canopsis

 01/03/2016  11:05    <DIR>          .
 01/03/2016  11:05    <DIR>          ..
 01/03/2016  09:35             7 081 connector-send_event2canopsis.ps1
 01/03/2016  10:13               238 testevent.json
                2 File(s)          7 319 bytes
                2 Dir(s)   1 973 293 056 bytes freeœ


