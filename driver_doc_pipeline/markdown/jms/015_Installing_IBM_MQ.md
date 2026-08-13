# 4.1 Installing IBM MQ

As part of installing IBM MQ for the driver, you should complete the following tasks consecutively. These instructions are for Windows, but you can follow the same procedure for other platforms.

* [Placing Prerequisite Jar Files and Scripts](installing-ibm-iq.html#b5j6nh4)
* [Creating a Server-Connection Channel and Queues](installing-ibm-iq.html#b5j6qgq)
* [Starting the Publish/Subscriber Broker](installing-ibm-iq.html#b5j6qxp)
* [Installing System Queues Necessary for Publish/Subscribe](installing-ibm-iq.html#b5j6r3a)
* [Creating a User Account](installing-ibm-iq.html#b5j6rdt)
* [Setting Up JMS for IBM MQ 8.x and 9.x](installing-ibm-iq.html#b5j6rjs)

## 4.1.1 Placing Prerequisite Jar Files and Scripts

1. (Conditional) If you are using IBM Websphere version lesser than 8.x, delete the following jars that are located at:

   *Linux:*
   /opt/novell/eDirectory/lib/dirxml/classes

   *Windows:*
   C:\Novell\NDS\lib

   * com.ibm.mq.jar
   * com.ibm.mq.jmqi.jar
   * com.ibm.mqjms.jar
   * connector.jar
   * dhbcore.jar
   * fscontext.jar
   * jndi.jar
   * com.ibm.mq.commonservices.jar
   * com.ibm.mq.headers.jar
2. Locate and copy the following jar files from your messaging server.

   For example, <MQ\_install\_path>\java\lib

   * com.ibm.mq.commonservices.jar
   * com.ibm.mq.headers.jar
   * com.ibm.mq.jar
   * com.ibm.mq.jmqi.jar
   * com.ibm.mqjms.jar
   * fscontext.jar
   * providerutil.jar
3. Download and copy javax-jms-api-2.0.jar from [MVN Repository](https://mvnrepository.com/artifact/javax.jms/javax.jms-api/2.0):
4. Paste the jar files that is mentioned in [Step 2](installing-ibm-iq.html#refer1) and [Step 3](installing-ibm-iq.html#refer2) to the Identity Manager server.

   The following table identifies where to place jar files on an Identity Management server, by platform.

   | Platform | Directory Path |
   | Windows | Local installation: C:\Novell\IdentityManager\NDS\lib  Remote installation: C:\Novell\IdentityManager\RemoteLoader\lib |
   | Linux/UNIX | Local installation: /usr/lib/dirxml/classes (pre-eDirectory 8.8) or opt/novell/eDirectory/lib/dirxml/classes (eDirectory 8.8)  Remote installation: /usr/lib/dirxml/classes (pre-eDirectory 8.8) or /opt/novell/eDirectory/lib/dirxml/classes (eDirectory 8.8) |
5. Restart eDirectory.
6. Locate the installation script that is saved during the JMS driver installation. The following table indicates the default directories where scripts are installed, by platform.

   | Platform | Directory Path |
   | Windows | C:\Novell\IdentityManager\NDS\DirXMLUtilities\jms\webmq |
   | Linux\UNIX | install-dir/lib/dirxml/rules/jms/webmq |
7. Copy the following scripts to your messaging server at <MQ\_install\_path>\java\bin.

   * idm\_jms\_install.scp
   * idm\_jms\_uninstall.scp
   * idm\_mq\_install.mqsc
   * idm\_mq\_uninstall.mqsc
   * netiqsamplejms.prop
   * vinstall.bat
   * vuninstall.bat
8. (Conditional) If necessary, restart your eDirectory server.

## 4.1.2 Creating a Server-Connection Channel and Queues

1. From the command line, change directories to <MQ\_HOME>\java\bin.
2. From the command line, execute the following command:

   runmqsc QM < idm\_mq\_install.mqsc

   This file is provided only as an example; you might need to customize the content.
3. Continue with [Starting the Publish/Subscriber Broker](installing-ibm-iq.html#b5j6qxp).

## 4.1.3 Starting the Publish/Subscriber Broker

1. From the command line, execute the following command:

   strmqbrk -m QM

   You should see a message indicating that the broker is running.
2. Continue with [Installing System Queues Necessary for Publish/Subscribe](installing-ibm-iq.html#b5j6r3a).

## 4.1.4 Installing System Queues Necessary for Publish/Subscribe

1. From the command line, execute the following command:

   runmqsc QM < MQJMS\_PSQ.mqsc

   You should see some tracing, indicating successful queue creation.

   *NOTE:*If you don’t enter this command, you might see the following error: “MQJMS1111: JMS 1.1 The required Queues/Publish Subscribe services are not set up {0} error.”
2. Continue with [Creating a User Account](installing-ibm-iq.html#b5j6rdt).

## 4.1.5 Creating a User Account

* [Creating a User](installing-ibm-iq.html#bgntg7g)
* [Making the User a Member of the mqm Group](installing-ibm-iq.html#bgntgq8)

### Creating a User

1. Click Start > Programs > Administrative Tools > Computer Management.
2. Expand the Local Users and Groups subtree.
3. Right-click the Users folder, then select New User.
4. Specify a user name. The scripts referenced in these instructions assume idm.
5. Specify a password. The scripts referenced in these instructions assume novell.
6. Deselect the User must change password at next login check box.
7. Click the Create button.
8. Click the Close button.
9. Continue with [Making the User a Member of the mqm Group](installing-ibm-iq.html#bgntgq8).

### Making the User a Member of the mqm Group

1. Right-click the newly created user, then click Properties.
2. Select the Member Of tab.
3. Select the mqm group.
4. Click Add.
5. Click OK twice.
6. Continue with [Setting Up JMS for IBM MQ 8.x and 9.x](installing-ibm-iq.html#b5j6rjs).

## 4.1.6 Setting Up JMS for IBM MQ 8.x and 9.x

1. On the MQ server, edit <MQ\_install\_path>\java\bin\JMSAdmin.config, and set the value to the following:

   INITIAL\_CONTEXT\_FACTORY=com.sun.jndi.fscontext.RefFSContextFactoryPROVIDER\_URL=file:/C:/JNDI-Directory

   *NOTE:*Depending on your OS platform adjust the PROVIDER\_URL to point to a valid file location path on the MQ server.
2. Edit <MQ\_install\_path>\java\bin\JMSAdmin.bat file, and set the JAVA envionment variable pointing to the correct location of the java executable under the jre folder set JAVA="%MQ\_JRE\_PATH%\bin\java"
3. Edit <MQ\_install\_path>\java\bin\PSIVTRun.bat file, and set the JAVA envionment variable pointing to the correct location of the java executable under the jre folder.
4. Edit netiqsamplejms.prop file, and set the values as follows:

   | Properties Key | Purpose |
   | IDM\_LOCAL\_USER\_ACCOUNT\_NAME | A local windows user account will be created. This account will be used by the NetIQ JMS connetor to connect to MQ.  Example: IDM |
   | IDM\_LOCAL\_USER\_ACCOUNT\_PWD | Password for the local windows account.  Example: NetIQ123 |
   | IDM\_QUEUE\_MANAGER\_NAME | A queue manager is a program that provides messaging services to applications that use the Message Queue Interface to put and get messages from the queue. This is the name of the Queue Manager under which the IDM queues will be created and controlled.Example: IDM.QM |
   | IDM\_LISTENER\_NAME | A listener is a WebSphere® MQ process that listens for connections to the queue manager. Provide the name for the listener that the above IDM queue manager will be using.Example: LISTENER.TCP |
   | IDM\_WEBMQ\_HOST | This is the hostname or IP address of the server where MQ is running.Example: webmq.lab.com or <IP address> |
   | IDM\_LISTENER\_PORT | This is the listener port where MQ server can accept messages. The default port for MQ is 1414, however each installation can be changed to listen on different ports. Enter the port number that is relevant to your installation.Example: 1414 |
   | IDM\_CHANNEL\_NAME | A channel is a communication link used by distributed queue managers identified by a unique name.Thereare two categories of channel in WebSphere® MQ:  * Message channels: which are unidirectional, and transfer messages from one queue manager to another. * MQI channels: which are bidirectional, and transfer MQI calls from a WebSphere MQ MQI client to aqueue manager, and responses from a queue manager to a WebSphere MQ client.  IDM integtration uses MQI channels. Provide a name that IDM will use.  Example: CHANNEL.IDM.QM |
   | IDM\_DRV\_QUEUE\_NAME | A WebSphere MQ queue is a named object on which applications can put and get messages.Specify a name that uniquely identifies the IDM queue where IDM events are sent and received from.Example: IDM.EVENTSQ |
   | IDM\_DRV\_TOPIC\_NAME | A topic is the subject of the information that is published in a publish/subscribe message. Specify a unique TOPIC name that IDM can use to pub/sub messages.Example: IDM.EVENTSTOPIC |
   | IDM\_DRV\_TOPIC\_STRING | A publisher creates a message, labels it with a topic string that best fits the subject of the publication and then publishers it. To receive publications, a subscriber creates a subscription with a pattern matching topic string to select publication topics.Example: IDM.TOPICSTR |
   | IDM\_JNDI\_PROVIDER\_URL | Sun engineered JNDI like JMS in that there is an API that MQ clients/apps use and an SPI or Service Provider Interface that is used by something called a “registry”. Although JNDI can be implemented in LDAP, one of the base implementations that Sun provided right out of the box was to use the local filesystem as the registry. JNDI uses the .bindings file as the "registry" and it holds all the administered object definitions.  The objects in the .bindings file are represented in Name/Type/Value triplets. Each .bindings file typically has many objects. Each object has many attributes. Each attribute has a name, a value and the type of variable that holds the value. IBM provides the JMSAdmin tool to generate and read the .bindings file. But a valid file system location should be made availble for the JMSAdmin tool where it can create the .bindings file.  Example: C:\JNDI-Directory |
5. In command prompt change location to <MQ\_install\_path>\java\bin\ and run vinstall.bat to create the MQ/JMS objects that will be used by the NetIQ JMS connector.
6. Make sure the .bindings file resides in the correct location.

   The .bindings file is generated during the IBM MQ configuration. When you run the JMSAdmin.bat -v idm\_jms\_install.scp command, the .bindings file is generated under the path specified in the JMSAdmin.config file.

   If the driver, IBM MQ, Identity Manager engine, and Identity Vault are all on the same server, make sure the .bindings file resides in the location specified by the PROVIDER\_URL option for the driver configuration (see [PROVIDER\_URL](driver-configuration.html#bs1qb36)).

   If the driver and IBM MQ are on one server and the Identity Manager engine and Identity Vault are on another server (a Identity Manager server), copy the .bindings file to the Identity Manager server and make sure the PROVIDER\_URL includes the correct path to the file. If multiple Identity Manager servers connect to the IBM MQ server, copy the .bindings file to the PROVIDER\_URL path on each Identity Manager server.
7. Copy .binding file from IBM MQ server location (Example: C:\JNDI-Directory) to Identity Manager server. (Example: C:\JNDI-Directory).
