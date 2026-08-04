DirXMLScript DTD: do-clone-xpath element



# do-clone-xpath

The **<do-clone-xpath>** action causes
deep copies of the nodes selected by
*src-expression* to be added to the set of
elements selected by
*dest-expression*. If *before* is not
specified the non-attribute cloned node(s) are
appended after any existing children of the
selected elements. If *before* is specified
then it is evaluated relative to each of the
elements selected by *expression* to determine
which of the children to insert before.
If *before* evaluates to an empty nodeset or a
nodeset that does not contain any children of the
selected element, then the non-attribute cloned
node(s) are appended after any existing children,
otherwise the non-attribute cloned node(s) will be
inserted before each of the nodes in the nodeset
selected by *before* that are children of the
selected node.

### Example

> ```
>
> <do-append-xml-element expression=".." name="delete"/>
>
> <do-clone-xpath dest-expression="../delete[last()]" src-expression="@*"/>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> EMPTY
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **before** | **CDATA**   XPATH 1.0 expression evalutated relative to each of the nodes select by *dest-expression* that returns a node-set containing the child node(s) which the non-attribute cloned node(s) should be inserted before. | #IMPLIED |
> | **dest-expression** | **CDATA**   XPATH 1.0 expression that returns a node-set containing the element(s) to which the cloned node(s) should be added. | #REQUIRED |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **src-expression** | **CDATA**   XPATH 1.0 expression that returns a node-set containing the node(s) that are to be cloned | #REQUIRED |
>
> ---

## 3. Content Declaration

> Empty


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
|| [**Tree**](DTD-TREE.html#do-clone-xpath)

---

[DirXMLScript DTD](index.html)

</details>


</details>
