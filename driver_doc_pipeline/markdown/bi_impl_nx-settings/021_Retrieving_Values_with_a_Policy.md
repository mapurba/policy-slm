# B.3 Retrieving Values with a Policy

You can retrieve values with a policy by calling methods from the driver shim. The following example demonstrates retrieving values with XPath expressions:

```
<do-set-local-variable name="DriverDN">
  <arg-string>
    <token-text xml:space="preserve">\MYD1\mydriver\drivers\NxSettings</token-text>
  </arg-string>
</do-set-local-variable>
<do-set-local-variable name="driverShimInstance">
  <arg-object>
    <token-xpath expression="NxSettingsInstance:getInstance($DriverDN)"/>
  </arg-object>
</do-set-local-variable>
<do-set-local-variable name="uid">
  <arg-string>
    <token-xpath expression='driverShim:getNextRangeValue($driverShimInstance,"DefaultSet", "uid")'/>
  </arg-string>
</do-set-local-variable>
```

This works as follows:

1. Local variable “DriverDN” is set to the DN of the driver. This value is used to retrieve the correct instance of the driver shim from the Java\* virtual machine.
2. The static getInstance method is called on the driver shim to retrieve a handle to the shim object.
3. The getNextRangeValue method is called on the driver shim with the following arguments:

   | Argument | Description |
   | driverShimInstance | The handle to the shim |
   | setName | The name of the settings set to retrieve the range value from (defined by the value of the settings tag name attribute) |
   | SettingName | The name of the setting containing the range information to be used to assign an ID |
