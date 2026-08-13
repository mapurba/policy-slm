# C.0 IDV Schema Extension

As part of solution, we need to extend the schema of eDirectory so that the Workday driver can create these additional objects in the IDV. The proposed schema extension in ldif and sch formats are available for download. The following classes are added in IDV.

* Auxiliary Class for User: wd-User

  The schema file should only be extended with the ndssch utility. Using any other method for importing the schema file fails for certain attributes. A sample syntax for importing the schema file has been provided below:

  ```
  /opt/novell/eDirectory/bin/ndssch -h idv.server.DNS.name -F /tmp/wd-schema.log admin.services.data /tmp/wd-schema.sch
  ```
* Effective Class for Relation Objects: wd-Relation
* Effective Class for Job Family Objects: wd-Jobfamily
* Effective Class for Job Profile Objects: wd-Jobprofile
* Effective Class for Location Objects: wd-Location
* Effective Class for Organization Objects: wd-Organization
* Effective Class for Photo Objects: wd-Photo
* Effective Class for Retry Settings: DirXML-WDSyncAttr
