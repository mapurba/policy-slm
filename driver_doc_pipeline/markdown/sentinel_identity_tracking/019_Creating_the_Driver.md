# 6.2 Creating the Driver

To create and maintain Identity data, the driver must have administrator privileges. NetIQ recommends that you create a Sentinel user account with administrator privileges specifically for use with the driver. This allows you to use audit events to track the changes made by the driver in the Sentinel system.

You need to configure the driver with the name and password of a Sentinel user account so that the driver can authenticate to the Sentinel server and make changes to the Sentinel database.

Before you create the driver, import the latest packages to Designer. This driver requires the following packages:

* NIQSENRESTB\_<version>.jar
* NIQSENIDTRK\_<version>.jar

To import the packages:

1. Launch Designer.
2. Create a new project for the driver.

   For more information, see "[Creating a Project](https://www.netiq.com/documentation/idm401/designer_admin/?page=/documentation/idm401/designer_admin/data/front.html)"in the [Designer Administration Guide](https://www.netiq.com/documentation/idm401/designer_admin/?page=/documentation/idm401/designer_admin/data/front.html).
3. Select Help > Check for Package Updates to install the Sentinel driver packages.
4. In the Outline view, right-click Package Catalog and click Import Packages.
5. If the driver packages are available in the packages list, select the packages and click OK.

   or

   Click Browse, then browse to select the packages on the file system.

   For more information, see "[Importing Packages](https://www.netiq.com/documentation/idm401/designer_admin/?page=/documentation/idm401/designer_admin/data/importpackage.html)"in the [Designer Administration Guide](https://www.netiq.com/documentation/idm401/designer_admin/?page=/documentation/idm401/designer_admin/data/importproject.html).
6. Go to Enterprise > Sentinel.
7. Verify whether Sentinel REST API BASE and Sentinel Identity Tracking packages are available.

To create the driver:

1. Drag the Sentinel application icon from the Designer palette > Enterprise > Sentinel folder to the Designer modeler.
2. From the Available Packages list, select Sentinel REST API Base and click Next.
3. From the Select Mandatory Features list, select Sentinel Identity Tracking and click Next.
4. Specify the following information, and then click Next:

   * *Sentinel account name:*
     Specify a name for the Sentinel account which the driver uses to perform operations in Sentinel.
   * *Sentinel account password:*
     Specify a password for the [Sentinel account](creating-the-driver.html#sentinelaccountname1).
   * *Sentinel server:*
     Specify the IP address of the Sentinel server. The Sentinel driver communicates with this server.
   * *Sentinel port:*
     Specify the port for the Sentinel server. The default port is 8443.
   * *Sentinel TLS/SSL certificate:*
     The driver uses Sentinel TLS/SSL to communicate with the Sentinel server.

     You must either obtain the Sentinel server [self-signed public key certificate](installing-on-windows.html#self_signedcerti) or the [trusted root certificate of the certificate authority](installing-on-windows.html#trusted_rootcert) used to sign the Sentinel server public key certificate.
5. If you want to connect the driver to a Remote Loader, select yes and specify the Remote Loader connection data.
6. Specify a name for the driver and click Next.
7. In the following screen, perform the following steps and click Next:

   *Matching Attributes:*
   This option allows you to find a matching Sentinel Identity object attribute values with the corresponding Identity Vault user object values. The default Identity Vault attributes are Full Name and Internet EMail Address. The standard mapping of these two Identity Vault attributes to Sentinel Identity attributes are name and email, respectively.

   You can change the default attributes to any attribute or attributes that your organization finds useful. To be useful for matching, each Identity Vault object must have values for the attributes you choose.

   *NOTE:*The values that you specify in Matching Attributes are considered when the driver’s matching policies do not find a match by DN and User GUID value. For more information, see [Understanding the Configuration](understanding-the-configuration.html).

   *Tenant ID:*
   If you are configuring the driver for a managed security customer or if the driver is synchronized to a Sentinel server that contains data for multiple managed security customers, select yes and specify the numeric Tenant Id of the managed security customer.

   *HINT:*The Tenant ID is available in the CUST table in the Sentinel database.
8. Click Next. Review the configuration settings and click Finish.
