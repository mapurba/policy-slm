# 10.1 Object class violation when creating a user with templates

The driver fails to create a user with the following error:

```
LDAPException: Object Class Violation (65) Object Class Violation
```

To workaround the issue, examine the template object used in eDirectory and remove the setPasswordAfterCreate attribute from the object.
