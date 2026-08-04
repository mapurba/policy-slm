DirXMLScript DTD: do-set-default-attr-value element



# do-set-default-attr-value

The **<do-set-default-attr-value>** action
causes the values specified by [<arg-value>](arg-value.html)'s to be
added to the [current
operation](policy.html#current_operation) for named attribute if no values for
that attribute already exist. It is only valid when
the [current
operation](policy.html#current_operation) is <add>. If write-back="true"
default values are also written back to the source
object.

### Example

> ```
>
> <do-set-default-attr-value name="L">
>   <arg-value>
>     <token-text>Unknown</token-text>
>   </arg-value>
> </do-set-default-attr-value>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-value**](arg-value.html)
> :   value argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **name** | **CDATA**   name of the attribute  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **write-back** | true   |  false   *true* if the default value should also be written back to the source object | false |
>
> ---

## 3. Content Rule

> ( [arg-value](arg-value.html) + ) 
>
> ---


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
|| [**Tree**](DTD-TREE.html#do-set-default-attr-value)

---

[DirXMLScript DTD](index.html)

</details>


</details>
