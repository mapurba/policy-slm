DirXMLScript DTD: do-set-op-association element



# do-set-op-association

The **<do-set-op-association>** action
causes the association value for the [current
operation](policy.html#current_operation) to be set to the value provided by [<arg-association>](arg-association.html).

### Example

> ```
>
> <do-set-op-association>
>   <arg-association>
>     <token-src-name/>
>   </arg-association>
> </do-set-op-association>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-association**](arg-association.html)
> :   association argument
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

> ( [arg-association](arg-association.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-set-op-association)

---

[DirXMLScript DTD](index.html)

</details>


</details>
