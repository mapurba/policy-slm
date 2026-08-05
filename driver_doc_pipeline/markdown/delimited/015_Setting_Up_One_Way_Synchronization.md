# 5.0 Setting Up One-Way Synchronization

If your data synchronization goes only one way, you need to disable the channel that you don’t use. To disable one of the channels, clear the filters on the channel you don’t need and remove the path for the input or output directory, depending on the channel.

For example, if you only need a Publisher channel:

1. In the Filter editor in Identity Console, clear the filters on the Subscriber channel.

   1. For example, select the User class.

      ![](../graphics/idconsole_filter.png)
   2. Select Ignore in the Subscribe section.

      The Subscriber channel icon for the User class changes to show that the class is no longer being synchronized.

      ![](../graphics/idconsole_filter_sub_ignore.png)
2. Click Save to save the changes.
3. Edit the driver properties to remove the path specified for the Output File Path. This setting is located under the Subscriber Settings for the Driver Parameters on the Configuration tab. For details, see [Driver Parameters](driver-configuration.html#b94psi3).

   ![](../graphics/idconsole_subcriber_settings.png)

If you only need a Subscriber channel, clear the filters on the Publisher object and remove the path specified for the Input File Path in the Driver Parameters section.
