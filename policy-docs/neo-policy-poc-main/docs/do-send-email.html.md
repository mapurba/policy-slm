DirXMLScript DTD: do-send-email element



# do-send-email

The **<do-send-email>** action causes an
email notification to be sent to the specified
server. Optional credentials for authentication to
the SMTP server are provided by the id attribute
and [<arg-password>](arg-password.html).
The type attribute identifies if the email message
contains plain text or HTML data. The various email
addresses, subject and message are provided within
[<arg-string>](arg-string.html)
elements and corresponding tag name attributes.

> | Tag Name | Description |
> | --- | --- |
> | to | Adds the address to the list of email recipients.  *Multiple instances are allowed.  May contain a comma separated list of recipients.* |
> | cc | Adds the address to the list of CC email recipients.  *Multiple instances are allowed.  May contain a comma separated list of recipients.* |
> | bcc | Adds the address to the list of BCC email recipients.  *Multiple instances are allowed.  May contain a comma separated list of recipients.* |
> | from | Specifies the address to be used as the originating email address. |
> | reply-to | Specifies the address to be used as the email message reply address. |
> | subject | Specifies the email subject. |
> | message | Specifies the content of the email message. |
> | encoding | Specifies the character encoding to use for the email message. |
> | custom-smtp-header | Specifies a custom SMTP header to add to the email message. |
> | The following string arguments are only applicable if the mail server is set for modern authentication: | |
> | tenant-id | Specifies the Global Unique Identifier (GUID) for your registered account on Azure Active Directory. Also referred to as the Tenant (Directory) ID. Use the Azure portal to obtain the value. |
> | client-id | Specifies the unique ID assigned by Azure Active Directory to your application. Also referred to as the Application (client) ID. Use the Azure portal to obtain the value. |
> | client-secret | Specifies a secret string that the application uses to prove its identity when requesting an access token. This encrypted value is unique for your application. Use the Azure portal to obtain the value. |
> | oauth-scope | Specifies the resource for which the token is granted during token redemption. It defines what the application can access on behalf of the user. It should be https://outlook.office365.com/.default for SMTP. The access token issued to the application is limited to the scope granted. |
> | grant-type | Used by the application to obtain an access token to access its own resources, not on behalf of a user. It is set to client\_credentials by default and should not be modified. |
> | requestURL | Specifies the request URI of the SMTP server, to which the application sends authentication requests containing client secret, scope, grant type, and auth mechanism in the payload. For example, https://login.microsoftonline.com/{tenantID}/oauth2/v2.0/token |
> | auth-mechanism | Specifies the format to use to encode and transmit the access token to the SMTP server. The access token authenticates the user's Outlook account. It is set to XOAUTH2 by default and should not be modified. |

If any type of error occurs as part of sending the
email, the error string will be available to the
enclosing policy in the local variable named
*error.do-send-email*. Otherwise that local
variable will be unavailable.

### Example

> ```
>
> <do-send-email id="user" server="smtp.company.com" type="text">
>   <arg-password>
>     <token-named-password name="email-server"/>
>   </arg-password>
>   <arg-string name="to">
>     <token-text>to_user1@company.com</token-text>
>   </arg-string>
>   <arg-string name="to">
>     <token-text>to_user2@company.com</token-text>
>   </arg-string>
>   <arg-string name="cc">
>     <token-text>cc_user@company.com</token-text>
>   </arg-string>
>   <arg-string name="bcc">
>     <token-text>bcc_user@company.com</token-text>
>   </arg-string>
>   <arg-string name="from">
>     <token-text>from_user@company.com</token-text>
>   </arg-string>
>   <arg-string name="subject">
>     <token-text>This is the email subject</token-text>
>   </arg-string>
>   <arg-string name="message">
>     <token-text>This is the email body</token-text>
>   </arg-string>
>   <arg-string name="custom-smtp-header">
>     <token-text>X-Priority: 1(Highest)</token-text>
>   </arg-string>
>   <arg-string name="tentant-id">
>     <token-text>tenant-ID</token-text>
>   </arg-string>
>   <arg-string name="cleint-id">
>     <token-text>cleint-ID</token-text>
>   </arg-string>
>   <arg-string name="client-secret">
>     <token-text>tenant-ID</token-text>
>   </arg-string>
>   <arg-string name="oauth-scope">
>     <token-text>https://outlook.office365.com/.default</token-text>
>   </arg-string>
>   <arg-string name="grant-type">
>     <token-text>client_credentials</token-text>
>   </arg-string>
>   <arg-string name="request-url">
>     <token-text>https://login.microsoftonline.com/0ec1e3e1-6010-4de9-b9fa-ce6f52504e8e/oauth2/v2.0/token</token-text>
>   </arg-string>
>   <arg-string name="auth-mechanism">
>     <token-text>XOAUTH2</token-text>
>   </arg-string>
> </do-send-email>
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
> | **id** | **CDATA**   user account on SMTP server  *supports variable expansion* | #IMPLIED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **password** | **CDATA**   password for user on SMTP server  *deprecated - use [<arg-password>](arg-password.html) with [<token-named-password>](token-named-password.html) instead* | #IMPLIED |
> | **server** | **CDATA**   DNS name or IP address of SMTP server  *supports variable expansion* | #REQUIRED |
> | **type** | text   |  html   identifies if email message contains plain text or HTML data | text |
>
> ---

## 3. Content Rule

> ( [arg-password](arg-password.html) ? , [arg-string](arg-string.html) \* ) 
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
|| [**Tree**](DTD-TREE.html#do-send-email)

---

[DirXMLScript DTD](index.html)

</details>


</details>
