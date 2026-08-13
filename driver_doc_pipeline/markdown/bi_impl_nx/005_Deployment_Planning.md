# 2.1 Deployment Planning

* Review [Section 3.0, Installing the Linux and UNIX Driver](b3r8si5.html) and [Section 5.0, Configuring the Linux and UNIX Driver](b3r8t50.html).
* Consider where and how you will install each component, and how you will respond to the installation script prompts and other installation decisions.
* Is this a new installation, or are you replacing a NIS driver or Fan-Out driver Platform Services installation? For details about upgrading from the NIS driver or the Fan-Out driver, see [Section 4.0, Upgrading from Another Driver](b3r9hzv.html).
* How do you plan to prototype, test, and roll out your deployment?
* Do you plan to use the include/exclude file on the connected system to limit your initial deployment to a small number of users and groups?
* If you are using AIX and want to publish password changes, will you use PAM or LAM?

  AIX version 5.3 can use either PAM or LAM, but previous AIX versions must use LAM.

  LAM supports only the files database type. LAM does not support NIS and NIS+. If you have AIX 5.2 and need to support NIS or NIX+, you can do either of the following:

  + Upgrade to AIX 5.3 or newer and use PAM
  + Require users to change their passwords on the Identity Vault.

  If you have AIX 5.3 or newer, /etc/security/login.cfg will include a configuration setting for auth\_type. The valid values for auth\_type are STD\_AUTH and PAM\_AUTH. Within the context of the bidirectional driver, if you choose STD\_AUTH, then you must use LAM to publish password changes. If you choose PAM\_AUTH, then you must use PAM to publish password changes.

  *NOTE:*The setting you choose for auth\_type may be influenced by reasons outside the scope of the bidirectional driver.
* If any of the systems you connect to Identity Manager are running AIX or HP-UX, you may need to replace the standard comm utility included with those operating systems. For more information, see [Replacing comm Utility for AIX and HP-UX](b3xccfu.html#bk2nxtn).
* Do you have NIS or NIS+ clients that you want to publish password changes from?
* What are the host names or IP addresses of all systems that will participate in your configuration?
* Will you use the default TCP port numbers?

  *Table 2-1* Default TCP Port Numbers

  | Purpose | TCP Port Number |
  | Driver shim connection to Metadirectory engine | 8090 |
  | Driver shim HTTP services for log viewing and access by remote NIS or NIS+ client PAM modules | 8091 |
  | Secure LDAP port | 636 |
  | Non-secure LDAP port | 389 |
