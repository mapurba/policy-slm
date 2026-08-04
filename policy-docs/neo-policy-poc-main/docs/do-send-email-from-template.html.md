DirXMLScript DTD: do-send-email-from-template element



# do-send-email-from-template

The **<do-send-email-from-template>**
action causes an email notification to be generated
using a SMTP notification configuration object,
email template object and replacement tokens. The
target SMTP server along with credentials for
authentication (except for the password, which when
needed is specified by [<arg-password>](arg-password.html))
and the originating address are read from the SMTP
notification configuration object. Specifying a from address
overrides the originator's address specified in the mail
server configuration. The subject and
email message are created using the template object
and template replacement tokens. Replacement tokens
are declared within a [<arg-string>](arg-string.html)
element and tag name attribute. The value of
[<arg-string>'s](arg-string.html) tag attribute is
interpretted as html, if it is enclosed within
*<use-html>...</use-html>* tags. Reserved
replacement tokens specify the various recipient
addresses.

> | Reserved Token | Description |
> | --- | --- |
> | from | Specifies the sender address. |
> | to | Adds the address to the list of email recipients.  *Multiple instances are allowed.  May contain a comma separated list of recipients.* |
> | cc | Adds the address to the list of CC email recipients.  *Multiple instances are allowed.  May contain a comma separated list of recipients.* |
> | bcc | Adds the address to the list of BCC email recipients.  *Multiple instances are allowed.  May contain a comma separated list of recipients.* |
> | reply-to | Specifies the address to be used as the email message reply address. |
> | encoding | Specifies the character encoding to use for the email message. |
> | custom-smtp-header | Specifies a custom SMTP header to add to the email message. |
> | attachment | Specifies the attachments for the email message.   *The files/attachments should be placed in mt\_files directory.  Linux: /opt/novell/eDirectory/lib/dirxml/rules/manualtask/mt\_files   Windows: C:\NetIQ\IDM\eDirectory\mt\_files* |

If any type of error occurs as part of sending the
email, the error string will be available to the
enclosing policy in the local variable named
*error.do-send-email-from-template*. Otherwise
that local variable will be unavailable.

### Example

> ```
>
> <do-send-email-from-template notification-dn="/cn=security/cn=DefaultNotification Collection" template-dn="/cn=security/cn=DefaultNotification Collection/cn=PS-Sync Fail">
>   <arg-password>
>     <token-named-password name="email-server"/>
>   </arg-password>
>   <arg-string name="manager">
>     <token-text>Bill Jones</token-text>
>   </arg-string>
>   <arg-string name="surname">
>     <token-text>Smith</token-text>
>   </arg-string>
>   <arg-string name="given-name">
>     <token-text>Joe</token-text>
>   </arg-string>
>   <arg-string name="from">
>     <token-text>from_user@company.com</token-text>
>   </arg-string>
>   <arg-string name="to">
>     <token-text>to_user@company.com</token-text>
>   </arg-string>
>   <arg-string name="cc">
>     <token-text>cc_user@company.com</token-text>
>   </arg-string>
>   <arg-string name="attachment">
>     <token-text>attachment1, attachment2</token-text>
>   </arg-string>
>   <arg-string name="custom-smtp-header">
>     <token-text>X-Priority: 1(Highest)</token-text>
>   </arg-string>
>   <arg-string name="FailureReason">
>     <token-text><use-html><p>sample reason 1</p><p>sample reason 2</p></use-html></token-text>
>   </arg-string>
> </do-send-email-from-template>
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
> | **notification-dn** | **CDATA**   slash form DN of SMTP notification configuration object  *supports variable expansion* | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **password** | **CDATA**   password for user on SMTP server  *deprecated - use [<arg-password>](arg-password.html) with [<token-named-password>](token-named-password.html) instead* | #IMPLIED |
> | **template-dn** | **CDATA**   slash form DN of email template object  *supports variable expansion* | #REQUIRED |
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
|| [**Tree**](DTD-TREE.html#do-send-email-from-template)

---

[DirXMLScript DTD](index.html)

</details>


</details>
