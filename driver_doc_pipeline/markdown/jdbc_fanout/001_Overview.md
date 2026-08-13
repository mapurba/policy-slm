# 1.0 Overview

The Identity Manager Java DataBase Connectivity (JDBC) Fanout driver supports the fanout capability at the driver level. The Fanout driver provisions users, groups, and password to multiple databases with minimal effort. This eliminates the need for the Identity Manager administrator to configure multiple JDBC drivers using the same policies to provision multiple databases of the same type. You can centrally manage user accounts and have them automatically created, configured, maintained, and removed when appropriate. This saves cost and time associated with managing the Identity Manager environment. In this configuration, the synchronization is unidirectional, from the Identity Vault to the connected database.

The Fanout driver supports the following features:

* Synchronizes users and groups from the Identity Vault to the target databases
* Synchronizes passwords from the Identity Vault to the target databases
* Provisions or deprovisions user accounts in the target databases based on entitlements
* Assigns or revokes user permissions in the target databases based on entitlements

IMPORTANT:

* The Fanout driver is a Subscriber channel only driver.
* The Remote Loader options do not apply to the Fanout driver. This driver uses the Fanout agent component to create multiple JDBC Fanout driver instances.
