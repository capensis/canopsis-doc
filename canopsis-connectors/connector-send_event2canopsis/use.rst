.. _connectors_send-event2canopsis_use:

Use
===

.. code-block:: bash

   C:\connector-send_event2canopsis>powershell ./connector-send_event2canopsis.ps1 -h
    Usage: send_event
   
    Options:
     -s [SERVER_ADDR]
             webserver address scheme://ip:port (default : http://localhost:8082)
     -a [AUTHKEY]
     -f [FILE_PATH]
            file contraining a json event to send
     -j [JSON]
            a json string containing a correct event to send
     -t
            timeout in second (default: 2000)
     -v
            show debug
     -vv
            show more debug
     -h
            show help

Example
=======

.. code-block:: bash

    C:\connector-send_event2canopsis>type testevent.json
    {"connector" : "MyConnector","connector_name": "MyConnectorName","source_type": "resource","event_type": "check","component": "MyComponent","resource": "MyResource","state": 0,"output": "My Output", "perf_data": "mymetric=45s;0;100;80;90;"}

To send that json event, use this command line :

.. code-block:: bash

    C:\connector-send_event2canopsis>powershell c:\connector-send_event2canopsis/connector-send_event2canopsis.ps1 -s http://IP -a authkey -f c:\connector-send_event2canopsis/testevent.json
    Sending done


To see verbose output,

.. code-block:: bash

    C:\connector-send_event2canopsis>powershell c:\connector-send_event2canopsis/connector-send_event2canopsis.ps1 -s http://IP -a authkey -f c:\connector-send_event2canopsis/testevent.json -v
    Initial Doc: {"connector":"MyConnector","connector_name":"MyConnectorName","source_type":"resource","event_type":"check","component":"MyComponent","resource":"MyResource","state":0,"output":"My Output","perf_data":"mymetric=45s;0;100;80;90;"}
    JSON Final: {"connector":"MyConnector","connector_name":"MyConnectorName","source_type":"resource","event_type":"check","component":"MyComponent","resource":"MyResource","state":0,"output":"My Output","perf_data":"mymetric=45s;0;100;80;90;"}
    Auth Cookie: beaker.session.id=b2a501c2ae73ae0eda12b8ee9142c4b48eeefe62555a893fe8fd18a5b924656cb41eda3f
    Post Params: {"event":"{\"connector\":\"MyConnector\",\"connector_name\":\"MyConnectorName\",\"source_type\":\"resource\",\"event_type\":\"check\",\"component\":\"MyComponent\",\"resource\":\"MyResource\",\"state\":0,\"output\":\"My Output\",\"perf_data\":\"mymetric=45s;0;100;80;90;\"}"}
    Buffer: 123 34 101 118 101 110 116 34 58 34 123 92 34 99 111 110 110 101 99 116
    111 114 92 34 58 92 34 77 121 67 111 110 110 101 99 116 111 114 92 34 44 92 34 9
    9 111 110 110 101 99 116 111 114 95 110 97 109 101 92 34 58 92 34 77 121 67 111
    110 110 101 99 116 111 114 78 97 109 101 92 34 44 92 34 115 111 117 114 99 101 9
    5 116 121 112 101 92 34 58 92 34 114 101 115 111 117 114 99 101 92 34 44 92 34 1
    01 118 101 110 116 95 116 121 112 101 92 34 58 92 34 99 104 101 99 107 92 34 44
    92 34 99 111 109 112 111 110 101 110 116 92 34 58 92 34 77 121 67 111 109 112 11
    1 110 101 110 116 92 34 44 92 34 114 101 115 111 117 114 99 101 92 34 58 92 34 7
    7 121 82 101 115 111 117 114 99 101 92 34 44 92 34 115 116 97 116 101 92 34 58 4
    8 44 92 34 111 117 116 112 117 116 92 34 58 92 34 77 121 32 79 117 116 112 117 1
    16 92 34 44 92 34 112 101 114 102 95 100 97 116 97 92 34 58 92 34 109 121 109 10
    1 116 114 105 99 61 52 53 115 59 48 59 49 48 48 59 56 48 59 57 48 59 92 34 125 3
    4 125 - Buffer Length:  275
    Sending done


