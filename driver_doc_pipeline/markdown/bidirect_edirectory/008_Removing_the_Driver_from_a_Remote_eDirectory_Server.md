# 3.3 Removing the Driver from a Remote eDirectory Server

The driver includes a new change-log utility, clutil. This utility allows you to remove change-log entries on a remote eDirectory server for bidirectional driver shims connected to it. Removing change-log entries removes the selected driver entry from the change-log in the remote eDirectory and removes the cache files.

On Linux, the Identity Manager install program installs this utility as a part of the novell-DXMLChlgx.rpm file. To configure it on an eDirectory server, locate the clutil script in the /opt/novell/eDirectory/bin location.

On Windows, this utility is provided with other deliverables for the Dirxml-ChangeLog file on the Identity Manager media. Create a lib directory in the location where eDirectory is installed (for example: C:\Novell\NDS\), and copy the clutil.jar file into it.

To run the utility, do the following:

1. Set PATH to a valid location where java is installed.

   For example:

   * *Linux:*
     /opt/novell/eDirectory/lib64/nds-modules/embox/jre/bin
   * *Windows:*
     C:\novell\NDS\embox\jre\bin
2. *On Linux:*
   Provide the execute permission to the clutil file if not already provided, and run the clutil command.

   *On Windows:*
   Browse to the eDirectory installation folder (For example, C:\Novell\NDS\) and run the clutil.bat file.

   Running this utility displays the list of change-log driver entries configured for the eDirectory server. This list shows a mapping of the driver names to their respective driver entries.
3. Stop the driver shim, then select the serial number corresponding to the change-log entry of the driver that you want to remove.
4. When prompted for credentials, enter the administrator user credentials in LDAP format and the password. This is the same administrator user account used during driver configuration.

   This deletes the driver entry, TAO files, and updates the configuration.

   *IMPORTANT:*If the remote eDirectory server is installed on Windows, you must delete the TAO file manually after shutting down eDirectory. This is because ndsd process locks the TAO file and clutil utility cannot delete it. However, when the TAO file is deleted, you can no longer use the corresponding driver because the driver fails to establish a successful connection with the remote eDirectory.
