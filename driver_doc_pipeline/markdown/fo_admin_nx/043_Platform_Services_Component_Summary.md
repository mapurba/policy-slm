# 8.1 Platform Services Component Summary

The Platform Services Process makes requests to Core Drivers for Authentication Services functions such as authentication, user name resolution, and password changes.

*NOTE:*For an overview of how Platform Services works with the components of the Core Driver—the other major part of Identity Manager Fan-Out Driver architecture—see [Section I, Concepts and Facilities](bex00oo.html).

*Figure 8-1* Platform Services

![](../graphics/platserv_a.gif)

The Platform Services System Intercept is hooked into the login process of a system using standard, vendor-provided mechanisms. It provides password verification and password change functions.

The Platform Receiver obtains provisioning events from Event Journal Services and acts on them by running Receiver scripts to create and maintain users and groups as appropriate.

Platform Services also provides an application programming interface (API) that you can use for your own applications. For more information, see [Section V, API Development](bexh68d.html).

Some types of platforms communicate with the Core Driver for Authentication Services using Secure Sockets Layer (SSL). Others use DES encryption. All platform communication with Event Journal Services uses SSL.

The Platform Services Cache Daemon obtains provisioning events from Event Journal Services and stores them in a local memory cache for efficient retrieval by the Name Service Switch. This information contains a complete record for a Linux or UNIX account or group, which may be accessed by services that use the Name Service Switch system calls.

The Name Service Switch is a system library providing complete account redirection as an alternative to storing user and group accounts and passwords locally. By providing such services through a memory cache, this data is protected from interactive accounts on the local system. In addition, the data remains centrally managed by eDirectory™ and a large number of accounts may be accessed by a single Linux or UNIX system, improving on traditional /etc/passwd methods for accomplishing this, which can be inefficient to update or access.
