# A.2 Limitations

* The Managed System Entitlement and Account Summary report displays inaccurate data for the following two components:

  + Number of Logical Systems
  + Account Entitlement Number of Assigned Accounts

  For example, if there are ‘n’ number of Logical Systems, the report displays ‘n+1’ number of Logical Systems. If there are ‘n’ Account tracking identifiers and ‘m’ Accounts, the report displays ‘m\*n’ Accounts.
* The driver displays User is unassociated exception while performing modify and delete operations with only dest-dn because these operations are not supported without providing user association.
