DirXMLScript DTD: do-clone-op-attr element



# do-clone-op-attr

The **<do-clone-op-attr>** action causes
all elements that are children of the [current
operation](policy.html#current_operation) with the attr-name attribute equal to
the name specified by src-name to be duplicated
within the operation with attr-name set to
dest-name.

### Example

> ```
>
> <do-clone-op-attr dest-name="Equivalent to Me" src-name="Member"/>
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
> | **dest-name** | **CDATA**   the attribute name to give to the clone  *supports variable expansion* | #REQUIRED |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **src-name** | **CDATA**   the attribute name to clone  *supports variable expansion* | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#do-clone-op-attr)

---

[DirXMLScript DTD](index.html)

</details>


</details>
