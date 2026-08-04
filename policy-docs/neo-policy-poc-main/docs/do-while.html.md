DirXMLScript DTD: do-while element



# do-while

The **<do-while>** action causes the
actions specified by [<arg-actions>](arg-actions.html) to
be repeated while the conditions specified by [<arg-conditions>](arg-conditions.html)
evaluate to true.

### Example

> ```
>
> <do-set-local-variable name="counter">
>   <arg-string>
>     <token-text>1</token-text>
>   </arg-string>
> </do-set-local-variable>
>
> <do-while>
>   <arg-conditions>
>     <and>
>       <if-local-variable mode="numeric" name="counter" op="not-gt">10</if-local-variable>
>     </and>
>   </arg-conditions>
>   <arg-actions>
>     <do-trace-message color="yellow" level="0">
>       <arg-string>
>         <token-text>Counter = </token-text>
>         <token-local-variable name="counter"/>
>       </arg-string>
>     </do-trace-message>
>     <do-set-local-variable name="counter">
>       <arg-string>
>         <token-xpath expression="$counter + 1"/>
>       </arg-string>
>     </do-set-local-variable>
>   </arg-actions>
> </do-while>
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

> ( [arg-conditions](arg-conditions.html) , [arg-actions](arg-actions.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-while)

---

[DirXMLScript DTD](index.html)

</details>


</details>
