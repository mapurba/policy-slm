# 8.10 Standard Exclude List

Platform Services normally excludes certain special users from Authentication Services processing and Identity Provisioning. You can use the platform configuration file to override this or to specify additional users and groups to be excluded.

Users excluded from Authentication Services are authenticated using the local security system. Provisioning events are not processed for users and groups excluded from Identity Provisioning.

For details about Include/Exclude processing, see

* [Using Include and Exclude Configuration Statements](beibhfbg.html)
* [AM.GROUP.INCLUDE Statement / AM.GROUP.EXCLUDE Statement](beiffigc.html#chddjjje)
* [AM.USER.INCLUDE Statement / AM.USER.EXCLUDE Statement](beiffigc.html#chdiefij)
* [AS.USER.INCLUDE Statement / AS.USER.EXCLUDE Statement](beiffigc.html#chdgehfb)

Following is the standard list of users and groups that are excluded from Authentication Services and Identity Provisioning processing.

| Account Operators | adm | admin |
| administrator | administrators | audit |
| Backup Operators | bin | Cert Publishers |
| cron | daemon | DB2XML |
| DHCP Administrators | dip | disk |
| DnsAdmins | DnsUpdateProxy | Domain Admins |
| Domain Computers | Domain Controllers | ecs |
| Enterprise Admins | floppy | ftp |
| games | gdm | gopher |
| Group Policy Creator Owners | guest | halt |
| hpdb | ibmuser | ident |
| imnadm | IUSR\_WIN2KEDIR | IWAM\_WIN2KEDIR |
| kmem | krbtgt | ldap |
| listen | lock | lp |
| lpd | mail | mailnull |
| man | mem | MTS Impersonators |
| news | nfsnobody | noaccess |
| nobody | nobody4 | nogroup |
| nscd | ntp | nusers |
| nuucp | nwgroup | nwldap |
| nwprint | nwroot | nwuser |
| operator | other | perf |
| Print Operators | printq | QAUTPROF |
| QBRMS | QCLUMGT | QCLUSTER |
| QCOLSRV | QDBSHR | QDBSHRDO |
| QDESADM | QDESUSR | QDFTOWN |
| QDIRSRV | QDLFM | QDOC |
| QDSNX | QEJB | QFNC |
| QGATE | QIJS | QIPP |
| QLPAUTO | QLPINSTALL | QMSF |
| QNETSPLF | QNETWARE | QNFSANON |
| QNTP | QPEX | QPGMR |
| QPM400 | QRJE | QSECOFR |
| QSNADS | QSPL | QSPLJOB |
| QSRV | QSRVBAS | QSVCDRCTR |
| QSYS | QSYSOPR | QTCM |
| QTCP | QTFTP | QTMHHTP1 |
| QTMHHTTP | QTMPLPD | QTSTRQS |
| QUMB | QUSER | QYPSJSVR |
| radvd | RAS and IAS Servers | Replicator |
| root | rpc | rpcuser |
| rpm | Schema Admins | security |
| Server Operators | shutdown | slocate |
| staff | sync | sys |
| sys1 | sysadmin | system |
| TsInternetUser | tty | users |
| usr | utmp | uucp |
| wheel | wine | www |
| xfs |  |  |
