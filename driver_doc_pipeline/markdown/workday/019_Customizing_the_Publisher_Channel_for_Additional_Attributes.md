# 3.1 Customizing the Publisher Channel for Additional Attributes

You can customize the stylesheet to:

* [Modifying an Existing Attribute](t4eqyl8053wa.html#t4flm8ss6ioi)
* [Adding a New Attribute](t4eqyl8053wa.html#t4flm96o5q9t)

## 3.1.1 Modifying an Existing Attribute

You can modify an existing attribute value in the custom stylesheet. For example, consider a scenario where you want to update your domestic phone number in place of your international phone number. In this scenario, you can just modify the phone attribute in the custom stylesheet as shown below:

* Stylesheet for phone attribute (in bold) is shown below:

  ```
  <attr>
  <xsl:attribute name="attr-name">
  <xsl:value-of select='"wd-WorkPrimaryPhone"'/>
  </xsl:attribute>
  <value>
  <xsl:value-of select="$primary_work_phone_node/@wd:International_Formatted_Phone"/>
  </value>
  </attr>
  ```
* The modified custom stylesheet:

  ```
  <attr>
  <xsl:attribute name="attr-name">
  <xsl:value-of select='"wd-WorkPrimaryPhone"'/>
  </xsl:attribute>
  <value>
  <xsl:value-of select="$primary_work_phone_node/@wd:National_Formatted_Phone"/>
  </value>
  </attr>
  ```

You can customize the Workday objects and their attributes using custom stylesheet over the Publisher and Subscriber channel. The custom XSLT paths must be specified for the required objects as per your environment to exchange information between Workday and Identity Vault. For more information on customization, see [Step 8](t4avmq79xc47.html#cust_attr_xslt).

*IMPORTANT:*These above mentioned attribute values (in the custom stylesheet) are sample values and must be used for reference purposes only. If you want to add a new custom attribute, or modify an existing attribute for the respective workday supported objects (files), there is no significant action or insertion required though the Workday driver configuration. The Workday driver shim, by default, would handle the existing objects that are supported by Workday and also their respective attribute transformations.

## 3.1.2 Adding a New Attribute

To add a new attribute, the perform the following steps:

1. Fetch the SOAP response from Workday.
2. Identify the XPATH of the required attribute from the fetched SOAP response.
3. Build the XPATH for the attribute in the required format. This path will be added in the XSLT stylesheet.
4. Add the XPATH of the new attribute to the XSLT stylesheet. For example, if you are adding an attribute for Marital Status, add the following to the XSLT stylesheet.

   ```
   <!--  **** Worker : Marital Status************* -->
   <attr>
   <xsl:attribute name="attr-name">
   <xsl:value-of select='"wd-MaritalStatusID"'/>
   </xsl:attribute>
   <value>
   <xsl:value-of select="wd:Worker_Data/wd:Personal_Data/wd:Marital_Status_Reference/wd:ID[@wd:type='Marital_Status_ID']"/>
   </value>
   </attr>
   ```

   *NOTE:*In the above example, the bold text is the XPATH that is built for Marital Status attribute, referring to the fetched schema file from Workday.
5. Extend the schema file for the new attribute. The attribute added in the XSLT stylesheet should be added in the schema extension (.sch) file also, so that Identity Manager supports that attribute.

   Ensure to add the attribute name to the Object Class, as shown below:

   ```
   "wd-MaritalStatusID" ATTRIBUTE ::=
   {
    Operation ADD,
    SyntaxID SYN_CI_STRING,
    Flags {DS_STRING_ATTR},
    ASN1ObjID {2 16 840 1 113719 1 14 4 1 2746}
   }
   ```
6. In Identity Console, click the IDM Administration tile.
7. On the Driver Dashboard, click the Workday Driver icon.
8. Click the Data Transformation and Synchronization tab.
9. Click Filter in the Publisher Channel.
10. Add the attribute name, for example wd-MaritalStatusID. To add:

    1. Select User as class and click Add Attribute.
    2. Click Show All Attribute to display the list of attributes applicable for the class.
    3. Add wd-MaritalStatusID, and save.
    4. Select the attribute from the class list and set the Publisher option to Synchronize to match the attribute name with the schema extension name.
11. Add the XSLT stylesheet path as prepared in [Step 4](t4eqyl8053wa.html#step4_xslt_path_publisher). To add the path:

    1. Click the Configuration tab.
    2. Expand the Driver Parameters section and click the Subscriber Settings tab.
    3. Add the path in the Import Worker Stylesheet field.
12. Save.
13. Restart the driver for the changes to take effect.

To add the XSLT stylesheet path, in Designer:

1. Double click the connector line, and navigate to Driver Configuration > Driver Parameters.
2. Select Publisher Options > Worker > Worker Poll Settings > Import Worker Stylesheet.
3. Restart the driver for the changes to take effect.
