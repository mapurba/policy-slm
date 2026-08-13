# 3.2 Starting the Fanout Agent

You can start the Fanout agent by passing the startAgent command in the command prompt or by using the startup script, which enables the agent as a startup service.

Before starting the Fanout agent, ensure that your server meets the following requirements:

* ActiveMQ is running.

  This allows the Fanout agent to initialize the required queues in ActiveMQ when the agent starts. If ActiveMQ is not running, the agent returns an error and does not start properly.
* The Java and Curl tool are included in the system path of your operating system.

  You use Java and Curl tool to manage the Fanout agent. If Curl is not present in your environment, download the SSL version of the Curl binary from [Curl Releases and Downloads](http://curl.haxx.se/download.html).
* Copy the appropriate third-party JDBC connector to the lib directory of the Fanout agent default installation folder. For example, ojdbc6.jar. For more information, see the [Supported Third Party JDBC Drivers](https://www.netiq.com/documentation/idm45drivers/jdbc/data/b667eza.html) in the [NetIQ Identity Manager Driver for JDBC Implementation Guide](https://www.netiq.com/documentation/idm45drivers/jdbc/data/bookinfo.html).

To start the Fanout Agent in the command prompt:

1. Open a command prompt.
2. Run the startAgent command and pass the default configuration file name as a parameter in the command.

   startAgent –config <FanoutAgent Installation Location>/config/fanoutagent-config.properties

   The installation path will vary depending on the Fanout agent version you are running.
3. (Optional) To change the agent and the shim passwords, use the setPassword command.

   The default passwords are netiq. For more information, see [Managing the Fanout Agent](how-to-manage-jdbc-fan-out-agent.html).
4. (Optional) To change the keystore password, use the setKSPassword command.

   The default password for the keystore is netiq123.
5. (Optional) To change the encryption key, use the setEncryptionKey command.

   The default value for the key is netiq.
6. (Optional) Establish a secure connection between the Fanout agent and ActiveMQ. For more information, see [Section 6.0, Securing Fanout Driver Communication](how-to-establish-ssl-communication-between-identity-manager-and-jdbc-fan-out-driver.html).

*IMPORTANT:*Ensure that you specify the same values for these parameters during Fanout driver configuration.

To enable the Fanout agent service to automatically start when the system starts, perform the following actions for your platform:

Linux:

1. Set the JAVA\_HOME environment variable.
2. Copy the fanoutdxml file from /opt/novell/dirxml/fanoutagent/bin to /etc/init.d.
3. Run the fanoutAgentAddSvc file from /opt/novell/dirxml/fanoutagent/bin by executing the following command:

   ./fanoutAgentAddSvc
4. Start the Fanout agent service by executing the following command:

   /etc/init.d/fanoutdxml start

To stop the Fanout agent service, execute the following command:

/etc/init.d/fanoutdxml stop

Windows:

1. Set the JAVA\_HOME environment variable.
2. Run vcredist\_x64.exe file from C:\NetIQ\IdentityManager\FanoutAgent\bin.
3. Install the Fanout agent service by executing the following command:

   ```
   C:\NetIQ\IdentityManager\FanoutAgent\bin\FanoutAgentSvc.exe –i
   ```

   The display name of the service is Fanout Agent Service.

   *NOTE:*If both ActiveMQ and Fanout agent services are running on the same server, ensure that ActiveMQ service starts before the Fanout agent service. To set the Fanout agent service to a delayed start, run the following command on Windows:

   ```
   sc config FanoutAgent start= delayed-auto
   ```
4. Start the Fanout agent service.

To remove the Fanout agent service on Windows, execute the following command:

C:\NetIQ\IdentityManager\FanoutAgent\bin\FanoutAgentSvc.exe –u

*IMPORTANT:*You can run only one Fanout agent instance on a specific server as a service. However, if you run a Fanout agent as an application, Identity Manager allows you to run multiple instances of the Fanout agent on the same server by using separate configuration files.

The Fanout agent service loads the configuration properties only from C:\NetIQ\IdentityManager\FanoutAgent\config path. Ensure that the configuration properties file name is fanoutagent-config.properties (default file name).

A Fanout agent instance that is started as a service must be stopped as a service only. This means that you should not stop the agent using the stopAgent command or REST endpoint if it is started as a service.
