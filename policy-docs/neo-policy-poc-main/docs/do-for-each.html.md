DirXMLScript DTD: do-for-each element



# do-for-each

The **<do-for-each>** action causes the
actions specified by [<arg-actions>](arg-actions.html) to
be repeated once for each node in [<arg-node-set>](arg-node-set.html)
with the local variable current-node set to a
node-set containing only that node. If the
current-node is an [<entitlement-impl>](../dirxmlentitlements/entitlement-impl.html)
element, then the actions will also be marked as if
they were also enclosed in [<do-implement-entitlement>](do-implement-entitlement.html).
If the current-node is a [<query-token>](../ndsdtd/query-token.html)
element returned by [<token-query>](token-query.html),
then that token is used to automatically retrieve
the and process the next batch of query
results.

### Examples

> ```
>
> <do-for-each>
>   <arg-node-set>
>     <token-added-entitlement name="Group"/>
>   </arg-node-set>
>   <arg-actions>
>     <do-add-dest-attr-value class-name="Group" name="Member">
>       <arg-dn>
>         <token-local-variable name="current-node"/>
>       </arg-dn>
>       <arg-value type="dn">
>         <token-dest-dn/>
>       </arg-value>
>     </do-add-dest-attr-value>
>   </arg-actions>
> </do-for-each>
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
|| [**Tree**](DTD-TREE.html#do-for-each)

---

[DirXMLScript DTD](index.html)

</details>


</details>
