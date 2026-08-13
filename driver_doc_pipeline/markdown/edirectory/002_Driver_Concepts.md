# 1.1 Driver Concepts

* [Key Terms](driver-concepts.html#key-terms)
* [How the eDirectory Driver Works](driver-concepts.html#how-the-edirectory-works)

## 1.1.1 Key Terms

*Driver:*
A set of policies, filters, and objects that act as the connector between an Identity Vault and the driver shim.

This software enables an application to publish events from an application to the directory, enables an application to subscribe to events from the directory, and synchronizes data between the directory and applications.

To establish a connection between the Metadirectory engine and an Identity Vault, you specify the driver’s configuration and connection parameters, policies, and filter values.

*Driver object:*
A collection of channels, policies, rules, and filters that connect an application to an Identity Vault that is running Identity Manager.

Each driver performs different tasks. Policies, rules, and filters tell the driver how to manipulate the data to perform those tasks.

The Driver object displays information about the driver’s configuration, policies, and filters. This object enables you to manage the driver and provide eDirectory management of the driver shim parameters.

*Driver shim:*
A Java file (NdsToNds.jar) loaded directly by Identity Manager. Communicates event changes to be sent from the Identity Manager Driver for eDirectory to an Identity Vault, communicates changes from the Identity Vault to the Identity Manager Driver for eDirectory, and operates as the link that connects the Identity Vault and the Identity Vault Driver object.

*Identity Vault.*
A hub, with applications and directories publishing their changes to it. The Identity Vault then sends changes to the applications and directories that have subscribed for them. This results in two main flows of data: the Publisher channel and the Subscriber channel.

## 1.1.2 How the eDirectory Driver Works

Channels, filters, and policies control data flow.

*Publisher and Subscriber Channels:*
The eDirectory driver is installed and configured in two trees. The driver’s Publisher channel in TreeA communicates with the driver’s Subscriber channel in TreeB. Conversely, the driver’s Publisher channel in TreeB communicates with the driver’s Subscriber channel in TreeA.

*Filters:*
Identity Manager uses filters to control which objects and attributes are shared. The default filter configurations for the eDirectory driver allow objects and attributes to be shared. For a list of synchronized attributes, see [Section B.0, Synchronized Attributes](synchronized-attributes.html).

*Policies:*
Identity Manager uses policies to control data synchronization between the eDirectory driver and the Identity Vaults.

The driver does not have any direct communication with eDirectory. It communicates with eDirectory via the Identity Manager engine. The driver is usually configured in pairs with an instance of the driver configured in each of the two trees being synchronized. The Subscriber of the driver instance in each tree connects to the Publisher of the driver instance in the other tree via a TCP connection. The connection is formed on demand when a driver instance needs to communicate with the other driver instance. When the connection is established, it remains intact until the connection is broken or one of the driver instances is stopped. If there is a broken connection or an attempt to connect to the other instance fails, the Subscriber channel issues a retry status to the Identity Manager engine and then attempts to reconnect when the Identity Manager engine resends the event. The port used for the connections is configurable and can be different for Subscriber to Publisher pair.

The Subscriber of each driver instance acts primarily as an event source for the Publisher of the other driver instance which in turn is the event source for the Publisher channel of the Identity Manager engine. Events provided by the Subscriber channel of one instance of the driver are passed across the TCP connection unchanged to the Publisher channel of the other instance of the driver which is then passed, mostly unchanged, to the subscriber channel of the Identity Manager engine.

Because the Subscriber channel is primarily an event source for the Publisher channel of the other instance, policies are usually not in place on the Publisher channel of either instance. The primary exception to this rule is that if any custom event filtering is to be done, it is usually more efficient to do that filtering as early in the dataflow as possible, which usually means in the Subscriber Event Transformation policy. The filters are also usually configured such that the filter of the Subscriber filter of one instance is identical (with the exception of the GUID attribute) to the Publisher filter of the other instance.

There are two different protocols used to transport the XML documents between the driver instances.

To guard against undetected loss of connectivity, such as when the network is physically unavailable or the other server crashes without gracefully closing all of its connections, a keep-alive message is periodically sent in each direction across an open connection. This causes an I/O error if the connection breaks in such a way which may be undetectable otherwise. The frequency of the keep-alive packets is configurable. You can tune it to either minimize the network traffic or minimize the amount of time it takes to detect recover from a broken connection.

The driver uses a value generated from the GUID attribute of one of the instances of the driver. The GUID attribute is required to be in the Subscriber filter for each class that is being synchronized. The GUID attribute is not present in the Publisher filter because it is usually not desirable to synchronize a value that is supposed to be globally unique. The GUID attribute is used to generate an association key only when the Publisher channel of a driver passes through an add event for an object that doesn't already have an association key.

The rights to objects are granted to the driver object by standard eDirectory rights management. Sufficient rights must be granted to the objects to perform the desired operations on the desired objects and attributes in each tree.

The connections between the two driver instances can be either clear or secured by SSL. Configuration of SSL requires the creation of a server certificate for each publisher that is signed by a certificate authority that is trusted by the Subscriber channel. For more information, see [Section 5.0, Securing Driver Communication](securing-driver-communication.html).
