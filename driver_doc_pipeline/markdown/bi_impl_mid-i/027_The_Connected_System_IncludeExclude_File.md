# 5.3 The Connected System Include/Exclude File

You can use an optional include/exclude file on the connected system to control which identities are or are not synchronized between the Identity Vault and the connected system. The include/exclude file is located in the driver IFS path at conf/include-exclude.conf. If you installed the driver using the default driver IFS path, the include/exclude file is /usr/local/i5osdrv/conf/include-exclude.conf.

The file is read when the driver shim starts. If you make changes to it, you must restart the driver shim.

The include/exclude file can contain include rules and exclude rules. To ensure optimal performance, each include/exclude file should contain no more than 50 entries total.

A default file that excludes many common i5/OS user IDs and groups, such as QSECOFR, is created by the installation process.

You can use the include/exclude file to phase in your deployment of the IBM i driver, excluding most users and groups at first, and then adding more as you gain confidence and experience.

* [Include/Exclude Processing](b3xxit1.html#b3zz6ui)
* [Include/Exclude File Syntax](b3xxit1.html#b3zz851)
* [Example Include/Exclude Files](b3xxit1.html#b3zz8n9)

## 5.3.1 Include/Exclude Processing

Identity Vault events for identities that match an exclude rule are discarded by the Subscriber shim. Local events for identities that match an exclude rule are not sent to the Metadirectory engine by the Publisher shim.

Included identities are treated normally by the Subscriber and Publisher shims.

Identities that do not match an include rule or an exclude rule in the file are included.

Identities are matched in the following priority:

1. Channel-specific (Publisher or Subscriber) exclude rules
2. Channel-specific include rules
3. General exclude rules
4. General include rules

Within each level of this matching priority, identities are matched against rules in the order that the rules appear in the file. The first rule that matches determines whether the identity is included or excluded.

## 5.3.2 Include/Exclude File Syntax

Except for class names, attribute names, and the values to match, the contents of the include/exclude file are case insensitive.

The include/exclude file can contain any number of include sections, exclude sections, and single-line rules.

Include sections and exclude sections can contain class matching rules, and class matching rules can contain attribute matching rules. Include sections and exclude sections can also contain association matching rules.

Include and exclude sections can be contained in subscriber and publisher sections to limit their scope to the specified channel.

Class and attribute names used in the include/exclude file must correspond to the names specified in the schema file. For details about the schema file, see [The Connected System Schema File](b3xxapt.html).

### Comments

Lines that begin with an octothorpe (#) are comments.

```
# This is a comment.
```

### Subscriber and Publisher Sections

Subscriber and publisher sections limit the include and exclude sections they contain to the specified channel.

A subscriber section begins with a subscriber line and ends with an endsubscriber line.

```
SUBSCRIBER
  .
  .
  .
ENDSUBSCRIBER
```

A publisher section begins with a publisher line and ends with an endpublisher line.

```
PUBLISHER
  .
  .
  .
ENDPUBLISHER
```

Each subscriber and publisher section can contain include and exclude sections.

### Include and Exclude Sections

Include and exclude sections provide rules to specify which objects are to be included or excluded from synchronization.

An include section begins with an include line and ends with an endinclude line.

```
INCLUDE
  .
  .
  .
ENDINCLUDE
```

An exclude section begins with an exclude line and ends with an endexclude line.

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

A class matching rule is defined by a class line that specifies the name of the class and ends with an endclass line.

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
# Exclude the User object if its USRPRF is USER01 or USER02.
EXCLUDE
CLASS UserProfile
    USRPRF=USER01
ENDCLASS
CLASS UserProfile
    USRPRF=USER02
ENDCLASS
ENDEXCLUDE
```

#### Association Matching Rules

You can specify association matching rules in an include or exclude section. Association matching rule expressions can specify an exact association or a limited regular expression. For details about limited regular expressions, see [Limited Regular Expressions](b3xxit1.html#b4a9yip).

By default, an association is defined as the profile name. Association formation can be customized in the Subscriber CL programs.

For example, to exclude the QSECOFR user, specify

```
EXCLUDE
  QSECOFR
ENDEXCLUDE
```

### Single-Line Rules

```
[SUBSCRIBER|PUBLISHER] INCLUDE|EXCLUDE [className] objectSelection
```

Where objectSelection can be

```
{associationMatch | attributeName=expression}
```

Single-line rules can specify the Subscriber or Publisher channel at the start of the rule. If a channel is specified, the rule applies only to that channel. Otherwise it applies to both channels.

You must specify whether the rule is to include or exclude the objects it matches.

You can specify a class name to limit matches to only objects of that class.

You must specify either an association or an attribute matching expression. The syntax of the association and attribute matching expression is the same as that of association matching rules and attribute matching rules previously described. For details, see [Association Matching Rules](b3xxit1.html#b40z0hu) and [Attribute Matching Rules](b3xxit1.html#b40z0ba).

For example, to ignore events from the ADMIN user in the Identity Vault:

```
# Do not subscribe to events for the ADMIN user.
SUBSCRIBER EXCLUDE adminUserProfile
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

## 5.3.3 Example Include/Exclude Files

*Example 5-1* Example 1

```
# Exclude users whose names start with TEMP
EXCLUDE
    CLASS UserProfile
        USRPRF=TEMP.*
    ENDCLASS
ENDEXCLUDE
```

*Example 5-2* Example 2

```
# Exclude USERA and USERB
# Because attribute rules are ANDed, these must be in separate
# CLASS sections.
EXCLUDE
    CLASS UserProfile
        USRPRF=USERA
    ENDCLASS
    CLASS UserProfile
        USRPRF=USERB
    ENDCLASS
ENDEXCLUDE
```

*Example 5-3* Example 3

```
# Exclude all users except those whose names start with IDM
# This works because channel-specific matching takes precedence
# over general matching.
EXCLUDE
    CLASS UserProfile
    ENDCLASS
ENDEXCLUDE

SUBSCRIBER INCLUDE UserProfile USRPRF=IDM.*
PUBLISHER INCLUDE UserProfile USRPRF=IDM.*
```
