# 7.4 Troubleshooting Network Issues

Detailed network troubleshooting, which can depend on a number of factors particular to your environment, are beyond the scope of this document. However, communication problems among the various Identity Manager Fan-Out components are often caused by basic issues.

## 7.4.1 IP Connections

To verify IP Connections between platforms and the Core Driver, use the ping command. From a command prompt on the Linux, UNIX or Windows system, use a command prompt to enter ping ipaddr, where ipaddr is the IP address of the remote computer.

## 7.4.2 Firewalls

Firewalls can disrupt connectivity between the Core Driver and its connected systems. To verify that the TCP port is reachable, use a command prompt to enter telnet ipaddr 3451, where ipaddr is the IP address of the remote computer. The TCP port 3451 is used by the Core Driver for communication with the connected platforms.

## 7.4.3 DNS

Check DNS if you are using named hosts in your platform or Core Driver address configurations. DNS resolution is necessary to verify certificates for SSL communication.
