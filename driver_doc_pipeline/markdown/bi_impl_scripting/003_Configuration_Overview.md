# 1.2 Configuration Overview

This section discusses driver configuration details specific to the Scripting driver. For basic configuration information, see “Managing Identity Manager Drivers” in the Identity Manager Administration Guide. For detailed information about configuring the Scripting driver, see [Section 4.0, Configuring the Scripting Driver](b8mp109.html).

Topics in this section include

* [Data Flow](b8mncmk.html#b8mndf0)
* [Policies](b8mncmk.html#b8mnf0k)

## 1.2.1 Data Flow

Filters and policies control the data flow of identities to and from the connected system and the Identity Vault. The Data Flow option, specified during driver import, determines how these filters and policies behave.

* *Bidirectional:*
  Sets classes and attributes to be synchronized on both the Subscriber and Publisher channels.
* *Application to Identity Vault:*
  Sets classes and attributes to be synchronized on the Publisher channel only.
* *Identity Vault to Application:*
  Sets classes and attributes to be synchronized on the Subscriber channel only.

## 1.2.2 Policies

The Metadirectory engine uses policies to control the flow of information into and out of the Identity Vault. Policies can be customized to support desired operations. The following table describes the policy functions for the Scripting driver in the default configuration:

*Table 1-1* Default Linux and UNIX Driver Policy Functions

| Policy | Description |
| Mapping | Maps the Identity Vault objects and selected attributes to connected system objects and attributes. |
| Publisher Event | Processes Publisher-side operations. |
| Publisher Matching | Restricts privileged accounts and defines matching criteria for placement in the Identity Vault. |
| Publisher Create | Defines creation rules for provisioning into the Identity Vault. |
| Publisher Placement | Defines where new objects are placed in the Identity Vault. |
| Publisher Command | Defines password publishing policies. |
| Subscriber Matching | Defines rules for matching identities in the connected system. |
| Subscriber Create | Defines required creation criteria. |
| Subscriber Command | Transforms attributes and defines password subscribing policies. |
| Subscriber Output | Sends e-mail notifications for password failures and converts information formats from the Identity Vault to the connected system. |
| Subscriber Event | Restricts events to a specified container. |
