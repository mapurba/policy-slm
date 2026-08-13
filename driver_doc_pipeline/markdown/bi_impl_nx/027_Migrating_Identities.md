# 5.3 Migrating Identities

When you first run the Linux and UNIX driver, you might have identities in the Identity Vault that you want to provision to the connected system, or vice versa. Identity Manager provides a built-in migration feature to help you accomplish this.

## 5.3.1 Migrating Identities from the Identity Vault to the Connected System

1. In iManager, open the Identity Manager Driver Overview for the driver.
2. Click Migrate from Identity Vault. An empty list of objects to migrate is displayed.
3. Click Add. A browse and search dialog box that allows you to select objects is displayed.
4. Select the objects you want to migrate, then click OK.

To view the results of the migration, click View the Driver Status Log. For details about the log, see [The Status Log](b3xzdtn.html#b3yeaix).

If a user has a Distribution Password, the Distribution Password is migrated to the connected system as the user’s password. Otherwise, no password is migrated. For information about Universal Passwords and Distribution Passwords, see the [Password Management Administration Guide](https://www.netiq.com/documentation/password_management33/).

## 5.3.2 Migrating Identities from the Connected System to the Identity Vault

1. In iManager, open the Identity Manager Driver Overview for the driver.
2. Click Migrate into Identity Vault to display the Migrate Data into the Identity Vault window.
3. Specify your search criteria:

   1. To view the list of eDirectory™ classes and attributes, click Edit List.
   2. Select class User or class Group.

      *IMPORTANT:*Identity Manager imports objects by class in the order specified in the list. Migrate users before you migrate groups so that the users can be added to the newly created groups.
   3. Select the attributes to be used as search criteria for objects of the selected class, then click OK.

      The eDirectory attributes map to Linux and UNIX attributes as specified by the driver schema: CN maps to loginName, etc. For the default mappings, see [Table 1-1, Default Linux and UNIX Driver Filter and Schema Mapping](b3wx9up.html#b456yf7).

      To see RFC 2307 attributes, click Show all attributes from all classes above the attribute list.
   4. Specify values for the selected attributes, then click OK.

      The values can include basic regular expressions. For details about basic regular expressions, use the man grep command.
4. Click OK.

To view the results of the migration, click View the Driver Status Log. For details about the log, see [The Status Log](b3xzdtn.html#b3yeaix).

Because local passwords are irreversibly encrypted, they cannot be submitted to the Metadirectory engine until they are changed. Install the PAM or LAM module to capture password changes. For information about installing the PAM or LAM module, see [Installing the PAM or LAM Module](b3xfnmq.html).

## 5.3.3 Synchronizing the Driver

To generate events for associated objects that have changed since the driver’s last processing, open the Identity Manager Driver Overview page for the driver in iManager, then click Synchronize.
