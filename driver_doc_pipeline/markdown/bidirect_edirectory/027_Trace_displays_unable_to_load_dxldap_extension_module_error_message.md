# 10.2 Trace displays unable to load dxldap extension module error message

Sometimes NDStrace displays the following error message when you refresh the LDAP server object or restart eDirectory on a computer that has change-log installed and had Identity Manager installed on it earlier:

```
Unable to load extension module dxldap, err = -5984 (0xffffffffffffe8a0)
```

When the LDAP server tries to load the dxldap handlers that were registered earlier with Identity Manager installation, it doesn't find them because dxldap module which has those handlers no longer exists on the computer.

It is safe to ignore this error.
