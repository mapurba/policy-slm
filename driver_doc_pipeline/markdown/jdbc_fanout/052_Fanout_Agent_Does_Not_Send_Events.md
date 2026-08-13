# 7.15 Fanout Agent Does Not Send Events

There are no events from the Fanout agent in one of the following conditions:

* The Fanout Agent and the JDBC driver are not pointing to the same ActiveMQ instance, the connection is not established.
* If the events are not available in the Fanout agent.
