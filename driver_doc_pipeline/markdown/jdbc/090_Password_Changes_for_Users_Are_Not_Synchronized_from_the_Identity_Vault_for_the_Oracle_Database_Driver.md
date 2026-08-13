# 15.2 Password Changes for Users Are Not Synchronized from the Identity Vault for the Oracle Database Driver

The Oracle Database driver created with an Indirect/Direct Synchronization sample package used an incorrect query to create or change the name and password of the users. The driver patch 2 fixed this issue, but after upgrading to patch 2, if the password is reset for an existing user, it fails with an error and displays the following message:

```
User does not exist.
```

To workaround this issue, after upgrading the driver, delete the existing user from the Oracle database and synchronize it from the Identity Vault.
