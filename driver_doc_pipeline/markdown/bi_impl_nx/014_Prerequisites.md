# 3.3 Prerequisites

* [Software Requirements](b3xccfu.html#b3xcf2n)
* [Account Management System Requirements](b3xccfu.html#bbdfboz)
* [Replacing comm Utility for AIX and HP-UX](b3xccfu.html#bk2nxtn)

## 3.3.1 Software Requirements

For information about supported platforms and operating environments, see [the Identity Manager 4.8 Drivers Documentation Web site](https://www.netiq.com/documentation/identity-manager-47-drivers). From this index page, you can select a readme file associated with the platform(s) for which you need support.

## 3.3.2 Account Management System Requirements

* Linux or UNIX systems using files (/etc/passwd), NIS, or NIS+ are supported.
* Either Pluggable Authentication Module (PAM), or Loadable Authentication Module (LAM) on AIX must be used if bidirectional password synchronization is desired. The driver uses PAM and LAM to intercept password changes on the connected system.

  Remote NIS and NIS+ client systems that use PAM are also supported.

You can modify the scripts to support other account management systems. Support for modified scripts is provided by the developer community.

## 3.3.3 Replacing comm Utility for AIX and HP-UX

If you use Identity Manager with a connected system running AIX or HP-UX, you may need to replace the standard comm utility (invoked by the comm command) included with the operating system. Versions of comm that are included with either of these operating systems have been known to fail when used with files that contain long text lines. In general, the problem occurs with text lines longer than 2000 characters.

The Identity Manager driver uses comm to get information from /etc/group. Therefore, if any of your AIX or HP-UX connected systems has an /etc/group file with a line that is longer than 2000 characters, you should use one of the following vendor-approved GNU packages to replace the comm utility:

| Operating System | Vendor Name and Link to Replacement Utilities |
| AIX | IBM |
| HP-UX | [HP](http://hpux.connect.org.uk/hppd/hpux/Gnu/coreutils-8.23/) |
