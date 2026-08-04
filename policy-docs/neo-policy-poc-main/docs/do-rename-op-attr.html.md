DirXMLScript DTD: do-rename-op-attr element



# do-rename-op-attr

The **<do-rename-op-attr>** action causes
all elements that are children of the [current
operation](policy.html#current_operation) with the attr-name attribute equal to
the name specified by src-name to have attr-name
set to dest-name.

### Example

> ```
>
> <do-rename-op-attr dest-name="sn" src-name="Surname"/>
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
> | **dest-name** | **CDATA**   the new attribute name  *supports variable expansion* | #REQUIRED |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **src-name** | **CDATA**   the original attribute name  *supports variable expansion* | #REQUIRED |
>
> ---

## 3. Content Declaration

> Empty


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**actions**](actions.html)
> :   actions that are performed by a <rule>
>
> [**arg-actions**](arg-actions.html)
> :   actions argument

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#do-rename-op-attr)

---

[DirXMLScript DTD](index.html)

</details>


</details>
