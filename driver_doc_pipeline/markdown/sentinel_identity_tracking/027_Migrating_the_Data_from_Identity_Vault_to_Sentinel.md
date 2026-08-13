# 9.2 Migrating the Data from Identity Vault to Sentinel

You can migrate the user data with or without manager references.

## 9.2.1 Migrating Data Without Manager References

If your Identity Vault user data does not have manager references between user objects, the migration is a one-step process.

You can either manually select the objects to be migrated by using the Migrate from Identity Vault option in Identity Console. or allow the Identity Vault to automatically submit all objects by using the Synchronize option in Identity Console.

After the migration is complete, enable the Subscriber channel by setting the Initial Synchronization Mode to false.

## 9.2.2 Migrating Data with Manager References

If your Identity Vault user data has manager references between user objects the migration is a two-step process.

First, perform the steps mentioned in [Migrating Data Without Manager References](migrating-the-data-from-idv-to-sentinel.html#bzpwuxs).

After the migration is complete, repeat the procedure. Repeating the procedure ensures that manager references that could not be established in the first step are resolved.

If an employee's Identity Vault object is synchronized before the employee's manager's Identity Vault object, the manager reference in Sentinel cannot be established because the manager's object does not exist in Sentinel yet. When you repeat the process, migration occurs after all objects are created in Sentinel so that all manager references can be established in Sentinel.
