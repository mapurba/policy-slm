DirXMLScript DTD: do-set-src-password element



# do-set-src-password

The **<do-set-src-password>** action
sets the password for an object in the source datastore, using the value
specified by [<arg-string>](arg-string.html)'s, which contain the old(optional) and the new passwords.
The target object is specified by either
[<arg-dn>](arg-dn.html) or [<arg-association>](arg-association.html)
if specified or by [current
object](policy.html#current_object) otherwise.

### Example

> ```
>
> <do-set-src-password>
>   <arg-dn>
>     <token-text>Users/Fred Flintstone</token-text>
>   </arg-dn>
>   <arg-string>
>     <token-text>oldpassword</token-text>
>   </arg-string>
>   <arg-string>
>     <token-text>newpassword</token-text>
>   </arg-string>
> </do-set-src-password>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-dn**](arg-dn.html)
> :   DN argument
>
> [**arg-association**](arg-association.html)
> :   association argument
>
> [**arg-string**](arg-string.html)
> :   string argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **class-name** | **CDATA**   class name of target object  *supports variable expansion* | #IMPLIED |
> | **direct** | true   |  false   use destCommandProcessor to carry out this action  *Deprecated - use when="direct" instead* | false |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **when** | auto   |  before   |  after   |  direct   when this action should be performed     **auto** - automatically determined (either in or after the[current operation](policy.html#current_operation))     **before** - before the [current operation](policy.html#current_operation)     **after** - after the [current operation](policy.html#current_operation)     **direct** - written directly to the destination datastore instead of being added to the current document | auto |
>
> ---

## 3. Content Rule

> (( [arg-dn](arg-dn.html) | [arg-association](arg-association.html) ) ? , [arg-string](arg-string.html) , [arg-string](arg-string.html) ? ) 
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
|| [**Tree**](DTD-TREE.html#do-set-src-password)

---

[DirXMLScript DTD](index.html)

</details>


</details>
