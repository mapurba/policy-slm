# 2.13 Advanced Synchronization of Worker Photos from the Workday Portal

The photo synchronization between Workday and the driver happens once in every 24-hours. If any Organization has a large number of worker base, the driver takes longer than usual to fetch all the worker’s photo. Sometimes in such cases, the process might fail due to timeout.

*IMPORTANT:*It is highly recommended to use the photo change business process to fetch worker photos from Workday. The following procedure to synchronize worker photos from the Workday is not recommended as this functionality might be deprecated in the near future.

The Workday system stores the date/time value of each change in worker’s photo. These date/time values can be used via calculated fields and custom reports (created using the calculated fields) to improve driver’s performance while performing photo synchronization. The Workday driver uses this custom report to compare the photo related details based on the last date/time value of the worker’s photo since the previous polling.

*NOTE:*The following configuration is not mandatory and only recommended to improve the driver’s performance.

Perform the following steps to create calculated fields and custom report in the Workday portal:

1. Create the following calculated fields using the Create Calculated Field option in the Workday portal:

   1. Create a calculated field. For example, we’ve created a field named CF\_TF\_RPT\_Is Action Event Photo Change.

      ![](../graphics/calc-field-1-1.png)
   2. Create another calculated field using the field created in the previous step as a Condition. For example, we’ve created the second field with the name CF\_ESI\_RPT Latest Photo Change Event.

      ![](../graphics/calc-field-2.png)
   3. Create a third calculated field using the field created in previous step as a Lookup Field. For example, we have created the field named CF\_LRV\_RPT Completion Date and Time of Latest Photo Event.

      ![](../graphics/calc-field-3.png)
2. Create a custom report using the Create Custom Report option in Workday portal. You must ensure that the integration user has access to this report or the report is created as an integration user.

   Create a custom report with the following mandatory fields:

   * Employee ID
   * Worker is Contingent Worker
   * The calculated field created (CF\_LRV\_RPT Completion Date and Time of Latest Photo Event) in [Step 1.c](t4dhw8clmwa0.html#calc-field).

   Note down the calculated field name appearing under Column Heading Override XML Alias as shown in the below image and specify the same in the Photo Update Calculated Field in Designer while configuring the driver.

   *NOTE:*You can add additional fields as per your requirement.

   ![](../graphics/cust-reprt-1-2.png)
3. Click on the Sort tab to enable Sorting Field for the newly created custom report based on alphabetical descending order. This helps to display the latest changes at the top of the report.

   ![](../graphics/cust-reprt-2-1.png)
4. Create prompts for the report under the Prompts tab.

   Provide default values for Worker Types as Contingent Worker and Employee. This will ensure that both types of Workers are included in the report.

   ![](../graphics/cust-reprt-3-2.png)
5. Enable the report as Web Service under the Advanced tab.

   *NOTE:*Note down the Namespace value and specify the same in the Photo Report Namespace field in Designer while configuring the driver.

   ![](../graphics/cust-reprt-4-1.png)
6. Click on Actions > Web Service > View URLs to get the Web Service URL of the report.

   ![](../graphics/cust-reprt-5.png)
7. Copy the URL for Workday XML > WSDL option and save it. You need to specify this URL in the Photo Update Report URL field in Designer while configuring the driver.

   ![](../graphics/cust-reprt-6-1.png)
