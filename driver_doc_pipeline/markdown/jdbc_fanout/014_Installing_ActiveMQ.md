# 2.4 Installing ActiveMQ

You must install ActiveMQ on a server other than the Identity Manager server to avoid port conflict. If you install ActiveMQ on the Identity Manager server, ActiveMQ installed by the User Application and ActiveMQ used by the Fanout agent attempt to use the same default port (61616). To avoid this situation, change the port number to any available port number. This consideration also applies to the Sentinel server.

To install ActiveMQ:

1. Download ActiveMQ 5.15.2 from the [Apache ActiveMQ 5.15.2 Download page](http://activemq.apache.org/activemq-5152-release.html).
2. Unzip the file to a preferred location on your computer.
3. Copy the activemq-all-<version>.jar file from the extracted file to your Identity Manager and Fanout Agent installation directories.

   For example, /opt/novell/eDirectory/lib/dirxml/classes/ or C:\NetIQ\IdentityManager\NDS\lib directory for Identity Manager installation and /opt/novell/dirxml/fanoutagent/lib or C:\NetIQ\IdentityManager\FanoutAgent\lib directory for Fanout agent installation.
4. Restart eDirectory.
