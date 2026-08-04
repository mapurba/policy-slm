DirXMLScript DTD: arg-match-attr element



# arg-match-attr

The **<arg-match-attr>** argument
specifies the attributes that are to be use to find
a match for the enclosing action or token. The name
attribute provides the name of the attribute to use
for matching. If there is an enclosed [<arg-value>](arg-value.html), then
it provides the attribute value to use for
matching, otherwise the value(s) come(s) from the
value(s) available in the [current
operation](policy.html#current_operation).

### Example

> See **[<do-find-matching-object>](do-find-matching-object.html)**
> .

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
> | **name** | **CDATA**   name of the attribute  *supports variable expansion* | #REQUIRED |
> | **search-criteria-id** | **CDATA**   Holds the id of a search criteria.  When a non-empty result is received for a particular search-criteria, this value will be appended as an attribute to the instance document(s)   *This value will only be used when the attribute **return-on-first-match** is set to true on **<do-find-matching-object>** element.  If this attribute is absent, the index position of the **<search-condtion>** under **<do-find-matching-object>** will be appended to the instance document.* | #IMPLIED |
>
> ---

## 3. Content Rule

> ( [arg-value](arg-value.html) ? ) 
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
|| [**Tree**](DTD-TREE.html#arg-match-attr)

---

[DirXMLScript DTD](index.html)

</details>


</details>
