# 1.3 Data Transfer Between Systems

There are two data transfer channels between the Identity Vault and the connected application:

* *Publisher Channel:*
  Transfers data and events from the connected application to the Identity Vault. The Sentinel Identity Tracking driver does not support this channel.
* *Subscriber Channel:*
  Transfers data and events from the Identity Vault to the connected application. The Sentinel Identity Tracking driver supports only data transfers from the Identity Vault to Sentinel. Communication is one-way only.

  The Subscriber channel does the following:

  + Watches for additions and modifications to the Identity Vault objects.
  + Makes changes to Sentinel's internal representation of Identities and Accounts that reflect those changes.

  *Figure 1-3* Data Transfer Between Systems

  ![](../graphics/data_transf_chanl_a.png)
