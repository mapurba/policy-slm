# 2.0 Installing the Driver Files

You can install Oracle EBS drivers on multiple systems and platforms. To verify the system requirement list, see the [NetIQ Identity Manager Setup Guide for Linux](../../../identity-manager-48/setup_linux/data/front.html#front) or [NetIQ Identity Manager Setup Guide for Windows](../../../identity-manager-48/setup_windows/data/front.html#front).

By default, the Oracle EBS driver files driver files are installed on the Identity Manager server at the same time as the Identity Manager engine. The installation program extends the Identity Vault’s schema and installs the driver shims and the driver packages. It does not create the driver in the Identity Vault (see [Section 3.0, Creating a New Driver Object](creating-a-new-driver-object.html)) or upgrade an existing driver’s configuration (see [Section 4.0, Upgrading an Existing Driver](upgrading-an-existing-driver.html)).

To install the drivers, you first need to install the driver files and driver packages, and then modify the driver configuration to suit your environment. This section tells you how to install the driver files. For information on installing and configuring the packages, see [Section 3.0, Creating a New Driver Object](creating-a-new-driver-object.html).

* [Prerequisites](prerequisites.html)
* [Installing the Oracle EBS Driver Jar Files](installing-the-oracle-ebs-driver-jar-files.html)
* [Installing the PL/SQL APIs](installing-the-pl-sql-apis.html)
* [Updating the PL/SQL APIs](updating-the-pl-sql-apis.html)
* [Creating a Web Service Endpoint](creating-a-soap-endpoint.html)
* [Subscribing to the Business Events](subscribing-to-the-business-events.html)
