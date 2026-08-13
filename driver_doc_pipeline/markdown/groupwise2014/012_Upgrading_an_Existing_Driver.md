# 4.0 Upgrading an Existing Driver

The GroupWise driver communicates with the GroupWise system. Ensure that earlier versions of GroupWise are upgraded to GroupWise 2014 SP1 or later versions, or GroupWise 18, before running the driver upgrade. The GroupWise upgrade program automatically associates GroupWise server with the Identity Vault. However, you should verify whether the Identity Vault is correctly linked with the upgraded GroupWise server.

1. Log in to the Administration console.
2. Navigate to the LDAP Server Configuration page.
3. Verify the Name field populates the name of the Identity Vault (eDirectory tree).
4. Specify other Identity Vault configuration information and save the settings.

   For more information, see [Associating Identity Vault with GroupWise System](create-driver-object-designer.html#b1d27cy6).
