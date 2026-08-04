DirXMLScript DTD: token-map-source-col element



# token-map-source-col

**<token-map-source-col>** is used to specify
multiple source columns in token-map. This cannot be used
in any other token other than token-map.

### Example

> ```
>
> <token-map-source-col name="dept">
>   <token-op-attr name="OU"/>
> </token-map-source-col>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**token-added-entitlement**](token-added-entitlement.html)
> :   the value(s) of an entitlement granted in the
>     current operation
>
> [**token-association**](token-association.html)
> :   the association value from the current operation
>
> [**token-attr**](token-attr.html)
> :   the value(s) of an attribute in the current
>     operation or current object in the source datastore
>
> [**token-base64-decode**](token-base64-decode.html)
> :   decode base64 data into a string
>
> [**token-base64-encode**](token-base64-encode.html)
> :   encode a string into base64 data
>
> [**token-char**](token-char.html)
> :   a unicode character
>
> [**token-class-name**](token-class-name.html)
> :   the object class name from the current operation
>
> [**token-convert-time**](token-convert-time.html)
> :   convert a date/time from one format to another
>
> [**token-dest-attr**](token-dest-attr.html)
> :   the value(s) of an attribute of current object in
>     the destination datastore
>
> [**token-dest-dn**](token-dest-dn.html)
> :   a value derived from the destination DN from the
>     current operation
>
> [**token-dest-name**](token-dest-name.html)
> :   the unqualified RDN derived from destination DN
>     from the current operation
>
> [**token-document**](token-document.html)
> :   read an XML document
>
> [**token-entitlement**](token-entitlement.html)
> :   the value(s) of a granted entitlement of the
>     current object
>
> [**token-escape-for-dest-dn**](token-escape-for-dest-dn.html)
> :   convert a string for use in a destination DN
>
> [**token-escape-for-src-dn**](token-escape-for-src-dn.html)
> :   convert a string for use in a source DN
>
> [**token-generate-password**](token-generate-password.html)
> :   generate a random password
>
> [**token-global-variable**](token-global-variable.html)
> :   the value of a global variable
>
> [**token-join**](token-join.html)
> :   join a node-set into a string
>
> [**token-json-object**](token-json-object.html)
> :   constructs a JSON string
>
> [**token-json-array**](token-json-array.html)
> :   constructs a JSON array
>
> [**token-local-variable**](token-local-variable.html)
> :   the value of a local variable
>
> [**token-lower-case**](token-lower-case.html)
> :   convert a string to lower case
>
> [**token-named-password**](token-named-password.html)
> :   the value of the named password
>
> [**token-map**](token-map.html)
> :   map a string through a mapping table
>
> [**token-op-attr**](token-op-attr.html)
> :   the value(s) of an attribute in the current
>     operation
>
> [**token-op-property**](token-op-property.html)
> :   the value of an operation property
>
> [**token-operation**](token-operation.html)
> :   the name of the current operation
>
> [**token-parse-dn**](token-parse-dn.html)
> :   parse and/or convert a DN
>
> [**token-password**](token-password.html)
> :   the value of the password in current operation
>
> [**token-query**](token-query.html)
> :   query the source or destination datastore
>
> [**token-removed-attr**](token-removed-attr.html)
> :   the value(s) of an attribute removed in the current
>     operation
>
> [**token-removed-entitlement**](token-removed-entitlement.html)
> :   the value(s) of an entitlement revoked in the
>     current operation
>
> [**token-replace-all**](token-replace-all.html)
> :   replace all instances of a substring within a
>     string
>
> [**token-replace-first**](token-replace-first.html)
> :   replace a single instance of a substring within a
>     string
>
> [**token-resolve**](token-resolve.html)
> :   resolve a DN to an association key or an
>     association key to a DN.
>
> [**token-split**](token-split.html)
> :   split a string into a node-set
>
> [**token-src-attr**](token-src-attr.html)
> :   the value(s) of an attribute of current object in
>     the source datastore
>
> [**token-src-dn**](token-src-dn.html)
> :   a value derived from the source DN from the current
>     operation
>
> [**token-src-name**](token-src-name.html)
> :   the unqualified RDN derived from source DN from the
>     current operation
>
> [**token-substring**](token-substring.html)
> :   substring of a string
>
> [**token-text**](token-text.html)
> :   constant text
>
> [**token-time**](token-time.html)
> :   the current date/time
>
> [**token-unique-name**](token-unique-name.html)
> :   a generated unique name
>
> [**token-unmatched-src-dn**](token-unmatched-src-dn.html)
> :   a DN relative to the one matched by if-src-dn
>
> [**token-upper-case**](token-upper-case.html)
> :   convert a string to upper case
>
> [**token-xml-parse**](token-xml-parse.html)
> :   parse XML
>
> [**token-xml-serialize**](token-xml-serialize.html)
> :   serialize XML
>
> [**token-xpath**](token-xpath.html)
> :   the result of an XPATH expression
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **name** | **CDATA**   Name of the column which could be one more source column to be used in token-map  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
>
> ---

## 3. Content Rule

> ( [token-added-entitlement](token-added-entitlement.html) | [token-association](token-association.html) | [token-attr](token-attr.html) |
> [token-base64-decode](token-base64-decode.html) | [token-base64-encode](token-base64-encode.html) | [token-char](token-char.html) |
> [token-class-name](token-class-name.html) | [token-convert-time](token-convert-time.html) | [token-dest-attr](token-dest-attr.html) |
> [token-dest-dn](token-dest-dn.html) | [token-dest-name](token-dest-name.html) | [token-document](token-document.html) | [token-entitlement](token-entitlement.html) |
> [token-escape-for-dest-dn](token-escape-for-dest-dn.html) | [token-escape-for-src-dn](token-escape-for-src-dn.html) |
> [token-generate-password](token-generate-password.html) | [token-global-variable](token-global-variable.html) | [token-join](token-join.html) |
> [token-json-object](token-json-object.html) | [token-json-array](token-json-array.html) | [token-local-variable](token-local-variable.html) |
> [token-lower-case](token-lower-case.html) | [token-named-password](token-named-password.html) | [token-map](token-map.html) | [token-op-attr](token-op-attr.html) |
> [token-op-property](token-op-property.html) | [token-operation](token-operation.html) | [token-parse-dn](token-parse-dn.html) | [token-password](token-password.html) |
> [token-query](token-query.html) | [token-removed-attr](token-removed-attr.html) | [token-removed-entitlement](token-removed-entitlement.html) |
> [token-replace-all](token-replace-all.html) | [token-replace-first](token-replace-first.html) | [token-resolve](token-resolve.html) | [token-split](token-split.html) |
> [token-src-attr](token-src-attr.html) | [token-src-dn](token-src-dn.html) | [token-src-name](token-src-name.html) | [token-substring](token-substring.html) |
> [token-text](token-text.html) | [token-time](token-time.html) | [token-unique-name](token-unique-name.html) | [token-unmatched-src-dn](token-unmatched-src-dn.html) |
> [token-upper-case](token-upper-case.html) | [token-xml-parse](token-xml-parse.html) | [token-xml-serialize](token-xml-serialize.html) | [token-xpath](token-xpath.html)
> ) + 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**token-map**](token-map.html)
> :   map a string through a mapping table

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#token-map-source-col)

---

[DirXMLScript DTD](index.html)

</details>


</details>
