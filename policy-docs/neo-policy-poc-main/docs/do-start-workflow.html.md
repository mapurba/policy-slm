DirXMLScript DTD: do-start-workflow element



# do-start-workflow

The **<do-start-workflow>** action starts
the workflow specified by *workflow-id* for
the recipient specified by [<arg-dn>](arg-dn.html) on the User
Application server specified by *url* using
credentials specified by *id* and [<arg-password>](arg-password.html).
The recipient must be an LDAP format DN of an
object in the directory served by the User
Application server. The additional arguments to the
workflow may be specified by named [<arg-string>](arg-string.html)'s.
Multiple values can be specified delimited by a *semi-colon(**;**)*. In case, a *semi-colon(**;**)*
is part of the value, then it should be escaped by using a *backslash(**\**)*
The number of the strings and the names used are
dependent on the workflow to be started.
There are some names that have special meaning and are available regardless of the workflow being started.

> | Name | Description |
> | --- | --- |
> | :InitiatorOverrideDN | The LDAP format DN of the initiator of the workflow, if other than the User used to authenticate. |
> | :CorrelationID | An identifier used to correlate related workflows. Default: Operation event correlation id is used if no value is specified. |

There will be one of these two local variables available to the enclosing policy
depending on the success or failure of this request.  

* *success.do-start-workflow* : This local variable will be available only if
  the workflow is started successfully. And it contains the Instance id of the provisioning request.
* *error.do-start-workflow* : This local variable will be available only if any
  type of error occurs while starting the workflow. And it contains the error string.

### Example

> ```
>
> <do-start-workflow id="cn=WorkflowAdmin,o=People" url="http://localhost:8080/IDMProv" workflow-id="CN=ApproveCellPhone,CN=RequestDefs,CN=AppConfig,CN=UserApplication,CN=DriverSet,O=novell" time-out="30000">
>   <arg-password>
>     <token-named-password name="workflow-admin"/>
>   </arg-password>
>   <arg-dn>
>     <token-parse-dn dest-dn-format="ldap" src-dn-format="qualified-slash">
>       <token-xpath expression="@qualified-src-dn"/>
>     </token-parse-dn>
>   </arg-dn>
>   <arg-string name="provider">
>     <token-text>ACMEWireless</token-text>
>   </arg-string>
>   <arg-string name="reason">
>     <token-text>new hire</token-text>
>   </arg-string>
>   <arg-string name="email">
>     <token-text>jmiller@acme.com; jack.miller@gmail.com; jackm@outlook.com</token-text>
>   </arg-string>
>   <arg-string name="text">
>     <token-text>one, two, and three\; a, b, and c\; first, second, and third</token-text>
>   </arg-string>
> </do-start-workflow>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-password**](arg-password.html)
> :   password argument
>
> [**arg-dn**](arg-dn.html)
> :   DN argument
>
> [**arg-string**](arg-string.html)
> :   string argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **id** | **CDATA**   the LDAP format DN of a user authorized to start workflows on the User Application server *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **time-out** | **CDATA**   the number of milliseconds to wait to establish a connection to the User Application server before timing out.  *supports variable expansion* | 0 |
> | **url** | **CDATA**   the URL of the User Application server where the worflow will run  *supports variable expansion* | #REQUIRED |
> | **workflow-id** | **CDATA**   the LDAP format DN of the workflow to start *supports variable expansion* | #REQUIRED |
>
> ---

## 3. Content Rule

> ( [arg-password](arg-password.html) , [arg-dn](arg-dn.html) , [arg-string](arg-string.html) \* ) 
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
|| [**Tree**](DTD-TREE.html#do-start-workflow)

---

[DirXMLScript DTD](index.html)

</details>


</details>
