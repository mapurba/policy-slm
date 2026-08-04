DirXMLScript DTD: if-password element



# if-password

**<if-password>** performs a test on a
password in the [current
operation](policy.html#current_operation). The type of test performed depends
on the operator specified by the op attribute. The
following table shows the type of test performed by
each operator.

> | operator | Returns true when... |
> | --- | --- |
> | available | there is password available in the [current operation](policy.html#current_operation). |
> | equal | there is password available in the [current operation](policy.html#current_operation) and its value equals the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | lt | there is password available in the [current operation](policy.html#current_operation) and its value is less than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | gt | there is password available in the [current operation](policy.html#current_operation) and its value is greater than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | not-available | available would return false. |
> | not-equal | equal would return false. |
> | not-lt | lt would return false. |
> | not-gt | gt would return false. |

### Examples

> ```
>
> <if-password op="available"/>
>
> <if-password mode="case" op="equal">fred</if-password>
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
|| [**Tree**](DTD-TREE.html#if-password)

---

[DirXMLScript DTD](index.html)

</details>


</details>
