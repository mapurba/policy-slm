# 1.0 Understanding the Bidirectional eDirectory Driver

The NetIQ Identity Manager Bidirectional eDirectory driver synchronizes data between the Identity Vault and eDirectory.

The traditional Identity Manager driver for eDirectory synchronizes objects and attributes between two eDirectory trees. This requires Identity Manager to be configured on both eDirectory servers. It also requires two instances of the eDirectory driver configuration.

Another way of connecting to eDirectory is by using the LDAP driver. However, connecting to eDirectory driver through an LDAP driver has the following limitations:

* The LDAP driver uses LDAP Search method to synchronize eDirectory data because eDirectory does not provide a change-log functionality. The LDAP Search method is not as efficient as the change-log method.
* The LDAP driver does not support universal password synchronization on the Publisher channel.

The Bidirectional eDirectory driver was designed to make the connection between two connected trees easier in cases where one of the trees did not have an Identity Manager server. This also reduces the licencing burden for customers who do not need Identity Manager in multiple trees.

If you are connecting two Identity Manager enabled trees, it is recommended to use the traditional eDirectory driver. The traditional eDirectory driver and the new Bidirectional eDirectory driver are mutually exclusive. The Bidirectional eDirectory driver’s change-log cannot be installed on an Identity Manager server. [Table 1-1](understanding-the-bidirectional-edir-driver.html#bwo84h3) contains details about the features of the two drivers.

*Table 1-1* Traditional NDS-to-NDS Driver Compared to the Bidirectional eDirectory Driver

| Features | Bidirectional eDirectory Driver | Traditional NDS-to-NDS Driver |
| Installation | The change-log module is installed on the connected eDirectory. | Identity Manager is installed on the connected eDirectory. |
| Configuration | One driver is configured for achieving data synchronization between Identity Vault and eDirectory. | Two drivers are configured for achieving synchronization.  The configuration is split across the Identity Vault and eDirectory. |
| Communication | LDAP/TLS is used for communication. | TCP/SSL is used for communication. |
| NDS Password Sync | Available | Available |
| Distribution Password Sync | Available | Available |
| Driver Package | Available | Available |
| Account Tracking | Available | Available |
| Entitlements | Available | Available |
| Data Collection Service | Available |  |

* [Driver Concepts](driver-concepts.html)
* [Standard Driver Features](standard-driver-features.html)
