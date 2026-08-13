# 5.2 Modifying Default Settings in Policies and the Filter

You set defaults for policies and filters when you import the driver configuration. If you want to change the default behavior of the driver, NetIQ recommends that you make modifications in this order:

1. Modify the driver filter to include additional attributes to be synchronized. See [Modifying the Driver Filter](modify-default-settings-policies-filter.html#adhymal) for more information.
2. Modify the Schema Mapping policy to include all attributes to be synchronized. See [Adding Entries to the Schema Mapping Policy](modify-default-settings-policies-filter.html#adhys1u) for more information.
3. Modify the Subscriber Create policy. See [Modifying the Create Policy](modify-default-settings-policies-filter.html#adi0o9o) for more information.
4. Modify the Subscriber Placement policy. See [Modifying Policies](modify-policies.html).

*IMPORTANT:*Ensure that you set the GroupWise attributes by using the do-add-dest-attr-value action instead of do-set-dest-attr-value action. An exception occurs if you set the attributes by using the do-set-dest-attr-value action. [Creating a Gateway Alias](modify-policies.html#agg2agx) provides an example code using this action.

## 5.2.1 Modifying the Driver Filter

The driver filter contains the Identity Vault classes and attributes for the Publisher and Subscriber channels. The purpose of the filter is to define how attributes are shared between systems.

If you add classes or attributes to the filter, you must append the merge-authority="edir" string to the added attribute in the Filter.

For example:

```
<filter-attr attr-name="Description" merge-authority="edir" publisher="ignore" subscriber="sync"/>
```

## 5.2.2 Adding Entries to the Schema Mapping Policy

The Schema Mapping policy is contained in the driver object and applies to both the Subscriber and Publisher channel. The purpose of the Schema Mapping policy is to map schema names (particularly attribute names and class names) between the Identity Vault namespace and the GroupWise namespace. Do not modify or remove existing entries in the Schema Mapping policy. You can, however, add entries to the Schema Mapping policy.

## 5.2.3 Modifying the Create Policy

You modify the Create policy to implement your specific business rules. The Create policy determines whether or not a GroupWise account is created. A Create policy also can perform other modifications to the Add event, such as providing default values for attributes.

In the driver configuration, the Create policy specifies two required attributes: CN and Surname for a User object and CN for a Group object.

## 5.2.4 Modifying the Matching Policy

Matching policies define the minimum criteria that two objects must meet to be considered the same.
