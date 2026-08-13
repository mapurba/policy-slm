# 4.2 Installing on JBoss Messaging

As part of installing JBoss for the driver, you should copy the jar files as indicated below. The instructions assume that JBoss already has the default queues and topics available. For information on installing and configuring JBoss Messaging, refer to the [JBoss User Guide](http://www.jboss.org/file-access/default/members/jbossmessaging/freezone/docs/userguide-1.3.0.GA/html/index.html).

1. On your messaging server, locate the jar files depending on your JBoss version:

   *For JBoss 4:*
   Locate the following files:

   * concurrent.jar
   * connector.jar
   * javaassist.jar
   * jboss-aop-jdk50.jar
   * jboss-aop-jdk50-client.jar
   * jboss-common-client.jar
   * jboss-messaging.jar
   * jboss-messaging-client.jar
   * jboss-remoting.jar
   * jboss-system-client.jar
   * jnp-client.jar
   * trove.jar

   *For JBoss 6.2:*
   Locate the following files:

   * hornetq-core-client-2.3.3.final.jar
   * hornetq-core.jar
   * hornetq-jboss-as-integration-2.2.9.as7.final.jar
   * jboss-client

   *NOTE:*
   hornetq 2.4(latest)

   Before using this jar, ensure you go through the known issue that exists with it in the [JBoss Developer page](https://issues.jboss.org/browse/HORNETQ-1317).
2. Copy the jar files to the Identity Manager server.

   The following table identifies where to place jar files on an Identity Management server, by platform.

   | Platform | Directory Path |
   | Windows | Local installation: novell\NDS\lib  Remote installation: novell\RemoteLoader\lib |
   | Linux/UNIX | Local installation: /usr/lib/dirxml/classes (pre-eDirectory 8.8) or opt/novell/eDirectory/lib/dirxml/classes (eDirectory 8.8)  Remote installation: /usr/lib/dirxml/classes (pre-eDirectory 8.8) or /opt/novell/eDirectory/lib/dirxml/classes (eDirectory 8.8) |
3. If necessary, restart your eDirectory server.
