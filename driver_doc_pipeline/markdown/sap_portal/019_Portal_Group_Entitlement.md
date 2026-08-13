# 5.4 Portal Group Entitlement

The portal group entitlement adds users to the SAP Portal Groups, and it is enabled by default. This entitlement contains parameters, which means it can be granted multiple times. The parameters for the entitlement are SAP groups returned by the entitlement query to the SAP Portal.

The SAP [ABAP](identity-manager-sap-portal-driver-terminology.html#bjfkp9g) roles might appear as [UME](identity-manager-sap-portal-driver-terminology.html#bjfkswf) Groups when the entitlement query is issued, but the SAP Portal driver cannot assign [ABAP](identity-manager-sap-portal-driver-terminology.html#bjfkp9g) roles directly.

To manually enable this entitlement:

1. Verify that an entitlement agent that contains your list of criteria to grant or revoke Portal group assignments in SAP exists. For more information, see [Entitlement Agents](entitlement-agents-for-identity-manager-sap-portal-driver.html).
2. If you have an existing driver, continue with [Step 3](understanding-portal-group-entitlement-for-identity-manager-sap-portal-driver.html#bj8aa71); otherwise, during the creation of a driver, select True for the Use Portal Group Entitlement option.

   This sets the entitlement GCVs to True.
3. Access the GCVs page on the driver.
4. Select True for the User Portal Group Entitlement option.
5. Click OK to save the changes.

The entitlement is now enabled. When a user is granted a [UME](identity-manager-sap-portal-driver-terminology.html#bjfkswf) group entitlement through one of the entitlement agents, the SAP Portal driver automatically adds the user to the associated Portal groups.
