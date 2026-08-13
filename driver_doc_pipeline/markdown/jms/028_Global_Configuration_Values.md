# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The JMS driver includes several GCVs that are created from driver parameters. When you modify the driver parameters, the GCVs are updated; likewise, when you modify the GCVs, the driver parameters are updated. These GCVs are created so that the driver parameter information can be more easily used in the driver’s policies.

You can also add your own GCVs if you discover you need additional ones as you implement policies in the driver.

To access the driver’s GCVs in Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Locate the Delimited Text driver icon, then click the driver icon to display the driver’s properties page.
4. Click Global Config Values drop down to display the GCV page.

To access the driver’s GCVs in Designer:

1. Open a project in the Modeler.
2. Right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select Properties > Global Configuration Values.

   or

   To add a GCV to the driver set, right-click the driver set icon ![](../graphics/driver_set_icon_n.png), then click Properties > GCVs.

*Destination unique ID:*
Specifies the identifier by which this destination is known in the Identity Manager namespace. This name is also the durable subscription name for topics.

This value must be unique per channel (Subscriber/Publisher).
