# 1.3 Driver Concepts

The following figure shows how the SAP Portal driver works. The driver provisions users from the Identity Vault and passes them to the SPML listener service on the portal. The SPML listener passes the requests to the User Management Engine (UME) and the UME writes the request to the UME local database, to an external LDAP directory, or to an [ABAP](identity-manager-sap-portal-driver-terminology.html#bjfkp9g) system, depending on the configuration of the identity store for the portal. If the request is written to the [ABAP](identity-manager-sap-portal-driver-terminology.html#bjfkp9g) system, the request can be passed to any [CUA](identity-manager-sap-portal-driver-terminology.html#bjxhksj) SAP systems that are part of the [ABAP](identity-manager-sap-portal-driver-terminology.html#bjfkp9g) back end.

*Figure 1-1* SAP Portal Driver

![](../graphics/portal_driver_a.png)

The SAP Portal driver synchronizes SAP users as well as the user’s SAP group assignments and SAP role assignments. If the Portal is configured with an [ABAP](identity-manager-sap-portal-driver-terminology.html#bjfkp9g) user store, the user account is synchronized and added to the [ABAP](identity-manager-sap-portal-driver-terminology.html#bjfkp9g) system; however, the [ABAP](identity-manager-sap-portal-driver-terminology.html#bjfkp9g) roles, which display as SAP group objects in the portal, cannot be assigned directly in the [SPML](identity-manager-sap-portal-driver-terminology.html#bjfkqvu) service. To synchronize groups, you must use the SAP User Management driver with the SAP Portal driver. For more information, see the [NetIQ Identity Manager Driver for SAP User Management Implementation Guide](../../z_sap_user/data/netiq-identity-manager-driver-for-sap-user-management.html#netiq-identity-manager-driver-for-sap-user-management).

The SAP Portal driver can be configured to use any of the back-end identity stores that are available.

The SAP Portal driver synchronizes information from the Identity Vault into the portal. Synchronizing information from the portal into the Identity Vault is not supported. This is a unidirectional driver.
