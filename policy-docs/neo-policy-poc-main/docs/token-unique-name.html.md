DirXMLScript DTD: token-unique-name element



# token-unique-name

**<token-unique-name>** expands to a
pattern based name that is unique in the
destination datastore according to the criteria
specified.

Each [<arg-string>](arg-string.html)
provides a pattern to be used to create a proposed
name.

A proposed name is tested by performing a query for
that value in the *name* attribute against the
destination datastore using [<arg-dn>](arg-dn.html) or [<arg-association>](arg-association.html)
as the base of the query and *scope* as the
scope of the query. If the destination datastore is
eDirectory and name is omitted, then a search is
performed against the pseudo-attribute
"[Entry].rdn", which represents the RDN of an
object without respect to what the naming attribute
might be. If the destination datastore is the
application, then name is required.

A pattern may be tested with and/or without a
counter as indicated by *counter-use* and
*counter-pattern*. When a pattern is tested
with a counter, the pattern is tested repeatedly
with an appended counter until a name is found that
does not return any instances or the counter is
exhausted. The counter starting value is specified
by *counter-start* and the counter maximum
value is specified in terms of the maximum number
of digits as specified by *counter-digits*. If
the number of digits is less than those specified,
then the counter will be right padded with zeros
unless the *counter-pad* attribute is set to
false. The counter is considered exhausted when the
counter can no longer be represented by the
specified number of digits.

As soon as a proposed name is determined to be
unique, the testing of names is stopped and the
unique name is returned.

The order of proposed names is tested as follows:

* Each pattern is tested in the order specified. If
  *counter-use*="always" and the pattern is
  one of the patterns indicated
  by *counter-pattern* then the pattern is
  tested with a counter, otherwise it is tested
  without a counter.
* If no unique name has been found after the
  patterns have been exhausted and
  *counter-use*="fallback", then the
  pattern(s) indicated by *counter-pattern*
  are retried with a counter.

If all specified combinations of patterns and
counters are exhausted, then the action specified
by *on-unavailable* is taken,

### Example

> ```
>
> <token-unique-name counter-digits="2" counter-pad="true" counter-pattern="first" counter-start="1" counter-use="fallback" name="CN" on-unavailable="error" scope="subtree" test-all-objects="true">
>   <arg-string>
>     <token-upper-case>
>       <token-substring length="1" start="0">
>         <token-attr name="Given Name"/>
>       </token-substring>
>       <token-attr name="Surname"/>
>     </token-upper-case>
>   </arg-string>
>   <arg-string>
>     <token-upper-case>
>       <token-substring length="1" start="0">
>         <token-attr name="Given Name"/>
>       </token-substring>
>       <token-substring length="1" start="0">
>         <token-attr name="MI"/>
>       </token-substring>
>       <token-attr name="Surname"/>
>     </token-upper-case>
>   </arg-string>
>   <arg-string>
>     <token-upper-case>
>       <token-attr name="Given Name"/>
>       <token-attr name="Surname"/>
>     </token-upper-case>
>   </arg-string>
> </token-unique-name>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-dn**](arg-dn.html)
> :   DN argument
>
> [**arg-association**](arg-association.html)
> :   association argument
>
> [**arg-string**](arg-string.html)
> :   string argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **counter-digits** | **CDATA**   width in digits of counter | #IMPLIED |
> | **counter-pad** | true   |  false   enable/disable right zero padding of counter | true |
> | **counter-pattern** | first   |  last   |  all   which pattern(s) to use counter with     **first** - use counter only with the first pattern     **last** - use counter only with the last pattern     **all** - use counter with all patterns | last |
> | **counter-start** | **CDATA**   number to start counter | 1 |
> | **counter-use** | always   |  never   |  fallback   when to use counters     **never** - don't use counters     **always** - always use counters on the patterns indicated by counter-pattern     **fallback** - use counters counter the patterns indicated by counter-pattern only after all patterns have failed without counters | fallback |
> | **name** | **CDATA**   name of attribute to check for uniqueness | #IMPLIED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **on-unavailable** | ignore   |  warning   |  error   |  fatal   action to take if unique name cannot be constructed     **ignore** - ignore and return empty name     **warning** - issue warning and return empty name     **error** - generate error and abort current transaction     **fatal** - generate fatal error and shut down driver | error |
> | **scope** | subordinates   |  subtree   scope in which to check uniqueness | subtree |
> | **test-all-objects** | true   |  false   include/exclude object class-name in unique-name query | false |
>
> ---

## 3. Content Rule

> (( [arg-dn](arg-dn.html) | [arg-association](arg-association.html) ) ? , [arg-string](arg-string.html) + ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**arg-association**](arg-association.html)
> :   association argument
>
> [**arg-component**](arg-component.html)
> :   component argument
>
> [**arg-dn**](arg-dn.html)
> :   DN argument
>
> [**arg-node-set**](arg-node-set.html)
> :   node set argument
>
> [**arg-password**](arg-password.html)
> :   password argument
>
> [**arg-string**](arg-string.html)
> :   string argument
>
> [**arg-value**](arg-value.html)
> :   value argument
>
> [**token-base64-decode**](token-base64-decode.html)
> :   decode base64 data into a string
>
> [**token-base64-encode**](token-base64-encode.html)
> :   encode a string into base64 data
>
> [**token-convert-time**](token-convert-time.html)
> :   convert a date/time from one format to another
>
> [**token-escape-for-dest-dn**](token-escape-for-dest-dn.html)
> :   convert a string for use in a destination DN
>
> [**token-escape-for-src-dn**](token-escape-for-src-dn.html)
> :   convert a string for use in a source DN
>
> [**token-join**](token-join.html)
> :   join a node-set into a string
>
> [**token-lower-case**](token-lower-case.html)
> :   convert a string to lower case
>
> [**token-map**](token-map.html)
> :   map a string through a mapping table
>
> [**token-map-source-col**](token-map-source-col.html)
> :   used in token-map to have multiple source columns
>
> [**token-parse-dn**](token-parse-dn.html)
> :   parse and/or convert a DN
>
> [**token-replace-all**](token-replace-all.html)
> :   replace all instances of a substring within a
>     string
>
> [**token-replace-first**](token-replace-first.html)
> :   replace a single instance of a substring within a
>     string
>
> [**token-split**](token-split.html)
> :   split a string into a node-set
>
> [**token-substring**](token-substring.html)
> :   substring of a string
>
> [**token-upper-case**](token-upper-case.html)
> :   convert a string to upper case
>
> [**token-xml-parse**](token-xml-parse.html)
> :   parse XML
>
> [**token-xml-serialize**](token-xml-serialize.html)
> :   serialize XML

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#token-unique-name)

---

[DirXMLScript DTD](index.html)

</details>


</details>
