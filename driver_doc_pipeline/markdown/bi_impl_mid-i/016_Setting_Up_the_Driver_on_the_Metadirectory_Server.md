# 3.6 Setting Up the Driver on the Metadirectory Server

1. In iManager, select Identity Manager Administration.
2. Under Administration, select Identity Manager Overview.
3. Select Driver Sets and choose your driver set name below.
4. Select Drivers > Add driver, then click Next.
5. Select Import a driver configuration from the client (.XML file).

   1. Under Show, select <all configurations>.
   2. Under Configurations, browse to select i50s-IDM3\_5\_0-V3.xml.
   3. Click Next.
6. Type in a name for the driver, select an installation method, then click Next.

   *NOTE:*For details about choosing the appropriate installation method, see [Choosing between the Basic and the Advanced Installation Methods](b40k7ry.html).
7. Specify the configuration settings as described in the following table, then click Next.

   | Configuration Setting | Action | Installation Method |
   | Data Flow | Select Bidirectional, Application to Identity Vault, or Identity Vault to Application. For details, see [Data Flow](b3xub84.html#b3xusu3). | Advanced |
   | Polling Interval | Specify the number of seconds the Publisher shim waits after running the polling CL program and sending events from the change log to the Metadirectory engine. For details, see [Polling Interval](b3xub84.html#b3xv8y7). | Advanced |
   | Base Container | Specify the Identity Vault container where synchronized users and groups reside.  You can specify separate containers for users and groups by updating the driver properties later. For details, see [User Base Container](b3xub84.html#b455w4s) and [Group Base Container](b3xub84.html#b3xvcn0). | Basic and Advanced |
   | Enable Entitlements | Select Yes or No. For details, see [Enable Entitlements](b3xub84.html#b3xvdmx). | Advanced |
   | Synchronize Group Membership | Select Yes or No. For details, see [Synchronize Group Membership](b3xub84.html#b3xvi0q). | Advanced |
   | Remote Host Name and Port | Specify the host name or IP address and TCP port number of the driver shim on your IBM i connected system. The default port number is 8090. | Basic and Advanced |
   | Use SSL | Select Yes or No. For details, see [Use SSL](b3xub84.html#b3xvlwp). | Advanced |
   | Driver Object Password Remote Loader Password | Specify secure passwords and remember them. You must enter them in [Step 7.h](b3xehpq.html#b3xejil) when you install the driver shim on the connected system. For details, see [Driver Object Password](b3xub84.html#b3xvqhp) and [Remote Loader Password](b3xub84.html#b3xvr2u). | Basic and Advanced |
8. Click Define Security Equivalences and make the driver equivalent to ADMIN or another high-rights user so the driver can obtain information from the Identity Vault and create users and groups there.

   *NOTE:*For details about the rights required by the user, see [Table 2-2, Base Container Rights Required by the Driver Security-Equivalent User](b484ok2.html#b4exk92).
9. (Optional) Click Exclude Administrative Roles to exclude users with administrative rights from being processed by the driver.
10. Click Finish to complete the driver installation.
11. Start the driver.

    Click the upper right corner of the driver icon, then click Start driver.
