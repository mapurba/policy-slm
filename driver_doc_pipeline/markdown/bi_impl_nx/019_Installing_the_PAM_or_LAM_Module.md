# 3.8 Installing the PAM or LAM Module

To synchronize passwords from the connected system, you must install the PAM or LAM module on the connected system.

To synchronize passwords from client systems in a NIS or NIS+ environment, you must install the PAM module on each client system.

To install the Linux and UNIX driver PAM or LAM module:

1. Log in to the target system as root, and run the installation script.

   For details, see [Running the Installation Script](b453l5q.html).
2. When prompted for the type of installation, enter the option for Install only PAM Module.

   For AIX systems, the option presented is Install only PAM and LAM Modules. AIX version 5.3 can use PAM, but previous AIX versions must use LAM.
3. Respond to additional prompts as appropriate.

If the driver shim is already installed, you can run the nxdrv-config command to reconfigure the PAM or LAM Module. For details about using the nxdrv-config command, see [Using the nxdrv-config Command](b4339kg.html).

*NOTE:*The Red Hat\* AS 2.1 and 3.0 PAM module pam\_unix.so does not work with the Linux and UNIX driver PAM module. Edit the PAM configuration file to use pam\_pwdb.so (located in the /lib/security directory) instead. For details about editing the PAM configuration file, see [PAM Configuration Details](b3yj5z9.html).
