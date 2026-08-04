DirXMLScript DTD: token-src-dn element



# token-src-dn

**<token-src-dn>** expands to the source
DN specified in the [current
operation](policy.html#current_operation) or a portion thereof. If start and
length are not specified or are set to the default
values {0,-1}, then the entire DN is used,
otherwise only the portion of the DN specified by
start and length is used. The format of the DN is
converted to the format of the destination
datastore if the convert attribute is set to true.

### Example

> ```
>
> <token-src-dn/>
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
> | **convert** | true   |  false   convert to DN format of destination datastore | false |
> | **length** | **CDATA**   number of DN segments to include  negative numbers are interpreted as (total # of segments + length) + 1 (e.g for a DN with 5 segments a length of -1 = (5 + (-1)) + 1 = 5, -2 = (5 + (-2)) + 1 = 4, etc.) | -1 |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **start** | **CDATA**   segment index to start with  0 is the rootmost segment >0 is an offset from the rootmost segment -1 is the leafmost segment <-1 is an offset from the leafmost segment towards the rootmost segment | 0 |
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
|| [**Tree**](DTD-TREE.html#token-src-dn)

---

[DirXMLScript DTD](index.html)

</details>


</details>
