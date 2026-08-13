# C.4 PAM Configuration Details

The PAM module can publish password information on the system running the driver shim or from a remote system such as a NIS or NIS+ client. The only task of the driver PAM module is to obtain the password during normal password change operations that use PAM-enabled tools, such as the passwd command.

You can install and optionally configure the PAM module at any time using the installation program. For details, see [Installing the PAM or LAM Module](b3xfnmq.html).

After it is installed, you can configure the PAM module with the nxdrv-config command. For details, see [Using the nxdrv-config Command](b4339kg.html).

The installation script installs the PAM module as appropriate for the server operating system as shown in the following table:

*Table C-3* PAM Modules

| Operating System | PAM Module |
| AIX | /usr/lib/security/pam\_nxdrv |
| HP-UX | /usr/lib/security/libpam\_nxdrv.1 |
| Linux | /lib/security/pam\_nxdrv.so |
| Solaris | /usr/lib/security/pam\_nxdrv.so.1 |

If you respond to the prompt to configure the PAM module, the installation script places an entry for the PAM module in the appropriate PAM configuration file for the password facility. The nxdrv-config command also does this.

You can edit your PAM configuration file manually. The PAM module requires a command line option as shown in [Table C-4](b3yj5z9.html#b4igolf). For the location and syntax of your PAM configuration file, see your system’s PAM documentation. If you choose to edit your own PAM configuration files, you must place the PAM module entry below the module that obtains the new password during a password change.

*Table C-4* Linux and UNIX Driver PAM Module Command Line Options

| Option | Description |
| debug=\* | Logs PAM module activity to the /usr/local/nxdrv/logs/pam\_nxdrv.log file. |
| host=hostName | Required for SOAP. Specifies the host name or IP address of the driver shim system. |
| mechanism=api | The PAM module uses the API to send password change information to the driver shim. This method is used when the PAM module is running on the same system as the driver shim. |
| mechanism=soap | The PAM module uses Simple Object Access Protocol (SOAP) to send password change information to the driver shim. This method is used when the PAM module is running on a different system from the driver shim, such as with NIS or NIS+ clients. |
| port=portNumber | Required for SOAP. Specifies the TCP port number of the driver shim system. The default port is 8091. |
| LC\_ALL=locale | Specifies the standard character set (locale) in use by the connected system. This ensures accurate text data conversion between the connected system and Identity Manager, which uses the UTF-8 character set. For example, the option LC\_ALL=iso8559-1 would enable the PAM module to convert passwords and user IDs in the iso8559-1 (Latin-1) character set to UTF-8. |

The Linux and UNIX driver PAM module is contained in the pam-password part of the PAM stack below the other PAM modules on the system. When the other PAM modules participate in a dialog with a user who is changing the password, the driver PAM module uses pam\_get\_item to get the new password from the PAM framework.

When the Linux and UNIX driver PAM module obtains a new password on the system running the driver shim, it writes the new password to the change log so it can be published into the Identity Vault.

When the PAM module is used from a host other than the one where the driver shim is running (such as NIS or NIS+ clients), it uses a secure TCP/IP channel to communicate with the driver shim. If the password change event cannot be sent to the driver shim, a message is written to the system log.
