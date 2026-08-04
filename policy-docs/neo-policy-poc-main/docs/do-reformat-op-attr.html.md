DirXMLScript DTD: do-reformat-op-attr element



# do-reformat-op-attr

The **<do-reformat-op-attr>** action
causes all values for the named attribute within
the [current
operation](policy.html#current_operation) to be replaced with the [<arg-value>](arg-value.html). The
value of [<arg-value>](arg-value.html) is
evaluated once for each value being replaced with
the local variable current-value set to the
original value.

### Examples

> ```
>
> <do-reformat-op-attr name="CN">
>   <arg-value>
>     <token-upper-case>
>       <token-local-variable name="current-value"/>
>     </token-upper-case>
>   </arg-value>
> </do-reformat-op-attr>
>
> <do-reformat-op-attr name="EMail Address">
>   <arg-value>
>     <token-xpath expression="$current-value/component[@name='eMailAddr']"/>
>   </arg-value>
> </do-reformat-op-attr>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-value**](arg-value.html)
> :   value argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **name** | **CDATA**   name of the attribute  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
>
> ---

## 3. Content Rule

> ( [arg-value](arg-value.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-reformat-op-attr)

---

[DirXMLScript DTD](index.html)

</details>


</details>
