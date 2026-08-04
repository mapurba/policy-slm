DirXMLScript DTD: do-delete-src-object element



# do-delete-src-object

The **<do-delete-src-object>** action
causes the object in the source datastore to be
deleted. The target object is specified by either
[<arg-dn>](arg-dn.html) or [<arg-association>](arg-association.html)
if specified or by the [current
object](policy.html#current_object) otherwise.

### Example

> ```
>
> <do-delete-src-object>
>   <arg-dn>
>     <token-text>Users/Fred Flintstone</token-text>
>   </arg-dn>
> </do-delete-src-object>
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

> (( [arg-dn](arg-dn.html) | [arg-association](arg-association.html) ) ? ) 
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
|| [**Tree**](DTD-TREE.html#do-delete-src-object)

---

[DirXMLScript DTD](index.html)

</details>


</details>
