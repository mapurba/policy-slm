DirXMLScript DTD: if-association element



# if-association

**<if-association>** performs a test on
the association value of [current
operation](policy.html#current_operation) or the [current
object](policy.html#current_object). The type of test performed depends on
the operator specified by the op attribute. The
following table shows the type of test performed by
each operator.

> | operator | Returns true when... |
> | --- | --- |
> | associated | there is an established association for the [current object](policy.html#current_object). |
> | available | there is a non-empty association value specified by the [current operation](policy.html#current_operation). |
> | equal | the association value specified by the [current operation](policy.html#current_operation) is equal to the content of the condition when compared using the specified comparison mode.  *Supports variable expansion*. |
> | lt | the association value specified by the [current operation](policy.html#current_operation) is less than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion*. |
> | gt | the association value specified by the [current operation](policy.html#current_operation) is greater than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion*. |
> | not-associated | associated would return false. |
> | not-available | available would return false. |
> | not-equal | equal would return false. |
> | not-lt | lt would return false. |
> | not-gt | gt would return false. |

### Examples

> ```
>
> <if-association op="associated "/>
>
> <if-association op="available"/>
>
> <if-association mode="case" op="equal">{07414faa-1b38-40ec-8b7c-c20aa21ddafb}</if-association>
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
> | **mode** | case   |  nocase   |  regex   |  src-dn   |  dest-dn   |  numeric   |  octet   comparison [mode](conditions.html#mode) if op implies a comparison | case |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **op** | associated   |  available   |  equal   |  lt   |  gt   |  not-associated   |  not-available   |  not-equal   |  not-lt   |  not-gt   test operator | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#if-association)

---

[DirXMLScript DTD](index.html)

</details>


</details>
