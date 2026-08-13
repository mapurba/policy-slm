# 1.3 Using Multiple Entitlements Service Drivers

If your Identity Manager system includes multiple driver sets and you want to use role-based entitlements with each driver set, you must create an Entitlements Service driver in each driver set. In addition, the Entitlements Service driver can manage only those User objects that are in a master or read/write replica on the Identity Manager server where the Entitlements Service driver is located.

If necessary, you can run multiple Entitlements Service drivers in the same driver set. However, you must make sure that the scope of users managed by each of the drivers does not overlap. For example, entitlements for User A should not be managed by two different Entitlement Service drivers.

To grant entitlements to users through one or more Entitlements Service drivers in your Identity Manager system, ensure that all the replicas of the user objects and the Root of the tree reside on the same server.
