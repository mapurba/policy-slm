# C.2 Customizing the Subscriber Channel

The following sections provide information about customizing the Subscriber channel to synchronize additional attributes from the different Oracle modules with which the drivers synchronize attributes.

* [Modifying the IDM\_DRIVER\_S PL/SQL Script](customizing-the-subscriber-channel.html#b1fx4oi7)
* [Verifying the Changes](customizing-the-subscriber-channel.html#b1fx4t31)

## C.2.1 Modifying the IDM\_DRIVER\_S PL/SQL Script

The Oracle EBS system provides many built-in APIs for making certain changes to the user or employee data. You can use the IDM\_DRIVER\_S PL/SQL package to make these changes on the Subscriber channel. This package uses some of the Oracle EBS built-in APIs.

[Table C-1](customizing-the-subscriber-channel.html#b1fx4pn5) lists the APIs used for each module.

*Table C-1* Oracle Module and EBS System APIs

| Oracle Modules | Oracle EBS System APIs |
| User Management | * fnd\_user\_pkg.createuser * fnd\_user\_pkg.updateuser |
| HR Implementation | * r\_employee\_api.create\_employee * hr\_person\_api.update\_person * hr\_person\_api.delete\_person |
| TCA | * hz\_party\_v2pub.create\_person * hz\_party\_v2pub.update\_person * hz\_contact\_point\_v2pub.create\_email\_contact\_point |

To understand which attributes are supported by these APIs, use the SQL Developer tool and connect to the database where Oracle EBS system is installed. The API information is stored under the Packages panel on the left side of the screen. To view the APIs, expand the Packages panel.

*NOTE:*Currently, the query operations are supported on the FND\_USER, PER\_ALL\_PEOPLE\_F, and HZ\_PARTIES tables.

[Table C-2](customizing-the-subscriber-channel.html#b1fx4rj4) lists the Identity Manager Schema attributes.

*Table C-2* Schema Attributes

| Condition | Action |
| Condition 1:The attribute is supported by one of the Oracle EBS system APIs and belongs to one of the FND\_USER, PER\_ALL\_PEOPLE\_F, or HZ\_PARTIES tables. | There is no change required in the PL/SQL script. You can directly add the attribute to the driver schema and filter for extending it. |
| Condition 2:The attribute is supported by one of the Oracle EBS system APIs but does not belong to any of the FND\_USER, PER\_ALL\_PEOPLE\_F, or HZ\_PARTIES tables. | Modify the query in the IDM\_DRIVER\_S package to specify the appropriate table name in the IF condition that starts with IF EVENT\_NAME = TO\_CHAR('oracle.apps.fnd.user.search') THEN statement. |
| Condition 3:The attribute is not supported by any of the Oracle EBS system APIs but belongs to one of the FND\_USER, PER\_ALL\_PEOPLE\_F, or HZ\_PARTIES tables. | Determine which Oracle EBS system API is required to find the attribute, then add that API to the IDM\_DRIVER\_S PL/SQL package. You can use the EMPLOYEE\_OPERATION and EXECUTE\_EMPLOYEE\_API functions as examples in the IDM\_DRIVER\_S package. |
| Condition 4:The attribute is neither supported by the Oracle EBS system APIs nor belongs to the FND\_USER, PER\_ALL\_PEOPLE\_F, or HZ\_PARTIES tables. | Make changes as instructed for condition 2 and 3. A new Oracle EBS system API is needed to find the attribute and then modify the query to include it in the new table. |

*IMPORTANT:*Restart the driver after making the required changes.

## C.2.2 Verifying the Changes

1. Create a user in the Identity Vault with the recently added attributes and verify that the newly added attributes are synchronized to the EBS.
2. Perform a query operation for the recently added attributes and verify the response.

*Example C-3*  XML Code for the Subscriber Changes

```
<EBS_EVENT>
               <EVENT_NAME>oracle.apps.fnd.user.insert</EVENT_NAME>
               <DRIVER_TYPE>UM</DRIVER_TYPE>
               <OBJECT TYPE="USER">
                  <x_user_name>IDM_TEST_SUB_996111</x_user_name>
                  <x_description>IDM_TEST_SUB_998</x_description>
                  <x_email_address>IDM_TEST_SUB_998@test.com</x_email_address>
                  <x_fax>19999989</x_fax>
               </OBJECT>
            </EBS_EVENT>
```
