DirXMLScript DTD: do-strip-op-attr element



# do-strip-op-attr

The **<do-strip-op-attr>** action causes
all elements that are children of the [current
operation](policy.html#current_operation) with the attr-name attribute equal to
the name specified by name to be stripped from the
[current
operation](policy.html#current_operation).

### Example

> ```
>
> <do-strip-op-attr name="Member"/>
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
> | **name** | **CDATA**   name of the attribute  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
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
|| [**Tree**](DTD-TREE.html#do-strip-op-attr)

---

[DirXMLScript DTD](index.html)

</details>


</details>
