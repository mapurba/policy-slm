# 6.2 The Connected System Schema File

The schema file on the connected system is used to specify the classes and attributes that are available on the system.

The schema file is read by the driver shim when the Metadirectory engine requests it. This typically happens at driver startup. The schema file is also used by the Policy Editor to map the schema of the Identity Vault to the schema of the external application.

If you change the schema file, you must restart the driver shim and the driver.

The REXX execs that are provided with the driver depend on the classes and attributes in the schema file that is provided with the driver.

The connected system schema file must be a sequential file or a member of a partitioned data set. The SCHEMDEF DD statement in the driver shim started task JCL identifies the schema file. An example schema file with the required classes and attributes is provided in the driver samples library member SCHEMDEF.

* [Schema File Syntax](b3xxapt.html#b3zz1g1)
* [Example Schema File](b3xxapt.html#b3zyqih)

## 6.2.1 Schema File Syntax

Each line in the schema file represents an element and must begin with the element name: SCHEMA, CLASS, or ATTRIBUTE.

The first element of the schema file is the schema definition. The schema definition is followed by class definitions. Each class definition can contain attribute definitions.

Except for the values of class and attribute names, the contents of the schema file are case insensitive.

### Comments

Lines that begin with an octothorpe (#) are comments.

```
  # This is a comment.
```

### Schema Definition

The first line in the schema file that is not a comment must be the schema definition.

```
  SCHEMA [HIERARCHICAL]
```

HIERARCHICAL specifies that the target application is not a flat set of users and groups, but is organized by hierarchical components, such as a directory-based container object.

### Class Definition

```
  CLASS className [CONTAINER]
```

You must specify a class name. Enclose the class name in double quotes (") if it contains spaces. Add the CONTAINER keyword if objects of this class can contain other objects. End the class definition by another class definition or by the end of the file.

### Attribute Definition

Any number of attribute definitions can follow a class definition. Attribute definitions define attributes for the class whose definition they follow.

```
  ATTRIBUTE attributeName [TypeAndProperties]
```

An attribute name is required. Enclose the attribute name in double quotes (") if it contains spaces.

If no attribute type is specified, the default is string. Allowable types are:

* STRING
* INTEGER
* STATE
* DN

Allowable attribute properties are:

* REQUIRED
* NAMING
* MULTIVALUED
* CASESENSITIVE
* READONLY

## 6.2.2 Example Schema File

For a complete example connected system schema file, see the driver samples library member SCHEMDEF. An excerpt from that file follows.

```
  SCHEMA
    CLASS USER
      ATTRIBUTE DirXML-RACF-userid NAMING REQUIRED
      ATTRIBUTE DirXML-RACF-groups MULTIVALUED DN
      ATTRIBUTE DirXML-RACF-category MULTIVALUED
      ATTRIBUTE DirXML-RACF-adsp STATE
      . . .
    CLASS GROUP
      ATTRIBUTE DirXML-RACF-group NAMING REQUIRED
      ATTRIBUTE DirXML-RACF-data
      ATTRIBUTE DirXML-RACF-omvs-gid INTEGER
      . . .
```
