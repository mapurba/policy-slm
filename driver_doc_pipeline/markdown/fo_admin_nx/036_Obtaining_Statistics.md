# 7.1 Obtaining Statistics

It may be useful, often for support purposes, to obtain statistics from the actively running Core Driver shim. You can view installation information, such as patch level and build dates, as well as configuration settings, such as directory and container locations, census and search object data, platforms and platform data. More detailed statistics, such as file handles, threads, and network resources are also available, but more useful for internal support.

To obtain statistics, use the following command:

/usr/local/ASAM/bin/CoreDriver/asamcdrv stats

*NOTE:*If LDAP client libraries are not in your executable path, you may need to export LD\_LIBRARY\_PATH=/opt/novell/eDirectory/lib64

The output will be printed to the console, similar to the following:

```
Build:                        4.8.3.0 20210111722
Start Time:                   20210121201627Z

Configuration:
  LDAP Server:                localhost:636
  Core Driver Object:         cn=fanout,ou=Agents,ou=ASAM System,o=system
  ASAM Master User:           cn=admin,ou=sa,o=system
  Install Directory:          /usr/local/ASAM/
  System Container:           ou=ASAM System,o=system
  Census Search Objects:      1
  Platform Sets:              1
  UID/GID Sets:               0
  Platforms:                  1
  Last Trawl Time:
```
