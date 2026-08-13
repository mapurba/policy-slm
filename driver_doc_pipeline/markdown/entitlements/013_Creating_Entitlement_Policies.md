# 6.0 Creating Entitlement Policies

The Entitlements Service driver implements entitlements through the use of entitlement policies. An entitlement policy contains the following:

* *Membership:*
  The list of users assigned to the policy. A user can be dynamically assigned to the policy when he or she meets the criteria for the policy, or the user can be statically (manually) assigned to the policy.
* *Entitlements:*
  The list of entitlements associated with the policy. Users assigned to the policy receive all of the entitlements associated with the policy. If the user is removed from the policy, he or she loses all entitlements associated with the policy.

To create an entitlement policy:

1. Log in to Identity Console.
2. In the IDM Administration, click Role-Based Entitlements.
3. In the Select driver set field, select the driver set where you want to create the entitlement policy.

   This list displays all entitlement policies that have been created for the driver set. If you are using role-based entitlements for the first time, no policies are listed.

   ![List of Entitlement Policies](../graphics/entitlement_idconsole.png "List of Entitlement Policies")
4. Click ![List of Entitlement Policies](../graphics/create_certificate.png "List of Entitlement Policies") to launch the Entitlement Policy Wizard.
5. On the Step 1 of 6: Name and describe the Entitlement Policy page, fill in the fields:

   *Entitlement Policy Name:*
   Provide a name that indicates the purpose of the entitlement. The name must be unique within the driver set and cannot include more than 64 characters.

   *Description:*
   Provide any additional information you want to identify the policy.

   Click Create.
6. On the Step 2 of 6: Define Dynamic Membership page, fill in the fields:

   Dynamic membership lets you define which users should be members of the entitlement policy by specifying criteria and specifying where in the tree to search for users that meet the criteria. If a user meets the criteria you specify, the policy’s entitlements are automatically applied to the user. If the user’s information changes and no longer meets the criteria, the entitlements are revoked without any manual intervention.

   *Search Identity:*
   Specify an object that has the rights that you want to be used when querying for Dynamic Membership. This field defaults to the object you logged in as, but you can change it to an object with the appropriate rights.

   For example, if you log in as the administrator, there might be parts of the tree that you have rights to, but you don't want them included in the query for the dynamic list of members.

   You could use this field to specify the Driver Set object, making sure that the Driver Set has the appropriate rights. Or, you could create a User object specifically for use with entitlement policies, and assign it the rights you want the query to use.

   *Begin Search at (Base DN):*
   Specify the base container where you want the user search to begin.

   *Scope of Search:*
   Specify whether you want to search the base container and all of its subcontainers (This container and its subcontainers) or only the base container (This container only).

   For the entitlement policy to evaluate users in the containers you specify, the users must be in a read/write or master replica on the Identity Manager server that is running the Entitlements Service driver.

   *Criteria:*
   Specify the criteria that determine which users are members of the policy. The criteria are organized into criteria groups. Each group can contain one or more criteria. You click the ![List of Entitlement Policies](../graphics/create_certificate.png "List of Entitlement Policies") icon to add criterion to a group. You can also click ![List of Entitlement Policies](../graphics/create_certificate.png "List of Entitlement Policies") near Criteria Group 1 to create additional groups.

   By default, the criteria include all User class objects (and objects of classes derived from the User class) within the search scope.

   If you create a new object class derived from User, an existing entitlement policy does not recognize that class until you make a modification to the entitlement policy. This prevents users of a new class from being granted entitlements unintentionally. When any modification is made to the entitlement policy, the list of user-derived classes for that policy is updated.
7. After you have added the criteria you want, click Test Filter to view the list or users who meet the criteria.
8. On the Step 3 of 6: Define Static Members page, fill in the fields:

   Static membership lets you include users who don’t meet the dynamic membership criteria or exclude users who meet the criteria but should not be members of the policy.

   *Include Members:*
   Type the DN of a user you want to include, or click ![List of Entitlement Policies](../graphics/create_certificate.png "List of Entitlement Policies") to browse for and select the user, then press Enter to add the user to the inclusion list. To remove a user from the inclusion list, select the user and press Delete. To edit a user name, double-click the user.

   *Exclude Members:*
   Type the DN of a user you want to exclude, or click ![List of Entitlement Policies](../graphics/create_certificate.png "List of Entitlement Policies") to browse for and select the user, then press Enter to add the user to the exclusion list. To remove a user from the exclusion list, select the user and press Delete. To edit a user name, double-click the user.
9. On the Step 4 of 6: Select Entitlements on the Connected Systems to Grant to Users page, add the entitlements you want associated with the policy:

   1. Click ![List of Entitlement Policies](../graphics/create_certificate.png "List of Entitlement Policies") to display a list of drivers with entitlements.
   2. Select the driver with the entitlement you want to add, then click Add to display a list of the driver’s entitlements.
   3. Select the entitlement you want to add, then click Add.
   4. (Optional) If the entitlement requires you to set a value, click ![List of Entitlement Policies](../graphics/create_certificate.png "List of Entitlement Policies") to add the value.

      or

      If the entitlement requires a query to display the appropriate values (for example, a query for the groups in the connected system), run the query and select the appropriate value.

      You can choose an external query, which runs a new query of the connected system, or you can choose a cached query, which simply displays the results of the last query that ran.
   5. To add another entitlement from the same driver, click the ![List of Entitlement Policies](../graphics/create_certificate.png "List of Entitlement Policies") icon located on the same line as the driver name.
   6. To add an entitlement from another driver, repeat [Step 9.a](create-entitlement-policies.html#bfqv2ah) through [Step 9.d](create-entitlement-policies.html#bfrb1kl).
10. On the Step 5 of 6: Assign Rights to Objects page, add the Identity Vault objects for which you want the entitlement policy to be a trustee.

    Each member of the policy becomes a trustee of the objects you add. There are several reasons why you might want to make the policy a trustee of an object:

    * One of the policy’s entitlements requires the policy’s members to have rights to an object.
    * You want to use the policy to assign users as trustees of an object even though rights to the object are not required for an entitlement. In this case, you are using the entitlement policy to grant and revoke trustee rights for members of the policy.

    Use the following options to manage the trustee assignments:

    *Add Object:*
    Use this option to browse for and select the objects that you want to make the policy a trustee of.

    *Rights to Selected Objects:*
    Click an object in the Object Name list to view the policy’s rights to the object. You can add or remove rights by selecting or deselecting the desired rights. The Inherit check box determines whether the rights flow down in the tree. For example, if you are assigning rights to a container object, and you want the entitlement policy to have the same rights to the objects and sub-containers that are below that container, select the Inherit check box.

    *Add Property:*
    In addition to doing a global assignment of rights to all properties ([All Attributes Rights]), you can assign rights to specific properties. This lets you limit rights to some properties and expand rights to others. To add a property, click ![List of Entitlement Policies](../graphics/create_certificate.png "List of Entitlement Policies") near Properties to browse for and select the desired property. After the property is added to the Rights to Selected Objects list, make the assigned rights modifications that you want.

    *Remove Object or Property:*
    Click the ![List of Entitlement Policies](../graphics/delete.png "List of Entitlement Policies") button to remove an object from the Object Name list or a property from the Rights to Selected Object list.
11. When you have finished making changes to trustee assignments, click Next.
12. On the Step 6 of 6: Entitlement Policy Summary page, review the policy information, then click Finish to create the policy and add it to the Entitlement Policy List.
13. Click ![List of Entitlement Policies](../graphics/action_menu.png "List of Entitlement Policies") > Restart to start the Entitlements Service driver.

    After the driver starts, it evaluates the new policy (and all other policies in the list) and grants the appropriate entitlements to the policy members.
