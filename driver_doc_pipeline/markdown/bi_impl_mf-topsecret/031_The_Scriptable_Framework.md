# 6.1 The Scriptable Framework

The driver provides a comprehensive scriptable framework that you can use to add to the built-in support for the security system, and to add support for other applications and security system fields that have been customized for a particular installation.

The driver scriptable framework includes components that simplify the job of extending the driver to support new applications and fields.

* Embedded Remote Loader

  + Full SSL support, and an installer to easily configure the certificates
  + Web access to debugging information from the embedded Remote Loader
* Encrypted change log that stores changes from the application to the Identity Vault if there is a communication problem
* Loopback detection system to prevent subscribed events from being published back to the Identity Vault
* z/OS name/token callable services helper programs that provide for securely passing large variables to and from the REXX execs
* Easily extendable connected system schema file to support any application
* Include/exclude file for simplified testing and deployment by the platform administrator
* Event support, both for applications that have exits or callouts, and for applications that must be polled for changes

The names of objects and attributes in the REXX execs are the names specified in the connected system schema file.

The following tables describe the major REXX execs.

*Table 6-1* Identity Vault Command Processing Execs

| REXX Exec | Identity Vault Event |
| IDMADDG | Add Group |
| IDMADDU | Add User |
| IDMCONNU | Add User to Group |
| IDMDELG | Delete Group |
| IDMDELU | Delete User |
| IDMDSABL | Disable User |
| IDMENABL | Enable User |
| IDMMODG | Modify Group |
| IDMMODPW | Password Change |
| IDMMODU | Modify User |
| IDMQUERY | Query |
| IDMRENG | Rename Group |
| IDMRENU | Rename User |
| IDMRMVU | Remove User from Group |

*Table 6-2* Other Execs

| REXX Exec | Purpose |
| IDMSUB | Calls the appropriate command processing exec based on the type of event and object. This is executed for every Subscriber event. |
| IDMPOLL | Not used for CA Top Secret. You can use this exec as needed to support your own applications if they do not generate events when changes are made. |
| IDMHRTBT | Heartbeat exec. |
| IDMGLBLS | Holds configurable options that all REXX execs can use during event processing. |
| IDMSTATS | Sends a status document to report the health of the application. |
| IDMTSOEX | Executes a TSO command and returns the command return code and command output. |
| SETPWDS | Sets the Remote Loader and Driver object passwords, which are used to authenticate and authorize the connection between the driver shim started task and the Metadirectory system. |
| SETCERT | Retrieves the certificate authority for the Metadirectory engine that uses SSL to communicate with the driver shim started task. |
