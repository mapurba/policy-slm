# 6.3 Security Considerations

The following considerations apply when you are using a Bidirectional eDirectory driver:

* The Bidirectional eDirectory driver requires appropriate read/write rights in the container on which it operates. The eDirectory servers where you install the driver must hold master or read/write replicas of the objects you want to be synchronized between eDirectory and Identity Vault. The following permissions are required for synchronizing changes with the connected system and the Identity Vault:

  + *Rights Required on the Connected System (eDirectory with change-log module):*
    For receiving events from the connected system, the driver’s Authentication DN must have the following rights to the base container of the connected system (eDirectory):

    - *Entry Rights:*
      Browse permission.
    - *Attributes Rights:*
      Read permission.
    - ACL: Supervisor

    For synchronizing changes to the connected system, ensure that the driver’s Authentication DN has the following rights to the base container of the connected system (eDirectory).

    - *Entry Rights:*
      The rights to create entries in the connected system.
    - *Attributes Rights:*
      The rights to modify the attributes in the connected system.
    - ACL: Supervisor

    For modifying the write-managed attributes, the driver’s Authentication DN must have the management rights on the objects whose DN is being modified.
  + *Rights Required on the Identity Vault:*
    To synchronize changes to the Identity Vault, ensure that the driver’s Security Equals DN has the following rights to the object container as well as the driver object in the Identity Vault:

    - *Entry Rights:*
      The rights to Browse, Create, Rename, and Delete entries in the Identity Vault.
    - *Attributes Rights:*
      The rights to Compare, Read, Write, and Modify attributes in the Identity Vault.

    For modifying the write-managed attributes, the driver’s Security Equals DN must have management rights on the objects whose DN is being modified.

    For receiving events from the Identity Vault, the driver’s Security Equals DN must have the following rights to the object container as well as the driver object in the Identity Vault.

    - *Entry Rights:*
      The rights to Browse, Create, Rename, and Delete entries in the Identity Vault.
    - *Attributes Rights:*
      The rights to Compare, Read, Write, and Modify attributes in the Identity Vault.
* The change-log file contains information about events on the connected eDirectory servers and passwords. It is encrypted, but it should be protected against access by unauthorized users. The change-log file is located in the DIB directory of eDirectory. The name of the change-log file is based on the GUID of the driver and has a .TAO extension. The change-log file can only be accessed by the owner of the eDirectory instance.
* Sensitive data like passwords and encrypted attributes is encrypted before writing it to the change-log cache file.
