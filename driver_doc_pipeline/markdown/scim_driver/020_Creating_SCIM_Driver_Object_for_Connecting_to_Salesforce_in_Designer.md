# 5.2 Creating SCIM Driver Object for Connecting to Salesforce in Designer

To begin with the configuration, you need to set up the SCIM driver object in the designer, and configure the SCIM driver with the specific parameters to connect to Salesforce application.

The generic steps to set up a driver object and the configuration parameters is shown below. If you already have the driver object setup in designer, you can skip to [Step 20](create_scim_driv_obj_slsfrce.html#config_subs_opt) to proceed with Salesforce specific configuration.

1. Open Designer.
2. In the toolbar, click Help > Check for Package Updates.
3. Select the required versions of the SCIM Base and SCIM Default packages as mentioned below:

   * SCIM Base Package:

     + Package Name: NETQSCIMBASE
     + Version: 1.0.0
     + Build Date: 20201117
     + Build Number: 124957
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
   * SCIM Entitlements (Mandatory)

     + Package Name: NETQSCIMENT
     + Version: 1.0.0
     + Build Date: 20201113
     + Build Number: 141225
4. Click OK to update the packages.
5. In the Outline view, right-click the Package Catalog.
6. Click Import Package and scroll to find the SCIM Salesforce Configuration package.

   * SCIM Salesforce Configuration Package (Mandatory):

     + Package Name: NETQSCIMSFCG
     + Version: 1.0.0
     + Build Date: 20200721
     + Build Number: 184139
7. Click OK to import the selected packages, then click OK in the successfully imported packages message. The designer is now updated with the selected package.
8. In Designer > Outline view, open your project.
9. Right click project > New > Identity Vault, or drag and drop Identity Vault from the Palette to Modeler window.
10. In the Add Server Association screen, select the following field values and click OK.

    * Server DN
    * Identity Manager Version
    * Identity Manager Edition

    The Identity Vault Credentials window appears.
11. In Identity Vault Credentials window, enter:

    | Field | Description |
    | Host | The IP address of the Identity Vault's host machine. |
    | Username | The name of the user. |
    | Password | The password of the user to login to the identity vault. |
12. Select Save Password, if you want to save your password for easy logins in the future.
13. Click OK.

    The Identity Vault with the Driver Set appears in the Modeler window.
14. In the right pane, drag and drop the SCIM driver icon from the Tools tab in the Modeler window, to the Identity Vault.
15. In the Driver Configuration Wizard, select SCIM Base Package (Contains the base functionality for a driver. You must install a driver base configuration package first), and click Next.

    *NOTE:*You can only select one base package.
16. In the Select Mandatory Features page, select the SCIM Default Package, and click Next.
17. (Optional) In the Select Optional Features page, select SCIM JSON Package, and click Next.
18. Verify if the required Important Note items are met, and click Next.
19. On the Driver Information page, specify a name for the driver, then click Next.
20. Select OAuth 2.0 in the Authentication Method field, as the SCIM driver should be configured to connect to Salesforce with OAuth 2.0 as the authentication method.
21. In the OAuth2.0 Authorization Token field, select the option as required. The available options are:

    * Bearer: To configure SCIM Driver with new bearer token, see [Configuring SCIM Driver with Bearer Token](create_scim_driv_obj_slsfrce.html#t4d7ifo4gwj6).
    * JWT: To configure SCIM Driver using JWT, see [Configuring SCIM Driver with JWT](create_scim_driv_obj_slsfrce.html#t4d7ig0aereu)
    * Manual: To configure SCIM Driver using an available bearer token, see [Configuring SCIM Driver Manually with an Available Token](create_scim_driv_obj_slsfrce.html#t4d7ig4fwtnb)

    *NOTE:*Configuring a JWT is recommended as it is more secured with a digital server certificate.

    #### Configuring SCIM Driver with Bearer Token

    Bearer is an access token issued by servers (Salesforce) to achieve multi-server authentication.

    ![](../graphics/scim_bearer_a.png)

    If you select Bearer, the following fields appear. Enter the values as shown in the following table.

    *IMPORTANT:*For any operation performed on the Salesforce application using OAuth 2.0, an access token is sent for authorization of the user from Salesforce. The access token expires post the session idle time set for Salesforce, or in case of a system restart. Salesforce displays Unauthorized Access error or an Invalid Session error for any request initiated with an expired access token. The presence of a refresh token helps to re-establish the failed session internally by generating a new access token without user’s intervention.

    | Field | Sample Field Value |
    | Access Token URL | <https://login.salesforce.com/services/oauth2/token> |
    | User Name | The user name to login to Salesforce. |
    | Password | The password to login to Salesforce. |
    | Query Options: The following fields appear.  * grant\_type * client\_id * issuer | * grant\_type: password * client\_id: <3MVG97quAmFZJfVwk3ylU.8elhRYBqG9h25m3TWewozjKnFIY0HrhOEJl7LMET9HHocaHnTB1k04kophr1CgW> * issuer: <https://login.Salesforce.com> * username: <username to login to Salesforce>  *NOTE:*In case of a driver upgrade, the issuer field does not auto populate the earlier configured value. You must enter the issuer field manually. |
    | Secret Query Options: The values specified in these options are hidden for security purposes.  * refresh\_token * client\_secret | * refresh\_token: 5Aep861Xq7VoDavIt6UxKW62EAmfy0hKFv1T\_X8yhb9PRQWtsOCrr97CYDrVasefykdl\_f.DTVaJGKxjmz50XjQ * client\_secret: E734505442694ECD0156D83F965B42C0F07601BB8BFDCA9879420C1FF23C8A87 * password: <password to login to Salesforce> |
    | Header Fields | * Name: Content-Type * Value: application/x-www-form-urlencoded |
    | Common fields in Connection Parameters  *NOTE:*The fields mentioned in the below rows are common for OAuth2.0 and Basic Authentication. |  |
    | Application Truststore File: The path and the name of the keystore file that contains the trusted certificates for the remote server to achieve SSL handshake.  *IMPORTANT:*For Bearer, add the public certificate to cacerts, present in the path /opt/netiq/common/jre/lib/security. | </root/scim\_configuration/trustSalesforce/Salesforce>  *NOTE:*Create the truststore file in .jks format for the connected application. For more information on how to create the truststore file, see [Configuring the Subscriber Channel](../../../identity-manager-48/driver_admin/data/t4d85ztex67n.html#t4d86gc0bqud) in "[NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle)". |
    | Mutual Authentication | Not supported in Salesforce |
    | Proxy Authentication | * Proxy host name and port: <192.168.0.0:port>. Choose an unused port number on the proxy server. * Username * Password * Re-enter Password |
    | HTTPS Connection Timeout | The timeout value must be greater than 0.  *NOTE:*The driver waits for the time specified (in minutes) and terminates the HTTPS connection displaying the error codes that are configured in the Subscriber Options > HTTPS error codes for retry field. |
    | SCIM 2.0 URL | <https://salesforce.com/api/rest/scim/v2/339216517038085> |

    #### Configuring SCIM Driver with JWT

    The JSON Web token is an access request token in the JSON Web Token (JWT) format. It is an encrypted data string consisting of a header, payload, and a signature, and is used to transfer authorization data in client-server applications to authenticate the identity of the resource.

    ![](../graphics/scim_jwt_a.png)

    If you select JWT, the following fields appear:

    | Field | Sample Field Value |
    | Query Options: The following fields appear:  * client\_id * subject * issuer * client\_auth\_type * recipient\_keystore | * client\_id: <3MVG97quAmFZJfVwk3ylU.8elhRYBqG9h25m3TWewozjKnFIY0HrhOEJl7LMET9HHocaHnTB1k04kophr1CgW> * subject:<username@microfocus.com> * issuer: <https://login.salesforce.com> * client\_auth\_type: private\_key\_jwt * recipient\_keystore: </Soft/Certs/recipient.jks> |
    | Secret Query Options: The values specified in these options are hidden for security purposes.  * recipient\_storepass * recipient\_keypass * refresh\_token * client\_secret | * recipient\_storepass: <novell> * recipient\_keypass: <novell> * refresh\_token: 5Aep861Xq7VoDavIt6UxKW62EAmfy0hKFv1T\_X8yhb9PRQWtsOCrr97CYDrVasefykdl\_f.DTVaJGKxjmz50XjQ * client\_secret: E734505442694ECD0156D83F965B42C0F07601BB8BFDCA9879420C1FF23C8A87 |
    | For the other common fields such as Application Truststore File, Mutual Authentication, Proxy Authentication, HTTPS connection Timeout, and SCIM 2.0 URL, see [Common fields in Connection Parameters The fields mentioned in the below rows are common for OAuth2.0 and Basic Authentication.](create_scim_driv_obj_slsfrce.html#common_conn_params_scim_slsfrce) |  |

    #### Configuring SCIM Driver Manually with an Available Token

    Select Manual if you already have an access token available or created by an external application.

    ![](../graphics/scim_manual_token_a.png)

    | Field | Sample Field Value |
    | Token | <00D2v000002mBdQ!ARQAQAzAXhpgilDpcvN3RDgCkrfh4pyzCOv2G1Iq5kEMh0TRi> |
    | Query Options: The following fields appear.  * client\_id * issuer | * client\_id: <3MVG97quAmFZJfVwk3ylU.8elhRYBqG9h25m3TWewozjKnFIY0HrhOEJl7LMET9HHocaHnTB1k04kophr1CgW> * issuer: <https://login.Salesforce.com> |
    | Secret Query Options: The values specified in these options are hidden for security purposes.  * refresh\_token * client\_secret | * refresh\_token: 5Aep861Xq7VoDavIt6UxKW62EAmfy0hKFv1T\_X8yhb9PRQWtsOCrr97CYDrVasefykdl\_f.DTVaJGKxjmz50XjQ * client\_secret: E734505442694ECD0156D83F965B42C0F07601BB8BFDCA9879420C1FF23C8A87 |
    | For the other common fields such as Application Truststore File, Mutual Authentication, Proxy Authentication, HTTPS connection Timeout, and SCIM 2.0 URL, see [Common fields in Connection Parameters The fields mentioned in the below rows are common for OAuth2.0 and Basic Authentication.](create_scim_driv_obj_slsfrce.html#common_conn_params_scim_slsfrce) |  |
22. In the Install SCIM Base page, specify the Subscriber Options and Publisher Options, and click Next.

    | Field | Sample Field Value |
    | Subscriber Options | HTTPS error codes for retry: <307 408 503 504>  *NOTE:*The operation is retried if these errors are encountered. |
    | Publisher Options | * Enable Publisher Channel: Select Yes to enable the Publisher channel. * Polling interval in minutes: <10> * Heartbeat interval in minutes: <10>  *IMPORTANT:*Polling Resource Options: After configuring the driver, double click the connector line in the modeler window and navigate to Driver Configuration > Publisher Options tab to specify the polling resource options. Select the option as required:  + Configured Resources: to poll all resources that are configured as part of the schema settings.   + Custom Resources: Click ![](../graphics/icon_plus_green_n.png) to configure customized polling Resource ID and Resource URL, as shown below:  - For User:  * Resource ID: Example, urn:ietf:params:scim:schemas:core:2.0:User       * Resource URL: Example, https://ap16.salesforce.com/services/scim/v2/Users?startIndex=1&count=100     - For Group:  * Resource ID: Example, urn:ietf:params:scim:schemas:core:2.0:Group       * Resource URL: Example, https://ap16.salesforce.com/services/scim/v2/Groups?startIndex=1&count=100 |
23. In the Install SCIM Base page, specify the parameters as shown in the following table, and click Next.

    *Table 5-1* Schema Settings

    | Field | Sample Field Value |
    | Refresh Schema on Driver Startup | Defaults to No, specify Yes if you want to refresh the schema.  For more information on schema, see [Section 6.0, SCIM Schema Utility](t4d2m59259wh.html). |
    | Schema Options | Select the option as required, the default value is SCIM 2.0.  The available options are:  * SCIM 2.0 * Application URL: <https://ap17.salesforce.com/services/scim/v2/Schemas> * Import JSON File: Import the user defined schema JSON file from the local file system. |
    | Resource Type | * Resource ID: Resource ID in URN Format. For example, urn:ietf:params:scim:schemas:core:2.0:Users * Resource Endpoint: The resource endpoint for the Resource ID. For example, Users. * Modify Method Operation: Select PUT when you want to modify a resource in Salesforce.  Similarly for Groups:  * Resource ID: Example, urn:ietf:params:scim:schemas:core:2.0:Group * Resource Endpoint: Groups * Modify Method Operation: Select PUT. |

    *Table 5-2* Modifier Settings

    | Field | Sample Field Value |
    | Custom Java Class | Defaults to Hide, select Show to configure Modifiers. |
    | Document Handling: Defaults to No, select Yes. | * Class: com.example.MyNewClass * Init Parameter: Specify the parameters in string format that you want to pass to the init() method of your class. |
24. In the Remote Loader page, if you are configuring the driver with a remote loader select yes, else select no. Click Next.

    For more information about installing Remote Loader, see [Deciding Whether to Use the Remote Loader](../../../identity-manager-48/driver_admin/data/t461objwsz6a.html#t461objwsz6a) in "[NetIQ Identity Manager Driver Administration Guide](../../../identity-manager-48/driver_admin/data/bktitle.html#bktitle)".
25. Review the summary of tasks, and click Finish. The configured driver appears in the designer screen.
