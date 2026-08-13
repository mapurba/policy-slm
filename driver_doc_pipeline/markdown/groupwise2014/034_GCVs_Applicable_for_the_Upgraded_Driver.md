# A.3 GCVs Applicable for the Upgraded Driver

The following GCVs are retained from the existing driver setup after the driver upgrade. They are applicable only for the upgraded driver. They don’t apply to a new driver.

*Synchronize GroupWise Distribution Lists:*
Select True if you want this driver to synchronize eDirectory’s GroupWise Distribution List objects with distribution lists in GroupWise. By default, it is set to False.

*Sync GroupWise External Entities to this Domain:*
This option is available only if Synchronize GroupWise Distribution Lists is set to True. Specify a non-GroupWise domain name that exists within the GroupWise system. This domain must host at least one external post office, defined in Sync GroupWise External Entities to this External Post Office.

*Synchronize GroupWise External Entity Objects:*
Select True to synchronize eDirectory’s GroupWise External Entity objects with external users in GroupWise. By default, it is set to False.

*Sync GroupWise External Entities to this External Post Office:*
This option is available only if Synchronize GroupWise Distribution Lists is set to True. Specify an external post office name that exists within the GroupWise system. This post office must be subordinate to the GroupWise domain defined in Sync GroupWise External Entities to this Domain.

*Action On eDirectory GroupWise External Entity Delete:*
Select the action you want the driver to take on an associated GroupWise account (mailbox), when a GroupWise external entity is deleted in eDirectory. The options are:

* Disable the GroupWise account
* Delete the GroupWise account
* Expire the GroupWise account
* Disable and Expire the GroupWise account

*Action On eDirectory GroupWise External Entity Expire/Unexpire:*
Select the action you want the drive to take on the associated GroupWise account (mailbox), when an expired or unexpired GroupWise external entity logs into eDirectory. The options are:

* Expire/Unexpire the GroupWise Account
* Disable/Enable the GroupWise Account
* Disable/Enable and Expire/Unexpire the GroupWise Account

*Action On eDirectory GroupWise External Entity Disable/Enable:*
Select the action you want the driver to take on the associated GroupWise account (mailbox), when a disabled or enabled GroupWise external entity logs into eDirectory. The options are:

* Expire/Unexpire the GroupWise Account
* Disable/Enable the GroupWise Account
* Disable/Enable and Expire/Unexpire the GroupWise Account

*Remove GroupWise External Entity from all Distribution Lists on expire:*
Select True if you want the driver to remove the GroupWise external entity from all distribution lists when the GroupWise account is expired; otherwise, select False.

*Remove GroupWise External Entity from all Distribution Lists on disable:*
Select True if you want the driver to remove the GroupWise external entity from all distribution lists when the GroupWise account is disabled; otherwise, select False.

*Use Distribution Lists Entitlement:*
Select True if you want the driver to manage GroupWise distribution lists based on the gwDistLists Entitlement; otherwise, select False.

*Synchronize the eDirectory password to the GroupWise regular password:*
Select True to allow passwords to flow from eDirectory to GroupWise. Select False if you do not want to set the regular password.

GroupWise has two passwords, the initial password and regular password. The initial password is stored in clear text and can be seen by an admin. The regular password is encrypted and cannot be viewed. When it is set, the regular password is used by GroupWise instead of the initial/default password. When a GroupWise user changes his or her password, it is stored as the regular password. For security, the initial password is never set to a password sent from eDirectory.
