DirXMLScript DTD: policy element



# policy

A **<policy>** consists of an ordered set
of [<rule>](rule.html)'s. A [<rule>](rule.html)
consists of a set of [<conditions>](conditions.html) to be
tested and an ordered set of [<actions>](actions.html) to be
performed when the conditions are met.

A <policy> operates on an XDS document and
its primary purpose is to examine and modify that
document. A <policy> can also get additional
context from outside of the document and cause side
effects that are not reflected in the result
document.

The following outline describes the basic operation
of a <policy>:

* The XDS document is divided into
  its constituent operations. An **operation**
  is any element that is a child of [<input>](../ndsdtd/input.html) or
  [<output>](../ndsdtd/output.html).
  An operation usually represents an event, a
  command, or a status.
* The
  <policy> is applied to separately to each
  operation. As the [<policy>](policy.html) is applied
  to each operation in turn, that operation becomes
  the **current operation**. The object that is
  described by the *current operation* src-dn,
  src-entry-id, dest-dn, dest-entry-id, and/or
  association from the becomes the **current
  object**.
* Each [<rule>](rule.html) is applied in
  order to the current operation. All of the [<rule>](rule.html)s
  are applied to the current operation unless an
  action is performed by a prior [<rule>](rule.html) that causes
  subsequent [<rule>](rule.html)'s to no longer
  be applied.
* The [<conditions>](conditions.html) for
  the [<rule>](rule.html) are tested and
  if the [<conditions>](conditions.html) for
  the [<rule>](rule.html) are met then
  the [<actions>](actions.html) are
  applied.

### Variables

DirXML Script
supports two kinds of variables: global and local. A
global variable is a variable that gets its value
from a Global Configuration Value that is defined for
the driver or the driverset. Global variables are by
definition read-only. A local variable is a variable
that is set by a policy. A local variable may exist
in one of two different scopes: policy or driver. A
policy scoped variable is only visible during the
processing of the *current operation* by the
policy that sets the variable. A driver scoped
variable is visible from all DirXML Script policies
running within the same driver until the driver is
stopped. A variable name must be a legal XML [Name](http://www.w3.org/TR/2004/REC-xml-20040204/#NT-Name).  
  
There are a number of global and local variables that
are automatically defined:  
  
> |  |  |  |
> | --- | --- | --- |
> | Name | **Type** | Description |
> | dirxml.auto.driverdn | global/string | Slash format DN of the current driver |
> | dirxml.auto.driverguid | global/string | GUID of the current driver |
> | dirxml.auto.treename | global/string | Tree name of the local eDirectory instance |
> | fromNDS | policy local/boolean | *true* if the source datastore is eDirectory  *false* if the source datastore is the connected application |
> | destQueryProcessor | policy local/java object | Instance of [XdsQueryProcessor](http://developer.novell.com/ndk/doc/dirxml/dirxmlbk/api/com/novell/nds/dirxml/driver/XdsQueryProcessor.html) used to query the destination datastore |
> | srcQueryProcessor | policy local/java object | Instance of [XdsQueryProcessor](http://developer.novell.com/ndk/doc/dirxml/dirxmlbk/api/com/novell/nds/dirxml/driver/XdsQueryProcessor.html) used to query the destination datastore |
> | destCommandProcessor | policy local/java object | Instance of [XdsCommandProcessor](http://developer.novell.com/ndk/doc/dirxml/dirxmlbk/api/com/novell/nds/dirxml/driver/XdsCommandProcessor.html) used to query the destination datastore |
> | srcCommandProcessor | policy local/java object | Instance of [XdsCommandProcessor](http://developer.novell.com/ndk/doc/dirxml/dirxmlbk/api/com/novell/nds/dirxml/driver/XdsCommandProcessor.html) used to query the destination datastore |
> | dnConverter | policy local/java object | Instance of [DNConverter](http://developer.novell.com/ndk/doc/dirxml/dirxmlbk/api/com/novell/nds/dirxml/driver/DNConverter.html) |
> | current-node | policy local/node-set | The loop variable for each iteration of [<do-for-each>](do-for-each.html) |
> | current-value | policy local/node-set | The loop variable for each iteration of [<do-reformat-op-attr>](do-reformat-op-attr.html) |
> | current-op | policy local/node-set | The *current operation*    Setting this variable using [<do-set-local-variable>](do-set-local-variable.html) causes the first operation specified by [<arg-node-set>](arg-node-set.html) to become the [current operation](policy.html#current_operation) for the remainder of the current policy execution or until it is set to another value. The new current operation must be an element sibling of the original [current operation](policy.html#current_operation) and must have been added by the current policy. |

### Variable Expansion

Many conditions, actions, and
tokens support dynamic variable expansion in their
attributes or content. Where supported, an embedded
reference of the form *$<variable-name>$*
is replaced with the value of the local or global
variable with the given name.
*$<variable-name>$* must be a [legal variable name](do-set-local-variable.html#legal-variable-name). If the given variable does
not exist the reference is replaced with the empty
string. Where it is desirable to use a single '$' and
not have it interpreted as a variable reference, it
should be escaped with an additional '$' (e.g. You
owe me $$100.00). Content and attributes that support
variable expansion are annotated with the phrase
*supports variable expansion*.  

### Date/Time Parameters

Tokens that deal with dates and times have arguments
that deal with the format, language, and time zone of
the date and time representation. Date formats
arguments may be specified in one of two ways. If the
format begins with a '!' character, then the format
is a named format. Legal names are defined in the
following table:  
> | Name | Description |
> | --- | --- |
> | !CTIME | Number of seconds since Midnight, January 1, 1970. (Compatible with eDirectory time syntaxes) |
> | !JTIME | Number of milliseconds since Midnight, January 1, 1970. (Compatible with Java time) |
> | !FILETIME | Number of 100-nanosecond intervals since January 1, 1601 (Compatible with Win32 FILETIME) |
> | !FULL.TIME | Language specific FULL time format. |
> | !LONG.TIME | Language specific LONG time format. |
> | !MEDIUM.TIME | Language specific MEDIUM time format. |
> | !SHORT.TIME | Language specific SHORT time format. |
> | !FULL.DATE | Language specific FULL date format. |
> | !LONG.DATE | Language specific LONG date format. |
> | !MEDIUM.DATE | Language specific MEDIUM date format. |
> | !SHORT.DATE | Language specific SHORT date format. |
> | !FULL.DATETIME | Language specific FULL date/time format. |
> | !LONG.DATETIME | Language specific LONG date/time format. |
> | !MEDIUM.DATETIME | Language specific MEDIUM date/time format. |
> | !SHORT.DATETIME | Language specific SHORT date/time format. |

If the format does not begin with '!', then the
format is interpreted as a custom date/time format
conforming to the patterns recognized by [java.text.SimpleDateFormat](http://java.sun.com/j2se/1.4.2/docs/api/java/text/SimpleDateFormat.html).  
  
Language arguments may be specified by an identifier
that comforms to [IETF RFC
3066](http://www.ietf.org/rfc/rfc3066.txt). The list of identifiers understood by the
system may be obtained by calling
java.util.Locale.getAvailableLocales() and
substituting all underscores in the result with a
hyphens. If a language argument is omitted or blank,
then the default system language is used.  
  
Time zone arguments may be specified in any
identifier recognizable by
java.util.TimeZone.getTimeZone(). A list of
identifies understood by the system may be obtained
by calling java.util.TimeZone.getAvailableIDs(). If a
time zone argument is omitted or blank, then the
default system time zone is used.  

### XPATH evaluation

Arguments to some conditions and actions take an [XPATH 1.0](http://www.w3.org/TR/1999/REC-xpath-19991116) expression. This XPATH is evaluated
with the following context:

* the context node is the [current operation](policy.html#current_operation) unless otherwise specified
  in the description of the expression.
* the context position and size are 1.
* available variables
  + those available as parameters to stylesheets
    within the Identity Manager metadirectory
    engine (currently fromNDS, srcQueryProcessor,
    destQueryProcessor, srcCommandProcessor,
    destCommandProcessor, and dnConverter.)
  + global configuration values
  + local policy variables
  + if there is a name conflict between the
    different variable sources then the order of
    precedence is local(policy scope),
    local(driver scope), global.
  + Due to the XPATH syntax, any variable that
    has a colon character in its name is not
    accessible from XPATH.
* available namespace
  definitions
  + Any namespaces that are explicity declared on
    <policy> using xmns:prefix.
  + The following implicitly defined namespaces
    (unless the same prefix has been explicitly
    defined):
    - xmlns:js="http://www.novell.com/nxsl/ecmascript"
    - xmlns:es="http://www.novell.com/nxsl/ecmascript"
    - xmlns:query="http://www.novell.com/nxsl/java/com.novell.nds.dirxml.driver.XdsQueryProcessor"
    - xmlns:cmd="http://www.novell.com/nxsl/java/com.novell.nds.dirxml.driver.XdsCommandProcessor"
    - xmlns:jdbc="urn:dirxml:jdbc"
  + Any namespace prefix that is not otherwise
    mapped will be automatically mapped to
    *http://www.novell.com/nxsl/java/<prefix>*
    if and only if prefix is a fully qualified
    Java class name that can be resolved to an
    available Java class via introspection.
* available functions
  + all built-in XPATH 1.0 functions
  + Java extension functions as provided by NXSL
    - Java extension functions are accessed via
      a namespace prefix mapped to a URI of the
      form:
      *http://www.novell.com/nxsl/java/<fully-qualified-class-name>*.
    - For convenience, any prefix that is not
      otherwise mapped, will be mapped to
      *http://www.novell.com/nxsl/java/<prefix>*
      if prefix is the fully qualified class
      name of a Java class that can be
      discovered via introspection.
  + ECMAScript extension functions as provided by
    NXSL
    - ECMAScript extension function definitions
      come from the set of ECMAScript resources
      that are associated with the driver.
    - ECMAScript extension functions are
      accessed via a namespace prefix mapped to
      the URI
      *http://www.novell.com/nxsl/ecmascript*.
    - For convenience, the prefixes *js*
      and *es* are both implicitly mapped
      to
      *http://www.novell.com/nxsl/ecmascript*
      unless otherwise explicitly defined.

### Example

> ```
>
> <policy>
>   <description>My policy</description>
>   <include name="..\..\Library\My shared policy"/>
>   <rule>
>     <description>Rule to disallow moving a user</description>
>     <comment>This rule was added because under no circumsances do we ever want to perform a move.</comment>
>     <conditions>
>       <and>
>         <if-class-name mode="nocase" op="equal">User</if-class-name>
>         <if-operation op="equal">move</if-operation>
>       </and>
>     </conditions>
>     <actions>
>       <veto/>
>     </actions>
>   </rule>
>   <rule>
>     <description>Rule to disallow operations on a disabled user or group</description>
>     <conditions>
>       <or>
>         <if-class-name mode="nocase" op="equal">User</if-class-name>
>         <if-class-name mode="nocase" op="equal">Group</if-class-name>
>       </or>
>       <or>
>         <if-attr mode="nocase" name="Login Disabled" op="equal">true</if-attr>
>       </or>
>     </conditions>
>     <actions>
>       <veto/>
>     </actions>
>   </rule>
> </policy>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**description**](description.html)
> :   description of a <policy> or a <rule>
>
> [**rule**](rule.html)
> :   rule within a policy
>
> [**include**](include.html)
> :   include rules from another policy
>
> ---

## 2. No Attributes

## 3. Content Rule

> ( [description](description.html) ? ,
> ( [rule](rule.html) | [include](include.html) ) \* ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> None

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#policy)

---

[DirXMLScript DTD](index.html)

</details>


</details>
