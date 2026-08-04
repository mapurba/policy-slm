DirXMLScript DTD: do-if element



# do-if

The **<do-if>** action causes the actions
specified by the first [<arg-actions>](arg-actions.html) to
be performed if the conditions specified by [<arg-conditions>](arg-conditions.html)
[evaluate to
true or the actions specified by the second](do-implement-entitlement.html) [<arg-actions>](arg-actions.html) (if
it exists) to be performed if the conditions
specified by [<arg-conditions>](arg-conditions.html)
evaluate to false.

### Example

> ```
>
> <do-if>
>   <arg-conditions>
>     <and>
>       <if-op-attr mode="nocase" name="Given Name" op="equal">fred</if-op-attr>
>     </and>
>   </arg-conditions>
>   <arg-actions>
>     <do-add-dest-attr-value name="Surname">
>       <arg-value type="string">
>         <token-text>Flintstone</token-text>
>       </arg-value>
>     </do-add-dest-attr-value>
>   </arg-actions>
>   <arg-actions>
>     <do-add-dest-attr-value name="Surname">
>       <arg-value type="string">
>         <token-text>Rubble</token-text>
>       </arg-value>
>     </do-add-dest-attr-value>
>   </arg-actions>
> </do-if>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-conditions**](arg-conditions.html)
> :   conditions argument
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

> ( [arg-conditions](arg-conditions.html) , [arg-actions](arg-actions.html) , [arg-actions](arg-actions.html) ? ) 
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
|| [**Tree**](DTD-TREE.html#do-if)

---

[DirXMLScript DTD](index.html)

</details>


</details>
