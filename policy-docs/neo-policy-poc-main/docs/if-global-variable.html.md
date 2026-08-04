DirXMLScript DTD: if-global-variable element



# if-global-variable

**<if-global-variable>** performs a test
on a global configuration value (GCV). The type of
test performed depends on the operator specified by
the op attribute. The following table shows the
type of test performed by each operator.

> | operator | Returns true when... |
> | --- | --- |
> | available | there is a global configuration value with the specified name. |
> | equal | there is a global configuration value with the specified name and its value equals the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | lt | there is a global configuration value with the specified name and its value is less than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | gt | there is a global configuration value with the specified name and its value is greater than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | not-available | available would return false. |
> | not-equal | equal would return false. |
> | not-lt | lt would return false. |
> | not-gt | gt would return false. |

### Examples

> ```
>
> <if-global-variable name="myGlobalVariable" op="available"/>
>
> <if-global-variable mode="nocase" name="myGlobalVariable" op="equal">enabled</if-global-variable>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> #PCDATA
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **mode** | case   |  nocase   |  regex   |  src-dn   |  dest-dn   |  numeric   |  octet   comparison [mode](conditions.html#mode) if op implies a comparison | nocase |
> | **name** | **CDATA**   name of the variable  *supports variable expansion*  *after expansion, must be a legal XML [Name](http://www.w3.org/TR/2004/REC-xml-20040204/#NT-Name)* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **op** | available   |  equal   |  lt   |  gt   |  not-available   |  not-equal   |  not-lt   |  not-gt   test operator | #REQUIRED |
>
> ---

## 3. Content Rule

> ( #PCDATA ) 
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
|| [**Tree**](DTD-TREE.html#if-global-variable)

---

[DirXMLScript DTD](index.html)

</details>


</details>
