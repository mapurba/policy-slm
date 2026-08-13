# 6.4 Enabling SSL for the Fanout Agent

1. Copy the client.ks and client.ts files to the server where you install the Fanout agent.
2. Open the config file and specify the parameters as follows:

   * *netiq.fanoutagent.connection.truststore.file:*
     Specify the client.ts path. For example, netiq.fanoutagent.connection.truststore.file=/home/keys/client.ts.
   * *netiq.fanoutagent.connection.keystore.file:*
     Specify the client.ks path. For example, netiq.fanoutagent.connection.keystore.file=/home/keys/client.ks.
3. Start the Fanout Agent in Server Only Mode where it accepts only the configuration changes.
4. Set the passwords as follows:

   * setAMQKSPassword -config <fanoutaget\_installdir>/Fanoutagent/config/fanoutagent-config.properties <keystore password> <agent password>
   * setAMQTSPassword -config <fanoutaget\_installdir>/Fanoutagent/config/fanoutagent-config.properties <truststore password> <agent password>
5. Stop and start the Fanout Agent.
