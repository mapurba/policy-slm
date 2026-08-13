# 8.1 Configuring Dynamic Attributes Using the Workday Driver

This section provides information on how to use various dynamic attributes provided by the Workday driver.

* [Synchronizing Custom IDs Using the Workday Driver](t4b44ov3owjn.html#t4b44p540azt)
* [Configuring Derived Attributes for Worker](t4b44ov3owjn.html#t4b44payzy58)
* [Configuring Custom Fields Using the Workday Driver](t4b44ov3owjn.html#t4b44paz0t79)
* [Adding New Attribute to the Filter](t4b44ov3owjn.html#t4b52f9ggury)

## 8.1.1 Synchronizing Custom IDs Using the Workday Driver

The driver can be configured to synchronize Other IDs displayed on the IDs tab of the Personal section in Workday. The driver and API refer to these other IDs as Custom IDs. Using the Change\_Other\_IDs\_Request API, the driver can update custom ids in Workday. Perform the following steps to configure Custom IDs for the Workday driver:

1. Collect Custom\_ID\_Type\_ID of the Custom IDs that need to be synchronized with Identity Manager. This information can be collected from the Workday implementation team. The IDs are case-sensitive.
2. In Designer, go to Workday Driver Properties > Driver Configurations > Driver Parameters > Driver Options > Transformation Parameters and specify the following:

   * *Parameter Name:*
     wdCustomIdList
   * *Parameter Value:*
     Multi valued list of all the IDs that are required to synchronize data between Workday and Identity Manager. For example, CUSTOM\_ID\_TYPE-6-10 is a parameter value of one Custom ID in Workday driver.
3. In Designer, add a driver schema mapping for {IDV attribute name} to {WD Custom Attribute}\_Custom\_ID on the Workday driver. For example, CUSTOM\_ID\_TYPE-6-10 to CUSTOM\_ID\_TYPE-6-10\_Custom\_ID.
4. If multiple Custom IDs are being updated from Identity Manager on Subscriber channel, then for each custom ID, you must create wd-user auxiliary class attribute in Designer or Identity Console to hold the Workday Reference ID of the Custom ID. This stores an internal Workday reference which is needed in order to update the value of the Custom ID in Workday. These auxiliary class attributes should be created as single valued and can be case ignore string. For example, AUX\_ID\_WID.
5. In schema mapping policy, add a mapping of {WD Custom Attribute}\_Custom\_ID\_Shared\_Reference with the attribute created in the previous step. For example, CUSTOM\_ID\_TYPE-6-10\_Custom\_ID\_Shared\_Reference to AUX\_ID\_WID.
6. Once a custom ID is specified in the wdCustomIdList, the driver shim will also return an attribute of the format {WD Custom Attribute}\_Description. For example, CUSTOM\_ID\_TYPE-6-10\_Description.
7. In driver filter, add an entry for the Identity Manager attribute that is mapped to {WD Custom Attribute}\_Custom\_ID so that it flows to Workday on the subscriber and/or from Workday on the publisher channels. For example, AUX\_ID.
8. If one or more custom IDs are updated from Identity Manager, then create a driver filter entry for each newly created attribute holding the custom ID attributes so they flow back to Identity Manager on the publisher channel. For example, AUX\_ID, AUX\_ID\_WID, AUX\_ID\_Description.
9. If one or more custom IDs are updated from Identity Manager, then create an output transformation policy to append the Shared Reference of the custom ID that is changing to the driver-operation-data. Ensure that value which is appended to the driver-operation-data is prefaced with WD- even though the attribute name in the data mapping does not have WD-.

   * Append the XML element WD-{WD Custom Attribute}\_Custom\_ID\_Shared\_Reference to driver-operation-data. For example, WD-CUSTOM\_ID\_TYPE-6-10\_Custom\_ID\_Shared\_Reference.
   * Append the text from the IDV source attribute. For example, AUX\_ID\_WID.
   * Create a rule for each Custom ID attribute that you are sending to Workday. The policy should be added after NETQWDDCFG-otp-user output transformation policy. If the attribute holding the custom ID is not in the IDV, nothing will be appended to the driver-operation-data. A sample policy rule has been shown below:

     ```
     <rule>
         <description>Add driver-operation-data element for modify AUX_ID events</description>
         <conditions>
             <and>
                 <if-op-attr name="AUX_ID_Custom_ID" op="changing"/>

                 <if-operation mode="nocase" op="equal">modify</if-operation>

                 <if-class-name mode="nocase" op="equal">User</if-class-name>
             </and>
         </conditions>
         <actions>
             <do-if>
                 <arg-conditions>
                     <and>
                         <if-attr name="AUX_ID_WID" op="available"/>
                     </and>
                 </arg-conditions>
                 <arg-actions>
                     <do-append-xml-element expression="driver-operation-data" name="WD-CUSTOM_ID_TYPE-6-10_Custom_ID_Shared_Reference"/>
                     <do-append-xml-text expression="driver-operation-data/WD-CUSTOM_ID_TYPE-6-10_Custom_ID_Shared_Reference">
                         <arg-string>
                             <token-attr name="AUX_ID_WID"/>
                         </arg-string>
                     </do-append-xml-text>
                 </arg-actions>
                 <arg-actions/>
             </do-if>
         </actions>
     </rule>
     ```

## 8.1.2 Configuring Derived Attributes for Worker

When an organization is added to the wdOrgList transformation parameter of the Workday driver, the shim will automatically derive the following 3 attributes on worker object for each organization type/organization sub-type combination:

* \_RefID is used for data in the Organization\_Reference\_ID element
* \_Name is used for data in the Organization\_Name element
* \_Code is used for data in the Organization\_Code element
* |RoleID\_Employee\_ID
* |RoleID\_Contingent\_Worker\_ID

The above derived attributes should be suffixed to the Organization-type | Organization-sub-type. These attributes are available to be added to the schema mapping policy and to the filter. For example:

```
Supervisory|Department_RefID
Supervisory|Department_Name
Supervisory|Department_Code
```

In the above example, Supervisory is the Organization type and Department is the Organization sub-type. The values for Organization type and Organization sub-type are derived from the following SOAP API response path of Get\_Workers API:

```
wd:Worker_Data/wd:Organization_Data//wd:Organization_Data[wd:Organization_Type_Reference/wd:ID[@wd:type='Organization_Type_ID'] | wd:Worker_Data/wd:Organization_Data//wd:Organization_Data[wd:Organization_Type_Reference/wd:ID[@wd:type='Organization_Type_ID']/wd:Organization_Subtype_Reference/wd:ID[@wd:type='Organization_Subtype_ID']
```

RoleID is derived from the following SOAP API response path of Get\_Workers API:

```
wd:Worker_Data/wd:Organization_Data//wd:Organization_Data[wd:Organization_Type_Reference/wd:iD[@wd:type='Organization_Type_ID']/wd:Organization_Support_Role_Data/wd:Organization_Support_Role/wd:Organization_Role_Reference/wd:iD[@wd:type='Organization_Role_ID']
```

## 8.1.3 Configuring Custom Fields Using the Workday Driver

Worker has a functionality where a Workday implementer can create override fields that have data calculated from the data in one or more other data fields. This option can be used to get data that the current driver shim does not return. For instance, one customer wanted to synchronize the pay grade which is a part of the compensation data returned if Include\_Compensation were included in the response group data. However, since Include\_Compensation includes all the salary information, the shim was purposely designed to not return that data. To get the pay grade for this customer, the Workday implementers set up an override field for just the pay grade.

In order to use Workday override calculated field information from the Worker data in the driver, you must take the following steps:

1. Obtain the Integration System ID from the Workday team. for more information, see [Obtaining Integration System ID from Workday](t4b44ov3owjn.html#t4cs8wgwzt6n).
2. Place the Integration System ID in the Publisher driver parameters in the Field and Parameter Criteria Provider Reference List of the corresponding class.
3. Obtain the override field name.
4. Once you have obtained the name of the override fields, the field names must be placed in the wdIntFieldAttrList transformation parameters.
5. The override fields are now available for data mapping or use in policies by appending \_CF to the override field name. For example, the override field returned by the shim will be mailStop\_CF for mailstop override field. This will be the application attribute name used in the schema mapping or input and output transformation policies.

### Obtaining Integration System ID from Workday

Perform the following steps to obtain the integration system ID from Workday:

1. Search for the View Integration Field Override Service in Workday.
2. Select your Integration Field Override Service and click OK.
3. View your Integration Field and click on the value of Integration System. For example, WorkDay\_Driver.
4. Collect the value from System ID field. Sample value for my tenant System ID is WorkDay\_Driver/WorkDay\_Driver/StartHere.
5. Place the Integration System ID in the Publisher driver parameters in the Field and Parameter Criteria Provider Reference List of the corresponding class

## 8.1.4 Adding New Attribute to the Filter

If you want the additional attributes (newly added to filter) to be populated on workers who are already migrated to the Identity Vault, You can perform one of the following steps:

* Migrate the workers again through the driver which in turn clears the cache.
* No changes required. The attributes will flow automatically as part of regular polling by the driver, provided that there is a change on that worker in Workday.

Another sync option is to set the wd-Merge attribute to True on the workers to sync. If the wd-Merge-effectiveDate is set before setting the wd-Merge to True, the sync will be according to the wd-Merge-effectiveDate if that is in the future. Otherwise, the current date will be used as the effective date for the sync. However, for this option to work correctly, all workers that have the wd-Merge attribute set to true, must already have the correct value for the wd-WorkerIDType (Employee\_ID or Contingent\_Worker\_ID).

If the worker has not been modified in Workday, the driver will never get that user data during polling and the new attributes will not be populated for that worker in Identity Vault. However, there will be delay in populating additional attributes until that worker gets modified in Workday.
