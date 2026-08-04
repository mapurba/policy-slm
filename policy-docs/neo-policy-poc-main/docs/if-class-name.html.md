DirXMLScript DTD: if-class-name element



# if-class-name

**<if-class-name>** performs a test on the
object class name in the [current
operation](policy.html#current_operation).

> | operator | Returns true when... |
> | --- | --- |
> | available | there is an object class name available in the [current operation](policy.html#current_operation). |
> | equal | there is an object class name available in the [current operation](policy.html#current_operation) and it equals the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | lt | there is an object class name available in the [current operation](policy.html#current_operation) and it is less than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | gt | there is an object class name available in the [current operation](policy.html#current_operation) and it is greater than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | not-available | available would return false. |
> | not-equal | equal would return false. |
> | not-lt | lt would return false. |
> | not-gt | gt would return false. |

### Examples

> ```
>
> <if-class-name op="available"/>
>
> <if-class-name mode="nocase" op="equal">User</if-class-name>
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
|| [**Tree**](DTD-TREE.html#if-class-name)

---

[DirXMLScript DTD](index.html)

</details>


</details>
