DirXMLScript DTD: do-remove-named-password element



# do-remove-named-password

The **<do-remove-named-password>** action removes the named password on an object specified by
[<arg-dn>](arg-dn.html). The name of the Named Password name is specified by [<arg-string>](arg-string.html)

> | Name | Description |
> | --- | --- |
> | name | Name of the Named Password. |

### Example

> ```
>
> <do-remove-named-password>
>   <arg-dn>
>     <token-text xml:space="preserve">System\driverset1\ldapdriver</token-text>
>   </arg-dn>
>   <arg-string name="name">
>     <token-text>keystorePwd</token-text>
>   </arg-string>
> </do-remove-named-password>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-dn**](arg-dn.html)
> :   DN argument
>
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

> ( [arg-dn](arg-dn.html) , [arg-string](arg-string.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-remove-named-password)

---

[DirXMLScript DTD](index.html)

</details>


</details>
