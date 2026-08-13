# 1.2 Design Architecture

Identity Manager drivers listen for events and then apply the proper Identity Manager policies for the event. That information is then passed to the Identity Manager engine that executes the policies.

The ID Provider driver is different from all other Identity Manager drivers. It also listens for events, but it has two sets of policies: the Identity Manager policies and the ID Provider policies. The ID Provider policies allow the driver to generate and assign unique IDs to objects.

The driver has three major components:

* *ID Client:*
  The ID client communicates with the ID Provider driver to obtain a unique ID. The client can be another Identity Manager driver (for example, the WorkOrder driver) or a standalone Java application.
* *ID Provider Driver:*
  The driver receives ID requests from clients, generates unique IDs that are stored in the Identity Vault, and passes the unique IDs back to the client. The driver uses LDAP to access the Identity Vault and uses Java RMI (Remote Method Invocation) to communicate with ID clients.
* *Identity Vault:*
  The Identity Vault provides the location for storing unique IDs and also contains the policies used to generate the IDs. All IDs and policies are stored in the ID Policy Container.

The ID Provider driver can be used in two different scenarios:

* [Scenario 1: Using the Identity Vault to Store the ID Provider Policies](design-architecture-of-id-provider-driver-for-identity-manager.html#bcg4j7d)
* [Scenario 2: Using an LDAP Database to Store the ID Provider Policies](design-architecture-of-id-provider-driver-for-identity-manager.html#bcg4jgj)

#### Scenario 1: Using the Identity Vault to Store the ID Provider Policies

This is the most commonly used scenario for this driver. The ID Provider policies are created and stored in the Identity Vault when the driver is created and configured. [Figure 1-1](design-architecture-of-id-provider-driver-for-identity-manager.html#bctvxbj) shows how a unique ID is generated.

*Figure 1-1* Identity Vault Stores the ID Provider Policies

![](../graphics/idm_sen1_edir_a.png)

1. A new User object is created in the Identity Vault, then the ID Provider driver picks up the Create event.
2. The ID Provider driver reads the last ID that was generated from the ID Provider policies in the Identity Vault and generates a new ID. The ID is then written back to the ID Provider policies in the Identity Vault to track the unique IDs.
3. The ID Provider driver then assigns the new ID to the new User object.

All events are tracked and stored in the Identity Vault.

#### Scenario 2: Using an LDAP Database to Store the ID Provider Policies

This scenario allows you to use an LDAP database to store the ID Provider policies instead of using the Identity Vault. [Figure 1-2](design-architecture-of-id-provider-driver-for-identity-manager.html#bctvyau) shows how a unique ID is generated with the LDAP database.

*Figure 1-2* LDAP Database Stores the ID Provider Policies

![](../graphics/idm_sen1_ldap_a.png)

1. A new User object is created in the Identity Vault, then the ID Provider driver picks up the Create event.
2. The ID Provider driver reads the last ID that was generated from the ID Provider policies in the LDAP database and generates a new ID. The ID is then written back to the ID Provider policies in the LDAP database to track the unique IDs.
3. The ID Provider driver then assigns the new ID to the new User object in the Identity Vault.
