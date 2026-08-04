DirXMLScript DTD: do-set-sso-passphrase element



# do-set-sso-passphrase

The **<do-set-sso-passphrase>** action
sets the passphrase question and answer specified
by [<arg-string>](arg-string.html)'s on
the object specified by [<arg-dn>](arg-dn.html) in the Single
Sign On credential store specified by
*store-def-dn*.

There will be one of these two local variables available to the enclosing policy
depending on the success or failure of this request.  

* *success.do-set-sso-passphrase* : This local variable will be available only if the
  SSO provider returns success.
* *error.do-set-sso-passphrase* : This local variable will be available only if the
  SSO provider returns any type of error . And it contains the error string.

### Example

> ```
>
> <do-set-sso-passphrase store-def-dn="../Library/SSO1">
>   <arg-dn>
>     <token-parse-dn dest-dn-format="ldap" length="-1" src-dn-format="src-dn" start="0">
>       <token-src-dn/>
>     </token-parse-dn>
>   </arg-dn>
>   <arg-string>
>     <token-text/>What favorite color <token-text/>
>   </arg-string>
>   <arg-string>
>     <token-text/>blue<token-text/>
>   </arg-string>
> </do-set-sso-passphrase>
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
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **store-def-dn** | **CDATA**   slash form DN of the credential store definition object  *may be relative to the including policy  supports variable expansion* | #REQUIRED |
>
> ---

## 3. Content Rule

> ( [arg-dn](arg-dn.html) , [arg-string](arg-string.html) , [arg-string](arg-string.html) ) 
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
|| [**Tree**](DTD-TREE.html#do-set-sso-passphrase)

---

[DirXMLScript DTD](index.html)

</details>


</details>
