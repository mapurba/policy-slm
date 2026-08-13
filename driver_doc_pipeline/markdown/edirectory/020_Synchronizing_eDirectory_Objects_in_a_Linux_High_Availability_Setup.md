# 8.2 Synchronizing eDirectory Objects in a Linux High Availability Setup

To start the user synchronization immediately after a failover in the Linux High Availability cluster, change the eDirectory driver configuration:

1. Set the Receive timeout in minutes option in Publisher options to a smaller value.
2. Delete the port number from the Authentication Context and specify two different ports in the Subscriber and Publisher settings.
3. In the Subscriber settings, go to the Advanced options, select the Socket local bind option and specify the IP address in the Local bind address for the subscriber socket option.

   This is the IP address where eDirectory is listening. You must specify the IP address if there are multiple IP addresses in the high availability setup.
4. Specify the same IP address that you specified in the Local bind address for the subscriber socket option in the Publisher settings.
