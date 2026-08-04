DirXMLScript DTD: do-clear-op-property element



# do-clear-op-property

The **<do-clear-op-property>** action
causes any [operation
property](do-set-op-property.html#operation_property) with the given name to be cleared from
the [current
operation](policy.html#current_operation).

### Example

> ```
>
> <do-clear-op-property name="myProperty"/>
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
> | **name** | **CDATA**   name of the operation property  *supports variable expansion*  *after expansion, must be a legal XML [Name](http://www.w3.org/TR/2004/REC-xml-20040204/#NT-Name)* | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#do-clear-op-property)

---

[DirXMLScript DTD](index.html)

</details>


</details>
