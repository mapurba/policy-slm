DirXMLScript DTD: do-add-src-object element



# do-add-src-object

The **<do-add-src-object>** action causes
an object of type class-name to be created in the
source datastore with a name and location provided
by [<arg-dn>](arg-dn.html). Any
attribute values to be added as part of the object
creation must be done in subsequent [<do-add-src-attr-value>](do-add-src-attr-value.html)
actions using the same [<arg-dn>](arg-dn.html).

### Example

> ```
>
> <do-add-src-object class-name="User">
>   <arg-dn>
>     <token-text>Users/Fred Flintstone</token-text>
>   </arg-dn>
> </do-add-src-object>
>
> <do-add-src-attr-value name="Surname">
>   <arg-dn>
>     <token-text>Users/Fred Flintstone</token-text>
>   </arg-dn>
>   <arg-value>
>     <token-text>Flintstone</token-text>
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
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **class-name** | **CDATA**   class name of target object  *supports variable expansion*   class name of object to create  *supports variable expansion* | #REQUIRED |
> | **direct** | true   |  false   use destCommandProcessor to carry out this action  *Deprecated - use when="direct" instead* | false |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **when** | auto   |  before   |  after   |  direct   when this action should be performed     **auto** - automatically determined (either in or after the[current operation](policy.html#current_operation))     **before** - before the [current operation](policy.html#current_operation)     **after** - after the [current operation](policy.html#current_operation)     **direct** - written directly to the destination datastore instead of being added to the current document | auto |
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
|| [**Tree**](DTD-TREE.html#do-add-src-object)

---

[DirXMLScript DTD](index.html)

</details>


</details>
