# 8.3 Configuring the Driver to Use the New Class

After you have placed the new .jar file in the correct location, configure the driver to use your new class by modifying the driver's properties.

1. In Identity Console, go to the Identity Manager Administration page:

   1. In the Identity Manager frame, click IDM Administration.
   2. Select the driver set that contains the driver.
   3. Click the driver icon.
2. Select Configuration tab.
3. Click Driver Parameters drop down, then click ![](../graphics/edit_xml.png) Edit XML.
4. Locate the <publisher-options> section of the file.

   This file defines which parameters and values appear in the Driver Parameters section of the Driver Configuration page.

   For each class you created that works on the Publisher channel, you enter an additional option in the <publisher-options> section. After you update this file, you see your new options in the interface.
5. For each new class you created on the Publisher channel, add an entry corresponding to the interface type. Use the following table as a guide:

   | Interface | New Entry |
   | InputSorter | <definition display-name="InputSorter Class" name=" input-sorter" type="string"> <value>com.acme.MyNewClass</value> </definition>  <definition display-name="InputSorter init string" name=" input-sorter-params" type="string"> <value>MY CONFIG PARAMS</value> </definition> |
   | InputSource | <definition display-name="InputSource Class" name=" input-source" type="string"> <value>com.acme.MyNewClass</value> </definition>  <definition display-name="InputSource init string" name=" input-source-params" type="string"> <value>MY CONFIG PARAMS</value> </definition> |
   | PreProcessor | <definition display-name="PreProcessor Class" name="pre-processor" type="string"> <value>com.acme.MyNewClass</value> </definition>  <definition display-name="PreProcessor init string" name="pre-processor-params" type="string"> <value>MY CONFIG PARAMS</value> </definition> |

   1. Replace com.acme.MyNewClass with the name of the class that you defined, along with a full package identifier.
   2. Replace MY CONFIG PARAMS with any information that you want to pass to the init method of your class.

      The init method of your class is then responsible for parsing the information contained in this string. If your class doesn’t require a configuration string to be passed to the init method, you can leave off the whole element, in which case null is passed to the init method.
6. If you created a PostProcessor rule, locate the <subscriber-options> section of the file and add the following lines:

   ```
   <definition display-name="PostProcessor Class" name="post-processor" type="string">
   <value>com.acme.MyNewClas</value>
   </definition>

   <definition display-name="PostProcessor Parameters" name="post-processor-params" type="string">
   <value>MY CONFIG PARAMS</value>
   </definition>
   ```

   1. Replace com.acme.MyNewClass with the name of the class that you have defined along with full package information.
   2. Replace MY CONFIG PARAMS with any information that you want to pass to the init method of your class.

      The init method of your class is then responsible for parsing the information contained in this string. If your class doesn’t require a configuration string to be passed to the init method, you can leave off the entire element, in which case null would be passed to the init method.
7. Click OK.
