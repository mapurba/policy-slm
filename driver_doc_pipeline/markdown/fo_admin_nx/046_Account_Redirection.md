# 8.4 Account Redirection

Account Redirection uses eDirectory for user and group account information. By extending your users and groups with the posixAccount and posixGroup auxiliary classes, you can assign the following Posix attributes for your users and groups:

* loginName
* uidNumber
* gidNumber
* gecos
* homeDirectory
* loginShell
* groupName
* memberUid

These attributes correspond to the following lines in /etc/passwd:

```
loginName:x:uidNumber:gidNumber:gecos:homeDirectory:loginShell
```

For groups, they correspond to the following lines in /etc/group:

```
groupName:x:gidNumber:memberUid
```

This Posix information will be synchronized to a local memory cache on your Linux or UNIX system and accessed by the Name Service Switch. The Name Service Switch runs when a user logs on and also when a command that requires information from this or another user or group account is invoked.
