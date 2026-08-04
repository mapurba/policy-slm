DirXMLScript DTD: if-entitlement element



# if-entitlement

**<if-entitlement>** performs a test on
entitlements of the [current
object](policy.html#current_object) in either the [current
operation](policy.html#current_operation) or the eDirectory datastore.

> | operator | Returns true when... |
> | --- | --- |
> | available | the named entitlement is available and granted in either the [current operation](policy.html#current_operation) or the eDirectory datastore |
> | changing | the [current operation](policy.html#current_operation) contains a change (grant or revoke) of the named entitlement. |
> | changing-from | the [current operation](policy.html#current_operation) contains a change that revokes a value of the named entitlement that has a value that equals the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | changing-to | the [current operation](policy.html#current_operation) contains a change that grants a value of the named entitlement that has a value that equals the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | equal | the named entitlement is available and granted in either the [current operation](policy.html#current_operation) or the eDirectory datastore and has a value that equals the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | lt | the named entitlement is available and granted in either the [current operation](policy.html#current_operation) or the eDirectory datastore and has a value that is less than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
> | gt | the named entitlement is available and granted in either the [current operation](policy.html#current_operation) or the eDirectory datastore and has a value that is greater than the content of the condition when compared using the specified comparison mode.  *Supports variable expansion.* |
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
> <if-entitlement name="notes-group" op="available"/>
>
> <if-entitlement name="notes-group" op="changing"/>
>
> <if-entitlement name="notes-group" op="changing-from">Sales</if-entitlement>
>
> <if-entitlement name="notes-group" op="changing-to">Sales</if-entitlement>
>
> <if-entitlement mode="nocase" name="notes-group" op="equal">Sales</if-entitlement>
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
> | **mode** | case   |  nocase   |  regex   |  src-dn   |  dest-dn   |  numeric   |  octet   comparison [mode](conditions.html#mode) if op="equal" or op="not-equal" or op="changing-from" or op="changing-to" | nocase |
> | **name** | **CDATA**   name of the entitlement    *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **op** | available   |  changing   |  changing-from   |  changing-to   |  equal   |  lt   |  gt   |  not-available   |  not-changing   |  not-changing-from   |  not-changing-to   |  not-equal   |  not-lt   |  not-gt   test operator | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#if-entitlement)

---

[DirXMLScript DTD](index.html)

</details>


</details>
