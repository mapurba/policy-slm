# 5.3 Setting the Remote Loader and Driver Object Passwords

The Remote Loader password is used by the Metadirectory engine to authenticate itself to the driver shim (embedded Remote Loader). The Driver object password is used by the driver shim to authenticate itself to the Metadirectory engine.

These passwords are set during installation. You can set them at any time later using the procedures in the following sections. The corresponding passwords you set on the connected system and in the Identity vault must be identical.

* [Connected System](b4aazqy.html#b6brtke)
* [Identity Vault](b4aazqy.html#b6brtt2)

## 5.3.1 Connected System

The Remote Loader and Driver object passwords are stored on the connected system under /opt/novell/racfdrv/keys in encrypted files dpwdlf40 (Driver object password) and lpwdlf40 (Remote Loader password).

To set the passwords on the connected system:

1. Run the REXX exec in the REXX exec library member SETPWDS and respond to the prompts.
2. Restart the driver shim started task.

## 5.3.2 Identity Vault

The Remote Loader and Driver object passwords are set for the driver through iManager and are stored in the Identity Vault. Each password on the connected system must exactly match its counterpart in the Identity vault.

To change the passwords in the Identity Vault after driver installation:

1. In iManager, navigate to the Driver Overview for the driver.
2. Click the driver icon.
3. Specify the Driver object password.
4. Specify the Remote Loader password.

   The Remote Loader password follows the Authentication heading.
5. Click Apply.
6. Restart the driver.
