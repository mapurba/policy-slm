DirXMLScript DTD: if-dest-attr element



# if-dest-attr

**<if-dest-attr>** performs a test on
attribute values of the [current
object](policy.html#current_object) or the object resolved using the specified [<arg-dn>](arg-dn.html) or
[<arg-association>](arg-association.html)
in the destination datastore. The type
of test performed depends on the operator specified
by the op attribute. The following table shows the
type of test performed by each operator.

> | operator | Returns true when... |
> | --- | --- |
> | available | there is a value available in the destination datastore for the specified attribute. |
> | equal | there is a value available for the specified attribute in the destination datastore that equals the content of the condition when compared using the specified comparison mode. If mode="structured" then the content must be a set of [<component>](component.html)'s, otherwise it must be text.  *Supports variable expansion.* |
> | lt | there is a value available for the specified attribute in the destination datastore that is less than the content of the condition when compared using the specified comparison mode. If mode="structured" then the content must be a set of [<component>](component.html)'s, otherwise it must be text.  *Supports variable expansion.* |
> | gt | there is a value available for the specified attribute in the destination datastore that is greater than the content of the condition when compared using the specified comparison mode. If mode="structured" then the content must be a set of [<component>](component.html)'s, otherwise it must be text.  *Supports variable expansion.* |
> | not-available | available would return false. |
> | not-equal | equal would return false. |
> | not-lt | lt would return false. |
> | not-gt | gt would return false. |

### Examples

> ```
>
> <if-dest-attr name="OU" op="available"/>
>
> <if-dest-attr mode="nocase" name="OU" op="equal">Sales</if-dest-attr>
>
> <if-dest-attr mode="structured" name="Language" op="equal">
>   <component name="string">EN</component>
>   <component name="string">JP</component>
> </if-dest-attr>
>
> <if-dest-attr class-name="User" name="Surname" op="equal">
> 	<arg-association>
> 		<token-text>IDU=34131,table=USR,schema=INDIRECT
> 		</token-text>
> 	</arg-association>
> 	<value>Burrows</value>
> </if-dest-attr>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-dn**](arg-dn.html)
> :   DN argument
>
> [**arg-association**](arg-association.html)
> :   association argument
>
> [**value**](value.html)
> :   value
>
> [**component**](component.html)
> :   value component
>
> #PCDATA
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **class-name** | **CDATA**   class name of target object  *supports variable expansion*   *required when [<arg-dn>](arg-dn.html) or [<arg-association>](arg-association.html) is being used* | #IMPLIED |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **mode** | case   |  nocase   |  regex   |  src-dn   |  dest-dn   |  numeric   |  octet   |  structured   comparison [mode](conditions.html#mode) if op implies a comparison | nocase |
> | **name** | **CDATA**   name of the attribute  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **op** | available   |  equal   |  lt   |  gt   |  not-available   |  not-equal   |  not-lt   |  not-gt   test operator | #REQUIRED |
>
> ---

## 3. Content Rule

> ((( [arg-dn](arg-dn.html) | [arg-association](arg-association.html) ) ,
> ( [value](value.html) ? | [component](component.html) \* ) ) ? |
> ( #PCDATA | [component](component.html) ) \* ) 
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
|| [**Tree**](DTD-TREE.html#if-dest-attr)

---

[DirXMLScript DTD](index.html)

</details>


</details>
