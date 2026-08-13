# 1.2 Data Transfer Between Systems

The data is transferred between the Identity Vault and the Fanout driver only on the Subscriber channel.

The Subscriber channel performs the following activities:

* Watches for changes to the Identity Vault objects.
* Makes changes to the target databases to reflect those changes.
