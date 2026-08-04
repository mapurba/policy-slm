DirXMLScript DTD: if-op-attr element



# if-op-attr

**<if-op-attr>** performs a test on
attribute values in the [current
operation](policy.html#current_operation).

> | operator | Returns true when... |
> | --- | --- |
> | available | there is a value available in the [current operation](policy.html#current_operation) (<add-attr>, <add-value> or <attr>) for the specified attribute. Available would return false if there is only a <remove-value> or a <remove-all-values> value for the specified attribute. |
> | changing | the [current operation](policy.html#current_operation) contains a change (<modify-attr> or <add-attr>) of the specified attribute. Changing would return true if it is an <add-attr>, <add-value>, <remove-value>, or <remove-all-values> operations for the specified attribute. |
> | changing-from | the [current operation](policy.html#current_operation) contains a change that removes a value (<remove-value>) of the specified attribute that equals the content of the condition when compared using the specified comparison mode. If mode="structured" then the content must be a set of [<component>](component.html)'s, otherwise it must be text. |
> | changing-to | the [current operation](policy.html#current_operation) contains a change that adds a value (<add-value> or <add-attr>) to the specified attribute that equals the content of the condition when compared using the specified comparison mode. If mode="structured" then the content must be a set of [<component>](component.html)'s, otherwise it must be text. |
> | equal | there is a value available in the [current operation](policy.html#current_operation) (other than a <remove-value>) for the specified attribute that equals the content of the condition when compared using the specified comparison mode. If mode="structured" then the content must be a set of [<component>](component.html)'s, otherwise it must be text.  *Supports variable expansion.* |
> | lt | there is a value available in the [current operation](policy.html#current_operation) (other than a <remove-value>) for the specified attribute that is less than the content of the condition when compared using the specified comparison mode. If mode="structured" then the content must be a set of [<component>](component.html)'s, otherwise it must be text.  *Supports variable expansion.* |
> | gt | there is a value available in the [current operation](policy.html#current_operation) (other than a <remove-value>) for the specified attribute that is greater than the content of the condition when compared using the specified comparison mode. If mode="structured" then the content must be a set of [<component>](component.html)'s, otherwise it must be text.  *Supports variable expansion.* |
> | not-available | available would return false. |
> | not-changing | changing would return false. |
> | not-changing-from | changing-from would return false. |
> | not-changing-to | changing-to would return false. |
> | not-equal | equal would return false. |
> | not-lt | lt would return false. |
> | not-gt | gt would return false. |

### Examples

> ```
>
> <if-op-attr name="OU" op="available"/>
>
> <if-op-attr name="OU" op="changing"/>
>
> <if-op-attr name="OU" op="changing-from">Sales</if-op-attr>
>
> <if-op-attr name="OU" op="changing-to">Sales</if-op-attr>
>
> <if-op-attr mode="nocase" name="OU" op="equal">Sales</if-op-attr>
>
> <if-op-attr mode="structured" name="Language" op="equal">
>   <component name="string">EN</component>
>   <component name="string">JP</component>
> </if-op-attr>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> #PCDATA
>
> [**component**](component.html)
> :   value component
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **mode** | case   |  nocase   |  regex   |  src-dn   |  dest-dn   |  numeric   |  octet   |  structured   comparison [mode](conditions.html#mode) if op="equal" or op="not-equal" or op="changing-from" or op="changing-to" | nocase |
> | **name** | **CDATA**   name of the attribute    *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **op** | available   |  changing   |  changing-from   |  changing-to   |  equal   |  lt   |  gt   |  not-available   |  not-changing   |  not-changing-from   |  not-changing-to   |  not-equal   |  not-lt   |  not-gt   test operator | #REQUIRED |
>
> ---

## 3. Content Rule

> ( #PCDATA | [component](component.html) ) \* 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**and**](and.html)
> :   logical conjunction
>
> [**or**](or.html)
> :   logical disjunction

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#if-op-attr)

---

[DirXMLScript DTD](index.html)

</details>


</details>
