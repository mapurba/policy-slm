# F.4 Multiple Addresses

If "multiple" is chosen a single GCV is exposed; "Provider Address Attribute" (pdsepicsdcfg.address.multiple.attr). Provide the attribute that contains the provider address(s) in this GCV. This attribute must be a multi-valued string attribute that contains the address in JSON format. Each value must be a JSON string containing the address information for a specific facility.

The format for the JSON string is as follows:

```
{
"addressID":"IDM-1",
"isPrimary":"1",
"active":"1",
"addr1":"123 Main St",
"addr2":"Suite 1",
"addr3":"Main Hospital",
"city":"Atlanta",
"state":"GA",
"zip":"12345",
"country":"USA",
"phone":"555.123.1234",
"fax":"555.321.4321",
"email":"name@hospital.com"
}
```

Within the JSON string the "addressID" element is mapped to the "Address External ID" (21200) in Epic. This value must be unique per address for each user. But the External ID may be re-used across multiple users.

*NOTE:*If the organization only has a single address, but it is stored in a single attribute in eDirectory, choose "Multiple" for the address type and ensure the attribute conforms to the JSON format as specified above.
