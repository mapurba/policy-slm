# 3.3 Creating ID Policies

An ID Policy container ![ID Policy container icon](../graphics/id_provider_policycont_n.png "ID Policy container icon") is a repository for ID policies and is used in conjunction with the ID Provider driver. An ID policy ![ID policy icon](../graphics/id_provider_policy_n.png "ID policy icon") allows the ID Provider driver to generate unique IDs. When the ID Provider driver receives an ID request from a client, it generates an ID based on the ID policy specified in the request and passes it to the client.

* [Default Policies](create-id-provider-policies.html#bs0qxm7)
* [Creating an ID Policy](create-id-provider-policies.html#bs0qxpw)
* [Managing the Access Control List](create-id-provider-policies.html#bs0qy2q)

## 3.3.1 Default Policies

By default, there are three ID policies that are created when the driver is imported. The three policies are sample policies. You can use these policies or create your own. The default policies are:

* *pid:*
  The pid policy generates unique IDs between 100000 to 2000000000. It also adds the prefix of “PID” to each unique ID.
* *wfid:*
  The wfid policy generates unique IDs between 10000000 to 99999999. It also adds the prefix of “WFID” to each unique ID for the workforce ID.
* *woid:*
  The woid policy generates unique IDs between 100000 to 2000000000. It also adds the prefix of “WOID” to each unique ID.

## 3.3.2 Creating an ID Policy

To create an ID policy:

1. In Designer, right-click the ID Policy container in the Outline tab, then click New > ID Policy.

   The ID Policy container is created when the ID Provider driver is created. The ID Policy container can only reside under the ID Provider driver.
2. Specify the name for the ID policy, then click OK.
3. Double-click the ID policy to access the properties page.
4. Use the following information to create your ID policy:

   *Policy Name:*
   Specify the name of the ID policy.

   *Policy’s Last ID:*
   The last ID number that was used by this ID policy. If you have deployed this ID policy, use the Connect icon to update this field to the last ID number that was stored in the Identity Vault for this ID policy.

   *NOTE:*Only the ID Provider driver can update the last value stored in the Identity Vault.

   *Constraints Minimum/Maximum:*
   Numbers must be between 0 and 2147483647. If you have a fixed system that can only handle eight digits, set the Maximum to 99999999.

   *Constraints Exclude/Include:*
   Allows you to include or exclude a set of numbers that you type in. Numbers can be typed in a coma-delimited list and you can use ranges, such as 10,100,1000,5000-10000,1099, etc.

   *Constraints Prefix:*
   Allows you to give a prefix to the IDs that are generated using this ID policy. If you create multiple ID policies, a prefix is useful to see which ID policies are being used. An example is WFID, for workforce IDs.

   *Constraints Fill Yes/No:*
   If you choose Yes, the ID is filled with leading zeros (0) up to the maximum length. This helps keep generated IDs at the same length. If you select No, it does nothing and the ID lengths increment over time.

   *Access Control Enabled:*
   Check this box if you want to enable access control list.

   *Access Control ACL:*
   Type in the access control lists you want to use. Access control must be enabled before you can type in ACLs. For more information, see [Managing the Access Control List](create-id-provider-policies.html#bs0qy2q).
5. Click OK to save the information.

## 3.3.3 Managing the Access Control List

The Access Control List (ACL) is also called the Object Trustee property. Whenever you make a trustee assignment, the trustee is added as a value to the Object Trustees (ACL) property of the target.

The value for the ACL parameter must match the value that the ACL client is using.
