# A.1 Attributes Not Added for New Users

If a user is added to the Identity Vault, but the driver does not add the attributes specified in the creation policy to the User object, ensure that the user meets the appropriate selection criteria.

* Use iManager to examine the driver’s GCVs under the Event Selection heading, and ensure that the user meets the driver’s event selection criteria.
* If the driver is configured to use Role-Based Entitlements, make sure that the user has the required entitlement.

  For details about using entitlements, see the Identity Manager 4.8 Administration Guide on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

You can obtain diagnostic information from a trace.

To obtain a driver trace of events related to adding a user:

1. Use iManager to navigate to the Driver Overview page.
2. Click the driver image to display the Driver Settings window.
3. Select Misc.

   With Internet Explorer, Misc is located under the Identity Manager tab.

   With other browsers, Misc is located in the drop-down menu at the top.
4. Set Trace Level to 10.
5. Run ndstrace to capture the trace information for the driver.

   Because a large volume of debug information is produced by the driver, we recommend that you record the trace to a file.
6. Add a user.

Trace messages pertaining to the NxSettings driver are preceded by a number and DVRS: NxSettings ST:. Search the trace, case insensitively, for the word error. If you find no errors, examine the Identity Vault to see if the driver set the attributes specified in the creation policy on the User object you added.

A null pointer exception from the Metadirectory engine can be caused by a problem with the NxSettings Stylesheet object’s contents or by a lack of free UIDs or GIDs available to be allocated. If you find a null pointer exception in the trace, search the trace for related status messages from the driver. For more information about status messages from the driver, see [Section C.0, Messages](b3fxjz5.html).
