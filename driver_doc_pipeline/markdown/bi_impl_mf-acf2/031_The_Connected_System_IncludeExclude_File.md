# 6.3 The Connected System Include/Exclude File

You can use an optional include/exclude file on the connected system to control which identities are or are not synchronized from the Identity Vault to the connected system.

To control which objects are synchronized from the connected system to the Identity Vault, use policies. For details about customizing policies, see the [Identity Manager 4.8 Documentation Web site](https://www.netiq.com/documentation/identity-manager-47/).

The connected system include/exclude file must be a sequential file or a member of a partitioned data set. The INCEXC DD statement in the driver shim started task JCL identifies the include/exclude file. An example include/exclude file that excludes many common z/OS users, such as JES, OMVS, and INIT, is provided in the driver samples library member INCEXC.

The file is read when the driver shim starts. If you make changes to it, you must restart the driver shim.

The include/exclude file can contain rules for both including and excluding accounts. To ensure optimal performance, each include/exclude file should contain no more than 50 entries total.

You can use the include/exclude file to phase in your deployment of the driver, excluding most users at first, and then adding more as you gain confidence and experience.

* [Include/Exclude Processing](b3xxit1.html#b3zz6ui)
* [Include/Exclude File Syntax](b3xxit1.html#b3zz851)
* [Example Include/Exclude Files](b3xxit1.html#b3zz8n9)

## 6.3.1 Include/Exclude Processing

Identity Vault events for identities that match an exclude rule are discarded by the Subscriber shim.

Included identities are treated normally by the Subscriber shim.

Identities that do not match an include rule or an exclude rule in the file are included.

Identities are matched in the following priority:

1. Exclude rules
2. Include rules

Within each level of this matching priority, identities are matched against rules in the order that the rules appear in the file. The first rule that matches determines whether the identity is included or excluded.

## 6.3.2 Include/Exclude File Syntax

Except for class names, attribute names, and the values to match, the contents of the include/exclude file are case insensitive.

The Subscriber Creation policy converts object names to uppercase. Use uppercase names in the include/exclude file to match identities.

The include/exclude file can contain any number of include sections, exclude sections, and single-line rules.

Include sections and exclude sections can contain class matching rules, and class matching rules can contain attribute matching rules. Include sections and exclude sections can also contain association matching rules.

Class and attribute names used in the include/exclude file must correspond to the names specified in the schema file. For details about the schema file, see [The Connected System Schema File](b3xxapt.html).

### Comments

Lines that begin with an octothorpe (#) are comments.

```
  # This is a comment.
```

### Include and Exclude Sections

Include and exclude sections provide rules to specify which objects are to be included or excluded from synchronization.

An include section begins with an INCLUDE line and ends with an ENDINCLUDE line.

```
  INCLUDE
    .
    .
    .
  ENDINCLUDE
```

An exclude section begins with an EXCLUDE line and ends with an ENDEXCLUDE line.

```
  EXCLUDE
    .
    .
    .
  ENDEXCLUDE
```

You can use class matching rules and association matching rules within an include section and an exclude section.

#### Class Matching Rules

Use a class matching rule within an include section or an exclude section to specify the name of a class of objects to include or exclude.

A class matching rule is defined by a class line that specifies the name of the class and ends with an ENDCLASS line.

```
  CLASS className
    .
    .
    .
  ENDCLASS
```

You can use attribute matching rules within a class matching rule.

#### Attribute Matching Rules

You can use attribute matching rules within a class matching rule to limit the objects that are included or excluded. If no attribute matching rules are specified for a class, all objects of the specified class are included or excluded.

An attribute matching rule comprises an attribute name, an equals sign (=), and an expression. The expression can be an exact value, or it can use limited regular expressions. For details about limited regular expressions, see [Limited Regular Expressions](b3xxit1.html#b4a9yip).

```
  attributeName=expression
```

Multiple attribute matching rules can be specified for a given class.

Attribute matching rules within a class matching rule are logically ANDed together. To logically OR attribute matching rules for a class, specify multiple class matching rules. For example, the following include/exclude file excludes both user01 and user02:

```
  # Exclude the User object if its ACF2 LID is USER01 or USER02.
  EXCLUDE
  CLASS Logonid
      LID=USER01
  ENDCLASS
  CLASS Logonid
      LID=USER02
  ENDCLASS
  ENDEXCLUDE
```

#### Association Matching Rules

You can specify association matching rules in an include or exclude section. Association matching rule expressions can specify an exact association or a limited regular expression. For details about limited regular expressions, see [Limited Regular Expressions](b3xxit1.html#b4a9yip).

By default, an association is the ACF2 user ID. Association formation can be customized in the Subscriber REXX execs.

For example, to exclude the root user, specify

```
  EXCLUDE
    ACFUSER
  ENDEXCLUDE
```

#### Special Considerations

Using the Include/Exclude rules can be a convenient way to control processing decisions from the ACF2 administration point. They can quickly filter events before they reach the Identity Manager Metadirectory engine, thus saving time and resources. However, it is not recommended that you use the Include/Exclude rules for processing if you plan to create more than 50 rules. Each rule adds additional complexity that the driver shim must process for every event.

### Single-Line Rules

```
  INCLUDE|EXCLUDE [className] objectSelection
```

Where objectSelection can be

```
  {associationMatch | attributeName=expression}
```

You must specify whether the rule is to include or exclude the objects it matches.

You can specify a class name to limit matches to only objects of that class.

You must specify either an association or an attribute matching expression. The syntax of the association and attribute matching expression is the same as that of association matching rules and attribute matching rules previously described. For details, see [Association Matching Rules](b3xxit1.html#b40z0hu) and [Attribute Matching Rules](b3xxit1.html#b40z0ba).

For example, to ignore events from the Admin user in the Identity Vault:

```
  # Do not subscribe to events for the Admin user.
  EXCLUDE ADMIN
```

### Limited Regular Expressions

A limited regular expression is a pattern used to match a string of characters.

Character matching is case sensitive.

Any literal character matches that character.

A period (.) matches any single character.

A bracket expression is a set of characters enclosed by left ([) and right (]) brackets that matches any listed character. Within a bracket expression, a range expression is a pair of characters separated by a hyphen, and is equivalent to listing all of the characters that sort between the given characters. For example, [0-9] matches any single digit.

An asterisk (\*) indicates that the preceding item is matched zero or more times.

A plus sign (+) indicates that the preceding item is matched one or more times.

A question mark (?) indicates that the preceding item is matched zero or one times.

You can use parentheses to group multiple expressions into a single item. For example, (abc)+ matches abc, abcabc, abcabcabc, etc. Nesting of parentheses is not supported.

## 6.3.3 Example Include/Exclude Files

*Example 6-1* Example 1

```
  # Exclude users whose names start with TEMP
  EXCLUDE
      CLASS Logonid
          LID=TEMP.*
      ENDCLASS
  ENDEXCLUDE
```

*Example 6-2* Example 2

```
  # Exclude USERA and USERB
  # Because attribute rules are ANDed, these must be in separate
  # CLASS sections.
  EXCLUDE
      CLASS Logonid
          LID=USERA
      ENDCLASS
      CLASS Logonid
          LID=USERB
      ENDCLASS
  ENDEXCLUDE
```
