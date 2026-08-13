# 6.4 Managing Additional Attributes

You can add additional attributes to the driver for both the Publisher and Subscriber channels. These attributes can be accessed by the REXX execs for all event types.

To publish or subscribe to additional attributes, you must add them to the filter and add support for them into the REXX execs.

* [Modifying the Filter](b3xywb2.html#b45fdpp)

## 6.4.1 Modifying the Filter

1. On the iManager Driver Overview page for the driver, click the Filter icon on either the Publisher or Subscriber channel. It is the same object.
2. In the Filter Edit dialog box, click the class containing the attribute to be added.
3. Click Add Attribute, then select the attribute from the list.
4. Select the flow of this attribute for the Publisher and Subscriber channels.

   * *Synchronize:*
     Changes to this object are reported and automatically synchronized.
   * *Ignore:*
     Changes to this object are not reported and not automatically synchronized.
   * *Notify:*
     Changes to this object are reported, but not automatically synchronized.
   * *Reset:*
     Resets the object value to the value specified by the opposite channel. (You can set this value on either the Publisher or Subscriber channel, but not both.)
5. Click Apply.

If you want to map this attribute to an existing attribute in the connected system schema file, modify the Schema Mapping policy for the driver.

For complete details about managing filters and Schema Mapping policies, see the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).
