# 2.3 Installing the SCIM Driver Files

You can install the SCIM driver files as a root user or as a non-root user in your system. The procedure to install the driver files is similar for any connected application.

You must ensure that you have the required SCIM driver files such as,.zip,.rpm, and.jar etc., from the required driver build available in [Micro Focus Download](https://dl.netiq.com/index.jsp) site to install the SCIM driver in your system.

For example:

* .zip file: SCIMDriver.zip
* .rpm file: <netiq-DXMLscim.rpm>
* .jar file: <SCIMUtils.jar>

This section explains the common procedure to install the driver files.

1. Download and unzip the contents of the SCIMDriver.zip file to a temporary location on your computer.
2. Install the driver files (for IDM 4.7.4 and above) based on your user role.

   To install as a:

   * root user, see [Installing Driver Files as a Root User](inst_scim_drv_files.html#t4dacf8kqbrk).
   * non-root user, see [Installing Driver Files as a Non-Root User](inst_scim_drv_files.html#t4dacftb44io).

   #### Installing Driver Files as a Root User

   1. Login as a root user on the server where you want apply the driver jar file.
   2. Navigate to the extracted SCIMDriver.zip directory and perform one of the following actions based on your platform:

      * Linux: Install the new netiq-DXMLscim.rpm in your driver installation directory by running one of the following command in a terminal window:

        + If you are installing the binary, run the command: rpm -Ivh (binaries-path)/netiq-DXMLscim.rpm
      * Windows: Copy the SCIMShim.jar file to the driver’s installation folder. For example, \NetIQ\IdentityManager\NDS(local installation) or \Novell\RemoteLoader\64bit (remote installation).

   #### Installing Driver Files as a Non-Root User

   1. Verify that the /rpmdirectory exists and contains the \_db.000 file.
   2. The\_db.000 file is created during a non-root installation of the Identity Manager engine. The absence of this file indicates that the Identity Manager is not installed properly. In such a case, reinstall the Identity Manager to correctly place the file in the mentioned directory.
   3. To set the root directory to the location of non-root in Identity Manager, enter the following command in the command prompt:

      ROOTDIR=<non-root eDirectory location>

      This will set the environmental variables to the directory where Identity Manager is installed as a non-root user.
   4. For example, to install the SCIM driver rpm, use this command:

      rpm --dbpath $ROOTDIR/rpm -Ivh --relocate=/usr=$ROOTDIR/opt/novell/eDirectory --relocate=/etc=$ROOTDIR/etc --relocate=/opt/novell/eDirectory=$ROOTDIR/opt/novell/eDirectory --relocate=/opt/novell/dirxml=$ROOTDIR/opt/novell/dirxml --relocate=/var=$ROOTDIR/var --badreloc --nodeps --replacefiles /home/user/netiq-DXMLscim.rpm

      *NOTE:*In the above command /opt/novell/eDirectory is the location where non-root Identity Manager is installed, and /home/user/ is the home directory of the non-root user.
3. (Conditional) If the driver is running locally, start the Identity Manager and the driver instance.
4. (Conditional) If the driver is running with a Remote Loader instance, start the Remote Loader instance and the driver instance.
