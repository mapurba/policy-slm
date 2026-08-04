DirXMLScript DTD: do-veto-if-op-attr-not-available element



# do-veto-if-op-attr-not-available

The **<do-veto-if-op-attr-not-available>**
action causes the [current
operation](policy.html#current_operation) to be cancelled if the named
attribute is not available in the [current
operation](policy.html#current_operation).

### Example

> ```
>
> <do-veto-if-op-attr-not-available name="CN"/>
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
|| [**Tree**](DTD-TREE.html#do-veto-if-op-attr-not-available)

---

[DirXMLScript DTD](index.html)

</details>


</details>
