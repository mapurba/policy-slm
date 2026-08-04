DirXMLScript DTD: rule element



# rule

**A <rule>** specifies a set of [<actions>](actions.html) and a set
of [<conditions>](conditions.html) under
which those [<actions>](actions.html) are
performed.

### Example

> See **[<policy>](policy.html).**

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**description**](description.html)
> :   description of a <policy> or a <rule>
>
> [**comment**](comment.html)
> :   long description of a <rule>
>
> [**conditions**](conditions.html)
> :   conditions under which the actions of a
>     <rule> are performed
>
> [**actions**](actions.html)
> :   actions that are performed by a <rule>
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
>
> ---

## 3. Content Rule

> ( [description](description.html) ? , [comment](comment.html) \* , [conditions](conditions.html) , [actions](actions.html) ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**policy**](policy.html)
> :   a policy

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#rule)

---

[DirXMLScript DTD](index.html)

</details>


</details>
