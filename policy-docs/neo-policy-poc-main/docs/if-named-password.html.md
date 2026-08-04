DirXMLScript DTD: if-named-password element



# if-named-password

**<if-named-password>** performs a test on
a named password from the driver. The type of test
performed depends on the operator specified by the
op attribute. The following table shows the type of
test performed by each operator.

> | operator | Returns true when... |
> | --- | --- |
> | available | there is password with the specified name available |
> | not-available | available would return false. |

### Example

> ```
>
> <if-named-password name="extraPassword" op="available"/>
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
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **name** | **CDATA**   name of the password  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **op** | available   |  not-available   test operator | #REQUIRED |
>
> ---

## 3. Content Declaration

> Empty


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
|| [**Tree**](DTD-TREE.html#if-named-password)

---

[DirXMLScript DTD](index.html)

</details>


</details>
