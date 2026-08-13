# E.0 Appendix – Directory Scopes

Below is the list of all authorized scopes required by the driver. It is highly recommended that you refer to the DirectoryScopes.txt file bundled with the driver and any driver patches as this list can and will change as new features are added or old endpoints are deprecated. When authorizing scopes, the values should be plain text (use a text file editor, do not copy and paste from a web, pdf, or rich document as that may result in failures due to extra information kept in the clipboard), all on one line, and comma separated. The DirectoryScopes.txt file is properly formatted and should be used for this purpose. See section 2.2.3 – Configuring API and Service Account – for more information.

```

https://www.googleapis.com/auth/admin.directory.group,
https://www.googleapis.com/auth/admin.directory.group.member,
https://www.googleapis.com/auth/admin.directory.orgunit,
https://www.googleapis.com/auth/admin.directory.user,
https://www.googleapis.com/auth/admin.directory.user.alias,
https://www.googleapis.com/auth/admin.directory.user.security,
https://www.googleapis.com/auth/admin.directory.userschema,
https://www.googleapis.com/auth/userinfo.profile,
https://www.googleapis.com/auth/userinfo.email,
http://www.google.com/m8/feeds,
https://www.googleapis.com/auth/contacts.readonly,
https://www.googleapis.com/auth/apps.groups.settings,
https://www.googleapis.com/auth/admin.directory.rolemanagement,
https://www.googleapis.com/auth/gmail.settings.basic,
https://www.googleapis.com/auth/gmail.settings.sharing,
https://www.googleapis.com/auth/gmail.labels,
https://apps-apis.google.com/a/feeds/emailsettings/2.0/
```
