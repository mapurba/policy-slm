DirXMLScript DTD: arg-object element



# arg-object

The **<arg-object>** argument specifies a
Java Object for storing in the local variable
specified by the enclosing [<do-set-local-variable>](do-set-local-variable.html)
action. The enclosed token must be a [<token-xpath>](token-xpath.html)
that specifies an expression that returns a Java
Object or a [<token-local-variable>](token-local-variable.html)
for a variable that already contains a Java Object.

### Examples

> See **[<do-set-local-variable>](do-set-local-variable.html)**
> .

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**token-local-variable**](token-local-variable.html)
> :   the value of a local variable
>
> [**token-xpath**](token-xpath.html)
> :   the result of an XPATH expression
>
> ---

## 2. No Attributes

## 3. Content Rule

> ( [token-local-variable](token-local-variable.html) | [token-xpath](token-xpath.html) ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**do-set-local-variable**](do-set-local-variable.html)
> :   set the value of a local variable

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#arg-object)

---

[DirXMLScript DTD](index.html)

</details>


</details>
