DirXMLScript DTD: do-set-op-property element



# do-set-op-property

The **<do-set-op-property>** action causes
an operation property with the given name to be set
to the value specified by [<arg-string>](arg-string.html) on
the [current
operation](policy.html#current_operation).

An operation property is a named value that is
stored as an attribute on an [<operation-data>](../ndsdtd/operation-data.html)
element within an operation and is typically used
to supply additional context that may be needed by
the policy that handles the results of an
operation.

### Example

> ```
>
> <do-set-op-property name="myProperty">
>   <arg-string>
>     <token-text>Fred</token-text>
>   </arg-string>
> </do-set-op-property>
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
> | **name** | **CDATA**   name of the operation property  *supports variable expansion*  *after expansion, must be a legal XML [Name](http://www.w3.org/TR/2004/REC-xml-20040204/#NT-Name)* | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#do-set-op-property)

---

[DirXMLScript DTD](index.html)

</details>


</details>
