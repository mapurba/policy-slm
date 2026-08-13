# A.2 Core Driver Indexes

eDirectory uses indexes to optimize attribute location. Installation of the Fan-Out Driver includes creation of additional indexes for specific attributes of the objects added to the Identity Vault. [Table A-1](blxyqwd.html#blxzg36) provides a list of these custom indexes.

*Table A-1* List of Indexes added to eDirectory for Fan-Out Driver

| Index Name | Attribute Name | Type |
| ASAM\_aliases | ASAM-aliases | Value |
| ASAM\_deletePendingsUpTo | ASAM-deletePendingsUpTo | Value |
| ASAM\_deletesUpTo | ASAM-deletesUpTo | Value |
| ASAM\_eGroupMembers | ASAM-eGroupMembers | Value |
| ASAM\_eGroupMembership | ASAM-eGroupMembership | Value |
| ASAM\_eventsUpTo | ASAM-eventsUpTo | Value |
| ASAM\_inputGUID | ASAM-inputGUID | Value |
| ASAM\_inputReference | ASAM-inputReference | Value |
| ASAM-NetAddressList | ASAM-NetAddressList | Value |
| ASAM\_passwordsUpTo | ASAM-passwordsUpTo | Value |
| ASAM\_platformAssociation | ASAM-platformAssociation | Value |
| Country | c | Value |
| GUID | GUID | Value |
| Locality | l | Value |
| Object\_Class | objectClass | Value |
| Organization | Organization | Value |
| ou | ou | Value |
| State | s | Value |
| Tree\_Root | t | Value |

Depending on the size of the existing tree in your Identity Vault, these indexes can take some time to install and bring online. Before you begin your first Trawl, verify that the indexes are in the online state.

To view the Server object indexes and their state:

1. In iManager, select eDirectory Maintenance > Index Management.
2. Select the Server object for the Core Driver.
