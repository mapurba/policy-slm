# D.1 Using the usdrv-config Command (Linux/UNIX only)

You can use /usr/sbin/usdrv-config to change the driver shim configuration. When you run this command, you are prompted for the function to perform.

```
> usdrv-config
Which configuration do you want to perform?
1) Set the Remote Loader and Driver object passwords
2) Configure the driver for Secure Sockets Layer (SSL)
Select one configuration option [q/?]:
```

Enter the number of the function you want to configure, then respond to the prompts.

## D.1.1 Setting the Remote Loader and Driver Object Passwords

The usdrv-config command prompts you to enter and confirm the Remote Loader password and the Driver object password.

```
Enter Remote Loader password:
Confirm Remote Loader password:
Enter Driver object password:
Confirm Driver object password:
```

The Remote Loader password is used by the Metadirectory engine to authenticate itself to the driver shim (embedded Remote Loader). The Driver object password is used by the driver shim to authenticate itself to the Metadirectory engine.

The Remote Loader and Driver object passwords set by usdrv-config are stored on the connected system. The Remote Loader and Driver object passwords set for the driver using iManager are stored in the Identity Vault. Each password on the connected system must exactly match its counterpart in the Identity vault.

To change the passwords after driver installation:

1. In iManager, navigate to the Driver Overview for the driver.
2. Click the driver icon.
3. Specify the Driver object password.
4. Specify the Remote Loader password.

   The Remote Loader password is below the Authentication heading.
5. Click Apply.
6. Restart the driver.

## D.1.2 Configuring the Driver for SSL

The usdrv-config command prompts you to enter the LDAP server host address and port, then displays the Certificate Authority for that server and asks you if you accept it.

```
You are about to connect to the eDirectory LDAP server to retrieve
the eDirectory Tree Trusted Root public certificate.

Enter the LDAP Server Host Address [localhost]: sr.digitalairlines.com
Enter the LDAP Server Port [636]:

Certificate Authority:
   Subject:       ou=Organizational CA,o=TREENAME
   Not Before:    20070321144845Z
   Not After:     20170321144845Z
Do you accept the Certificate Authority? (Y/N) y
```

Enter the host name or IP address and TCP port number of an LDAP server for your Identity Vault. The LDAP server must be configured for SSL, and it must be listening on the SSL port. The default SSL port is 636.

The driver shim connects to the specified server and displays information about the Certificate Authority. If you accept the Certificate Authority, the driver shim saves it to the local file system.

If you do not have LDAP configured for SSL, you can use a manual process to configure the driver for SSL. For details, see Section A.2.3, "Driver Certificate Setup Failure."
