DirXMLScript DTD: do-add-association element



# do-add-association

The **<do-add-association>** action causes
an [<add-association>](../ndsdtd/add-association.html)
command to be sent to eDirectory. The dest-dn for
the command will come from the value [<arg-dn>](arg-dn.html)
if it is specified or from the [current
object](policy.html#current_object) otherwise. The association value sent is
provided by [<arg-association>](arg-association.html).

### Example

> ```
>
> <do-add-association>
>   <arg-dn>
>     <token-src-dn/>
>   </arg-dn>
>   <arg-association>
>     <token-src-name/>
>   </arg-association>
> </do-add-association>
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
> | **direct** | true   |  false   use destCommandProcessor to carry out this action  *Deprecated - use when="direct" instead* | false |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **when** | auto   |  before   |  after   |  direct   when this action should be performed     **auto** - automatically determined (either in or after the[current operation](policy.html#current_operation))     **before** - before the [current operation](policy.html#current_operation)     **after** - after the [current operation](policy.html#current_operation)     **direct** - written directly to the destination datastore instead of being added to the current document | auto |
>
> ---

## 3. Content Rule

> ( [arg-dn](arg-dn.html) ? , [arg-association](arg-association.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-add-association)

---

[DirXMLScript DTD](index.html)

</details>


</details>
