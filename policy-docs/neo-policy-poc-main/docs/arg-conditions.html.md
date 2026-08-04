DirXMLScript DTD: arg-conditions element



# arg-conditions

The **<arg-conditions>** argument
specifies the conditions associated with the
enclosing action. It is different from other
argument types in that it contains conditions
instead of tokens.

### Example

> See **[<do-if>](do-if.html), [<do-while>](do-while.html)**.

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**and**](and.html)
> :   logical conjunction
>
> [**or**](or.html)
> :   logical disjunction
>
> ---

## 2. No Attributes

## 3. Content Rule

> ( [and](and.html) \* | [or](or.html) \* ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**do-if**](do-if.html)
> :   conditionally perform actions
>
> [**do-while**](do-while.html)
> :   repeat actions while a conditions are true

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#arg-conditions)

---

[DirXMLScript DTD](index.html)

</details>


</details>
