# 1.1 Supported Operations

* Add Operations

  + Add operations are supported for both EMP and SER records
* Modify Operations

  + Add Value is supported for both EMP and SER records
  + Remove Value is supported for EMP records
  + Remove All Values is supported for both EMP and SER records
* Delete Operations

  + Delete operations are supported for EMP records, but severely discouraged by Epic
* Rename Operations

  + Rename operations are not supported by Epic
* Move Operations

  + Move operations are not supported by Epic
* Query Operations

  + The following query operations and classes are supported:

    - EMP class

      * Supports SystemLoginID, InternalID, ExternalID, and CID
    - SER class

      * Supports Identifier attribute with the format “userIDType|userID”
    - Configured entitlement classes

      * Only supported for Code Map Refresh events
      * Query executes against configured CSV files
  + <query-ex> operations are not supported by Epic
* Modify Password Operations

  + Modify Password operations are supported for EMP records
* Check Object Password Operations

  + Check Object Password Operations are not supported by Epic
* External Identifiers and Passwords

  + External Identifiers and External Passwords are supported
