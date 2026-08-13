# D.1 Managing Quotas

Your API quotas and current usage can be viewed at any time from your developerâs console: <https://console.developers.google.com>

Note that Google can and does change their policies and web interfaces at any time without warning. The information provided here may no longer be correct or current, though we will attempt to keep it up to date.

TIP: Log in with the account used to create the project in the first place.

Select the project which created the credential used by the Google Driver.Â The overview will give you a snapshot of your usage overall.

*Figure D-1* Overall Google Driver Usage

![](../graphics/figure52.png)

From the APIs & Auth section, select APIs, then select Enabled APIs.

*Figure D-2* Configuring APIs for Analysis

![](../graphics/figure53.png)

Select the Admin SDK. This API provides all services for the driver with the exception of Group Settings and Domain Shared Contacts. Selecting Usage will allow you to see a usage summary overÂ time.Â

*Figure D-3* Generating Usage Data

![](../graphics/figure54.png)

Select "Quotas" to see your current quotas and current remaining quota.

*Figure D-4* Applying for Higher Google Quotas

![](../graphics/figure55.png)

If you have exceeded your quota for requests per day, click the highlighted link to create a request to Google for more daily quota.Â

You can also go to this URL directly to access the Quota request form for the Admin SDK: <https://support.google.com/code/contact/admin_sdk_quota>

Clicking the "Change" button allows you to change your per-user limit of 15 requests per user per second, though it is unlikely that the driver will ever exceed this threshold.

For more information on the Admin SDK and quota limits, see the Google documentation: <https://developers.google.com/admin-sdk/directory/v1/limits>
