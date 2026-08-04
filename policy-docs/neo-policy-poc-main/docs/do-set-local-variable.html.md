DirXMLScript DTD: do-set-local-variable element



# do-set-local-variable

The **<do-set-local-variable>** action
causes a local variable with the given name to be
set to the string value specified by [<arg-string>](arg-string.html), the
XPATH 1.0 Node Set specified by [<arg-node-set>](arg-node-set.html),
or the Java Object specified by [<arg-object>](arg-object.html).

### Examples

> ```
>
> <do-set-local-variable name="lastName" scope="policy">
>   <arg-string>
>     <token-attr name="Surname"/>
>   </arg-string>
> </do-set-local-variable>
>
> <do-set-local-variable name="lastName" scope="policy">
>   <arg-node-set>
>     <token-attr name="Surname"/>
>   </arg-node-set>
> </do-set-local-variable>
>
> <do-set-local-variable name="lastName">
>   <arg-object>
>     <token-xpath expression="jrandom:new()"/>
>   </arg-object>
> </do-set-local-variable>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-string**](arg-string.html)
> :   string argument
>
> [**arg-node-set**](arg-node-set.html)
> :   node set argument
>
> [**arg-object**](arg-object.html)
> :   Java Object argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **name** | **CDATA**   name of the variable  *supports variable expansion*  *after expansion, must be a legal XML [Name](http://www.w3.org/TR/2004/REC-xml-20040204/#NT-Name)* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **scope** | policy   |  driver   scope of the variable     **policy** - variable is visible only within the current policy during the current invocation of the policy     **driver** - variable is visible to all policies within the current driver until the driver is stopped  *supports variable expansion* | policy |
>
> ---

## 3. Content Rule

> ( [arg-string](arg-string.html) | [arg-node-set](arg-node-set.html) | [arg-object](arg-object.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-set-local-variable)

---

[DirXMLScript DTD](index.html)

</details>


</details>
