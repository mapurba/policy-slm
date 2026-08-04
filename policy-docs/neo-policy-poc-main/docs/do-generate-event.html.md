DirXMLScript DTD: do-generate-event element



# do-generate-event

The **<do-generate-event>** action causes
a Identity Manager user defined event to be sent to
NetIQ Audit service. Identity Manager user defined
event id's must be between the range of 1000 to
1999. Valid event levels are definend in the
following table. The remaining event data fields
are provided by four [<arg-string>](arg-string.html)
elements with name attributes. The NetIQ Audit
event structure contains two strings (text1, text2)
along with one integer (value) and generic field
(data). The two text fields are limited to 256
bytes while the data field may contain upto 3KB of
information.

> | Level | Description |
> | --- | --- |
> | log-emergency | Events that cause the Identity Manager metadirectory engine or driver to shutdown. |
> | log-alert | Events that require immediate attention. |
> | log-critical | Events that can cause parts of the Identity Manager metadirectory engine or driver to malfunction. |
> | log-error | Events describing errors which can be handled by the Identity Manager metadirectory engine or driver. |
> | log-warning | Negative events not representing a problem. |
> | log-notice | Events (positive or negative) an administrator can use to understand or improve use and operation. |
> | log-info | Positive events of any importance. |
> | log-debug | Events of relevance for support or engineers to debug operation of the Identity Manager metadirectory engine or driver. |

> | Tag | Description |
> | --- | --- |
> | text1 | Text entered here will be stored in the text1 event field. |
> | text2 | Text entered here will be stored in the text2 event field. |
> | value | Any number entered here will be stored in the value1 event field. |
> | data | Data entered here will be stored in the blob event field. |

### Example

> ```
>
> <do-generate-event id="1000" level="log-info">
>   <arg-string name="text1">
>     <token-text>User defined data for text1 field</token-text>
>   </arg-string>
>   <arg-string name="text2">
>     <token-text>User defined data for text2
> field</token-text>
>   </arg-string>
>   <arg-string name="value">
>     <token-text>-602</token-text>
>   </arg-string>
>   <arg-string name="data">
>     <token-text>User defined blob data</token-text>
>   </arg-string>
> </do-generate-event>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-string**](arg-string.html)
> :   string argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **id** | **CDATA**   Identity Manager user defined event id (1000-2000)  *supports variable expansion* | #REQUIRED |
> | **level** | log-emergency   |  log-alert   |  log-critical   |  log-error   |  log-warning   |  log-notice   |  log-info   |  log-debug   NetIQ Audit log level | log-info |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
>
> ---

## 3. Content Rule

> ( [arg-string](arg-string.html) \* ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**actions**](actions.html)
> :   actions that are performed by a <rule>
>
> [**arg-actions**](arg-actions.html)
> :   actions argument

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#do-generate-event)

---

[DirXMLScript DTD](index.html)

</details>


</details>
