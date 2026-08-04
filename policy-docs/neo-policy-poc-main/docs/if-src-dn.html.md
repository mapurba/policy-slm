DirXMLScript DTD: if-src-dn element



# if-src-dn

**<if-src-dn>** performs a test on the
source DN in the [current
operation](policy.html#current_operation).

> | operator | Returns true when... |
> | --- | --- |
> | available | there is a source DN available. |
> | equal | there is a source DN available and it equals the content of the condition when compared using semantics appropriate to the DN format of the source datastore.  *Supports variable expansion.* |
> | in-container | there is a source DN available and it represents an object in the container specified by the content of the condition when compared using semantics appropriate to the DN format of the source datastore. |
> | in-subtree | there is a source DN available and it represents an object in the subtree specified by the content of the condition when compared using semantics appropriate to the DN format of the source datastore. |
> | not-available | available would return false. |
> | not-equal | equal would return false. |
> | not-in-container | in-container would return false. |
> | not-in-subtree | in-subtree would return false. |

### Examples

> ```
>
> <if-src-dn op="available"/>
>
> <if-src-dn op="equal">Novell\Users\Fred</if-src-dn>
>
> <if-src-dn op="in-container">Novell\Users</if-src-dn>
>
> <if-src-dn op="in-subtree">Novell</if-src-dn>
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
|| [**Tree**](DTD-TREE.html#if-src-dn)

---

[DirXMLScript DTD](index.html)

</details>


</details>
