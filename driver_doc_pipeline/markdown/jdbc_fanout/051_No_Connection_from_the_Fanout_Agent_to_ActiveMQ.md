# 7.14 No Connection from the Fanout Agent to ActiveMQ

The Fanout agent is not able to establish a connection with ActiveMQ when one of the following conditions exist:

* ActiveMQ instance's IP address or port are not correctly configured in the Fanout agent or the JDBC driver configuration.
* The previous session of the Fanout agent or the JDBC driver is not properly stopped.
