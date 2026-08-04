DirXMLScript DTD: if-dest-dn element



# if-dest-dn

**<if-dest-dn>** performs a test on the
destination DN in the [current
operation](policy.html#current_operation).

> | operator | Returns true when... |
> | --- | --- |
> | available | there is a destination DN available. |
> | equal | there is a destination DN available and it equals the content of the condition when compared using semantics appropriate to the DN format of the destination datastore.  *Supports variable expansion.* |
> | in-container | there is a destination DN available and it represents an object in the container specified by the content of the condition when compared using semantics appropriate to the DN format of the destination datastore.  *Supports variable expansion.* |
> | in-subtree | there is a destination DN available and it represents and object in the subtree specified by the content of the condition when compared using semantics appropriate to the DN format of the destination datastore.  *Supports variable expansion.* |
> | not-available | available would return false. |
> | not-equal | equal would return false. |
> | not-in-container | in-container would return false. |
> | not-in-subtree | in-subtree would return false. |

### Examples

> ```
>
> <if-dest-dn op="available"/>
>
> <if-dest-dn op="equal">Novell\Users\Fred</if-dest-dn>
>
> <if-dest-dn op="in-container">Novell\Users</if-dest-dn>
>
> <if-dest-dn op="in-subtree">Novell</if-dest-dn>
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
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **op** | available   |  equal   |  in-container   |  in-subtree   |  not-available   |  not-equal   |  not-in-container   |  not-in-subtree   test operator | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#if-dest-dn)

---

[DirXMLScript DTD](index.html)

</details>


</details>
