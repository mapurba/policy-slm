DirXMLScript DTD: do-strip-xpath element



# do-strip-xpath

The **<do-strip-xpath>** action causes
nodes selected by the XPATH 1.0 expression to be
remove from the [current
operation](policy.html#current_operation). The expression must evaluate to a
node-set.

### Example

> ```
>
> <do-strip-xpath expression="*[@attr-name='OU']"/>
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
> | **expression** | **CDATA**   xpath expression | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#do-strip-xpath)

---

[DirXMLScript DTD](index.html)

</details>


</details>
