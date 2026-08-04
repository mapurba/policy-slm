DirXMLScript DTD: comment element



# comment

A **<comment>** is a long description
and/or other textual information relating to the
containing [<rule>](rule.html). It does not
affect the execution of the [<rule>](rule.html).

A comment may have a name which may have special
meaning to a user interface agent that displays or
edits the rule. Policy Builder currently supports
one instance per rule of an unnamed comment, and
one instance each of comments with the names
*author*, *version*, and
*lastChanged*. Additional named and unnamed
comments are allowed but will be ignored by Policy
Builder.

### Example

> See **[<policy>](policy.html).**

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> #PCDATA
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **name** | **CDATA**   name of the comment | #IMPLIED |
>
> ---

## 3. Content Rule

> ( #PCDATA ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**rule**](rule.html)
> :   rule within a policy

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#comment)

---

[DirXMLScript DTD](index.html)

</details>


</details>
