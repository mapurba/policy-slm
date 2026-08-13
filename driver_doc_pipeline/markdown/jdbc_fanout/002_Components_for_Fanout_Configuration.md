# 1.1 Components for Fanout Configuration

The Fanout driver relies on the following independent components. [Figure 1-1](components-to-configure-identity-manager-jdbc-fan-out-driver.html#t482udtdrl0g) shows how these components work together.

* *Fanout Driver Shim:*
  The Fanout driver shim is a Java-based interface driver. The driver shim virtually connects to the Fanout agent through ActiveMQ.
* *ActiveMQ:*
  The Fanout driver and the Fanout agent use ActiveMQ for transferring the Subscriber events, configuration data, and the queries. The Fanout agent creates a separate queue for each JDBC driver instance. The JDBC driver instances wait for the events in their respective queues. For information about installing ActiveMQ, see [Working with ActiveMQ](how-to-use-activemq-with-jdbc-fan-out-driver.html). To manage the ActiveMQ queues, launch the URL: http://<ActiveMQ IP Address>:8161/admin/queues.jsp.
* *Fanout Agent:*
  The Fanout agent is a standalone Java process that works independently of the Identity Vault. The Fanout agent loads the JDBC driver instances based on the configuration of the connection objects in the Fanout driver. For more information about the connection objects, see [Driver Concepts](jdbc-fan-out-driver-concepts.html).

  The Fanout agent provides an interface through REST endpoints for performing basic monitoring and management tasks. To ease the initial deployment, the Fanout agent auto-initializes with the default configuration values when it is started for the first time. To change the default settings, use the REST endpoints. For more information about REST endpoints supported for the driver, see [Section D.0, REST Endpoints](the-jdbc-fan-out-rest-endpoints.html). The driver installation folder contains sample scripts that you can run to manage the Fanout agent. The sample scripts internally use the REST endpoints. For more information, see [Managing the Fanout Agent](how-to-manage-jdbc-fan-out-agent.html).

  Alternatively, you can manually edit the configuration file. This method requires you to restart the Fanout agent for the changes to take effect. However, this is not required for all the changes made through the REST endpoints. To understand which changes need a restart of the Fanout agent, see [Generating the Default Configuration File](how-to-generate-the-default-configuration-file.html).

*Figure 1-1* Identity Manager JDBC Fanout Driver Architecture

![](../graphics/architecture_diagram_fanout driver .png)

The Fanout process works as follows:

1. The Identity Vault stores the connection object configuration. The configuration includes connection, authentication, and trace information.
2. The Fanout driver receives the initialization document from the engine.
3. The Fanout driver and the Fanout agent perform a handshake to establish a connection. This signals the start of the communication between the agent and the driver. The handshake is done through challenge-response sets.
4. The Fanout driver queries the Identity Vault for the connection objects associated with this driver and creates multiple initialization documents based on the content in the connection objects.
5. The Fanout driver sends the initialization documents to the Fanout agent through ActiveMQ.
6. The Fanout agent loads the JDBC driver instances.
7. The Fanout driver sends the events to the Fanout agent through ActiveMQ.
8. The Fanout agent determines which JDBC driver instances this event should be sent to.
9. The JDBC driver processes the event and sends the status of the event to the Fanout agent, which in turn sends this information to the Fanout driver through ActiveMQ.
10. The Fanout driver sends this status to the Identity Manager engine.

*NOTE:*Only one flavour of database can be managed per agent. For example: only Oracle databases or only MS SQL databases on a single agent.
