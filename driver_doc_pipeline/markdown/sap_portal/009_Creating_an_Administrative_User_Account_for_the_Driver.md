# 3.2 Creating an Administrative User Account for the Driver

The driver must authenticate to the SAP Portal as a member of the Administrators group in order to create, delete, and modify accounts in the SAP Portal system. Creating a separate account that has administrative rights prevents the SAP Administrator account from ever being locked by any actions of the SAP Portal driver. For example, the Administrator password is changed, but the old password is still stored in the driver. The driver attempts to log into the portal as part of its normal activity and locks the Administrator account based on the SAP Portal security policy.

To create an administrative user for the driver:

1. Log into the SAP Portal as the Administrator.
2. Search for the Administrator user account in Identity Management.
3. Select the Administrator user account.
4. Click Copy to New User to create a user with the same rights as the Administrator.
5. Specify the Logon ID for the administrative user.
6. Specify a password for this user in the Define Initial Password field.
7. Click Save to save the new user.
8. Log out of the portal.
9. Log back into the portal as the new administrative user.

   This prompts the user to set a permanent password.
10. Specify this user in the [Authentication ID:](identity-manager-sap-portal-driver-configuration.html#bsa1k1r), then update the password in the [Authentication Password:](identity-manager-sap-portal-driver-configuration.html#bsa1mqh) on the Subscriber settings of the driver.

After the permanent password is set, the driver has the same rights as the Administrator user. You can check the administrative user’s rights by verifying that it is a member of the Administrators group in the [UME](identity-manager-sap-portal-driver-terminology.html#bjfkswf) configuration.
