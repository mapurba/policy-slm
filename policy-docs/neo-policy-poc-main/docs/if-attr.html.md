DirXMLScript DTD: if-attr element



# if-attr

**<if-attr>** performs a test on attribute
values of the [current
object](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/policy.html#current_object) in either the [current
operation](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/policy.html#current_operation) or the source datastore. It can
logically be thought of as equivalent to:

> ```
> <or>
>   <if-op-attr/>
>   <if-src-attr/>
> </or>
>
> ```

The type of test performed depends on the operator
specified by the op attribute. The following table
shows the type of test performed by each operator.

The condition works in 2 phases. In the first phase it checks if the value in the operation matches the given condition. If not in the second phase , a query is fired to the data source to fetch the values associated with the operation. If it matches, it proceeds with action.

> | operator | Returns true when... |
> | --- | --- |
> | available | there is a value available in either the [current operation](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/policy.html#current_operation) or the source datastore for the specified attribute. |
> | equal | there is a value available in either the [current operation](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/policy.html#current_operation) or the source datastore for the specified attribute that equals the content of **the condition when compared using the specified comparison mode. If mode="structured" then the content must be a set of [<component>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/component.html)'s, otherwise it must be text.**  ***Supports variable expansion*.** |
> | lt | there is a value available in either the [current operation](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/policy.html#current_operation) or the source datastore for the specified attribute that is less than the content of **the condition when compared using the specified comparison mode.**  ***Supports variable expansion*.** |
> | gt | there is a value available in either the [current operation](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/policy.html#current_operation) or the source datastore for the specified attribute that is greater than the content of **the condition when compared using the specified comparison mode.**  ***Supports variable expansion*.** |
> | not-available | available would return false. |
> | not-equal | equal would return false. |
> | not-lt | lt would return false. |
> | not-gt | gt would return false. |

### Examples

> ```
> <if-attr name="OU" op="available"/>
>
> <if-attr mode="nocase" name="OU" op="equal">Sales</if-attr>
>
> <if-attr mode="structured" name="Language" op="equal">
>   <component name="string">EN</component>
>   <component name="string">JP</component>
> </if-attr>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> #PCDATA
>
> [**component**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/component.html)
> :   value component
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **mode** | case   |  nocase   |  regex   |  src-dn   |  dest-dn   |  numeric   |  octet   |  structured   comparison [mode](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/conditions.html#mode) if op implies a comparison | nocase |
> | **name** | **CDATA**   name of the attribute  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **op** | available   |  equal   |  lt   |  gt   |  not-available   |  not-equal   |  not-lt   |  not-gt   test operator | #REQUIRED |
>
> ---

## 3. Content Rule

> ( #PCDATA | [component](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/component.html) ) \* 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**and**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/and.html)
> :   logical conjunction
>
> [**or**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/or.html)
> :   logical disjunction

---

[**Top Elements**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/TOP-ELEM.html) ||
[**All Elements**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/ALL-ELEM.html)
|| [**Tree**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/DTD-TREE.html#if-attr)

---

[DirXMLScript DTD](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/index.html)

</details>


</details>
