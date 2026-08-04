DirXMLScript DTD: do-invoke-rest-endpoint element



# do-invoke-rest-endpoint

The **<do-invoke-rest-endpoint>** action initiates a REST request to the endpoint specified by *url* using
the authentication method specified by *auth-method*. The type of the request(POST, PUT, GET, DELETE) should be
specified by *type*. If the authentication method is oauth2, then the authentication url is specified by *auth-url*.
The request is made using credentials specified by *id* and [<arg-password>](arg-password.html).
Additional optional arguments to the REST request may be specified by named
[<arg-string>](arg-string.html)'s.

> | Name | Description |
> | --- | --- |
> | payload | Payload for the REST request |
> | truststore | Trust store. |
> | truststorepwd | Trust store password. |
> | auth-query-name | Authentication Query Name. |
> | auth-query-name | Authentication Query Value. |
> | auth-header-name | Authentication Header Name |
> | auth-header-value | Authentication Header Value |
> | operation-header-name | Operation Header Name |
> | operation-header-value | Operation Header Value |

There will be one of these two local variables available to the enclosing policy
depending on the success or failure of this request.  

* *success.do-invoke-rest-endpoint* : This local variable will be available only if
  the endpoint is invoked successfully
* *error.do-invoke-rest-endpoint* : This local variable will be available only if any
  type of error occurs while invoking the endpoint. And it contains the error string.

### Example

> ```
>
> <do-invoke-rest-endpoint 
> 	auth-method="oauth2" auth-url="https://164.99.90.85:8543/osp/a/idm/auth/oauth2/grant" 
> 	id="dcsdrv" time-out="30000" 
> 	type="POST" url="https://164.99.90.85:8543/IDMProv/rest/catalog/resources">
>   <arg-password>
> 	<token-text xml:space="preserve">novell</token-text>
>   </arg-password>
>   <arg-string name="auth-query-name">
> 	<token-text>grant_type</token-text>
>   </arg-string>
>   <arg-string name="auth-query-value">
> 	<token-text>password</token-text>
>   </arg-string>
>   <arg-string name="auth-query-name">
> 	<token-text>username</token-text>
>   </arg-string>
>   <arg-string name="auth-query-value">
> 	<token-text>cn=uaadmin,ou=sa,o=data</token-text>
>   </arg-string>
>   <arg-string name="auth-query-name">
> 	<token-text>password</token-text>
>   </arg-string>
>   <arg-string name="auth-query-value">
> 	<token-text>novell</token-text>
>   </arg-string>
>   <arg-string name="auth-header-name">
> 	<token-text>Content-Type</token-text>
>   </arg-string>
>   <arg-string name="auth-header-value">
> 	<token-text>application/x-www-form-urlencoded</token-text>
>   </arg-string>
>   <arg-string name="truststore">
> 	<token-text>/root/9085tomcat.ks</token-text>
>   </arg-string>
>   <arg-string name="keystore">
> 	<token-text>/root/9085tomcat.ks</token-text>
>   </arg-string>
>   <arg-string name="keystorepwd">
> 	<token-text>novell</token-text>
>   </arg-string>
>   <arg-string name="truststorepwd">
> 	<token-text>novell</token-text>
>   </arg-string>
>   <arg-string name="operation-header-name">
> 	<token-text>content-type</token-text>
>   </arg-string>
>   <arg-string name="operation-header-value">
> 	<token-text>application/json</token-text>
>   </arg-string>
>   <arg-string name="payload">
> 	<token-local-variable name="resourceJsonPayload"/>
>   </arg-string>
> </do-invoke-rest-endpoint>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-password**](arg-password.html)
> :   password argument
>
> [**arg-string**](arg-string.html)
> :   string argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **auth-method** | **CDATA**   the authentication method to use. Either basic or oauth2  *supports variable expansion* | #REQUIRED |
> | **auth-url** | **CDATA**   the authentication url. Needed only when auth-method is oauth2  *supports variable expansion* | #REQUIRED |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **id** | **CDATA**   Admin ID *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **time-out** | **CDATA**   the number of milliseconds to wait to establish a connection to the User Application server before timing out.  *supports variable expansion* | 0 |
> | **type** | **CDATA**   API request type (POST | PUT | GET | DELETE). Default: *false* | #REQUIRED |
> | **url** | **CDATA**   the Endpoint URL   *supports variable expansion* | #REQUIRED |
>
> ---

## 3. Content Rule

> ( [arg-password](arg-password.html) , [arg-string](arg-string.html) \* ) 
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
|| [**Tree**](DTD-TREE.html#do-invoke-rest-endpoint)

---

[DirXMLScript DTD](index.html)

</details>


</details>
