DirXMLScript DTD: do-add-src-attr-value element



# do-add-src-attr-value

The **<do-add-src-attr-value>** action
causes the value specified by [<arg-value>](arg-value.html) to be
added to the named attribute on an object in the
source datastore. The target object is specified by
either [<arg-dn>](arg-dn.html) or [<arg-association>](arg-association.html)
if specified or by the [current
object](policy.html#current_object) otherwise.

### Example

> ```
>
> <do-add-src-attr-value name="Member">
>   <arg-dn>
>     <token-text>Users/ManagerGroup</token-text>
>   </arg-dn>
>   <arg-value>
>     <token-dest-dn/>
>   </arg-value>
> </do-add-src-attr-value>
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
> [**arg-value**](arg-value.html)
> :   value argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **class-name** | **CDATA**   class name of target object  *supports variable expansion*   class name of object to modify  *May be required (for schema mapping purposes) if object is other than current object..*  *supports variable expansion* | #IMPLIED |
> | **direct** | true   |  false   use destCommandProcessor to carry out this action  *Deprecated - use when="direct" instead* | false |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **name** | **CDATA**   name of the attribute  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **when** | auto   |  before   |  after   |  direct   when this action should be performed     **auto** - automatically determined (either in or after the[current operation](policy.html#current_operation))     **before** - before the [current operation](policy.html#current_operation)     **after** - after the [current operation](policy.html#current_operation)     **direct** - written directly to the destination datastore instead of being added to the current document | auto |
>
> ---

## 3. Content Rule

> (( [arg-dn](arg-dn.html) | [arg-association](arg-association.html) ) ? , [arg-value](arg-value.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-add-src-attr-value)

---

[DirXMLScript DTD](index.html)

</details>


</details>
