# C.2 SAFQUERY Tool

The driver query processor uses the system authorization facility (SAF) to retrieve information from the security system. Queries are used by the Metadirectory engine for matching and merging. The TSO command, SAFQUERY, is used to extract information from the RACF database. SAFQUERY has the following format for read operations:

```
  SAFQUERY SCOPE(entry) CLASS(class) ASSOCIATION(association)
    [READATTRS(attrs...)|ALLREADATTRS] [PRINT]
```

The SCOPE tells SAFQUERY that information about a specific profile is being requested. The CLASS operand specifies whether it’s a User or Group profile. The ASSOCIATION operand specifies the association of the object to read. It must have the format USER\userid or GROUP\groupname. The TEADATTRS operand specifies a list of attributes to return; optionally, you may specify ALLREADATTRS instead to return everything. The PRINT operand instructs SAFQUERY to print the results to the display. The output is a series of lines, each with a name=value pair. These pairs are interpreted by the driver shim to create an appropriate XDS document that the engine can use for processing. For example:

```
  SAFQUERY SCOPE(ENTRY) CLASS(User) ASSOCIATION(USER\IBMUSER)
    READATTRS(DirXML-RACF-special) PRINT

  COMMAND=instance
  CLASS_NAME=USER
  EVENT_ID=?
  ASSOCIATION=USER\IBMUSER
  ATTR_DirXML-RACF-special=true
  COMMAND=status
  STATUS_LEVEL=success
```

For search operations, a search criteria is specified:

```
  SAFQUERY SCOPE(subtree) SEARCHCLASSES(classes..) SEARCHATTRS('attr=value' ...)
    [READATTRS(attrs...)|ALLREADATTRS] [PRINT]
```

The subtree SCOPE tells SAFQUERY that information about a specific profile is being requested. The SEARCHCLASSES operand lists the class(es) of interest. The SEARCHATTRS provides a list of values and attributes to search on. For example:

```
  SAFQUERY SCOPE(subtree) SEARCHCLASSES(User)
    SEARCHATTRS('DirXML-RACF-revoke=true') PRINT

  COMMAND=instance
  CLASS-NAME=USER
  EVENT_ID=?
  ASSOCIATION=USER\ASCH
  COMMAND=instance
  CLASS_NAME=USER
  EVENT_ID=?
  ASSOCIATION=USER\CICSA
  COMMAND=instance
  CLASS_NAME=USER
  EVENT_ID=?
  ASSOCIATION=USER\CICSTART
  COMMAND=status
  STATUS_LEVEL=success
```

You will notice that there are multiple results returned. Search operations may return zero or more responses.
