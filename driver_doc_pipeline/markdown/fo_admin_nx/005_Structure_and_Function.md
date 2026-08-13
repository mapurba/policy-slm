# 2.0 Structure and Function

There are two structural divisions of the NetIQ® Identity Manager Fan-Out Driver: the Core Driver and Platform Services.

*Figure 2-1* Fan-Out Driver Components

![](../graphics/comp_a.gif)

The Core Driver provides Authentication Services and information about changes to users and groups to target platforms that have been configured to run Platform Services.

The driver obtains and stores the information it uses in an eDirectory™-based “Identity Vault.” To access the Identity Vault, the Core Driver uses LDAP Services for eDirectory.

For ease of management, target platforms that share the same user and group population are grouped together into Platform Sets.

Communication between the driver components occurs through TCP/IP and is encrypted.

The driver includes a secure Web interface that works as an iManager plug-in for administration and monitoring.

The Core Driver records significant occurrences in an Audit Log, and each component writes an Operational Log. Each Core Driver component maintains performance statistics, which can be viewed in the Web interface.

The Fan-Out Driver includes an application programming interface (API). This allows programmers to extend applications to use Authentication Services, which allows them to take advantage of your existing eDirectory constructs.

Binary files, configuration files, and other files used by the driver components are stored in the ASAM directory in the file system of the host server.

#### Additional Resources

Details about configuring and administering the Core Driver and Platform Services are provided in later sections of this guide. Other sections provide information about API development and driver system messages. Also be aware that this is one of three available administration guides for the Fan-Out Driver, each tailored to the range of platforms with which it can work:

* Identity Manager Fan-Out Driver for Linux and UNIX Administration Guide
* Identity Manager Fan-Out Driver for Mainframes Administration Guide (z/OS)
* Identity Manager Fan-Out Driver for Midrange Administration Guide (IBM i, OS/400, i5/OS)

For information about eDirectory, see the NetIQ eDirectory Administration Guide.

#### Section Topics

The topics in this section describe the structure and function of the Identity Manager Fan-Out Driver.

* [Core Driver](br12c5c.html)

  + [Object Services](br12c5c.html#bfgjb3s)

  + [Event Journal Services](br12c5c.html#bfgjbgu)

  + [Audit Services](br12c5c.html#bfgjbpe)

  + [Certificate Services](br12c5c.html#bfgjbuu)

  + [Web Services](br12c5c.html#bfgjbym)

  + [Authentication Services](br12c5c.html#bfgjd7m)

  + [Event Subsystem](br12c5c.html#bfgjdo3)
  + [Embedded Remote Loader](br12c5c.html#bfgjdu4)
* [Platform Services](br12c5n.html)
* [Directory Objects](br12c66.html)
* [Migration](br12c6m.html)
