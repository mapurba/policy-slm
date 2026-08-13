# 5.2 The Connected System Schema File

The schema.def file on the connected system is stored in the schema directory under the driver installation directory. It is used to specify the classes and attributes that are available on the system.

The schema file is read by the driver shim when the Metadirectory engine requests it. This typically happens at driver startup. The schema file is also used by the Policy Editor to map the schema of the Identity Vault to the schema of the external application.

If you change the schema file, you must restart the driver shim and the driver.

The scripts written for the driver depend on the classes and attributes in the schema file.

## 5.2.1 Schema File Syntax

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

You must specify a class name. Enclose the class name in double quotes (").

Add the CONTAINER keyword if objects of this class can contain other objects.

The class definition is ended by another class definition or by the end of the file.

### Attribute Definition

Any number of attribute definitions can follow a class definition. Attribute definitions define attributes for the class whose definition they follow.

```
ATTRIBUTE attributeName [TypeAndProperties]
```

An attribute name is required. Enclose the attribute name in double quotes (").

If no attribute type is specified, the attribute has the string type. The allowable types are:

* STRING
* INTEGER
* STATE
* DN

The allowable attribute properties are:

* REQUIRED
* NAMING
* MULTIVALUED
* CASESENSITIVE
* READONLY

### Example Schema File

```
SCHEMA HIERARCHICAL
   CLASS "User"
      ATTRIBUTE "cn" NAMING REQUIRED
      ATTRIBUTE "Group Membership" MULTIVALUED DN
   CLASS "Group"
      ATTRIBUTE "cn" NAMING REQUIRED
      ATTRIBUTE "Group Members" MULTIVALUED DN
```
