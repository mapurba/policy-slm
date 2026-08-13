# 3.1 Generating the Default Configuration File

When you run the Fanout agent without any options, the agent creates the default configuration file and then stops running. To run the Fanout agent, execute one of the following commands based on your platform:

* *Linux:*
  ./startAgent
* *Windows:*
  startAgent.bat

The Fanout agent creates the following directories in default installation path of the Fanout agent:

* *config:*
  This directory contains the default configuration file for the Fanout agent. The following table lists the parameters included in the default configuration file. Except netiq.fanoutagent.connection.url, you can leave other parameters unchanged. Specify the URL of the ActiveMQ instance in this parameter.

  | Parameter | Description |
  | netiq.fanoutagent.trace.level | Fanout Agent trace level. Range 1-5. Setting the value of this parameter to 3 provides most of the XML and operation traces. |
  | netiq.fanoutagent.trace.file | Path of the Fanout agent trace file. |
  | netiq.fanoutagent.instance.name | Name of the Fanout agent instance. |
  | netiq.fanoutagent.connection.url | Connection URL of the ActiveMQ instance. |
  | netiq.fanoutagent-config.recv.queue | Configuration queue to receive the initialization parameters. |
  | netiq.fanoutagent-config.snd.queue | Configuration queue to query specific configurations. |
  | netiq.fanoutagent-query.in.recv.queue | Query-in queue to receive query responses from the Identity Vault. |
  | netiq.fanoutagent-query.in.send.queue | Query-in queue to send queries to the Identity Vault. |
  | netiq.fanoutagent-sub.event.recv.queue | Subscriber event queue to receive the Subscriber events. |
  | netiq.fanoutagent-sub.event.send.queue | Subscriber event queue to send the Subscriber event status. |
  | netiq.fanoutagent-sub.delayed.event.send.queue | Subscriber event queue to send the status of the delayed event. |
  | netiq.fanoutagent-query.out.recv.queue | Query-out queue to receive the query for the agent. |
  | netiq.fanoutagent-query.out.send.queue | Query-out queue to send the query response. |
  | netiq.fanoutagent.cmd.trace.level | Trace level for the Fanout command server. |
  | netiq.fanoutagent.cmd.srv.ip | IP address to which the command server establishes connection with. This helps you to restrict the command server to listen to a specific interface. |
  | netiq.fanoutagent.cmd.srv.port | Port number on which the command server listens. |
  | netiq.fanoutagent.cmd.trace.file.count | Number of trace files available for the command server. After the limit is reached, the older file are automatically deleted. |
  | netiq.fanoutagent.cmd.allow.http | Parameter to disable https on the command server. |
  | netiq.fanoutagent.cmd.trace.file.size | Size of the Fanout agent command server trace files in MB. |
  | netiq.fanoutagent.cmd.keystore.file | Path to the keystore used by the command server. |
  | netiq.fanoutagent.cmd.trace.dir | The directory where the Fanout agent command server traces are created. |
  | netiq.fanoutagent.connection.truststore.file | Path to the truststore file used for mutual authentication for a secure connection. |
  | netiq.fanoutagent.connection.keystore.file | Path to the keystore file used for mutual authentication for a secure connection. |
  | netiq.fanoutagent.connection.enforceSuiteB | The default setting is false. This means that the Fanout agent does not use Suite B cryptographic algorithms to communicate with the Fanout driver.  *NOTE:*This parameter is included in Fanout agent 1.1. |
  | netiq.fanoutagent.connection.secureprotocol | Version of the TLS protocol that the Fanout agent uses to connect to the Fanout driver. The Fanout agent supports TLSv1, TLSv1\_1, and TLSv1\_2.  *NOTE:*This parameter is included in Fanout agent 1.1. |
  | netiq.fanoutagent-sub.event.max.retry | The maximum limit for retrying an event. The default value is -1. This allows the JDBC instance running in the Fanout agent to retry an event for every 30 seconds until a success or an error is received from the JDBC driver shim.  If you want a JDBC instance to retry an event for a finite number of times until a success or an error is received from the driver shim, set the parameter to a value greater than or equal to zero.  For example, when you set the value to 3, the instance retries an event three times. If the instance receives a retry status after the retry limit has been exhausted, the Fanout agent discards that event and returns an error status to the Identity Manager engine.  *NOTE:*The retrying of events in one instance does not affect the event processing in other instances running in the Fanout agent. |

  You can change the default configuration of the Fanout agent to suit your requirement. Changes are dynamically reflected in some parameters. For changes to take effect in other parameters, restart the Fanout agent. The following parameters are dynamically reflected:

  + netiq.fanoutagent.trace.level
  + netiq.fanoutagent.trace.file
  + netiq.fanoutagent.cmd.trace.level
  + netiq.fanoutagent.cmd.trace.file.count

  Password changes are dynamically reflected. For example, agent password values is changed dynamically. For future commands, you must use the new agent password.

  *NOTE:*If you run the Fanout agent without any options after customizing the default configuration file, the agent will overwrite the changes made to the parameters. NetIQ recommends that you rename the configuration file to a different name to avoid overwriting the file and use the renamed file for subsequent operations.
* *logs:*
  This directory contains the trace files.
* *tmp:*
  This directory contains the temporary files created by the Fanout agent.

The Fanout agent also creates .profile file under the root folder. This file contains information about the Fanout installation directory and the current Java path that is used by the Fanout agent. The following example is a .profile file:

```
JAVA_HOME=/opt/novell/jdk1.7.0_25/jre
PATH=$PATH:/opt/novell/jdk1.7.0_25/jre/bin
FANOUTHOME=/opt/novell/mysql-fanout/agent
```

*NOTE:*For multiple Fanout agents, you require equal number of ActiveMQs. If you are using the same ActiveMQ with multiple Fanout agents, you need to manually clean the ActiveMQ queues before using that ActiveMQ with a different Fanout agent. To clean an ActiveMQ queue, use ActiveMQ Web console. ActiveMQ also provides other options for cleaning the queues. For more information, see [ActiveMQ documentation](http://activemq.apache.org/how-do-i-purge-a-queue.html).
