DirXMLScript DTD: do-append-xml-text element



# do-append-xml-text

The **<do-append-xml-text>** action causes
the text provided by [<arg-string>](arg-string.html) to be
appended to the set of elements selected by
expression. If *before* is not specified the
text is appended after any existing children of the
selected elements. If *before* is specified
then it is evaluated relative to each of the
elements selected by *expression* to determine
which of the children to insert before.
If *before* evaluates to an empty nodeset or a
nodeset that does not contain any children of the
selected element, then the text is appended after
any existing children, otherwise the text will be
inserted before each of the nodes in the nodeset
selected by *before* that are children of the
selected node.

### Example

> See **[<do-append-xml-element>](do-append-xml-element.html).**

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-string**](arg-string.html)
> :   string argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **before** | **CDATA**   XPATH 1.0 expression evalutated relative to each of the nodes select by *expression* that returns a node-set containing the child node(s) which the text should be inserted before. | #IMPLIED |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **expression** | **CDATA**   XPATH 1.0 expression that returns a node-set containing the element(s) to which the text should be appended | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
>
> ---

## 3. Content Rule

> ( [arg-string](arg-string.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-append-xml-text)

---

[DirXMLScript DTD](index.html)

</details>


</details>
