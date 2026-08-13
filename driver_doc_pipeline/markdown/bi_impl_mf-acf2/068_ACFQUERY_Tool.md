# C.2 ACFQUERY Tool

The driver query processor uses the ACF2 API to retrieve information from the security system. Queries are used by the Metadirectory engine for matching and merging. The TSO command, ACFQUERY, is used to extract information from the ACF2 database. ACFQUERY has the following format for read operations:

```
  ACFQUERY SCOPE(entry) CLASS(class) ASSOCIATION(association)
    [READATTRS(attrs...)|ALLREADATTRS] [PRINT]
```

The SCOPE tells ACFQUERY that information about a specific profile is being requested. The CLASS operand should always be set 'Logonid'. The ASSOCIATION operand specifies the association of the object to read. For Logonid profiles, simply use the LID field for association values. READATTRS operand specifies a list of attributes to return; optionally, you may specify ALLREADATTRS instead to return everything. The PRINT operand instructs ACFQUERY to print the results to the display. The output is a series of lines, each with a name=value pair. These pairs are interpreted by the driver shim to create an appropriate XDS document that the engine can use for processing. For example:

```
  ACFQUERY SCOPE(entry) CLASS(Logonid) ASSOCIATION(IBMUSER)
     READATTRS(ACCOUNT)PRINT
```

```
  COMMAND=instance
  CLASS_NAME=Logonid
  ASSOCIATION=IBMUSER
  ATTR_ACCOUNT=true
  COMMAND=status
  STATUS_LEVEL=success
```

For search operations, a search criteria is specified:

```
  ACFQUERY SCOPE(subtree) SEARCHCLASSES(classes..) SEARCHATTRS('attr=value' ...)
    [READATTRS(attrs...)|ALLREADATTRS] [PRINT]
```

The subtree SCOPE tells ACFQUERY that information about a specific profile is being requested. The SEARCHCLASSES operand lists the class(es) of interest. The SEARCHATTRS provides a list of values and attributes to search on. For example:

```
  ACFQUERY SCOPE(subtree) SEARCHCLASSES(Logonid)
    SEARCHATTRS('ACCOUNT=true') PRINT

  COMMAND=instance
  CLASS-NAME=Logonid
  ASSOCIATION=ASCH
  COMMAND=instance
  CLASS_NAME=Logonid
  ASSOCIATION=CICSA
  COMMAND=instance
  CLASS_NAME=Logonid
  ASSOCIATION=CICSTART
  COMMAND=status
  STATUS_LEVEL=success
```

You will notice that there are multiple results returned. Search operations may return zero or more responses.
