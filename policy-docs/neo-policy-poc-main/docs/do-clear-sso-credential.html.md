DirXMLScript DTD: do-clear-sso-credential element



# do-clear-sso-credential

The **<do-clear-sso-credential****>**
action clears a credential from the object
specified by [<arg-dn>](arg-dn.html) in the Single
Sign On credential store specified by
*store-def-dn* for the application specified
by *app-id*. Additional information about the
credential to be cleared may be specified by
additional named [<arg-string>](arg-string.html)'s.
The number of the strings and the names used are
dependent on the credential store and application
for which the credential is targeted.

There will be one of these two local variables available to the enclosing policy
depending on the success or failure of this request.  

* *success.do-clear-sso-credential* : This local variable will be available only if
  the SSO provider returns success.
* *error.do-clear-sso-credential* : This local variable will be available only if
  the SSO provider returns any type of error. And it will be of the form: <4-Digit Number>:<Text
  Description>.

### Example

> ```
>
> <do-clear-sso-credential app-id="AD7" store-def-dn="../Library/SSO1">
>   <arg-dn>
>     <token-parse-dn dest-dn-format="ldap" length="-1" src-dn-format="src-dn" start="0">
>       <token-src-dn/>
>     </token-parse-dn>
>   </arg-dn>
> </do-clear-sso-credential>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

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
> | **app-def-dn** | **CDATA**   DN of the application credential definition object  *only used by the UI so the various UI's should agree on the DN format used* | #IMPLIED |
> | **app-id** | **CDATA**   application ID for the credential *supports variable expansion* | #REQUIRED |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **store-def-dn** | **CDATA**   slash form DN of the credential store definition object  *may be relative to the including policy  supports variable expansion* | #REQUIRED |
>
> ---

## 3. Content Rule

> ( [arg-dn](arg-dn.html) , [arg-string](arg-string.html) \* ) 
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
|| [**Tree**](DTD-TREE.html#do-clear-sso-credential)

---

[DirXMLScript DTD](index.html)

</details>


</details>
