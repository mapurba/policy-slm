DirXMLScript DTD: do-set-op-template-dn element



# do-set-op-template-dn

The **<do-set-op-template-dn>** action
causes the template DN for the [current
operation](policy.html#current_operation) to be set to the value provided by [<arg-dn>](arg-dn.html).
It is only valid when the [current
operation](policy.html#current_operation) is <add>.

### Example

> ```
>
> <do-set-op-template-dn>
>   <arg-dn>
>     <token-text>Novell\Users\UserTemplate</token-text>
>   </arg-dn>
> </do-set-op-template-dn>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-dn**](arg-dn.html)
> :   DN argument
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

> ( [arg-dn](arg-dn.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-set-op-template-dn)

---

[DirXMLScript DTD](index.html)

</details>


</details>
