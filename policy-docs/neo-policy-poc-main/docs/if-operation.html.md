DirXMLScript DTD: if-operation element



# if-operation

**<if-operation>** performs a test on the
name of the [current
operation](policy.html#current_operation). The type of test performed depends
on the operator specified by the op attribute. The
following table shows the type of test performed by
each operator.

> | operator | Returns true when... |
> | --- | --- |
> | equal | the name of the [current operation](policy.html#current_operation) is equal to content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | lt | the name of the [current operation](policy.html#current_operation) is less than content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | gt | the name of the [current operation](policy.html#current_operation) is greater than content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | not-equal | equal would return false. |
> | not-lt | lt would return false. |
> | not-gt | gt would return false. |

### Example

> ```
>
> <if-operation mode="case" op="equal">add</if-operation>
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
> | **op** | equal   |  lt   |  gt   |  not-equal   |  not-lt   |  not-gt   test operator | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#if-operation)

---

[DirXMLScript DTD](index.html)

</details>


</details>
