DirXMLScript DTD: if-xpath element



# if-xpath

**<if-xpath>** performs a test on the
results of evaluating an [XPATH 1.0](http://www.w3.org/TR/1999/REC-xpath-19991116) expression. The type of test
performed depends on the operator specified by the
op attribute. The following table shows the type of
test performed by each operator.

> | operator | Returns true when... |
> | --- | --- |
> | true | the XPATH expression evaluates to true. |
> | not-true | true would return false. |

### Example

> ```
>
> <if-xpath op="true">add-attr[@attr-name='OU]/value[string(.) = "Sales"]</if-xpath>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> #PCDATA
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **op** | true   |  not-true   test operator | #REQUIRED |
>
> ---

## 3. Content Rule

> ( #PCDATA ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**and**](and.html)
> :   logical conjunction
>
> [**or**](or.html)
> :   logical disjunction

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#if-xpath)

---

[DirXMLScript DTD](index.html)

</details>


</details>
