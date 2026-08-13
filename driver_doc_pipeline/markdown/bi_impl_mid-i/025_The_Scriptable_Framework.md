# 5.1 The Scriptable Framework

The IBM i driver provides a comprehensive scriptable framework that you can use to add to the built-in support for the IBM i security system, and to add support for other applications.

The IBM i driver uses Control Language (CL) programs to implement driver functions. The scriptable framework includes components that simplify the job of extending the driver to support new applications.

* Embedded Remote Loader

  + Full SSL support, and an installer to easily configure the certificates
  + Web access to debugging information from the embedded Remote Loader
* Encrypted change log that stores changes from the application to the Identity Vault if there is a communication problem
* Loopback detection system to prevent subscribed events from being published back to the Identity Vault
* Helper programs for securely passing variables to and from the CL programs through a user space
* Easily extendable connected system schema file to support any application
* Include/exclude file for simplified testing and deployment by the platform administrator
* Event support, both for applications that have exits or callouts, and for applications that must be polled for changes

The names of objects and attributes in the CL programs are the names specified in the connected system schema file.

The following tables describe the major CL programs.

*Table 5-1* Identity Vault Command Processing CL Programs

| CL Program | Identity Vault Event |
| ADDGROUP | Add Group |
| ADDGRPMEM | Add Group Member |
| ADDUSER | Add User |
| DELGROUP | Delete Group |
| DELUSER | Delete User |
| MODGROUP | Modify Group |
| MODPWD | Password Change |
| MODUSER | Modify User |
| RMVGRPMEM | Remove Group Member |
| QUERY | Query |
| RENGROUP | Rename Group |
| RENUSER | Rename User |

*Table 5-2* Other CL Programs

| CL Program | Purpose |
| ASSIGNVAR | Obtains a value from the Identity Vault or uses a default |
| ERROR | Trace message helper |
| EXEC | Executes an i5/OS command |
| FAILED | Trace message helper |
| POLL | Called to detect changes in user applications |
| STATUS | Trace message helper |
| STOREPWD | Stores a password |
| SUBSCRIBER | Calls the appropriate CL program based on the type of event and object |
| TRACE | Trace message helper |
| TRACEMSGS | Trace message helper |
