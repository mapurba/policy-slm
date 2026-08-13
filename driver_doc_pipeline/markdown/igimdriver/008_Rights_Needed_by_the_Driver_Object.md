# 2.3 Rights Needed by the Driver Object

The driver must have appropriate rights to the Identity Vault objects that it reads or writes. You can ensure this by making the driver object security equivalent to another user object with those rights. Security Equivalence refers to an object being equivalent in rights to another object. This ensures that a client (for example, Identity Governance) accessing the driver’s REST APIs has the necessary access to report the changes.

The user object (trustee) that is security equivalent to the driver object must have the following minimum permissions:

* For reading changes on the Identity Vault objects, the trustee must have the following rights (inherited to the child objects) on the base container:

  + [All Attribute Rights] - Compare, Read
  + [Entry Rights] - Browse
* For the driver operations, the trustee must have the following rights on the driver object:

  + [All Attribute Rights] - Compare, Read, and Write
  + [Entry Rights] - Browse
  + DirXML-DriverFilter - Compare, Read, and Write
  + DirXML-AccessSubmitCommand - Compare, Read, and Write
  + DirXML-AccessRun - Read, Compare, and Write
  + DirXML-AccessConfigure - Read, and Compare
