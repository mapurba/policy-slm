# 1.1 Driver Concepts

Data flows between the Oracle EBS system and the Identity Vault by using the Publisher and Subscriber channels.

The Publisher channel does the following:

* Reads events from the Oracle EBS system on the server that the driver shim is connecting to.
* Submits that information to the Identity Vault.

The Subscriber channel does the following:

* Watches for additions and modifications to the Identity Vault objects.
* Makes changes to the Oracle EBS system to reflect those changes.

Through the use of filters and policies, the driver can be configured to control and manage what changes are detected and sent to the Oracle EBS system.

The driver uses SOAP (Simple Object Access Protocol) or REST (Representational State Transfer) to exchange data between Identity Manager and a Web service.

*NOTE:*REST service is only available for User Management driver at this moment.
