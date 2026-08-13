# 5.2 The Connected System Schema File

The schema file on the connected system is used to specify the classes and attributes that are available. The schema file is located in the driver IFS path at schema/schema.def. If you installed the driver using the default driver IFS path, the schema file is /usr/local/i5osdrv/schema/schema.def.

The schema file is read by the driver shim when the Metadirectory engine requests it. This typically happens at driver startup. The schema file is also used by the Policy Editor to map the schema of the Identity Vault to the schema of the external application.

If you change the schema file, you must restart the driver shim and the driver.

The CL programs that are provided with the driver depend on the classes and attributes in the schema file that is provided with the driver.

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

You must specify a class name.

Add the CONTAINER keyword if objects of this class can contain other objects.

The class definition is ended by another class definition or by the end of the file.

### Attribute Definition

Any number of attribute definitions can follow a class definition. Attribute definitions define attributes for the class whose definition they follow.

```
ATTRIBUTE attributeName [TypeAndProperties]
```

An attribute name is required.

If no attribute type is specified, the attribute has the string type. The allowable types are

* STRING
* INTEGER
* STATE
* DN

The allowable attribute properties are

* REQUIRED
* NAMING
* MULTIVALUED
* CASESENSITIVE
* READONLY

## 5.2.2 Example Schema File

```
######################################################################
#  IBM i Driver Schema File
#
# Syntax:
#   SCHEMA [HIERARCHICAL]
#
#     HIERARCHICAL defines whether the schema has a hierarchy.
#                  Default is false.
#
#   CLASS <class-name> [CONTAINER]
#
#     CONTAINER defines whether the class is a container class.
#               Default is false.
#
#   ATTRIBUTE <attribute-name> [CASESENSITIVE] [MULTIVALUED] [NAMING]
#                              [READONLY] [REQUIRED] [STRING] [INTEGER]
#                              [STATE] [DN]
#
#     CASESENSITIVE defines this attribute to be case sensitive.
#                   Default is false.
#
#     MULTIVALUED defines this attribute to be multivalue.
#                 Default is false.
#
#     NAMING defines this attribute as the class naming attribute.
#            Default is false.
#
#     READONLY defines this attribute to be read-only.
#              Default is false.
#
#     REQUIRED defines this attribute to be required for class
#              definition.
#              Default is false.
#
#     STRING defines this attribute to be of type string.
#            String is the default type.
#
#     INTEGER defines this attribute to be of type integer.
#            String is the default type.
#
#     STATE defines this attribute to be of type Boolean (TRUE or
#           FALSE)
#            String is the default type.
#
#     DN defines this attribute to be a distinguished name
#       (referential)
#            String is the default type.
#
######################################################################

SCHEMA

  CLASS UserProfile

    ATTRIBUTE USRPRF NAMING REQUIRED  # User Profile Name
    ATTRIBUTE PASSWORD                #
    ATTRIBUTE PWDEXP                  # Password Expired *YES or *NO
    ATTRIBUTE STATUS                  # *ENABLED or #DISABLED
    ATTRIBUTE USRCLS                  # User Class
    ATTRIBUTE ASTLVL                  # Assistance Level
    ATTRIBUTE CURLIB                  # Current Library
    ATTRIBUTE INLPGM                  # Initial Program to Call
    ATTRIBUTE INLMNU                  # Initial Menu
    ATTRIBUTE LMTCPB                  # Limit Capabilities
    ATTRIBUTE TEXT                    # Text Description
    ATTRIBUTE SPCAUT                  # Special Authority
    ATTRIBUTE SPCENV                  # Special Environment
    ATTRIBUTE DSPSGNINF               # Display sign-on information
    ATTRIBUTE PWDEXPITV               # Password Expiration Interval
    ATTRIBUTE LMTDEVSSN               # Limit Device Sessions
    ATTRIBUTE KBDBUF                  # Keyboard Buffering
    ATTRIBUTE MAXSTG                  # Maximum Allowed Storage
    ATTRIBUTE PTYLMT                  # Highest Schedule Priority
    ATTRIBUTE JOBD                    # Job Description
    ATTRIBUTE GRPPRF                  # Group Profile
    ATTRIBUTE OWNER                   # Owner
    ATTRIBUTE GRPAUT                  # Group Authority
    ATTRIBUTE GRPAUTTYP               # Group Authority Type
    ATTRIBUTE SUPGRPPRF MULTIVALUED   # Supplemental Groups
    ATTRIBUTE ACGCDE                  # Accounting Code
    ATTRIBUTE MSGQ                    # Message Queue
    ATTRIBUTE DLVRY                   # Message Queue Delivery Method
    ATTRIBUTE SEV                     # Message Severity Code Filter
    ATTRIBUTE PRTDEV                  # Print Device
    ATTRIBUTE OUTQ                    # Output Queue
    ATTRIBUTE ATNPGM                  # Attention Program
    ATTRIBUTE SRTSEQ                  # Sort Sequence
    ATTRIBUTE LANGID                  # Language ID
    ATTRIBUTE CNTRYID                 # Country or Region ID
    ATTRIBUTE CCSID                   # Coded Character Set ID
    ATTRIBUTE CHRIDCTL                # Character Identifier Control
    ATTRIBUTE SETJOBATR               # Locale Job Attributes
    ATTRIBUTE LOCALE                  # Locale
    ATTRIBUTE USROPT                  # User Options
    ATTRIBUTE UID INTEGER             # User ID number
    ATTRIBUTE GID INTEGER             # Group ID number
    ATTRIBUTE HOMEDIR                 # Home Directory
    ATTRIBUTE GroupMembership MULTIVALUED # Virtual attr for GRPPRF &
                                          # SUPGRPPRF
# Distribution Directory Entry Attributes
    ATTRIBUTE USRID                   # User Identifier
    ATTRIBUTE USRD                    # User Description
    ATTRIBUTE USER                    # User Profile
    ATTRIBUTE SYSNAME                 # System Name
    ATTRIBUTE NETUSRID                # Network User ID
    ATTRIBUTE LSTNAM                  # Last Name
    ATTRIBUTE FSTNAM                  # First Name
    ATTRIBUTE MIDNAM                  # Middle Name
    ATTRIBUTE PREFNAM                 # Preferred Name
    ATTRIBUTE FULNAM                  # Full Name
    ATTRIBUTE DEPT                    # Department
    ATTRIBUTE TITLE                   # Job Title
    ATTRIBUTE CMPNY                   # Company
    ATTRIBUTE TELNBR1                 # Telephone Number 1
    ATTRIBUTE TELNBR2                 # Telephone Number 2
    ATTRIBUTE FAXTELNBR               # FAX Telephone Number
    ATTRIBUTE LOC                     # Location
    ATTRIBUTE BLDG                    # Building
    ATTRIBUTE OFC                     # Office
    ATTRIBUTE ADDR1                   # Address Line 1
    ATTRIBUTE ADDR2                   # Address Line 2
    ATTRIBUTE ADDR3                   # Address Line 3
    ATTRIBUTE ADDR4                   # Address Line 4
    ATTRIBUTE INDUSR                  # Indirect User
    ATTRIBUTE PRTPERS                 # Print Private Mail
    ATTRIBUTE PRTCOVER                # Print Cover Page
    ATTRIBUTE NFYMAIL                 # Mail Notification
    ATTRIBUTE NFYMSGS                 # Messages
    ATTRIBUTE TEXT                    # Text
    ATTRIBUTE CMDCHRID                # Command Character Identifier
    ATTRIBUTE COUNTRY                 # Country or Region ID
    ATTRIBUTE ADMD                    # Administration Domain
    ATTRIBUTE PRMD                    # Private Management Domain
    ATTRIBUTE SURNAM                  # Surname
    ATTRIBUTE GIVENNAM                # Given Name
    ATTRIBUTE INITIALS                # Initials
    ATTRIBUTE GENQUAL                 # Generational Qualifier
    ATTRIBUTE ORG                     # Organization
    ATTRIBUTE ORGUNIT MULTIVALUED     # Organizational Units
    ATTRIBUTE DMNDFNATR MULTIVALUED   # Domain-defined Attributes
    ATTRIBUTE USRDFNFLD MULTIVALUED   # User-defined Fields
    ATTRIBUTE MSFSRVLVL               # Mail Service Level
    ATTRIBUTE PREFADR                 # Preferred Address
    ATTRIBUTE CCMAILADR               # cc:Mail Address
    ATTRIBUTE CCMAILCMT               # cc:Mail Comment
    ATTRIBUTE ALWSYNC                 # Allow Synchronization
    ATTRIBUTE DLOOWN                  # DLO Owner

  CLASS GroupProfile

    ATTRIBUTE USRPRF NAMING REQUIRED  # User Profile Name
    ATTRIBUTE PWDEXP                  # Password Expired *YES or *NO
    ATTRIBUTE STATUS                  # *ENABLED or #DISABLED
    ATTRIBUTE USRCLS                  # User Class
    ATTRIBUTE ASTLVL                  # Assistance Level
    ATTRIBUTE CURLIB                  # Current Library
    ATTRIBUTE INLPGM                  # Initial Program to Call
    ATTRIBUTE INLMNU                  # Initial Menu
    ATTRIBUTE LMTCPB                  # Limit Capabilities
    ATTRIBUTE TEXT                    # Text Description
    ATTRIBUTE SPCAUT                  # Special Authority
    ATTRIBUTE SPCENV                  # Special Environment
    ATTRIBUTE DSPSGNINF               # Display sign-on information
    ATTRIBUTE PWDEXPITV               # Password Expiration Interval
    ATTRIBUTE LMTDEVSSN               # Limit Device Sessions
    ATTRIBUTE KBDBUF                  # Keyboard Buffering
    ATTRIBUTE MAXSTG                  # Maximum Allowed Storage
    ATTRIBUTE PTYLMT                  # Highest Schedule Priority
    ATTRIBUTE JOBD                    # Job Description
    ATTRIBUTE GRPPRF                  # Group Profile
    ATTRIBUTE OWNER                   # Owner
    ATTRIBUTE GRPAUT                  # Group Authority
    ATTRIBUTE GRPAUTTYP               # Gropu Authority Type
    ATTRIBUTE SUPGRPPRF MULTIVALUED   # Supplemental Groups
    ATTRIBUTE ACGCDE                  # Accounting Code
    ATTRIBUTE DOCPWD                  # Document Password
    ATTRIBUTE MSGQ                    # Message Queue
    ATTRIBUTE DLVRY                   # Delivery
    ATTRIBUTE SEV                     # Severity Code Filter
    ATTRIBUTE PRTDEV                  # Print Device
    ATTRIBUTE OUTQ                    # Output Queue
    ATTRIBUTE ATNPGM                  # Attention Program
    ATTRIBUTE SRTSEQ                  # Sort Sequence
    ATTRIBUTE LANGID                  # Language ID
    ATTRIBUTE CNTRYID                 # Country or Region ID
    ATTRIBUTE CCSID                   # Coded Character Set ID
    ATTRIBUTE CHRIDCTL                # Character Identifier Control
    ATTRIBUTE SETJOBATR               # Locale Job Attributes
    ATTRIBUTE LOCALE                  # Locale
    ATTRIBUTE USROPT                  # User Options
    ATTRIBUTE UID INTEGER             # User ID number
    ATTRIBUTE GID INTEGER             # Group ID number
    ATTRIBUTE HOMEDIR                 # Home Directory
    ATTRIBUTE EIMASSOC                # EIM Association
    ATTRIBUTE Members MULTIVALUED     # Virtual attribute that has
                                      # all members
```
