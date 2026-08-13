# 6.5 Verifying the Functionality

After you deploy and configure the driver, you need to verify that the driver correctly creates and updates Sentinel Identity and Account data.

1. Ensure that you have started the driver.
2. Create a test user in the Identity Vault with all attributes required by the matching attributes you configured.
3. Verify that a corresponding Sentinel Identity is found in Sentinel > People browser.

   For more information, see "[Integrating Identity Information with Sentinel Events](https://www.netiq.com/documentation/sentinel70/s701_user/?page=/documentation/sentinel70/s701_user/data/bhklhcm.html)" in the [Sentinel User Guide](https://www.netiq.com/documentation/sentinel70/s701_user/?page=/documentation/sentinel70/s701_user/data/bhklhcm.html).
4. In the People browser, verify that a Sentinel account corresponding to the Identity Vault account appears under the Identity's Profile tab.
5. If your Identity Vault already contains objects with Identity Tracking data from other systems, such as Active Directory with the Identity Tracking package, you can use Migrate from Identity Vault in Identity Console to validate the configuration.
