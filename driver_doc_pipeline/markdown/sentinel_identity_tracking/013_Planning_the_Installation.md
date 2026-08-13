# 4.2 Planning the Installation

You can install the driver shim on either the Identity Manager system or a remote host. [Figure 4-1](planning-the-installation.html#b10f0ans) illustrates the two installation options. The installation includes the following components:

* *Identity Vault:*
  Used by NetIQ Identity Manager to store data for synchronization with Sentinel. The Identity Vault is a persistent database powered by NetIQ eDirectory. The vault can be viewed as a private data store for Identity Manager or as a metadirectory that holds enterprise-wide data. Data in the vault is available to any protocol supported by eDirectory, including NCP (the traditional protocol used by utilities, such as ConsoleOne and Identity Console), LDAP, and DSML.Since the Identity Vault is powered by eDirectory, you can easily integrate Identity Manager into your corporate directory infrastructure by using your existing directory tree as the vault. The Identity Vault runs on any platform supported by Identity Manager and communicates with the module on the connected system over a secure network link. For information on the supported platforms, see "[Supported Platforms](https://www.netiq.com/documentation/idm401/idm_integrated_install/?page=/documentation/idm401/idm_integrated_install/data/bpo8wc2.html)"in the [Identity Manager Installation Guide.](https://www.netiq.com/documentation/idm401/idm_integrated_install/?page=/documentation/idm401/idm_integrated_install/data/bpo8wc2.html)
* *Driver Shim (Integration Module for Sentinel):*
  Converts the XML based Identity Manager command and event language (XDS) to the protocols and API calls required to interact with Sentinel. This driver uses a Java based driver shim (SentinelRESTShim.jar.) The driver shim is an executable code and is available on the [NetIQ download Web site](http://download.novell.com/index.jsp).
* *Remote Loader:*
  Enables a driver shim to execute outside of the Identity Manager engine. The Remote Loader is typically used when a requirement of the driver shim is not met by the Identity Manager server. For example, if Identity Manager engine is running on Linux but you want to integrate with Active Directory, the Remote Loader is used to execute the Active Directory driver shim on a Windows server.

  The Remote Loader is a service that executes the driver shim and passes information between the shim and Identity Manager engine. You can install the driver shim on the server where the Remote Loader is running. You can choose to use SSL to encrypt the connection between the Identity Manager engine and the Remote Loader.

  When you use the Remote Loader with the driver shim, two network connections are established:

  + Between Identity Manager and Remote Loader
  + Between Sentinel and the driver shim

  For more information on Remote Loader, see "[Designer](../../../identity-manager-49/driver_admin/data/b18xta1v.html#t45lujgcj7b0)" in the [NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-49/driver_admin/data/bktitle.html#bktitle).

The following figure illustrates the two options for installing the driver shim:

*Figure 4-1* Installing the Driver Shim

![](../graphics/installation_architecture_a.png)

## 4.2.1 Installing the Driver Shim on the Identity Manager System

The most common hosting for Identity Manager integration is in the Identity Manager engine.

*Advantages:*

* The Integration module logs the trace messages in the Identity Manager server trace log. Therefore, troubleshooting might be easier.
* No need to configure a Remote Loader instance.
* No extra TCP/IP traffic between Identity Manager and Remote Loader.

*Disadvantages:*

* Resource consumption on the Identity Manager server (memory, processor time).
* The requirement to restart the Identity Manager server each time the integration module is installed or updated.

## 4.2.2 Installing the Driver Shim on a Remote System

The following are the advantages and disadvantages of the installing the driver shim on a remote system:

*Advantages:*

* Resource consumption (memory, processor time) is in a different process, or on another host.
* You need to restart only the Remote Loader process when the integration module is updated.

*Disadvantages:*

* Multiple trace files. Therefore, when troubleshooting, you might need to examine trace files from both the Identity Vault process and the Remote Loader process.
* The need to configure a Remote Loader instance.
* Extra TCP/IP traffic between the Identity Vault and the Remote Loader.
