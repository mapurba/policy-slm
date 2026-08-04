DirXMLScript DTD: arg-query-condition element



# arg-query-condition

The **<arg-query-condition>** argument
specifies the logical conditional search expression to be used to find a match for the enclosing action or token.
It can be enclosed inside [<token-query>](token-query.html),
[<do-find-matching-object>](do-find-matching-object.html) and **arg-query-condition**.  
An **<arg-query-condition>** element can have combination of [<arg-match-attr>](arg-match-attr.html) and **<arg-query-condition>** as children.

A **<arg-query-condition>** element along with its children can be read as a prefix expression, where the **<arg-query-condition>** is the operator and its children are the operands in the expression.

Possible names for the search condition are:

**and**
:   a logical **and** operation should be performed on the enclosed operands.

**or**
:   a logical **or** operation should be performed on the enclosed operands.

**not**
:   a logical **not** operation should be performed on the enclosed operand.
    If the attribute **name** is set to **not**, the **arg-query-condition** should have only one child, either [<search-attr>](search-attr.html) or a **<search-condtion>**

In the resultant <query>, for each <arg-query-condition> there will be <search-condition> populated with <search-attr>'s and
<search-condition>'s   
**Note:** The support for **<arg-query-condition>** depends on the implementation in the target Driver Shim.

### Example

> ```
> <arg-query-condition name="and">
> 	<arg-match-attr name="Surname"/>
> 	<arg-query-condition name="or">
> 		<arg-match-attr name="OU"/>
> 		<arg-query-condition name="not">
> 			<arg-match-attr name="Title">
> 				<arg-value type="string">
> 					<token-text xml:space="preserve">SSE</token-text>
> 				</arg-value>
> 			</arg-match-attr>
> 		</arg-query-condition>
> 	</arg-query-condition>
> </arg-query-condition>
>
> ```
>
> Also See **[<do-find-matching-object>](do-find-matching-object.html)** and  **[<token-query>](token-query.html)**
> .

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-match-attr**](arg-match-attr.html)
> :   match attribute argument
>
> [**arg-query-condition**](arg-query-condition.html)
> :   query condition argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **name** | and   |  or   |  not   name of the attribute  *supports variable expansion* | and |
> | **search-criteria-id** | **CDATA**   Holds the id of a search criteria.  When a non-empty result is received for a particular search-criteria, this value will be appended as an attribute to the instance document(s)   *This value will only be used when the attribute **return-on-first-match** is set to true on **<do-find-matching-object>** element.  If this attribute is absent, the index position of the **<search-condtion>** under **<do-find-matching-object>** will be appended to the instance document.* | #IMPLIED |
>
> ---

## 3. Content Rule

> (( [arg-match-attr](arg-match-attr.html) | [arg-query-condition](arg-query-condition.html) ) + ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**arg-query-condition**](arg-query-condition.html)
> :   query condition argument
>
> [**do-find-matching-object**](do-find-matching-object.html)
> :   automatically associate the current object
>
> [**token-query**](token-query.html)
> :   query the source or destination datastore

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#arg-query-condition)

---

[DirXMLScript DTD](index.html)

</details>


</details>
