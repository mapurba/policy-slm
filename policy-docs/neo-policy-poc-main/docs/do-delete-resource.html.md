DirXMLScript DTD: do-delete-resource element



# do-delete-resource

The **<do-delete-resource>** action initiates a request to the Roles Based
Provisioning Module (RBPM) to delete the Resource specified by *dn*. The
request is made to the RBPM enabled User Application server specified by *url*
using credentials specified by *id* and the first [<arg-password>](arg-password.html). This action uses IDM REST api which in turn uses
the OAuth2 protocol for authentication. The OSP client id needed for this authentication
should be specified by *osp-clientid*. And the client password should be
specified by the second [<arg-password>](arg-password.html).
Additional optional arguments to the Resource creation request may be specified by named
[<arg-string>](arg-string.html)'s.

There will be one of these two local variables available to the enclosing policy
depending on the success or failure of this request.  

* *success.do-delete-resource* : This local variable will be available only if
  the resource is deleted successfully. And it contains the DN of the created resource.
* *error.do-delete-resource* : This local variable will be available only if any
  type of error occurs while creating the resource. And it contains the error string.

### Example

> ```
>
> <do-delete-resource 
> 	id="CN=UAAdmin,OU=Sa,O=Data"
> 	osp-clientid="rbpm"
> 	url="http://localhost:8080/IDMProv"
> 	dn="CN=Printer,CN=ResourceDefs,CN=RoleConfig,CN=AppConfig,CN=User Application Driver,CN=driverset1,O=system"
> 	time-out="30000">
>   <arg-password>
>     <token-named-password name="resource-admin"/>
>   </arg-password>
>   <arg-password>
>     <token-named-password name="osp-client-secret"/>
>   </arg-password>
> </do-delete-resource>
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
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **id** | **CDATA**   the LDAP format DN of a user authorized to make the request *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **osp-clientid** | **CDATA**   the client id needed to authenticate to osp.  *supports variable expansion* | #REQUIRED |
> | **time-out** | **CDATA**   the number of milliseconds to wait to establish a connection to the User Application server before timing out.  *supports variable expansion* | 0 |
> | **url** | **CDATA**   the URL of the User Application server hosting RBPM  *supports variable expansion* | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#do-delete-resource)

---

[DirXMLScript DTD](index.html)

</details>


</details>
