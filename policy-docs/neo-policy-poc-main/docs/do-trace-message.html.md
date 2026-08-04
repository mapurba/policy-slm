DirXMLScript DTD: do-trace-message element



# do-trace-message

The **<do-trace-message>** action causes
the trace message provided by [<arg-string>](arg-string.html)to
DSTRACE if the specified level is less than or
equal to the currently configured trace level.

Example

> ```
>
> <do-trace-message color="blue" level="0">
>   <arg-string>
>     <token-text>placing new object at </token-text>
>     <token-dest-dn/>
>   </arg-string>
> </do-trace-message>
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
> | **color** | black   |  blue   |  green   |  cyan   |  red   |  purple   |  brown   |  grey   |  drgrey   |  brblue   |  brgreen   |  brcyan   |  brred   |  brpurple   |  yellow   |  white   color of text to emit | brpurple |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **level** | **CDATA**   minimum trace level at which to emit message | 0 |
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
|| [**Tree**](DTD-TREE.html#do-trace-message)

---

[DirXMLScript DTD](index.html)

</details>


</details>
