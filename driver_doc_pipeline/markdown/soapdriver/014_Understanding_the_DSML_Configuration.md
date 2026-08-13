# 5.1 Understanding the DSML Configuration

The DSML package uses DSML 2.0 and binds with SOAP 1.1, using HTTP or HTTPS 1.1 as the transport. All data transformation and processing is done in policies and style sheets that are delivered in the DSML package.

The DSML package does the following:

* Shows a simple configuration for pairing with the Identity Vault DSML implementation.
* Provides XDS-to-DSML and DSML-to-XDS conversions in policies.
* Handles Users, Groups, and Organizational Units.

  Other objects can be processed through policy and style sheet customization.
* Supports string, structured, and distinguished name (DN) attribute types.

  This sample has two examples of handling attributes with other data types. The Postal AddressÂ attribute shows how structured attributes can be handled. The Member attribute shows how a DN attribute can be handled. Other attribute data types can be handled through policy and style sheet customization.
* Handles a subset of the query operations.

  Specific query operations can be handled through policy and style sheet customization.
* Supports password set operation.

  Password synchronization is possible through policy and style sheet customization.
* The Subscriber channel uses the destination DN for the association key.
* The Publisher channel uses the application-provided DN for the association key.
