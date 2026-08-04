DirXMLScript DTD: do-set-op-class-name element



# do-set-op-class-name

The **<do-set-op-class-name>** action
causes the object class name for the [current
operation](policy.html#current_operation) to be set to the value provided by [<arg-string>](arg-string.html).

### Example

> ```
>
> <do-set-op-class-name>
>   <arg-string>
>     <token-text>User</token-text>
>   </arg-string>
> </do-set-op-class-name>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-string**](arg-string.html)
> :   string argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
>
> ---

## 3. Content Rule

> ( [arg-string](arg-string.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-set-op-class-name)

---

[DirXMLScript DTD](index.html)

</details>


</details>
