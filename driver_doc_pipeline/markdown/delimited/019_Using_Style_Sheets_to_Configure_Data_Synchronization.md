# 7.0 Using Style Sheets to Configure Data Synchronization

The real power of Identity Manager is in managing the shared data itself. This section covers some common customizations for the Delimited Text driver.

The example configuration available with the driver uses comma-separated value files. However, you can use the driver in many ways. It is designed to be as flexible as possible. The driver passes the text-based files largely unchanged to the style sheets. The style sheets do most of the work. You can write new style sheets to allow the driver to work with almost any text-based file that contains predictably repeatable patterns.

The basis for this exchange is the <delimited-text> XML element. For example, to design a Publisher channel that reads information from a text file, create an Input Transform style sheet that receives the contents of the file and converts it into a <delimited-text> element.

The following is an example of a <delimited-text> element:

```
<delimited-text>
     <record>
          <field name="FirstName">John</field>
          <field name="LastName">Maxfield</field>
          <field name="Phone">555-1212</field>
     </record>
     <record>
          <field name="FirstName">Sarah</field>
          <field name="LastName">Lopez</field>
          <field name="Phone">555-3434</field>
     </record>
</delimited-text>
```

For detailed information on writing style sheets to handle other document types, refer to the sample style sheets that come with this driver. If you create the driver by using the example configuration, you can use Input Transform, Output Transform, and Event Transformation style sheets as a starting point.
