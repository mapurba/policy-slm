# 6.1 Refreshing the Fetched Connected Application’s Schema

When you configure the driver for the first time, you must set the Refresh Schema on Driver Startup to Yes and specify the Schema Options for fetching the connected application’s schema. Once these parameters are set and you start the driver, the driver fetches the connected applications schema and stores it in the driver storage (DirXML-DriverStorage: ), which is available in Identity console > Driver Configuration > Driver parameter.

In Identity Console, the procedure to fetch a new schema for mapping is shown below:

1. Login to Identity Console.
2. Select IDM Administrator.
3. Click Driver Sets, all the configured drivers appear.

   *NOTE:*If the driver set is not listed on the Driver Sets tab, use the Search In field to search for and display the driver set.
4. Click the driver name, go to Data Transformation and Synchronization tab.
5. Select Filter in the SCIM driver diagram.
6. In the Right Pane, click ![](../graphics/add_attribute.png) to add attributes.

   Similarly, map all the resource types with their corresponding attributes. For more information on mapping attributes see, [Section C.0, Mapping Attributes for Identity Manager and Connected Application](t4d0rwcd9ohv.html).
7. In the Filter window, scroll to find the mapped attribute and select it. The fields associated with the selected attribute appears in the right pane.
8. Select the Synchronize radio button in the Publish and Subscribe options.
9. Click Save.

In Designer, the procedure to refresh the schema is shown below:

1. Open Designer.
2. Import the driver changes.
3. In the Outline tab, expand your required driverset.
4. Right click the driver name and click Live < Refresh Application Schema.
