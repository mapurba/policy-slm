# 9.2 Conflict Resolution between Entitlement Policies

When you are creating entitlement policies, itâs possible that the policies that affect a particular user might conflict in assigning entitlements to that user. The following sections provide information to help you if conflicts are not being resolved the way you expect:

* [Conflict Overview](bnxmlz5.html#bpbnrxl)
* [Changing the Conflict Resolution Method for an Individual Entitlement](bnxmlz5.html#bnxnkt9)
* [Prioritizing Entitlement Policies](bnxmlz5.html#bnxngnt)

## 9.2.1 Conflict Overview

The following list describes how conflicts are resolved. For some entitlements, you can change the conflict resolution.

* *Entitlements that donât have values are additive.*
  In most cases an account entitlement doesnât have values. If a user is granted an account on a connected system by any entitlement policy, the user receives an account on that system. It does not matter whether another entitlement policy is in conflict; the result is additive.

  This method of conflict resolution for granting accounts cannot be changed.

  For example, if the Manager entitlement policy grants Jean Chandler an Exchange account, but Jean Chandler is excluded from the Mail Room Employees entitlement policy that also grants Exchange accounts, Jean still gets an Exchange account.
* *Entitlements that have values are additive by default, but you can choose to resolve by priority.*
  Entitlements, such as group membership, have a list of group names for the values, or have an attribute with a value. By default, these kinds of entitlements are also additive.

  You can change the conflict resolution for these kinds of entitlements, if desired.

  + *conflict-resolution=âunionâ:Â*
    A value of âunionâ means that the entitlements are additive. A user is granted all the entitlements that he or she is assigned by membership in any policy. The differing entitlement values are simply added together and the user gets them all.

    For example, if Jameel is a member of the Trade Show Contractors policy that grants membership in a GroupWise e-mail distribution list named Trade Show Mailing List, and he is excluded from membership in the Trade Show Managers policy that also assigns the e-mail distribution list named Trade Show Mailing List, he still receives membership in the e-mail distribution list.

    As another example, if Consuela is granted membership in the Active Directory group named Mailroom Staff by the Mailroom policy, and also granted membership in the Active Directory group named Emergency Response by the Emergency Volunteers policy, she is granted membership in both groups in Active Directory.

    With this setting, the order of an entitlement policy in the list of policies is not important for the entitlement.
  + *conflict-resolution=âpriorityâ:Â*
    A value of âpriorityâ means that if the values in two different policies conflict, or if one policy includes the user and another excludes the user, the entitlements granted to the user are only those in the entitlement policy that is listed higher in the list of Entitlement policies.

    The previous examples would have a different result with this setting.

    In the example above for Jameel, if the GroupWise e-mail distribution list entitlement had a value of âpriority,â and the Trade Show Managers policy was higher in the list than the Trade Show Contractors policy, Jameel would not be granted membership in the Trade Show Mailing List.

    In the example above for Consuela, if the Active Directory NOS group membership entitlement had a value of âpriority,â and the Mailroom policy was higher in the list than the Emergency Volunteers policy, Consuela would be granted membership only in the Mailroom Staff group. She would not be granted membership in the Emergency Response group because the conflict resolution is by priority, not additive.

    This functionality is useful if, for example, you configure your environment to use role-based entitlements to place users in a hierarchical structure on another system. You would want the user to be placed in either one place or another, not in two places at the same time.

    Keep in mind that the setting is independent for each entitlement offered by each driver.

    As a general rule, if you use the âpriorityâ setting, you should place administrator or manager policies higher in the list than policies for end users or individual contributors. You should put groups with narrower membership higher than groups with broader membership.

## 9.2.2 Changing the Conflict Resolution Method for an Individual Entitlement

1. Log in to Identity Console and select IDM Administration under Identity Manager. Select a driver set.
2. Click ![List of Entitlement Policies](../graphics/action_menu.png "List of Entitlement Policies") button, then select Stop driver.
3. Click the driver icon for the driver that offers the entitlement you want to change.
4. On the Driver Overview page, click the Advanced tab, then click Entitlements.
5. Click the entitlement name to edit the entitlement in the XML viewer.
6. Select the check box for Enable XML editing.
7. In the XML, find the definition of the entitlement you want to change.

   Hereâs an example of the line you should look for:

   ```
   <entitlement conflict-resolution="union" description="Grants membership to GroupWise Distribution lists" display-name="GroupWise Distribution Lists" name="gwDistLists">
   ```
8. Change the conflict-resolution value. The two possible values are the following:

   ```
   conflict-resolution="union"
   ```

   ```
   conflict-resolution="priority"
   ```

   For information about these values, see [Conflict Resolution between Entitlement Policies](bnxmlz5.html).
9. Click OK to save the changes and restart the driver.
10. Click IDM Administration to browse to and restart the Entitlements Service driver.

## 9.2.3 Prioritizing Entitlement Policies

By default, the order of the list of Entitlement Policies does not matter. This is because the driver configurations shipped with Identity Manager have conflict-resolution="union" as the method of conflict resolution for each entitlement.

If you change any of the entitlements to conflict-resolution="priority," then the order of the list of Entitlement Policies matters, but only for those entitlements you changed. For information about these values, see [Conflict Resolution between Entitlement Policies](bnxmlz5.html).

1. In Identity Console, click Role-Based Entitlements > Role-Based Entitlements.
2. Search for and select a driver set.

   A page appears with a list of the Entitlement policies.
3. Change the priority of the Entitlement policies by selecting a policy and using the arrow buttons to move it up and down in the list.

   Moving an entitlement policy higher in the list gives it a higher priority.
4. Click Close to restart the driver.

   Changes in priority donât take effect until the driver is restarted.
