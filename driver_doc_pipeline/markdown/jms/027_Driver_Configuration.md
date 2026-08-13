# A.1 Driver Configuration

In Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Click the driver icon to display the driver’s properties page.

In Designer:

1. Open a project in the Modeler, then right-click the driver line and click Properties > Driver Configuration.

The Driver Configuration options are divided into the following sections:

* [Driver Module](driver-configuration.html#b4jzjxt)
* [Driver Object Password](driver-configuration.html#b4jzp0o)
* [Authentication](driver-configuration.html#b4jzr84)
* [Startup Option](driver-configuration.html#b4m4gci)
* [Driver Parameters](driver-configuration.html#b4m4h9a)
* [ECMAScript](driver-configuration.html#brtl6rb)
* [Global Configurations](driver-configuration.html#brtl75n)

## A.1.1 Driver Module

The driver module changes the driver from running locally to running remotely or the reverse.

*Java:*
Used to specify the name of the Java class that is instantiated for the shim component of the driver. This class can be located in the classes directory as a class file, or in the lib directory as a .jar file. If this option is selected, the driver is running locally.

The name of the Java class is:com.novell.idm.driver.jms.JMSDriverShim

*Native:*
This option is not used with the driver.

*Connect to Remote Loader:*
Used when the driver is connecting remotely to the connected system. Designer includes two suboptions:

* *Remote Loader Client Configuration for Documentation:*
  Includes information on the Remote Loader client configuration when Designer generates documentation for the JMS driver.
* *Driver Object Password:*
  Specifies a password for the Driver object. If you are using the Remote Loader, you must enter a password on this page. Otherwise, the remote driver does not run. The Remote Loader uses this password to authenticate itself to the remote driver shim.

## A.1.2 Driver Object Password

*Driver Object Password:*
Use this option to set a password for the driver object. If you are using the Remote Loader, you must enter a password on this page or the remote driver does not run. This password is used by the Remote Loader to authenticate itself to the remote driver shim.

## A.1.3 Authentication

The Authentication section stores the information required to authenticate to the connected system.

*Authentication ID:*
Specify a user application ID. This ID is used to pass Identity Vault subscription information to the application.

Example: Administrator

*Authentication Context:*
Specify the IP address or name of the server the application shim should communicate with.

*Application Password:*
Specify the password for the user object listed in the Authentication ID field.

*Remote Loader Connection Parameter:*
Used only if the driver is connecting to the application through the Remote Loader.

In Identity Console, enter hostname=xxx.xxx.xxx.xxx port=xxxx secureprotocol=TLS version enforceSuiteB=true/false kmo=certificatename.

* hostname specifies the IP address of the Remote Loader server.
* port specifies the TCP/IP port on which the Remote Loader listens for connections from the remote interface shim. The default port for the Remote Loader is 8090.
* secureprotocol specifies the version of the TLS protocol that the Remote Loader uses to connect to the Identity Manager engine. Identity Manager supports TLSv1, TLS v1\_1, and TLSv1\_2 versions only.
* enforceSuiteB specifies whether the Remote Loader uses Suite B for communicating with the Identity Manager engine. To use Suite B, specify enforceSuiteB=true. The communication supports only TLS version 1.2 version. Communication is not established if the connection has non-Suite B authentication algorithms.
* The kmo entry is optional. Use it only when an SSL connection exists between the Remote Loader and the Identity Manager engine.

  For example: hostname=10.0.0.1 port=8090 kmo=IDMCertificate

*Remote Loader Password:*
Used only if the driver is connecting to the application through the Remote Loader. The password is used to control access to the Remote Loader instance. It must be the same password specified during the configuration of the Remote Loader on the connected system.

*Cache limit (KB):*
Specify the maximum event cache file size (in KB). If it is set to zero, the file size is unlimited. Click Unlimited to set the file size to unlimited in Designer

## A.1.4 Startup Option

The Startup Option section allows you to set the driver state when the Identity Manager server is started.

*Auto start:*
The driver starts every time the Identity Manager server is started.

*Manual:*
The driver does not start when the Identity Manager server is started. The driver must be started through Designer or Identity Console.

*Disabled:*
The driver has a cache file that stores all of the events. When the driver is set to Disabled, this file is deleted and no new events are stored in the file until the driver state is changed to Manual or Auto Start.

*Do not automatically synchronize the driver:*
This option only applies if the driver is deployed and was previously disabled. If this is not selected, the driver re-synchronizes the next time it is started.

## A.1.5 Driver Parameters

The Driver Parameters section lets you configure the driver-specific parameters. When you change driver parameters, you tune driver behavior to align with your network environment.

The parameters are presented by category:

* [Driver Options](driver-configuration.html#bs1pe79)
* [Subscriber Options](driver-configuration.html#bs1r40v)
* [Publisher Options](driver-configuration.html#bs1s8ty)

### Driver Options

*Default JMS version:*
Specifies the API version this driver should use when communicating with message brokers. If you are uncertain, 1.0.2 is the more widely adopted standard.

This setting is global for all message brokers.

*Broker ID:*
Specifies an identifier for this broker by which it is known in the Identity Manager namespace.The default value is WebSphere MQ 6. To use a value other than the default, you need to specify it.

*Show connected-related options:*
Displays connection-related parameters, such as JNDI connection factory names and usernames or passwords. Select show to display the following options.

* *Username:*
  Specify the username to authenticate to the message broker.
* *Password:*
  Specify the password to authenticate to the message broker.

  After entering the password, you need to re-enter it for validation.
* *Show queue connection factory options:*
  Select show to display the queue connection factory options.

  + *JNDI name:*
    Specify the JNDI name of the connection factory used to create the connections to the queues.
* *Show topic connection factory options:*
  Select show to display topic connection factory options.

  + *JNDI name:*
    Specify the JNDI name of the connection factory used to create connections to the topics.
  + *Client ID:*
    Specify the client ID used to create the durable topic subscriptions.

    *NOTE:*Changing this value after durable subscriptions have been defined is not recommended. If it is changed, the Publisher is unable to unsubscribe from existing topic subscriptions unless the client ID is set to the same value the subscriptions were created with.

*Show standard JNDI context properties:*
Select show to display the standard JNDI context properties for this message broker. These properties are primarily used to specify the URL, username, and password used to connect to or authenticate with this broker.

* *INITAL\_CONTEXT\_FACTORY:*
  The name that uniquely identifies this JNDI context property.
* *Value:*
  Specify the name of the Java class used to create a JNDI context for this message broker.
* *PROVIDER\_URL:*
  The name that uniquely identifies this JNDI context property. This contains .binding.file. For example: C:\JNDI-Directory
* *Value:*
  Specify the URL of this message broker. A URL usually contains a protocol, an IP address, and a port number.
* *SECURITY\_CREDENTIALS:*
  The name that uniquely identifies this JNDI context property.
* *Value:*
  Specify the password used to authenticate to this message broker.
* *SECURITY\_PRINCIPAL:*
  The name that uniquely identifies this JNDI context property.
* *Value:*
  Specify the username used to authenticate to this message broker.
* *URL\_PKG\_PREFIXES:*
  The name that uniquely identifies this JNDI context property.
* *Value:*
  Specify the value of this JNDI context property.
* *Show remaining standard properties:*
  Select show to display the remaining, less commonly used standard JNDI context properties.

  + *APPLET:*
    The name that uniquely identifies this JNDI context property.
  + *Value:*
    Specify the name of the applet using used.
  + *AUTHORITATIVE:*
    The name that uniquely identifies this JNDI context property.
  + *Value:*
    The value of this JNDI context property.
  + *BATCHSIZE:*
    The name that uniquely identifies this JNDI context property.
  + *Value:*
    The value of this JNDI context property.
  + *DNS\_URL:*
    The name that uniquely identifies this JNDI context property.
  + *Value:*
    The value of this JNDI context property.
  + *LANGUAGE:*
    The name that uniquely identifies this JNDI context property.
  + *Value:*
    The value of this JNDI context property.
  + *OBJECT\_FACTORIES:*
    The name that uniquely identifies this JNDI context property.
  + *Value:*
    The value of this JNDI context property.
  + *REFERRAL:*
    The name that uniquely identifies this JNDI context property.
  + *Value:*
    The value of this JNDI context property.
  + *SECURITY\_AUTHENTICATION:*
    The name that uniquely identifies this JNDI context property.
  + *Value:*
    The value of this JNDI context property.
  + *SECURITY\_PROTOCOL:*
    The name that uniquely identifies this JNDI context property.
  + *Value:*
    The value of this JNDI context property.
  + *STATE\_FACTORIES:*
    The name that uniquely identifies this JNDI context property.
  + *Value:*
    The value of this JNDI context property.

*Show vendor-specific JNDI context properties:*
Select show to display the vendor-specific JNDI context properties.

* *Name:*
  The name that uniquely identifies this JNDI context property.
* *Value:*
  Specify the value of this JNDI context property.

### Subscriber Options

*Disable subscriber:*
Select Yes to prevent this channel from sending messages to the JMS provider.

*Show default message options:*
Select show to display the options that are global to all messages.

* *Default message expiration (milliseconds):*
  In milliseconds, specify how long messages should live after they reach the destination. This setting is global for all sent messages.
* *Default message priority:*
  Select the priority of the message. The options are:

  + 0 (normal)
  + 1 (normal)
  + 2 (normal)
  + 3 (normal)
  + 4 (normal, default)
  + 5 (expedited)
  + 6 (expedited)
  + 7 (expedited)
  + 8 (expedited)
  + 9 (expedited)

  Specifying expedited delivery can result in “out-of-order” message processing. This setting is global for all sent messages.
* *Default message type:*
  Select the default message type as text or bytes. This setting is global for all sent messages.
* *Show default destination options:*
  Select show to display the parameters that show the properties sent with the message.

  Message properties can be used to prevent message loopback or to pass application-specific information in messages. These properties are global for all sent messages.

  + *Name:*
    Message property names beginning with “JMS” must match those defined by the JMS specification or third-party providers.

    Property names fall into three general categories:

    - Standard JMS properties. They usually begin with JMS or JMSX.
    - Provider-specific properties. They usually begin with JMS\_.
    - Application-specific. Anything else.
  + *Value:*
    The value of the message property.

*Show default destination options:*
Select show to display the options global to all destinations.

* *Default destination type:*
  Select whether all destinations are queues (default) or topics. This setting is global for all destinations.
* *Default omit message envelope:*
  Select whether the JMS message envelope should be omitted from received messages. This setting is global to all destinations.
* *Default receive timeout (seconds):*
  Select how long a channel should wait to receive a response to a sent message. The default value is 10 seconds. Permitted values are no wait and 1-25. This setting is global to all destinations.
* *Default message filter:*
  Select how the destinations filter receives the messages. The options are:

  + Receive all messages
  + Receive messages from this instance
  + Receive messages from this channel
  + Receive messages from the other channel
  + Block messages from this instance (default)
  + Block messages from this channel
  + Block messages from the other channel
  + Specify a custom message selector
* *Default message selector:*
  If you select specify a custom message selector, specify a custom message selector to filter received messages. Message selectors are like SQL WHERE clauses, such as JMSCorrelationID LIKE '%01=whatever%'.

  The % wildcard character can be used to disregard content before or after the part of a header or property value you are interested in filtering on. When used in tandem with a message filter, the message selector is appended to the end of the filter by using an AND operator.

*Destination unique id:*
Specify the identifier for this destination by which it is known in the Identity Manager namespace. This name is also the durable subscription name for topics. This value must be unique per channel (Subscriber/Publisher).

*Show additional destination options:*
Select show to display additional options for this selected destination.

* *Destination JNDI name:*
  Specify the identifier for this destination that is known in the JNDI namespace. This might not be the name the destination is known by to the broker. This value does not need to be unique.
* *Destination type:*
  Select whether the destination type is inherited, a topic, or a queue.
* *Destination mode:*
  Select whether the destination is used to send or receive messages.
* *Message type:*
  Select whether messages are sent as a text or as bytes.
* *Show message properties:*
  Select show to display message properties sent with messages. Message properties can be used to prevent message loopback or pass provider or application-specific information along with messages.

  + *Name:*
    The message property names beginning with JMS must match those defined by the JMS specification or third-party providers. Property names fall into three general categories:

    - Standard JMS properties. They usually begin with JMS or JMSX.
    - Provider-specific properties. They begin with JMS\_.
    - Application-specific. Anything else.
  + *Value:*
    Specify the value of the message property.

*Destination unique id:*
Specify the identifier by which this destination is known in the Identity Manager namespace. This name is also the durable subscription name for topics. This value must be unique per channel (Subscriber/Publisher).

*Show additional destination options:*
Select show to display additional options for this selected destination.

* *Destination JNDI name:*
  Specify the identifier by which this destination is known in the JNDI namespace. This might or might not be the name the destination is known by to the message broker.

  This value does not need to be unique.
* *Destination type:*
  Select whether the destination is inherited, a queue, or a topic.
* *Destination mode:*
  Select whether the destination is used to send or receive messages.
* *Omit message envelope:*
  Select whether the JMS message envelope is omitted from messages received by this destination.
* *Receive timeout (seconds):*
  Select how long a channel should wait to receive a response to a sent message. The default value is 10 seconds. Permitted values can range from 1-25.
* *Message filter:*
  Select how this destination filter receives messages. The options are:

  + Receive all messages
  + Receive messages from this instance
  + Receive messages from this channel
  + Receive messages from the other channel
  + Block messages from this instance (default)
  + Block messages from this channel
  + Block messages from the other channel
  + Specify a custom message selector
* *Message selector:*
  If you selected specify a custom message selector, specify a custom message selector to filter received messages. Message selectors are like SQL WHERE clauses, such as JMSCorrelationID = whatever. When used in tandem with a message filter, the message selector is appended to the end of the filter by using an AND operator.

### Publisher Options

*Disable publisher:*
Select Yes to prevent this channel from sending messages to the JMS provider.

*Heartbeat interval (minutes):*
Specifies how many minutes of inactivity should elapse before this channel sends a heartbeat document. In practice, more than the number of minutes specified can elapse. That is, this parameter defines a lower bound.

*Show default message options:*
Select show to display options global to all messages.

* *Default message expiration (milliseconds):*
  Specify how long the messages live after they reach a destination. Specify the time duration in milliseconds. 0 means the message lives indefinitely. This setting is global for all sent messages.
* *Default message priority:*
  Select the priority of the message. The options are:

  + 0 (normal)
  + 1 (normal)
  + 2 (normal)
  + 3 (normal)
  + 4 (normal, default)
  + 5 (expedited)
  + 6 (expedited)
  + 7 (expedited)
  + 8 (expedited)
  + 9 (expedited)

  Specifying expedited delivery can result in “out-of-order” message processing. This setting is global for all sent messages.
* *Default message type:*
  Select whether the messages type is text or bytes. This setting is global for all sent messages.
* *Show default message properties:*
  Select show to display the parameter that specifies the properties sent with messages.

  Message properties can be used to prevent message loopback or pass application-specific information in messages. These properties are global for all sent messages.

  + *Name:*
    The message property names beginning with JMS must match those defined by the JMS specification or third-party providers. Property names fall into three general categories:

    - Standard JMS properties. They usually begin with JMS or JMSX.
    - Provider-specific properties. They begin with JMS\_.
    - Application-specific. Anything else.
  + *Value:*
    Specify the value of the message property.

*Show default session options:*
Select show to display options that are global to all sessions.

* *Default message acknowledgement threshold:*
  Specify how many messages are received by a monitored destination before an acknowledgement is sent to the broker.

*Show default destination options:*
Select show to display options that are global to all destinations.

* *Default destination type:*
  Select whether the default destination type is a queue (default) or a topic.
* *Default omit message envelope:*
  Select whether the JMS message envelope is omitted from the received messages. This setting is global for all destinations.
* *Default receive timeout (seconds):*
  Select how long a channel waits to receive a response to a sent message. The default value is 10 seconds. The permitted values range from 1-25 seconds.
* *Default message filter:*
  Select how the destination’s filter receives the messages. The options are:

  + Receive all messages
  + Receive messages from this instance
  + Receive messages from this channel
  + Receive messages from the other channel
  + Block messages from this instance (default)
  + Block messages from this channel
  + Block messages from the other channel
  + Specify a custom message selector
* *Default message selector:*
  If you selected specify a custom message selector, specify a custom message selector to filter received messages. Message selectors are like SQL WHERE clauses, such as JMSCorrelationID LIKE '%01=whatever%'.

  The % wildcard character is used to disregard content before or after the part of a header or property value you are interested in filtering on. When used in tandem with a message filter, the message selector is appended to the end of the filter by using an AND operator.
* *Default polling interval (milliseconds):*
  Specify how often the destinations are polled for new messages (in milliseconds).

*Destination unique id:*
Specify the identifier by which this destination is known in the Identity Manager namespace. This name is also the durable subscription name for topics. This value must be unique per channel (Subscriber/Publisher).

*Show additional destination options:*
Select show to display parameters for this selected destination.

* *Destination JNDI name:*
  Specify the identifier for this destination that is known in the JNDI namespace. This might not be the name the destination is known by to the broker. This value does not need to be unique.
* *Destination type:*
  Select whether the destination type is inherited, a topic, or a queue.
* *Destination mode:*
  Select whether the destination is used to send or receive messages.
* *Message type:*
  Select whether messages are sent as a text or as bytes.
* *Show message properties:*
  Select show to display message properties sent with messages. Message properties can be used to prevent message loopback or pass provider or application-specific information along with messages.

  + *Name:*
    The message property names beginning with JMS must match those defined by the JMS specification or third-party providers. Property names fall into three general categories:

    - Standard JMS properties. They usually begin with JMS or JMSX.
    - Provider-specific properties. They begin with JMS\_.
    - Application-specific. Anything else.
  + *Value:*
    Specify the value of the message property.

## A.1.6 ECMAScript

Displays an ordered list of ECMAScript resource files. The files contain extension functions for the driver that Identity Manager loads when the driver starts. You can add additional files, remove existing files, or change the order in which the files are executed.

## A.1.7 Global Configurations

Displays an ordered list of Global Configuration objects. The objects contain extension GCV definitions for the driver that Identity Manager loads when the driver is started. You can add or remove the Global Configuration objects, and you can change the order in which the objects are executed.
