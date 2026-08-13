# 2.2 Rights Needed by the Driver Object (for 1.1.0.0100 and later)

The driver must have appropriate rights to the Identity Vault objects that it reads or writes. IGIM driver authorizes the user specified in the REST API User field. It allows only that user to call the APIs using valid credentials. The Rest API User has the privileges to access Rest endpoints of eDirectory. This ensures that a client (for example, Identity Governance) accessing the driver’s REST APIs has the necessary access to report the changes.

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
