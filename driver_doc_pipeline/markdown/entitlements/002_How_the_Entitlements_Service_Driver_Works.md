# 1.1 How the Entitlements Service Driver Works

The Entitlements Service driver grants entitlements to and revokes entitlements from users, as shown in [Figure 1-1](how-entitlement-driver-works.html#bfq7xz7).

*Figure 1-1* Entitlements Service Driver Process

![](../graphics/entitlement_over_001_a.png)

The driver implements entitlements through the use of entitlement policies. An entitlement policy contains the following:

* *Membership:*
  The list of users assigned to a policy. A user can be dynamically assigned to a policy when he or she meets the criteria for the policy, or the user can be statically (manually) assigned to the policy. In [Figure 1-1](how-entitlement-driver-works.html#bfq7xz7), User A, User B, and User C are all members of Entitlement Policy 1. User D and User E are members of Entitlement Policy 2.
* *Entitlements:*
  The list of entitlements associated with the policy. Users assigned to the policy receive all of the entitlements associated with the policy. If the user is removed from the policy, he or she loses all entitlements associated with the policy. In [Figure 1-1](how-entitlement-driver-works.html#bfq7xz7), the Entitlements Service driver has granted the AD User Account entitlement and GroupWise Mailbox entitlement to User A, User B, and User C. Likewise, the driver has granted the AD User Account entitlement and Exchange Mailbox entitlement to User D and User E.

The Entitlements Service driver uses the following basic process to grant entitlements to and revoke entitlements from users:

1. The driver evaluates the users within its defined scope to see if they meet the criteria established for membership in a policy. This occurs whenever:

   * Any criteria attribute used for determining membership in an entitlement policy is modified.
   * A user is moved.
   * A user is renamed.
   * You manually initiate a reevaluation of a policy’s membership.
2. The driver updates the DirXML-EntitlementRef attribute of any user whose entitlements have changed. This includes granting entitlements if the user was added to an entitlement policy or revoking entitlements if the user was removed from a policy.
3. After the DirXML-EntitlementRef attribute for a user is updated, the Entitlements Service driver’s job is finished. For the entitlement to be implemented, the entitlement must be defined on the appropriate driver and the driver’s policies must include the actions required to enforce the entitlement. For information about creating entitlements and the policies to support them, see the [NetIQ Identity Manager Entitlements Guide](../../../identity-manager-49/entitlements/data/identity-manager-entitlements.html#identity-manager-entitlements).
