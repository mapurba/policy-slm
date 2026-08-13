# 6.3 Migrating Identities

When you first run the IBM i driver, you might have identities in the Identity Vault that you want to provision to the connected system, or vice versa. Identity Manager provides a built-in migration feature to help you accomplish this.

## 6.3.1 Migrating Identities from the Identity Vault to the Connected System

1. In iManager, open the Identity Manager Driver Overview for the driver.
2. Click Migrate from Identity Vault. An empty list of objects to migrate is displayed.
3. Click Add. A browse and search dialog box that allows you to select objects is displayed.
4. Select the objects you want to migrate, then click OK.

To view the results of the migration, click View the Driver Status Log. For details about the log, see [The Status Log](b3xzdtn.html#b3yeaix).

If a user has a Distribution Password, the Distribution Password is migrated to the connected system as the user’s password. Otherwise, no password is migrated. For information about Universal Passwords and Distribution Passwords, see the appropriate version of the Password Management Administration Guide at the [NetIQ Documentation Web site](https://www.netiq.com/documentation).

## 6.3.2 Migrating Identities from the Connected System to the Identity Vault

1. In iManager, open the Identity Manager Driver Overview for the driver.
2. Click Migrate into Identity Vault to display the Migrate Data into the Identity Vault window.
3. Specify your search criteria:

   1. To view the list of eDirectory™ classes and attributes, click Edit List.
   2. Select class User or class Group.

      *IMPORTANT:*Identity Manager imports objects by class in the order specified in the list. Migrate users before you migrate groups so that the users can be added to the newly created groups.
   3. Select the attributes to be used as search criteria for objects of the selected class, then click OK.

      The eDirectory attributes map to i5/OS attributes as specified by the driver schema: CN maps to USRPRF, etc. For the default mappings, see [Table 1-2, Default eDirectory User to i5/OS UserProfile Mapping](b3wx9up.html#b4r8562) and [Table 1-3, Default eDirectory Group to IBM i GroupProfile Mapping](b3wx9up.html#b4r8dxo).

      To see i5/OS attributes, click Show all attributes from all classes above the attribute list.
   4. Specify values for the selected attributes, then click OK.

      The values can include basic regular expressions.
4. Click OK.

To view the results of the migration, click View the Driver Status Log. For details about the log, see [The Status Log](b3xzdtn.html#b3yeaix).

Because local passwords cannot be retrieved from the IBM i security system, they cannot be submitted to the Metadirectory engine until they are changed. The Validate Password exit program captures password changes.

## 6.3.3 Synchronizing the Driver

To generate events for associated objects that have changed since the driver’s last processing, open the Identity Manager Driver Overview page for the driver in iManager, then click Synchronize.
