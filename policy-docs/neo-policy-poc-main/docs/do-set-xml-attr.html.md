DirXMLScript DTD: do-set-xml-attr element



# do-set-xml-attr

The **<do-set-xml-attr>** action causes a
custom XML attribute named by the name attribute to
be set on the set of elements selected by
expression.

### Example

> ```
>
> <do-set-xml-attr expression="." name="cert-id">
>   <arg-string>
>     <token-text>c:\lotus\domino\data\eng.id</token-text>
>   </arg-string>
> </do-set-xml-attr>
>
> <do-set-xml-attr expression="." name="cert-pwd">
>   <arg-string>
>     <token-text>certify2eng</token-text>
>   </arg-string>
> </do-set-xml-attr>
>
> ```

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
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **expression** | **CDATA**   XPATH 1.0 expression that returns a node-set containing the elements(s) on which the XML attribute should be set | #REQUIRED |
> | **name** | **CDATA**   tag name of the XML attribute  *supports variable expansion  after expansion, must be a legal [XML QName](http://www.w3.org/TR/REC-xml-names/#ns-qualnames)  may contain a namespace prefix if and only if that prefix maps to an [available namespace definition](policy.html#ns)* | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#do-set-xml-attr)

---

[DirXMLScript DTD](index.html)

</details>


</details>
