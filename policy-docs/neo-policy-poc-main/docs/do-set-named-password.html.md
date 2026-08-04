DirXMLScript DTD: do-set-named-password element



# do-set-named-password

The **<do-set-named-password>** action sets or creates a named password on an object using the value specified by
*arg-password*. The target object is specified by *arg-dn*. The name and display name of the named password are
specified by [<arg-string>](arg-string.html)'s.

> | Name | Description |
> | --- | --- |
> | name | Name of the Named Password. |
> | display-name | Display Name of the Named Password.  Default: Name of named password. |

### Example

> ```
>
> <do-set-named-password>
>   <arg-dn>
>     <token-text xml:space="preserve">System\driverset1\ldapdriver</token-text>
>   </arg-dn>
>   <arg-password>
>     <token-text xml:space="preserve">novell</token-text>
>   </arg-password>
>   <arg-string name="name">
>     <token-text>keystorePwd</token-text>
>   </arg-string>
>   <arg-string name="display-name">
>     <token-text>Keystore Password</token-text>
>   </arg-string>
> </do-set-named-password>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-dn**](arg-dn.html)
> :   DN argument
>
> [**arg-password**](arg-password.html)
> :   password argument
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

> ( [arg-dn](arg-dn.html) , [arg-password](arg-password.html) , [arg-string](arg-string.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-set-named-password)

---

[DirXMLScript DTD](index.html)

</details>


</details>
