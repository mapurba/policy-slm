# A.2 Global Configuration Values

Global configuration values (GCVs) are values that can be used by the driver to control functionality. GCVs are defined on the driver or on the driver set. Driver set GCVs can be used by all drivers in the driver set. Driver GCVs can be used only by the driver on which they are defined.

The WorkOrder driver includes one predefined GCV:

*WorkOrder Container:*
This is the WorkOrder container that is specified by the [WorkOrder Container](global-configuration-values.html#bs8icx2) setting on the Driver Configuration page. You can change the setting on the Driver Configuration page or on the GCV page.

The GCV is included as a driver set GCV (not a driver GCV) so that it can be used by other drivers as they create work orders to be placed in the WorkOrder container.

To access the driver’s GCVs in Identity Console:

1. Click the IDM Administration tile.
2. Select the driver set that contains the driver whose properties you want to edit.
3. Locate the driver icon, then click the driver icon to display the driver’s properties page.
4. Click Global Config Values drop down to display the GCV page.

To modify the driver’s GCVs in Designer:

1. Open a project in the Modeler.
2. To add a GCV to the WorkOrder driver, right-click the driver icon ![](../graphics/driver_icon_n.png) or line, then select Properties > Global Configuration Values.

   or

   To add a GCV to the driver set, right-clickthe driver set icon ![](../graphics/driver_set_icon_n.png), then click Properties > GCVs.
