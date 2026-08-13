# 5.2 Understanding the SPML Configuration

The SPML package uses SPML 1.0 or SPML 2.0 and binds with SOAP 1.1, using HTTP or HTTPS 1.1 as the transport. All data transformation and processing is done in policies and style sheets that are delivered in the SPML package.

The SPML package does the following:

* Provides generic SPML functionality based on the OASIS SPML V2 core xsd standard.

  The SPML package does not pair with any specific SPML application. In some specific implementations, you can modify the default policies to conform with the provider standards. For example, the containerID attribute is optional as per the OASIS SPML V2 core xsd standard, whereas it is mandatory for Quest One ActiveRoles SPML Provider.
* Provides XDS-to-SPML and SPML-to-XDS conversions in policies.
* Handles Users, Groups, and Organizational Units

  Other objects can be handled through policy and style sheet customization.
* Handles a single value per attribute.

  Multiple values for an attribute can be handled through policy and style sheet customization.
* Handles a subset of the query operations.

  The configuration handles all queries as SPML scope = “subtree” and uses the entry and subordinate scope concepts. Specific query operations can be handled through policy and style sheet customization.
* Supports string, structured, and distinguished name (DN) attribute types.
* Supports password set operation.

  Password synchronization is possible through policy and style sheet customization.
* Handles the single (non-batch) operations of execution=synchronous and processing=sequential.

  Batch requests can be supported through policy and style sheet customization.
* Doesn’t handle <addResponse><attributes> or <modifyResponse><modifications>.
* The Subscriber channel uses the application-returned Identifier value for the association key.
* The Publisher channel uses the DN for the association key and returns the association key as the Identifier value.
