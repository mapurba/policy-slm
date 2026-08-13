# 3.5 Location Attribute

The user attribute Location exposes and processes a structured value representing a set of location values which are part of the user information available in the Google user object. Google exposes the following Location data elements. (Taken from Google API documentation – <https://developers.google.com/admin-sdk/directory/v1/reference/users>)

*Table 3-4* Location Attribute Data Elements

| Data Element | Description |
| area | Textual location. This is most useful for display purposes to concisely describe the location. For example, "Mountain View, CA" or "Near Seattle." |
| buildingId | Building identifier |
| deskCode | Most specific textual code of individual desk location |
| floorName | Floor name/number |
| floorSection | Floor section. More specific location within the floor. For example, if a floor is divided into sections "A," "B," and "C," this field would identify one of those values. |

These data elements are collected into a group identified with a “type.” There are three acceptable values for type:

* desk
* default
* custom

If custom is chosen, then an additional element customType is needed.

The connector supports one instance of each type or custom/customType combination. Any added values of type “desk,” for example, will replace any existing “desk” location sets. Any removed values for type “desk” will remove any “desk” location set values. The pair of type “custom” and the value of customType will uniquely identify one element.

Location is supported via a structured attribute with these components:

* type

  + Must be desk, default, or custom
  + If set to “custom”, the component customType becomes mandatory.
* customType

  + Mandatory if type is custom
  + Ignored if type is not custom
* area

  + Optional, string
* buildingId

  + Optional, string
  + The value MUST resolve to a building resource which exists in the domain\*
* deskCode

  + Optional, string
* floorName

  + Optional, string
* floorSection

  + Optional, string

*NOTE:*Building ID values will be rejected by the API stack if they do not refer to a building resource within the Google domain. This is done through the Google Admin interface. For more information, see: <https://support.google.com/a/answer/1033925?hl=en&ref_topic=1034362>

## 3.5.1 Examples

### Add Value

```

<modify-attr attr-name="Location">
 <add-value>
 <value type="structured">
 <component name="type">default</component>
 <component name="customType"/>
 <component name="area">MyArea</component>
 <component name="buildingId"/>
 <component name="deskCode">Desk1121</component>
 <component name="floorName">1st Floor</component>
 <component name="floorSection"/>
 </value>
 </add-value>
</modify-attr>
```

### Remove Value

```

<modify-attr attr-name="Location">
 <remove-value>
 <value type="structured">
 <component name="type">default</component>
 </value>
 </remove-value>
</modify-attr>
```

On remove value elements, only type and, if needed, customType, are examined. All other components are ignored.
