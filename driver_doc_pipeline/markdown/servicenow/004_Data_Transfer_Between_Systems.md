# 1.3 Data Transfer Between Systems

The data is transferred between the Identity Vault and the ServiceNow driver only on the Subscriber channel. Communication is one-way only.

The Subscriber channel does the following:

* Watches for additions and modifications to the Identity Vault objects.
* Makes changes to ServiceNow's internal representation of user identities that reflect those changes.
