# 6.4 Managing Additional Attributes

You can add additional attributes to the driver for both the Publisher and Subscriber channels. These attributes can be accessed by the scripts for all event types.

To publish or subscribe to additional attributes, you must add them to the filter and add support for them into the scripts.

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

If you want to map this attribute to an existing attribute in the Linux and UNIX schema, modify the Schema Mapping policy for the driver.

For complete details about managing filters and Schema Mapping policies, see the policy documentation on the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

## 6.4.2 Modifying the Scripts for New Attributes

In the Subscriber channel, a specific shell script is called to take the appropriate action for each type of event. If the additional attribute is required for adds and modifies of users, modify add-user.sh and modify-user.sh to process the additional attribute.

Publishing additional attributes requires that you act on changes made in the Linux or UNIX source application.
