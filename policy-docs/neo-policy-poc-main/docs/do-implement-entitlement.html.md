DirXMLScript DTD: do-implement-entitlement element



# do-implement-entitlement

The **<do-implement-entitlement>** marks
the actions specified by [<arg-actions>](arg-actions.html)
with the [<entitlement-impl>](../dirxmlentitlements/entitlement-impl.html)
elements specified in [<arg-node-set>](arg-node-set.html)
so that the Identity Manager metadirectory engine
knows to report the results of those actions to the
DirXML-EntitlementResult attribute of the current
object.

### Examples

> ```
>
> <do-implement-entitlement>
>   <arg-node-set>
>     <token-removed-entitlement name="Account"/>
>   </arg-node-set>
>   <arg-actions>
>     <do-set-dest-attr-value name="Login Disabled">
>       <arg-value type="state">
>         <token-text>true</token-text>
>       </arg-value>
>     </do-set-dest-attr-value>
>   </arg-actions>
> </do-implement-entitlement>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-node-set**](arg-node-set.html)
> :   node set argument
>
> [**arg-actions**](arg-actions.html)
> :   actions argument
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

> ( [arg-node-set](arg-node-set.html) , [arg-actions](arg-actions.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-implement-entitlement)

---

[DirXMLScript DTD](index.html)

</details>


</details>
