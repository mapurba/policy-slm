DirXMLScript DTD: token-generate-password element



# token-generate-password

**<token-generate-password>** expands to a
randomly generated password that conforms to the
password policy specified by policy-dn. If policy-dn
is not specified, the effective password policy of the
current object in eDirectory is used. If the current object
does not yet exist in eDirectory (e.g. the target of an add
operation on the publisher channel), the effective password
policy of the target container is used.

### Example

> ```
>
> <token-generate-password policy-dn="..\my password policy"/>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> EMPTY
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **policy-dn** | **CDATA**   slash form DN of a nspmPasswordPolicy object  *may be relative to the including policy*  *supports variable expansion* | #IMPLIED |
>
> ---

## 3. Content Declaration

> Empty


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
|| [**Tree**](DTD-TREE.html#token-generate-password)

---

[DirXMLScript DTD](index.html)

</details>


</details>
