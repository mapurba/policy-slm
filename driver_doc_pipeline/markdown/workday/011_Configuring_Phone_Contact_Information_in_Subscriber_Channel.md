# 2.7 Configuring Phone Contact Information in Subscriber Channel

This section explains how to configure the phone contact information of a Workday user in the Subscriber channel. As a prerequisite, you must first fetch the Country Phone Code and Phone Type ID values from Workday.

The following procedures explain how to fetch these IDs and configure the phone contact information:

* [Fetching Country Phone Code ID and Phone Type ID from Workday](t4finm0426n2.html#t4finohor8km)
* [Adding the Phone Contact Information in Subscriber Channel](t4finm0426n2.html#t4fjj9lp4bcp)

## 2.7.1 Fetching Country Phone Code ID and Phone Type ID from Workday

Prior to configuring the phone contact information, you must fetch the Country Phone Code and the Phone Type ID from Workday. The procedures to fetch this information from Workday is explained in the following sections:

* [Fetching Country Phone Code ID from Workday](t4finm0426n2.html#t4fjj81c6kyj)
* [Fetching Phone Type ID from Workday](t4finm0426n2.html#t4fjj8gp39pa)

### Fetching Country Phone Code ID from Workday

The following procedure explains how to fetch a country phone code value from Workday.

1. Login to Workday.
2. Perform a search for Country Phone Code.
3. In the search results, click Country Phone Code link.
4. Navigate to ![](../graphics/wd_search_icon.png) > Integration ID > View ID.
5. Copy the value displayed in the ID column. For example, ALB\_355 is for the country Albania. This ID value will be added to the Country Phone Codes in Designer.

### Fetching Phone Type ID from Workday

The following procedure explains how to fetch a phone type ID from Workday.

1. Login to Workday.
2. Perform a search for Devices.
3. In the search results, select Phone Device Types.
4. Scroll over the corresponding Phone Type, and navigate to ![](../graphics/wd_search_icon.png) > Integration ID > View ID.
5. Copy the ID value. For example, in Workday, the ID value for telephone device type is 1063.5, and for mobile device type is 1063.1.

## 2.7.2 Adding the Phone Contact Information in Subscriber Channel

To add the Home and Work phone contact information in the Subscriber channel, perform the below tasks:

1. In Designer, double click the connector line, and navigate to GCVs > User Config.
2. In the Advanced Settings section, set User Advanced Settings to True.
3. Scroll to the Country Phone Code field and add the Country Code ID value as fetched in [Fetching Country Phone Code ID from Workday](t4finm0426n2.html#t4fjj81c6kyj) by clicking the ![](../graphics/icon_plus_green_n.png) icon. If the required value is already present, you can just select the required ID value from the list.
4. Click Apply > OK, and deploy the driver.

In Identity Console:

1. Click the User Management tile.

   1. Select the required user.
   2. On the Modify Users page, select the Others tab.
   3. Ensure the following attributes are present in the Valued Attributes list.

   * wd-HomePrimaryPhone
   * wd-HomePrimaryDeviceType
   * wd-WorkPrimaryPhone
   * wd-WorkPrimaryDeviceType

   If these attributes are not present, add them from the unvalued attribute list by clicking the + sign.
2. Edit these attributes and add their corresponding values, as shown below:

   * wd-HomePrimaryPhone: Add the new phone number with the country code. For example, <+297 1122334456>.
   * wd-HomePrimaryDeviceType: Add the home device type ID as fetched from Workday. For more information, see [Fetching Phone Type ID from Workday](t4finm0426n2.html#t4fjj8gp39pa).
   * wd-WorkPrimaryPhone: Add the new phone number with the country code. For example, <+297 8877665554>.
   * wd-WorkPrimaryDeviceType: Add the work device type ID as fetched from Workday. For more information, see [Fetching Phone Type ID from Workday](t4finm0426n2.html#t4fjj8gp39pa).

   *IMPORTANT:*You must ensure to add the ID values to the above mentioned attributes based on the device types respectively.

   For example:

   * For a mobile device type:

     + wd-HomePrimaryPhone as <+297 1122334456>
     + wd-HomePrimaryDeviceType ID as 1063.1
   * For a telephone device type:

     + wd-WorkPrimaryPhone as <+297 8877665554>
     + wd-WorkPrimaryDeviceType ID 1063.5
3. Save.
