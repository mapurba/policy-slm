DirXMLScript DTD: if-xml-attr element



# if-xml-attr

**<if-xml-attr>** performs a test on an
XML attribute of
the [current
operation](policy.html#current_operation). The type of test performed depends
on the operator specified by the op attribute. The
following table shows the type of test performed by
each operator.

> | operator | Returns true when... |
> | --- | --- |
> | available | there is an XML attribute with the specified name on the [current operation](policy.html#current_operation). |
> | equal | there is a an XML attribute with the specified name on the [current operation](policy.html#current_operation) and its value equals the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | lt | there is a an XML attribute with the specified name on the [current operation](policy.html#current_operation) and its value is less than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | gt | there is a an XML attribute with the specified name on the [current operation](policy.html#current_operation) and its value is greater than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | not-available | available would return false. |
> | not-equal | equal would return false. |
> | not-lt | lt would return false. |
> | not-gt | gt would return false. |

### Examples

> ```
>
> <if-xml-attr name="from-merge" op="available"/>
>
> <if-xml-attr mode="nocase" name="level" op="equal">error</if-xml-attr>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> #PCDATA
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **mode** | case   |  nocase   |  regex   |  src-dn   |  dest-dn   |  numeric   |  octet   comparison [mode](conditions.html#mode) if op implies a comparison | nocase |
> | **name** | **CDATA**   tag name of the XML attribute  *supports variable expansion*  *after expansion, must be a legal [XML QName](http://www.w3.org/TR/REC-xml-names/#ns-qualnames)*  *may contain a namespace prefix if and only if that prefix maps to an [available namespace definition](policy.html#ns)* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **op** | available   |  equal   |  lt   |  gt   |  not-available   |  not-equal   |  not-lt   |  not-gt   test operator | #REQUIRED |
>
> ---

## 3. Content Rule

> ( #PCDATA ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**and**](and.html)
> :   logical conjunction
>
> [**or**](or.html)
> :   logical disjunction

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#if-xml-attr)

---

[DirXMLScript DTD](index.html)

</details>


</details>
