# 6.2 Enabling SSL for ActiveMQ

1. Copy the files broker.ks and broker.ts to the server where ActiveMQ is installed.
2. Edit the activemq.xml file.

   1. Navigate to the <AMQ install path>/conf/ folder and open the activemq.xml file.
   2. Add the transport connector to enable SSL in the transportConnectors section.

      <transportConnector name="ssl" uri="ssl://0.0.0.0:61617?trace=true"/>
   3. Add the keystore or truststore paths and their passwords in the sslContext section.

      <sslContext> <sslContext keyStore="file:///root/activemqkeystore/broker.ks" keyStorePassword="novell" trustStore="file:///root/activemqkeystore/broker.ts" trustStorePassword="novell"/> </sslContext>
3. Restart ActiveMQ.

*NOTE:*For more information about enabling secure transport on ActiveMQ, see [Using Spring to configure SSL for a Broker instance](http://activemq.apache.org/how-do-i-use-ssl.html).
