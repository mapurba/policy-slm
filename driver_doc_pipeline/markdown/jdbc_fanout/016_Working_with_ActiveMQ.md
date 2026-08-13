# 2.6 Working with ActiveMQ

You can perform several management tasks by using ActiveMQ. For example:

*Change default port*
: To change the default ports, perform the following steps:

1. Navigate to <AMQ Installation Directory>/conf/activemq.xml.
2. In a text editor, open activemq.xml.
3. Under <transportConnectors>, change the ports as required.

   For example, change the port from 61616 to a different port for TCP protocol:

   ```
   <transportConnector name="openwire" uri="tcp://0.0.0.0:61616?maximumConnections=1000&amp;wireFormat.maxFrameSize=104857600"/>
   ```

*Change Web console port:*
To change the Web console port, complete the following steps:

1. Navigate to <AMQ Installation Directory>/conf/jetty.xml.
2. Open the jetty.xml file in a text editor.
3. Change the Web console port from 8161 to a different port.
4. Save the jetty.xml file.

*Monitor the queues managed by the Fanout Agent:*
To view the queues managed by the Fanout agent, specify https://<ActiveMQ IP Address/servername>:<Port>/admin/queues.jsp in the address bar of your browser. For example: https://192.168.0.1:8161/admin/queues.jsp.
