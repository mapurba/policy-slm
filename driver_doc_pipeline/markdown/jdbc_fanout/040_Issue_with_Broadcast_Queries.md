# 7.3 Issue with Broadcast Queries

When you issue a dxcmd query without a specific instance to the driver, the driver sends the query to all the instances. This is not the case if the driver is configured to run with the Subscriber Service channel, where the queries are routed through this channel.
