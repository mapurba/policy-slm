DirXMLScript DTD: include element



# include

**<include>** causes the rules from the
policy referenced by the name attribute to be
included at runtime into the including policy as if
they were part of the including policy at the point
of inclusion.

The name attribute should be the slash form DN of
the object containing the policy to be included.
The DN may be relative to the including policy.

The inclusion is recursive in that a policy may
include other policies. It is an error for a policy
to directly or indirectly include itself.

### Example

> See **[<policy>](policy.html).**

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> EMPTY
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **name** | **CDATA**   the name of the policy to include | #REQUIRED |
>
> ---

## 3. Content Declaration

> Empty


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**policy**](policy.html)
> :   a policy

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#include)

---

[DirXMLScript DTD](index.html)

</details>


</details>
