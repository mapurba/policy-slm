# 1.3 Creating SCIM Driver Object for Connecting to SAP Cloud

To begin with the configuration, you need to set up the SCIM driver object in the Designer, and configure certain parameters to connect to SAP Cloud.

The procedure to set up the SCIM driver in Designer is similar for any connected application. The generic steps to set up a driver object in Designer is shown from step 1 to step 20. If you are familiar with the generic driver object set up, you can choose to skip [Step 17](t4d8epejpvqc.html#config_conn_params) to continue with the configuration parameters specific to SAP Cloud.

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Select the required package as shown in [Installing the Driver Packages in Designer](t4cfey7g8704.html#install_driv_packages) to download and click OK. The Designer is updated with the selected packages.
4. In Designer > Outline view, open your project.
5. Right click project > New > Identity Vault, or drag and drop Identity Vault from the Palette to Modeler window.
6. In the Add Server Association screen, select the following field values and click OK.

   * Server DN
   * Identity Manager Version
   * Identity Manager Edition

   The Identity Vault Credentials window appears.
7. In Identity Vault Credentials window, enter:

   | Field | Description |
   | Host | The identity vault hosting machine's IP address |
   | Username | The name of the user, for example, Admin, if the user is an administrator. |
   | Password | The password of the user to login to the identity vault |
8. Select Save Password, if you want to save your password for easy logins in the future.
9. Click OK.

   The Identity Vault with the Driver Set appears in the Modeler window.
10. In the right pane, drag and drop the SCIM driver icon from Palette > Tool tab to the Modeler window.
11. In the Driver Configuration Wizard, select SCIM Base (Contains the base functionality for a driver. You must install a driver base configuration package first).

    *NOTE:*You can only select one base package.
12. Click Next.
13. In the Select Mandatory Features page, select the SCIM Default Package, and click Next.
14. In the Select Optional Features page, select the SCIM SAPCloud Configuration Package, and if required select SCIM JSON Package, and click Next.

    *IMPORTANT:*Though the SCIM SAPCloud Configuration Package appears in the Select Optional Features page, to configure the SCIM driver for SAP Cloud you must select this package mandatorily.
15. Verify if the required Important Note items are met, and click Next.
16. On the Driver Information page, specify a name for the driver, then click Next. The Connection Parameters page appears.
17. Select Basic in the Authentication Method field.

    *IMPORTANT:*The SCIM driver for SAP Cloud is currently certified with Basic authentication only.

    ![](../graphics/scim_manual_token_a.png)
18. Enter the following fields as shown in the table below:

    | Field | Sample Values |
    | Authentication Method | Select Basic. |
    | User Name: Specify the User ID obtained from SAP Cloud. The procedure to obtain the User ID is explained in [Prerequisites](t4e5teg7ok48.html). | <be1a0804-7e91-46a1-be48-8a728fb60ef8> |
    | Password: Specify the password in the Enter Password and Re-enter Password fields that you have set in SAP Cloud. The procedure to set the password is explained in [Prerequisites](t4e5teg7ok48.html). | <user defined password set in SAP Cloud> |
    | Application Login URL: The login URL of SAP Cloud. | <https://tenant\_name.accounts.ondemand.com/admin/> |
    | Header Fields: Click the ![](../graphics/icon_plus_green_n.png) icon to create the header fields. Enter the required header fields and supported values for the selected authentication method. | * Name: Content-Type * Value: application/scim+json |
    | Application Truststore File: The path and the name of the keystore file that contains the trusted certificates for the remote server to achieve SSL handshake. The trusted DigiCert CA certificate must be imported from the SAP Cloud portal.  Import the keystore file by running the following command: keytool -import -file <name\_of\_cert\_file> -trustcacerts -noprompt - keystore <filename> -storepass <password> | </root/scim\_configuration/trustSapCloud/SapCloud> |
    | Mutual Authentication:Enable and specify this field, if the authentication is supported by the connected application. You must ensure to have both the server certificates stored in Identity Manager and the connected application. | Mutual Authentication is not mandatory for SAP Cloud. |
    | Proxy Authentication: Defaults to Hide. Select Show if you want to set proxy authentication parameters. Specify the host address and the host post when a proxy host and port are used. | * Proxy host name and port: <192.168.0.0:port>. Choose an unused port number on the proxy server. * Username: <user name for proxy authentication> * Enter Password: <password for proxy authentication> * Re-enter Password: <password for proxy authentication> |
    | HTTPS Connection Timeout: Specify the HTTP connection time out value. | The timeout value must be greater than 0.  *NOTE:*The driver waits for the time specified (in minutes) and terminates the HTTPS connection displaying the error codes that are configured in the Subscriber Options > HTTPS error codes for retry field. |
    | SCIM 2.0 URL: Enter the URL for the SCIM Application. SCIM Resources like User, Group etc. will be appended to this URL. | <https://<tenant ID>.accounts.ondemand.com/service/scim/> |
19. In the Install SCIM Base page, specify the Subscriber Options and Publisher Options, and click Next.

    | Field | Description and Sample Values |
    | Subscriber Options | HTTPS error codes for retry: Specify the HTTPS errors that must return a retry status. Error codes must be a list of integers separated by spaces. For example: <307 408 503 504>  *NOTE:*The operation will be retried if these errors are encountered. |
    | Publisher Options | * Enable Publisher Channel: Select Yes to enable the Publisher channel. * Polling interval in minutes: The time interval to poll resources from SAP Cloud. Specify the polling interval in minutes.  For example: <10> * Heartbeat interval in minutes: This option is used to configure the driver shim to send a periodic status message on the Publisher channel. By default, this is set to 10 minutes.  *IMPORTANT:*Polling Resource Options: This field does not appear when you are setting up the driver for the first time. These fields appear after configuring the driver in Designer. Once the driver is configured, double click the connector line in the modeler window and navigate to Driver Configuration > Publisher Options tab.  * Select the Configured Resources option to poll on all resources that are configured as part of the schema settings. * Select the Custom Resources option and click ![](../graphics/icon_plus_green_n.png) to configure customized polling Resource ID and Resource URL.  + For User:  - Resource ID: Specify the schema’s Uniform Resource Name (URN) of the user. Example, urn:ietf:params:scim:schemas:core:2.0:User     - Resource URL: Specify the schema’s Uniform Resource Locator (URL) of the user. Example, https://<tenant ID>.accounts.ondemand.com/service/scim/Users?startIndex=1&count=100  *NOTE:*In the above URL’s, the startIndex refers to the resource from where the poll must start and count refers to the number of resources from the startIndex for polling.   + For Group:  - Resource ID: Specify the schema’s Uniform Resource Name (URN) of the group. Example, urn:ietf:params:scim:schemas:core:2.0:Group     - Resource URL: Specify the schema’s Uniform Resource Locator (URL) of the group. Example, https://<tenant ID>.accounts.ondemand.com/service/scim/Groups?startIndex=1&count=100 |
20. In the Schema Settings page, enter the values as shown in the following table:

    ![](../graphics/scim_adv_modif_setting_a.png)

    *Table 1-1* Schema Settings

    | Field | Description with Sample Values |
    | Refresh Schema on Driver Startup | Specify Yes, to refresh the schema.  *IMPORTANT:*You must select Yes only for the first time to load the application schema or if the application schema has changed. It is recommended to change it to No after you load the application schema. |
    | Schema Options | Select SCIM 2.0.  * SCIM 2.0: SCIM 2.0 Schema for User and Group, as defined in [RFC7643](https://tools.ietf.org/html/rfc7643). |
    | Resource Type | Specify the Resource ID and the Resource EndPoint for resources like Users, Groups, Roles, Entitlements etc. in Uniform Resource Name (URN) Format.  * Resource ID: The schema’s Uniform Resource Name (URN) of the user. For example, urn:ietf:params:scim:schemas:core:2.0:Users * Resource Endpoint: Specify the resource endpoint of the Resource ID. For example, Users. * Modify Method Operation: This option is used to make partial updates to the resources in SAP Cloud. Select PUT.  Similarly for Groups:  * Resource ID: Specify the schema’s Uniform Resource Name (URN) of the group. For example, urn:ietf:params:scim:schemas:core:2.0:Group * Resource Endpoint: Groups * Modify Method Operation: Select PUT. |

    *Table 1-2* Modifier Settings

    | Field | Description with Sample Values |
    | Custom Java Class | Not Applicable for SAP Cloud. |
    | Document Handling | Not Applicable for SAP Cloud. |
21. Review the summary of tasks that will be completed to create the driver, then click Finish. The configured driver appears in the Designer screen.
