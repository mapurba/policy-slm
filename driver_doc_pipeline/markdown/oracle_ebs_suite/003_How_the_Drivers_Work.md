# 1.2 How the Drivers Work

The driver is a bidirectional synchronization product between the Oracle EBS system and the Identity Vault. This framework uses XML and XSLT to provide data and event transformation capabilities that convert Identity Vault data and events into Oracle data and vice-versa.

The Identity Vault acts as a hub, with other applications and directories publishing their changes to it. The Identity Vault then sends changes to the applications and directories that have subscribed for them. This results in two main flows of data: the Publisher channel and the Subscriber channel.

* [Publisher Channel](how-the-driver-works.html#alvpnqh)
* [Subscriber Channel](how-the-driver-works.html#alvpuso)
* [Associations](how-the-driver-works.html#alvqmhh)

## 1.2.1 Publisher Channel

The Oracle Workflow Business Event System (BES) is an application service that uses Oracle Advanced Queuing (AQ) technology to communicate business events among different Oracle systems. The BES consists of the Event Manager and Workflow that process event activities. The BES can propagate Add, Delete, and Modify event data to the Identity Vault. Only events specifically selected by the system administrator are transported from the Oracle EBS system to the PL/SQL APIs. The PL/SQL APIs (installed in the Oracle EBS system as part of the driver installation) handle the parsing of the events and read the appropriate data fields specified by the driver configuration, and provide secure transport of the data over an HTTP/HTTPS port to the Publisher channel. [Figure 1-1](how-the-driver-works.html#b120hfae) shows the Publisher channel data flow from the Oracle EBS system to the Identity Vault.

Only the event attributes that have been specified in the driver Publisher filter are published to the Identity Vault. The Publisher channel then submits XML-formatted documents to the Identity Manager engine to publish them into the Identity Vault.

*Figure 1-1* Publisher Channel Data Transfer

![](../graphics/oracle_ebspub_driver_a.png)

The business events are cached and stored into a database table (idmusrmgt.idm\_events table) in the Oracle EBS system. To guarantee the delivery of events to the Identity Manager, the events remain in the idmusrmgt.idm\_events table until they are successfully send to the Identity Vault. The Publisher channel uses a SOAP/REST endpoint to poll the idmusrmgt.idm\_events table for certain future events such as future add or delete events or modification of roles and responsibilities to the existing users, which are meant to be executed at a later time. A future date of when these events need to be executed is specified along with the events. Future events are immediately synchronized with the Identity Vault. The login attribute is disabled for the future events until when they are required to be operational.

## 1.2.2 Subscriber Channel

The Subscriber channel receives XML-formatted Identity Vault events from the Identity Manager engine. The driver uses the Web Service security (WSS) token for authentication and updates the idmusrmgt.idm\_events table with the Identity Vault changes.

*Figure 1-2* Subscriber Channel Data Transfer

![](../graphics/oracle_ebssub_driver_a-updated.png)

For data to flow from the Identity Vault to the Oracle system, the driver uses the SOAP/REST functions. By using Identity Manager and other Identity Manager drivers, the data can be shared with other business applications and directories. These other applications can add additional data, which in turn can be transferred back to the idmusrmgt.idm\_events table using the SOAP/REST service on the Subscriber channel.

## 1.2.3 Associations

Associations are created between the Oracle EBS system and the Identity Vault objects during the synchronization process. For the Oracle EBS user object, a unique 7-digit number must be created. However, the Identity Vault and other applications do not need to share this same unique ID. Identity Manager allows various naming policies in an organization to be applied to objects by using the DirXML-Association attribute.

The DirXML-Association attribute is multivalued. Therefore, if Identity Manager is being used to synchronize an object among multiple applications, all of the object’s unique IDs (or associations) can be stored in this attribute on the Identity Vault object.

The unique ID association links objects from the Oracle EBS database to the corresponding objects in the Identity Vault. When an Add or Matching event occurs, the association is made. This association allows the driver to perform subsequent tasks on the appropriate object.

The DirXML-Associations field is stored on the Identity Vault object on the Identity Manager property page. The User ID of a user in the Oracle EBS system is used to create association for the User Management and TCA drivers. The Person ID of an employee is used to create association for the HR driver.
