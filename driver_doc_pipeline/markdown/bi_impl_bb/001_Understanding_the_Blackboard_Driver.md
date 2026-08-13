# 1.0 Understanding the Blackboard Driver

The NetIQÂ® Identity Manager 4.8 driver for Blackboard lets you synchronize data in the Identity Vault to data stored in a Blackboard Learn implementation. Prior to 4.8, the Blackboard Driver used Java Snapshot APIs to integrate directly on the Blackboard system. In 4.8, the architecture was significantly changed in order to support the latest integration techniques recommended by Blackboard. As a result, you no longer need to install the driver directly on the Blackboard system. This change allows for both on-premise and cloud-based configurations.

The Subscriber channel receives XDS command documents for users and groups from the Identity Manager Metadirectory engine, converts them to Blackboard REST API calls, and executes them. The Publisher channel is not implemented at this time.

The Subscriber channel does not perform validation of attribute values in the XDS command document. If the requirements of Blackboard are not met, the results of the Blackboard REST API calls are unpredictable. Exceptions detected by the Blackboard REST API bubble up to the driver trace to assist in troubleshooting data validity problems.

The following sections provide a basic overview of the driver:

* [Version Support](btvhwdn.html)
* [Blackboard Driver Concepts](btvi7q3.html)
* [Support for Standard Driver Features](btviyt2.html)
* [Differences Between eDirectory and Blackboard](btvj3fi.html)
