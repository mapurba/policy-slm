# 3.2 Customizing the Subscriber Channel for Additional Attributes

The procedure involves the following steps for subscriber channel:

1. Fetch the XDS event from the Workday log.
2. Identify the XPATH of the required attribute from the fetched XDS event.
3. Build the XPATH for the attribute in the required format, to add to the custom stylesheet.
4. Add the XPATH of the new attribute to the custom stylesheet. You can copy the custom stylesheet, edit and upload it as per your requirement.

   *NOTE:*

   * Ensure that you provide a complete updated stylesheet file when configuring the driver.
   * This feature is supported only for worker and photo objects.

   For example, you have to add BirthDate template and the Caller template (to call the BirthDate template) in the custom stylesheet for the BirthDate attribute.

   The examples for BirthDate and BirthDate Caller templates are shown below:

   #### Sample BirthDate template:

   ```
   <xsl:template name="Date_of_Birth">
   <xsl:param name="Birthdate"/>
   <xsl:param name="workerIdValue"/>
   <xsl:param name="workerIdType"/>
   <!-- Prepare SOAP envelope for DOB -->
   <soapenv:Envelope
   xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
   xmlns:bsvc="urn:com.workday/bsvc">
   <soapenv:Header />
   <soapenv:Body>
   <xsl:message>version is: <xsl:value-of select="$wdVersion"/></xsl:message>
   <bsvc:Change_Personal_Information_Request bsvc:version="{$wdVersion}">
   <bsvc:Change_Personal_Information_Data>
   <bsvc:Worker_Reference bsvc:Descriptor="?">
   <bsvc:ID bsvc:type="{$workerIdType}">
   <xsl:value-of select="$workerIdValue"/></bsvc:ID>
   </bsvc:Worker_Reference>
   <bsvc:Personal_Information_Data>
   <bsvc:Date_of_Birth><xsl:value-of select="$Birthdate"/></bsvc:Date_of_Birth>
   </bsvc:Personal_Information_Data>
   </bsvc:Change_Personal_Information_Data>
   </bsvc:Change_Personal_Information_Request>
   </soapenv:Body>
   </soapenv:Envelope>
   </xsl:template>
   ```

   #### Sample BirthDate Caller template:

   ```
   <!--Personal Info attributes -->
    <xsl:variable name="lv-Birthdate" select="modify-attr[(@attr-name='wd-BirthDate')]/add-value/value/text()"/>
   <xsl:call-template name="Date_of_Birth">
   <xsl:with-param name="Birthdate" select="$lv-Birthdate"/>
   <xsl:with-param name="workerIdType" select="$lv-wd-WorkerIDType"/>
   <xsl:with-param name="workerIdValue" select="$lv-wd-EMPLID"/>
   </xsl:call-template>
   ```

   *NOTE:*In the above example, the bold text is the XPATH that is built for BirthDate attribute by referring to the fetched schema file from Workday.
5. In Identity Console, click the IDM Administration tile.
6. On the Driver Dashboard, click the Workday Driver icon.
7. Click the Data Transformation and Synchronization tab.
8. Click Filter in the Subscriber Channel.
9. Add the attribute wd-BirthDate. To add:

   1. Select User as class and click Add Attribute.
   2. Click Show All Attribute to display the list of attributes applicable for the class.
   3. Add wd-BirthDate, and save.
10. Select the attribute from the class list and set the Subscriber option to Synchronize to match the attribute name with the schema extension name.
11. Restart the driver for the changes to take effect.

In Designer:

1. double click the connector line and navigate to Driver Configuration > Driver Parameters.
2. Select Subscriber Options > Worker Settings > Import Worker Stylesheet.
3. Add the XSLT stylesheet path as prepared in [Step 4](t4eqymkdeu0j.html#step4_xslt_path_subscriber), and deploy the driver.
4. Restart the driver for the changes to take effect.

*NOTE:*When supplied stylesheets are used as a template to create external stylesheets, it is critical that the results of processing the response document through the stylesheet will return the right association value in the resulting XML. For the most efficient processing, the external stylesheet must return the attributes only that have a different value or any new attributes. However, it is advised to retain the code that generates association as is, to ensure that the results of the external stylesheet are correctly merged with the results from the internal stylesheet.
