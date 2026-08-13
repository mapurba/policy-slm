# 1.2 Installing the SCIM Driver Files and Packages

To start with installing the driver, you must first download and install the driver files and packages. The following sections explain the procedures to install the driver files and packages.

## 1.2.1 Downloading the Driver Files

The SCIM Driver build files are available in the [Download Website](https://dl.netiq.com/index.jsp). You can perform a search and download them into your computer.

## 1.2.2 Installing the Driver Files

You can install the SCIM driver files as a root user or as a non root user in your system. The procedure to install the driver files is similar for any connected application.

You must ensure that you have the required SCIM drivers files such as,.zip,.rpm,and.jar etc, handy to install the SCIM driver in your system.

The following files are required to install the driver:

* .zip file: NIdm\_Driver\_SCIM.zip
* .rpm file: <netiq-DXMLscim.rpm>
* .jar file: <SCIMUtils.jar>

The following section explains the procedure to install the driver files.

1. Download and unzip the contents of the NIdM\_Driver\_SCIM.zip file to a temporary location on your computer.
2. To install the driver files as a root user, for IDM 4.7.4 and above:

   1. On the server where you want apply the driver jar file, log in as root.
   2. Navigate to the extracted NIdM\_Driver\_SCIM.zip directory and perform one of the following actions based on your platform:

      * Linux: Install the new netiq-DXMLscim.rpm in your driver installation directory by running the following command in a terminal window:

        + If you are installing the binary, run the command: rpm -Ivh (binaries-path)/netiq-DXMLscim.rpm
      * Windows: Copy the SCIMShim.jar file to the driver’s installation folder. For example, \NetIQ\IdentityManager\NDS(local installation) or \Novell\RemoteLoader\64bit (remote installation).
3. (Conditional) To update the driver files as a non-root user:

   1. Verify that the /rpmdirectory exists and contains the \_db.\* file.

      The\_db.\* file is created during a non-root installation of the Identity Manager engine. The absence of this file indicates that the Identity Manager is not installed properly. In such a case, reinstall the Identity Manager to correctly place the file in the mentioned directory.
   2. To set the root directory to the location of non-root Identity Vault, enter the following command in the command prompt:

      ROOTDIR=<non-root eDirectory location>

      This command sets the environmental variables to the directory to the location where the Identity Vault is installed as a non-root user.
   3. To install the driver files, enter the following command:

      For example, to install the SCIM driver rpm, use this command:

      rpm --dbpath $ROOTDIR/rpm -Ivh --relocate=/usr=$ROOTDIR/opt/novell/eDirectory --relocate=/etc=$ROOTDIR/etc --relocate=/opt/novell/eDirectory=$ROOTDIR/opt/novell/eDirectory --relocate=/opt/novell/dirxml=$ROOTDIR/opt/novell/dirxml --relocate=/var=$ROOTDIR/var --badreloc --nodeps --replacefiles /home/user/netiq-DXMLscim.rpm

      *NOTE:*In the above command /opt/novell/eDirectory is the location where non-root Identity Vault is installed, and /home/user/ is the home directory of the non-root user.
4. (Conditional) If the driver is running locally, start the Identity Vault and the driver instance.
5. (Conditional) If the driver is running with a Remote Loader instance, start the Remote Loader instance and the driver instance.

## 1.2.3 Extending the eDirectory (Identity Vault) Schema

You can upload new attributes through the Identity Vault to extend the SCIM schema.

1. Copy the following schema file to the system where Identity Manager is installed.

   For example:

   /root/schema/scim-schema.sch
2. Run the following ndssch command.

   ndssch [-h hostname[:port]] [-t tree\_name] [-d] admin\_FDN schemafile [schema\_description]

   For example:

   ndssch -h 10.71.131.123:524 -t SLES12SP3\_Quality\_131123\_TREE -d admin.sa.system /root/schema/scim-schema.sch scim-Group
3. The log file is created in the default location, i.e /root/schema.log for troubleshooting.

   *NOTE:*You must reload the iManager session for the schema changes to take effect.

## 1.2.4 Installing the Driver Packages in Designer

You must install the SCIM Base, SCIM Default and the SAP Cloud configuration packages mandatorily. The required packages and the versions to be installed are as follows:

* SCIM Base Package:

  + Package Name: NETQSCIMBASE
  + Version: 1.0.0
  + Build Date: 20201222
  + Build Number: 142319
* SCIM Default Package:

  + Package Name: NETQSCIMDCFG
  + Version: 1.0.0
  + Build Date: 20201113
  + Build Number: 132234
* SCIM JSON Package (Optional):

  + Package Name: NETQSCIMJSON
  + Version: 1.0.0
  + Build Date: 20200721
  + Build Number: 184051
* SCIM SAPCloud Configuration Package (Mandatory):

  + Package Name: NETQSCIMSCCG
  + Version: 1.0.0
  + Build Date: 20201020
  + Build Number: 175433
* SCIM Entitlements (Optional)

  + Package Name: NETQSCIMENT
  + Version: 1.0.0
  + Build Date: 20201221
  + Build Number: 171309

For more information to install the SCIM driver packages in the Designer, see [SCIM Driver Packages](../../scim_driver/data/t4czl7k7x983.html#t4czl7k7x983) in "[NetIQ SCIM Driver Implementation Guide](../../scim_driver/data/driver-for-scim.html#driver-for-scim)".
