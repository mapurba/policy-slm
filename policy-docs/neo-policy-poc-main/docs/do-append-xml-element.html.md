DirXMLScript DTD: do-append-xml-element element



# do-append-xml-element

The **<do-append-xml-element>** action
causes a custom element named by the name attribute
to be added to the set of elements selected by
*expression*. If *before* is not
specified the new element is appended after any
existing children of the selected elements.
If *before* is specified then it is evaluated
relative to each of the elements selected
by *expression* to determine which of the
children to insert before. If *before*
evaluates to an empty nodeset or a nodeset that
does not contain any children of the selected
element, then the new element is appended after any
existing children, otherwise the new element will
be inserted before each of the nodes in the nodeset
selected by *before* that are children of the
selected node.

### Example

> ```
>
> <do-append-xml-element expression=".." name="jdbc:statement"/>
>
> <do-append-xml-element expression="../jdbc:statement[last()]" name="jdbc:sql"/>
>
> <do-append-xml-text expression="../jdbc:statement[last()]/jdbc:sql">
>   <arg-string>
>     <token-text> UPDATE dirxml.emp SET fname = '</token-text>
>     <token-op-attr name="Given Name"/>
>     <token-text>' </token-text>
>   </arg-string>
> </do-append-xml-text>
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
> | **before** | **CDATA**   XPATH 1.0 expression evalutated relative to each of the nodes select by *expression* that returns a node-set containing the child node(s) which the new element(s) should be inserted before. | #IMPLIED |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **expression** | **CDATA**   XPATH 1.0 expression that returns a node-set containing the element(s) to which the new element(s) should be added. | #REQUIRED |
> | **name** | **CDATA**   tag name of the element *supports variable expansion  after expansion, must be a legal [XML QName](http://www.w3.org/TR/REC-xml-names/#ns-qualnames)  may contain a namespace prefix if and only if that prefix maps to an [available namespace definition](policy.html#ns)* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
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
|| [**Tree**](DTD-TREE.html#do-append-xml-element)

---

[DirXMLScript DTD](index.html)

</details>


</details>
