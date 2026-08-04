DirXMLScript DTD: do-status element



# do-status

The **<do-status>** action causes a status
notification to be generated with the specified
level and with a message provided by [<arg-string>](arg-string.html).

If level is *retry* then the policy will
immediately halt processing of the input document
and schedule a retry of the event currently being
processed.

If level is *fatal* then the policy will
immediately halt processing of the input document
and initiate a shutdown of the driver.

If a the [current
operation](policy.html#current_operation) has an event-id, then that event-id
will by used for the status notification, otherwise
there will be no event-id reported.

### Example

> ```
>
> <do-status level="warning">
>   <arg-string>
>     <token-src-dn/>
>     <token-text>: operation vetoed on out-of-scope object</token-text>
>   </arg-string>
> </do-status>
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
> | **level** | **CDATA**   status level  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
>
> ---

## 3. Content Rule

> ( [arg-string](arg-string.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-status)

---

[DirXMLScript DTD](index.html)

</details>


</details>
