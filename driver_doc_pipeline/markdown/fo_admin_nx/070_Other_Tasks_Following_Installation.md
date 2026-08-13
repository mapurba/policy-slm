# 11.3 Other Tasks Following Installation

After the initial installation or upgrade of Platform Services, other tasks that you may need to perform from time to time include the following:

* [Configuring PAM](bfmrhmm.html#bfmri70)
* [Configuring LAM on AIX](bfmrhmm.html#brk4a87)
* [Running a Full Synchronization](bfmrhmm.html#bfmrj29)
* [Starting Platform Services](bfmrhmm.html#bfmrj2a)
* [Stopping Platform Services](bfmrhmm.html#bfmrj2b)
* [Testing Platform Services for PAM or LAM](bfmrhmm.html#bk8rud8)

## 11.3.1 Configuring PAM

If you have chosen to configure for authentication redirection on a platform that is running Linux or UNIX, you will need to manually configure PAM on that system. For technical instructions on how to configure PAM for authentication, see [PAM Configuration Notes](chdibedb.html).

The Platform Services installer automatically copies sample configurations you can use as templates to the following location:

* If you are running Linux: /usr/local/ASAM/PlatformServices/pam.d/
* If you are running UNIX: /usr/local/ASAM/PlatformServices/pam.conf.sample/

## 11.3.2 Configuring LAM on AIX

If you have chosen to configure for authentication redirection on a platform that is running AIX, and you want to use IBM’s proprietary Loadable Authentication Module (LAM), you will need to manually configure the Fan-Out Driver’s LAM module on that AIX system. For technical instructions on how to configure LAM for authentication, see [LAM Configuration Notes](brk5h3s.html).

The Platform Services installer automatically copies sample LAM-related configuration files you can use as templates to the following location:

```
  /usr/local/ASAM/bin/PlatformServices/methods.cfg.sample
  /usr/local/ASAM/bin/PlatformServices/user.sample
  /usr/local/ASAM/bin/PlatformServices/user.sample2
```

## 11.3.3 Running a Full Synchronization

Upon initial deployment of the Fan-Out Driver Platform Services, you may find it useful and necessary to perform an initial migration or synchronization of users and groups within the Identity Vault. You can perform a full synchronization by executing asamrcvrd fullsync. Location of this executable will vary depending on your target platform. See [Table 11-3](bfmrhmm.html#bfn5s2r) for the appropriate full command line that includes your directory location.

*Table 11-3* Command for Full Synchronization by Platform

| Platform | Synchronization Command |
| Linux | /etc/init.d/asamrcvrd fullsync |
| Solaris | /etc/init.d/asamrcvrd fullsync |
| AIX | /etc/rc.d/init.d/asamrcvrd fullsync |
| HP-UX | /sbin/init.d/asamrcvrd fullsync |
| FreeBSD | /usr/local/rc.d/init.d/asamrcvrd fullsync |
| Tru64 | /sbin/init.d/asamrcvrd fullsync |

## 11.3.4 Starting Platform Services

Starting Platform Services requires you to start one or more of the following components, depending on your configuration:

* Platform Receiver
* Platform Services Process
* Platform Services Cache Daemon

For more information about these components, see [About Platform Services for Linux and UNIX](bbcjcgif.html) and [Section 12.0, Configuring and Administering Platform Services](bexh69p.html).

### Starting the Platform Receiver

You can start the Platform Receiver by executing asamrcvrd start. Location of this executable will vary depending on your target platform. See [Table 11-4](bfmrhmm.html#bfn76zg) for the appropriate full command line that includes your directory location.

*Table 11-4* Command for Starting the Platform Receiver

| Platform | Platform Receiver Start Command |
| Linux | /etc/init.d/asamrcvrd start |
| Solaris | /etc/init.d/asamrcvrd start |
| AIX | /etc/rc.d/init.d/asamrcvrd start |
| HP-UX | /sbin/init.d/asamrcvrd start |
| FreeBSD | /usr/local/rc.d/init.d/asamrcvrd start |
| Tru64 | /sbin/init.d/asamrcvrd start |

### Starting the Platform Services Process

You can start the Platform Services Process by executing asampspd start. Location of this executable will vary depending on your target platform. See [Table 11-5](bfmrhmm.html#bfn7ho5) for the appropriate full command line that includes your directory location.

*Table 11-5* Command for Starting the Platform Services Process

| Platform | Platform Services Process Start Command |
| Linux | /etc/init.d/asampspd start |
| Solaris | /etc/init.d/asampspd start |
| AIX | /etc/rc.d/init.d/asampspd start |
| HP-UX | /sbin/init.d/asampspd start |
| FreeBSD | /usr/local/rc.d/init.d/asampspd start |
| Tru64 | /sbin/init.d/asampspd start |

### Starting the Platform Services Cache Daemon

You can start the Platform Services Cache Daemon by executing asampsd start. Location of this executable will vary depending on your target platform. See [Table 11-6](bfmrhmm.html#bfn7hoe) for the appropriate full command line that includes your directory location.

*Table 11-6* Command for Starting the Platform Services Cache Daemon

| Platform | Platform Services Cache Daemon Start Command |
| Linux | /etc/init.d/asampsd start |
| Solaris | /etc/init.d/asampsd start |
| AIX | /etc/rc.d/init.d/asampsd start |
| HP-UX | /sbin/init.d/asampsd start |

## 11.3.5 Stopping Platform Services

Stopping Platform Services requires you to stop one or more of the following components, depending on your configuration:

* Platform Receiver
* Platform Services Process
* Platform Services Cache Daemon

For more information about these components, see [About Platform Services for Linux and UNIX](bbcjcgif.html) and [Section 12.0, Configuring and Administering Platform Services](bexh69p.html).

### Stopping the Platform Receiver

You can stop the Platform Receiver by executing asamrcvrd stop. Location of this executable will vary depending on your target platform. See [Table 11-7](bfmrhmm.html#bfn7kzt) for the appropriate full command line that includes your directory location.

*Table 11-7* Command for Stopping the Platform Receiver

| Platform | Platform Receiver Stop Command |
| Linux | /etc/init.d/asamrcvrd stop |
| Solaris | /etc/init.d/asamrcvrd stop |
| AIX | /etc/rc.d/init.d/asamrcvrd stop |
| HP-UX | /sbin/init.d/asamrcvrd stop |
| FreeBSD | /usr/local/rc.d/init.d/asamrcvrd stop |
| Tru64 | /sbin/init.d/asamrcvrd stop |

### Stopping the Platform Services Process

You can stop the Platform Services Process by executing asampspd stop. Location of this executable will vary depending on your target platform. See [Table 11-8](bfmrhmm.html#bfn7l02) for the appropriate full command line that includes your directory location.

*Table 11-8* Command for Stopping the Platform Services Process

| Platform | Platform Services Process Stop Command |
| Linux | /etc/init.d/asampspd stop |
| Solaris | /etc/init.d/asampspd stop |
| AIX | /etc/rc.d/init.d/asampspd stop |
| HP-UX | /sbin/init.d/asampspd stop |
| FreeBSD | /usr/local/rc.d/init.d/asampspd stop |
| Tru64 | /sbin/init.d/asampspd start |

### Stopping the Platform Services Cache Daemon

You can stop the Platform Services Cache Daemon by executing asampsd stop. Location of this executable will vary depending on your target platform. See [Table 11-9](bfmrhmm.html#bfn7l0b) for the appropriate full command line that includes your directory location.

*Table 11-9* Command for Stopping the Platform Services Cache Daemon

| Platform | Platform Services Cache Daemon Stop Command |
| Linux | /etc/init.d/asampsd stop |
| Solaris | /etc/init.d/asampsd stop |
| AIX | /etc/rc.d/init.d/asampsd stop |
| HP-UX | /sbin/init.d/asampsd stop |

## 11.3.6 Testing Platform Services for PAM or LAM

If you are using PAM (or LAM on AIX) for password authentication, it may be helpful to verify that the Platform Services Process (asampsp) and the API Library (libascauth) are functioning properly, before you finalize PAM configuration. You can do this with a program called asctest, which is included with your Platform Services installation. Here’s where to find it:

```
/usr/local/ASAM/bin/PlatformServices/PlatformClient/asctest
```

This program allows you to test the various calls (listed in [Table 11-10](bfmrhmm.html#bk8sc08)) that can be made to the API library in support of PAM. To use asctest, simply enter it from a command line with no parameters. When prompted select the desired method by entering its corresponding letter (a-o) and respond to any further prompts. The following table provides descriptions of the API methods.

*Table 11-10* API methods used for PAM.

| API Method | Description |
| ASC\_ADMINRSTPASSWD | Reset a user password using an administrative reset. |
| ASC\_CHGPASSWD | Change a user’s password. |
| ASC\_CHKPASSWD | Check a user’s password. |
| ASC\_DAYS | Convert seconds to days. |
| ASC\_GETCONTEXT | Look up a user’s context from a contextless name. |
| ASC\_GETGROUPBYGID | Look up a group by its gidNumber. |
| ASC\_GETUSERBYUID | Look up a user by its uidNumber. |
| ASC\_GRPMEM | List a group’s members. |
| ASC\_LISTSEQV | List a user’s security equivalences. |
| ASC\_READATTR | Read a single-valued attribute on a user. |
| ASC\_READGROUPATTR | Read an attribute on a group. |
| ASC\_RIGHTS | Test attribute rights for one object over another. |
| ASC\_SECEQUAL | Check user security equivalence to another object. |
| ASC\_STRERROR | Convert ASCLIENT error code into a human-readable text string. |
| ASC\_USER\_INCLUDE\_EXCLUDE | Check whether a user matches the include/exclude list. |
