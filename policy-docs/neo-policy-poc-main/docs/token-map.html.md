DirXMLScript DTD: token-map element



# token-map

**<token-map>** maps the result of
the enclosed tokens from the values specified by
the *src* column to the *dest* column in
the the [mapping
table](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlmap/index.html) specified by *table.* If the values from multiple
source columns are to be mapped to a *dest* column,
[<token-map-source-col>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-map-source-col.html) can to be used
inside **<token-map>** with the details
of multiple source dolumns. The *type* attribute can be used
to specify if all the values of the source columns have to be matched
or the value of any of source column can be matched. Refer *examples* below.

The *table* attribute should be the slash form
DN of the DirXML-Resource object containing the [mapping table](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlmap/index.html) to
be used. The DN may be relative to the including
policy.

If this token is evaluated in a context where a
node-set result is expected and multiple rows are
matched by the value being mapped, then a node-set
is returned that contains the values from the
destination column of each matching row. Otherwise
only the value from the first matching row is
returned.

If no rows are matched by the value being mapped and
a non-empty value for *default-value* is provided,
then the token returns the value of *default-value*,
otherwise it returns the empty string if being evaluated
in a context that is expecting a string, or an empty node-set
if evaluated in a context that is expecting a node-set.

### Example

> ```
> <token-map dest="code" source="dept" table="./Department Table">
>   <token-op-attr name="OU"/>
> </token-map>
>
> ```

> ```
> <token-map dest="resourceDN" source="entitlementName" table="..\EntitlementLLIDMapping" type="AND">
>   <token-local-variable="entName"/>
>   <token-map-source-col name="LLID">
>     <token-local-variable name="_llid_"/>
>   </token-map-source-col>
> </token-map>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**token-map-source-col**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-map-source-col.html)
> :   used in token-map to have multiple source columns
>
> [**token-added-entitlement**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-added-entitlement.html)
> :   the value(s) of an entitlement granted in the
>     current operation
>
> [**token-association**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-association.html)
> :   the association value from the current operation
>
> [**token-attr**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-attr.html)
> :   the value(s) of an attribute in the current
>     operation or current object in the source datastore
>
> [**token-base64-decode**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-base64-decode.html)
> :   decode base64 data into a string
>
> [**token-base64-encode**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-base64-encode.html)
> :   encode a string into base64 data
>
> [**token-char**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-char.html)
> :   a unicode character
>
> [**token-class-name**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-class-name.html)
> :   the object class name from the current operation
>
> [**token-convert-time**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-convert-time.html)
> :   convert a date/time from one format to another
>
> [**token-dest-attr**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-dest-attr.html)
> :   the value(s) of an attribute of current object in
>     the destination datastore
>
> [**token-dest-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-dest-dn.html)
> :   a value derived from the destination DN from the
>     current operation
>
> [**token-dest-name**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-dest-name.html)
> :   the unqualified RDN derived from destination DN
>     from the current operation
>
> [**token-document**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-document.html)
> :   read an XML document
>
> [**token-entitlement**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-entitlement.html)
> :   the value(s) of a granted entitlement of the
>     current object
>
> [**token-escape-for-dest-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-escape-for-dest-dn.html)
> :   convert a string for use in a destination DN
>
> [**token-escape-for-src-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-escape-for-src-dn.html)
> :   convert a string for use in a source DN
>
> [**token-generate-password**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-generate-password.html)
> :   generate a random password
>
> [**token-global-variable**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-global-variable.html)
> :   the value of a global variable
>
> [**token-join**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-join.html)
> :   join a node-set into a string
>
> [**token-json-object**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-json-object.html)
> :   constructs a JSON string
>
> [**token-json-array**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-json-array.html)
> :   constructs a JSON array
>
> [**token-local-variable**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-local-variable.html)
> :   the value of a local variable
>
> [**token-lower-case**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-lower-case.html)
> :   convert a string to lower case
>
> [**token-named-password**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-named-password.html)
> :   the value of the named password
>
> [**token-map**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-map.html)
> :   map a string through a mapping table
>
> [**token-op-attr**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-op-attr.html)
> :   the value(s) of an attribute in the current
>     operation
>
> [**token-op-property**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-op-property.html)
> :   the value of an operation property
>
> [**token-operation**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-operation.html)
> :   the name of the current operation
>
> [**token-parse-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-parse-dn.html)
> :   parse and/or convert a DN
>
> [**token-password**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-password.html)
> :   the value of the password in current operation
>
> [**token-query**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-query.html)
> :   query the source or destination datastore
>
> [**token-removed-attr**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-removed-attr.html)
> :   the value(s) of an attribute removed in the current
>     operation
>
> [**token-removed-entitlement**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-removed-entitlement.html)
> :   the value(s) of an entitlement revoked in the
>     current operation
>
> [**token-replace-all**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-replace-all.html)
> :   replace all instances of a substring within a
>     string
>
> [**token-replace-first**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-replace-first.html)
> :   replace a single instance of a substring within a
>     string
>
> [**token-resolve**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-resolve.html)
> :   resolve a DN to an association key or an
>     association key to a DN.
>
> [**token-split**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-split.html)
> :   split a string into a node-set
>
> [**token-src-attr**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-src-attr.html)
> :   the value(s) of an attribute of current object in
>     the source datastore
>
> [**token-src-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-src-dn.html)
> :   a value derived from the source DN from the current
>     operation
>
> [**token-src-name**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-src-name.html)
> :   the unqualified RDN derived from source DN from the
>     current operation
>
> [**token-substring**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-substring.html)
> :   substring of a string
>
> [**token-text**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-text.html)
> :   constant text
>
> [**token-time**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-time.html)
> :   the current date/time
>
> [**token-unique-name**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-unique-name.html)
> :   a generated unique name
>
> [**token-unmatched-src-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-unmatched-src-dn.html)
> :   a DN relative to the one matched by if-src-dn
>
> [**token-upper-case**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-upper-case.html)
> :   convert a string to upper case
>
> [**token-xml-parse**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-xml-parse.html)
> :   parse XML
>
> [**token-xml-serialize**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-xml-serialize.html)
> :   serialize XML
>
> [**token-xpath**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-xpath.html)
> :   the result of an XPATH expression
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **default-value** | **CDATA**   default value for the destination column  *supports variable expansion* | #IMPLIED |
> | **dest** | **CDATA**   name of the destination column  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **source** | **CDATA**   name of the source column  *supports variable expansion* | #REQUIRED |
> | **table** | **CDATA**   slash form DN of a DirXML-Resource object containing the mapping table  *may be relative to the including policy*  *supports variable expansion* | #REQUIRED |
> | **type** | AND   |  OR   To decide whether all source column values are to be matched or any value can be matched | AND |
>
> ---

## 3. Content Rule

> ( [token-map-source-col](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-map-source-col.html) + |
> ( [token-added-entitlement](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-added-entitlement.html) | [token-association](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-association.html) | [token-attr](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-attr.html) |
> [token-base64-decode](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-base64-decode.html) | [token-base64-encode](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-base64-encode.html) | [token-char](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-char.html) |
> [token-class-name](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-class-name.html) | [token-convert-time](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-convert-time.html) | [token-dest-attr](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-dest-attr.html) |
> [token-dest-dn](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-dest-dn.html) | [token-dest-name](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-dest-name.html) | [token-document](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-document.html) | [token-entitlement](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-entitlement.html) |
> [token-escape-for-dest-dn](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-escape-for-dest-dn.html) | [token-escape-for-src-dn](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-escape-for-src-dn.html) |
> [token-generate-password](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-generate-password.html) | [token-global-variable](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-global-variable.html) | [token-join](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-join.html) |
> [token-json-object](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-json-object.html) | [token-json-array](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-json-array.html) | [token-local-variable](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-local-variable.html) |
> [token-lower-case](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-lower-case.html) | [token-named-password](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-named-password.html) | [token-map](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-map.html) | [token-op-attr](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-op-attr.html) |
> [token-op-property](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-op-property.html) | [token-operation](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-operation.html) | [token-parse-dn](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-parse-dn.html) | [token-password](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-password.html) |
> [token-query](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-query.html) | [token-removed-attr](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-removed-attr.html) | [token-removed-entitlement](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-removed-entitlement.html) |
> [token-replace-all](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-replace-all.html) | [token-replace-first](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-replace-first.html) | [token-resolve](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-resolve.html) | [token-split](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-split.html) |
> [token-src-attr](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-src-attr.html) | [token-src-dn](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-src-dn.html) | [token-src-name](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-src-name.html) | [token-substring](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-substring.html) |
> [token-text](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-text.html) | [token-time](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-time.html) | [token-unique-name](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-unique-name.html) | [token-unmatched-src-dn](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-unmatched-src-dn.html) |
> [token-upper-case](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-upper-case.html) | [token-xml-parse](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-xml-parse.html) | [token-xml-serialize](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-xml-serialize.html) |
> [token-xpath](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-xpath.html) ) \* ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**arg-association**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-association.html)
> :   association argument
>
> [**arg-component**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-component.html)
> :   component argument
>
> [**arg-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-dn.html)
> :   DN argument
>
> [**arg-node-set**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-node-set.html)
> :   node set argument
>
> [**arg-password**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-password.html)
> :   password argument
>
> [**arg-string**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-string.html)
> :   string argument
>
> [**arg-value**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-value.html)
> :   value argument
>
> [**token-base64-decode**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-base64-decode.html)
> :   decode base64 data into a string
>
> [**token-base64-encode**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-base64-encode.html)
> :   encode a string into base64 data
>
> [**token-convert-time**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-convert-time.html)
> :   convert a date/time from one format to another
>
> [**token-escape-for-dest-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-escape-for-dest-dn.html)
> :   convert a string for use in a destination DN
>
> [**token-escape-for-src-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-escape-for-src-dn.html)
> :   convert a string for use in a source DN
>
> [**token-join**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-join.html)
> :   join a node-set into a string
>
> [**token-lower-case**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-lower-case.html)
> :   convert a string to lower case
>
> [**token-map**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-map.html)
> :   map a string through a mapping table
>
> [**token-map-source-col**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-map-source-col.html)
> :   used in token-map to have multiple source columns
>
> [**token-parse-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-parse-dn.html)
> :   parse and/or convert a DN
>
> [**token-replace-all**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-replace-all.html)
> :   replace all instances of a substring within a
>     string
>
> [**token-replace-first**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-replace-first.html)
> :   replace a single instance of a substring within a
>     string
>
> [**token-split**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-split.html)
> :   split a string into a node-set
>
> [**token-substring**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-substring.html)
> :   substring of a string
>
> [**token-upper-case**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-upper-case.html)
> :   convert a string to upper case
>
> [**token-xml-parse**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-xml-parse.html)
> :   parse XML
>
> [**token-xml-serialize**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-xml-serialize.html)
> :   serialize XML

---

[**Top Elements**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/TOP-ELEM.html) ||
[**All Elements**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/ALL-ELEM.html)
|| [**Tree**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/DTD-TREE.html#token-map)

---

[DirXMLScript DTD](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/index.html)

</details>


</details>
