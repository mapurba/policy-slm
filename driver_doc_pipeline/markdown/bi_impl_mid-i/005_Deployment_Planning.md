# 2.1 Deployment Planning

* Review [Section 3.0, Installing the IBM i Driver](b3r8si5.html) and [Section 6.0, Configuring the IBM i Driver](b3r8t50.html).
* Consider how you will respond to the installation prompts and other installation decisions.
* Is this a new installation, or are you replacing a Fan-Out driver Platform Services installation? For details about upgrading from the Fan-Out driver, see [Section 4.0, Upgrading from the Fan-Out Driver](b3r9hzv.html).
* How do you plan to prototype, test, and roll out your deployment?
* Do you plan to use the include/exclude file on the connected system to limit your initial deployment to a small number of users and groups?
* What are the host names or IP addresses of all systems that will participate in your configuration?
* Will you use the default TCP port numbers?

  *Table 2-1* Default TCP Port Numbers

  | Purpose | TCP Port Number |
  | Driver shim connection to Metadirectory engine | 8090 |
  | Secure LDAP port | 636 |
  | Non-secure LDAP port | 389 |
