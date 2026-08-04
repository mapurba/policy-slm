DirXMLScript DTD: do-move-src-object element



# do-move-src-object

The **<do-move-src-object>** action causes
an object in the source datastore to be moved. If
two arguments are provided then the object
identified by the first argument will be moved to
the container identified by the second argument. If
only a single argument is provided then the [current
object](policy.html#current_object) will be moved to the container
identified by the single argument.

### Example

> ```
>
> <do-move-src-object>
>   <arg-dn>
>     <token-text>Users/Active/FredFlintstone</token-text>
>   </arg-dn>
>   <arg-dn>
>     <token-text>Users/InActive</token-text>
>   </arg-dn>
> </do-move-src-object>
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
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
>
> ---

## 3. Content Rule

> (( [arg-dn](arg-dn.html) | [arg-association](arg-association.html) ) ? ,
> ( [arg-dn](arg-dn.html) | [arg-association](arg-association.html) ) ) 
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
|| [**Tree**](DTD-TREE.html#do-move-src-object)

---

[DirXMLScript DTD](index.html)

</details>


</details>
