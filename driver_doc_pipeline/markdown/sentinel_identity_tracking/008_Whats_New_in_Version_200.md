# 2.3 What’s New in Version 2.0.0?

This version provides the following key features and functions:

* The Driver for Sentinel, formerly known as the Sentinel Driver, removes the dependency on the Collector for Identity Manager and Sentinel integration.
* This driver now facilitates simplified configuration. The previous version of the driver used a JMS bus and sent information to a Sentinel Collector, which then sent the information to the Sentinel database. This driver uses the native Sentinel 7.0.1 REST APIs to perform the integration, which sends the account information directly to the Sentinel database.
