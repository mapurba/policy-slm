# 3.7 Installing the Driver Shim on the Connected System

The driver shim and its files are installed into the /usr/local/nxdrv directory and other appropriate system locations. For details see [Files and Directories Modified by Installing the Driver Shim](b4ab5n6.html).

The driver uses an embedded Remote Loader. It is not necessary to install Java on the connected system.

1. Log in to the connected system as root, and run the installation script.

   For details, see [Running the Installation Script](b453l5q.html).
2. When prompted for the type of installation, enter the option for Install Driver Shim on Linux or UNIX system.
3. Respond to additional prompts as appropriate.

   1. Provide the Remote Loader and Driver object passwords that you entered when creating the driver in [Step 12](b1bybgrg.html#b1bxqts5).
   2. Specify the Metadirectory server host name or IP address and secure LDAP port number.

      These are used to secure the driver shim with SSL.
   3. Install the PAM or LAM module if you intend to publish passwords from the connected system. For details, see [Installing the PAM or LAM Module](b3xfnmq.html).
4. Start the driver shim.

   To start the driver shim, run the appropriate command for your operating system as shown in [Table 7-1, Starting the Driver Shim](b432wif.html#b47mkvj).
