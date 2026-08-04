DirXMLScript DTD: actions element



# actions

The [<actions>](actions.html) that are
performed when [<conditions>](conditions.html) of
the enclosing [<rule>](rule.html) are met. All
individual actions are represented by an element of
the form <do-\*>.

Most actions take arguments that further describe
the action to be taken. Arguments that take a fixed
string that will never change at run-time are
represented by attributes on the action element.
Arguments that can be re-evaluated at run-time are
represented by child elements of the form
<arg-\*>. The content of most (exceptions
noted on the documentation for the individual
arguments) of these arguments consists of a set of
tokens represented by elements of the form
<token-\*>. The individual tokens are expanded
at run-time based on the rule evaluation context
and the results of the expansion of are
concatenated together to form the actual argument.

*NOTE:*
For the tokens that support regular expression, Identity Manager evaluates the following special characters in the regular expression context:  
\ $ ^.? \* + [ ] ( ) |

To use these characters as literals in a regular expression, escape the character with a backslash (“\”).

### Example

> See **[<policy>](policy.html).**

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**do-add-association**](do-add-association.html)
> :   associate the current object
>
> [**do-add-dest-attr-value**](do-add-dest-attr-value.html)
> :   add a value to an attribute in the destination
>     datastore
>
> [**do-add-dest-object**](do-add-dest-object.html)
> :   add an object in the destination datastore
>
> [**do-add-src-attr-value**](do-add-src-attr-value.html)
> :   add a value to an attribute in the source datastore
>
> [**do-add-src-object**](do-add-src-object.html)
> :   add an object in the source datastore
>
> [**do-add-role**](do-add-role.html)
> :   request the assignment of a Role to an Identity
>
> [**do-add-resource**](do-add-resource.html)
> :   request the assignment of a Resource to an Identity
>
> [**do-append-xml-element**](do-append-xml-element.html)
> :   append a custom XML element to existing elements
>
> [**do-append-xml-text**](do-append-xml-text.html)
> :   append custom XML text to existing elements
>
> [**do-break**](do-break.html)
> :   stop processing the current operation with this
>     policy
>
> [**do-clear-dest-attr-value**](do-clear-dest-attr-value.html)
> :   clear all values of an attribute in the destination
>     datastore
>
> [**do-clear-op-property**](do-clear-op-property.html)
> :   clear an operation property
>
> [**do-clear-src-attr-value**](do-clear-src-attr-value.html)
> :   clear all values of an attribute in the source
>     datastore
>
> [**do-clear-sso-credential**](do-clear-sso-credential.html)
> :   clear a credential in an SSO credential store
>
> [**do-clone-op-attr**](do-clone-op-attr.html)
> :   apply all operations on an attribute in the current
>     operation to a different attribute
>
> [**do-clone-xpath**](do-clone-xpath.html)
> :   clone and append set of nodes to existing elements
>
> [**do-create-resource**](do-create-resource.html)
> :   create a resource
>
> [**do-create-role**](do-create-role.html)
> :   create a role
>
> [**do-delete-dest-object**](do-delete-dest-object.html)
> :   delete an object in the destination datastore
>
> [**do-delete-src-object**](do-delete-src-object.html)
> :   delete an object in the source datastore
>
> [**do-delete-resource**](do-delete-resource.html)
> :   delete a resource
>
> [**do-delete-role**](do-delete-role.html)
> :   delete a role
>
> [**do-find-matching-object**](do-find-matching-object.html)
> :   automatically associate the current object
>
> [**do-for-each**](do-for-each.html)
> :   repeat actions for each node in a node-set
>
> [**do-generate-event**](do-generate-event.html)
> :   generate an user defined event
>
> [**do-generate-xdas-event**](do-generate-xdas-event.html)
> :   generate an xdas event
>
> [**do-if**](do-if.html)
> :   conditionally perform actions
>
> [**do-implement-entitlement**](do-implement-entitlement.html)
> :   implement an entitlement
>
> [**do-invoke-rest-endpoint**](do-invoke-rest-endpoint.html)
> :   Invoke a REST Endpoint
>
> [**do-modify-resource**](do-modify-resource.html)
> :   modify a resource
>
> [**do-modify-role**](do-modify-role.html)
> :   modify a role
>
> [**do-move-dest-object**](do-move-dest-object.html)
> :   move an object in the destination datastore
>
> [**do-move-src-object**](do-move-src-object.html)
> :   move an object in the source datastore
>
> [**do-reformat-op-attr**](do-reformat-op-attr.html)
> :   change the format of all values of a particular
>     attribute in the current operation
>
> [**do-remove-association**](do-remove-association.html)
> :   disassociate an application object
>
> [**do-remove-dest-attr-value**](do-remove-dest-attr-value.html)
> :   remove a value from an attribute in the destination
>     datastore
>
> [**do-remove-named-password**](do-remove-named-password.html)
> :   Remove a Named Password
>
> [**do-remove-role**](do-remove-role.html)
> :   request the revocation of a Role from an Identity
>
> [**do-remove-resource**](do-remove-resource.html)
> :   request the revocation of a Resource for an Identity
>
> [**do-remove-src-attr-value**](do-remove-src-attr-value.html)
> :   remove a value from an attribute in the source
>     datastore
>
> [**do-rename-dest-object**](do-rename-dest-object.html)
> :   rename an object in the destination datastore
>
> [**do-rename-op-attr**](do-rename-op-attr.html)
> :   change an attribute name for all operations on that
>     attribute in the current operation
>
> [**do-rename-src-object**](do-rename-src-object.html)
> :   rename an object in the source datastore
>
> [**do-send-email**](do-send-email.html)
> :   generate an email notification
>
> [**do-send-email-from-template**](do-send-email-from-template.html)
> :   generate an email notification using SMTP
>     configuration and email template objects
>
> [**do-set-default-attr-value**](do-set-default-attr-value.html)
> :   set the default value for an attribute to be
>     created in the destination datastore
>
> [**do-set-dest-attr-value**](do-set-dest-attr-value.html)
> :   set the value of an attribute in the destination
>     datastore
>
> [**do-set-dest-password**](do-set-dest-password.html)
> :   set the password for an object in the destination
>     datastore
>
> [**do-set-local-variable**](do-set-local-variable.html)
> :   set the value of a local variable
>
> [**do-set-named-password**](do-set-named-password.html)
> :   Set/Create a Named Password
>
> [**do-set-op-association**](do-set-op-association.html)
> :   set that association value for the current
>     operation
>
> [**do-set-op-class-name**](do-set-op-class-name.html)
> :   set the object class name for the current operation
>
> [**do-set-op-dest-dn**](do-set-op-dest-dn.html)
> :   set the destination DN for the current operation
>
> [**do-set-op-property**](do-set-op-property.html)
> :   set an operation property
>
> [**do-set-op-src-dn**](do-set-op-src-dn.html)
> :   set the source DN for the current operation
>
> [**do-set-op-template-dn**](do-set-op-template-dn.html)
> :   set the template DN for the current add operation
>
> [**do-set-src-attr-value**](do-set-src-attr-value.html)
> :   set the value of an attribute in the source
>     datastore
>
> [**do-set-src-password**](do-set-src-password.html)
> :   set the password for an object in the source
>     datastore
>
> [**do-set-sso-credential**](do-set-sso-credential.html)
> :   set a credential in an SSO credential store
>
> [**do-set-sso-passphrase**](do-set-sso-passphrase.html)
> :   set a passphrase in an SSO credential store
>
> [**do-set-xml-attr**](do-set-xml-attr.html)
> :   set custom XML attribute on existing elements
>
> [**do-start-workflow**](do-start-workflow.html)
> :   start a workflow
>
> [**do-status**](do-status.html)
> :   report status
>
> [**do-strip-op-attr**](do-strip-op-attr.html)
> :   strip an attribute from the current operation
>
> [**do-strip-xpath**](do-strip-xpath.html)
> :   strip arbitrary data from the current operation
>
> [**do-trace-message**](do-trace-message.html)
> :   emit trace message
>
> [**do-veto**](do-veto.html)
> :   veto the current operation
>
> [**do-veto-if-op-attr-not-available**](do-veto-if-op-attr-not-available.html)
> :   veto the current operation if a particular
>     attribute is not available in the operation
>
> [**do-while**](do-while.html)
> :   repeat actions while a conditions are true
>
> ---

## 2. No Attributes

## 3. Content Rule

> ( [do-add-association](do-add-association.html) | [do-add-dest-attr-value](do-add-dest-attr-value.html) | [do-add-dest-object](do-add-dest-object.html) |
> [do-add-src-attr-value](do-add-src-attr-value.html) | [do-add-src-object](do-add-src-object.html) | [do-add-role](do-add-role.html) |
> [do-add-resource](do-add-resource.html) | [do-append-xml-element](do-append-xml-element.html) | [do-append-xml-text](do-append-xml-text.html) |
> [do-break](do-break.html) | [do-clear-dest-attr-value](do-clear-dest-attr-value.html) | [do-clear-op-property](do-clear-op-property.html) |
> [do-clear-src-attr-value](do-clear-src-attr-value.html) | [do-clear-sso-credential](do-clear-sso-credential.html) | [do-clone-op-attr](do-clone-op-attr.html) |
> [do-clone-xpath](do-clone-xpath.html) | [do-create-resource](do-create-resource.html) | [do-create-role](do-create-role.html) |
> [do-delete-dest-object](do-delete-dest-object.html) | [do-delete-src-object](do-delete-src-object.html) | [do-delete-resource](do-delete-resource.html) |
> [do-delete-role](do-delete-role.html) | [do-find-matching-object](do-find-matching-object.html) | [do-for-each](do-for-each.html) |
> [do-generate-event](do-generate-event.html) | [do-generate-xdas-event](do-generate-xdas-event.html) | [do-if](do-if.html) |
> [do-implement-entitlement](do-implement-entitlement.html) | [do-invoke-rest-endpoint](do-invoke-rest-endpoint.html) |
> [do-modify-resource](do-modify-resource.html) | [do-modify-role](do-modify-role.html) | [do-move-dest-object](do-move-dest-object.html) |
> [do-move-src-object](do-move-src-object.html) | [do-reformat-op-attr](do-reformat-op-attr.html) | [do-remove-association](do-remove-association.html) |
> [do-remove-dest-attr-value](do-remove-dest-attr-value.html) | [do-remove-named-password](do-remove-named-password.html) |
> [do-remove-role](do-remove-role.html) | [do-remove-resource](do-remove-resource.html) | [do-remove-src-attr-value](do-remove-src-attr-value.html) |
> [do-rename-dest-object](do-rename-dest-object.html) | [do-rename-op-attr](do-rename-op-attr.html) | [do-rename-src-object](do-rename-src-object.html) |
> [do-send-email](do-send-email.html) | [do-send-email-from-template](do-send-email-from-template.html) |
> [do-set-default-attr-value](do-set-default-attr-value.html) | [do-set-dest-attr-value](do-set-dest-attr-value.html) |
> [do-set-dest-password](do-set-dest-password.html) | [do-set-local-variable](do-set-local-variable.html) | [do-set-named-password](do-set-named-password.html) |
> [do-set-op-association](do-set-op-association.html) | [do-set-op-class-name](do-set-op-class-name.html) | [do-set-op-dest-dn](do-set-op-dest-dn.html) |
> [do-set-op-property](do-set-op-property.html) | [do-set-op-src-dn](do-set-op-src-dn.html) | [do-set-op-template-dn](do-set-op-template-dn.html) |
> [do-set-src-attr-value](do-set-src-attr-value.html) | [do-set-src-password](do-set-src-password.html) | [do-set-sso-credential](do-set-sso-credential.html) |
> [do-set-sso-passphrase](do-set-sso-passphrase.html) | [do-set-xml-attr](do-set-xml-attr.html) | [do-start-workflow](do-start-workflow.html) |
> [do-status](do-status.html) | [do-strip-op-attr](do-strip-op-attr.html) | [do-strip-xpath](do-strip-xpath.html) | [do-trace-message](do-trace-message.html) |
> [do-veto](do-veto.html) | [do-veto-if-op-attr-not-available](do-veto-if-op-attr-not-available.html) | [do-while](do-while.html) ) \* 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**rule**](rule.html)
> :   rule within a policy

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#actions)

---

[DirXMLScript DTD](index.html)

</details>


</details>
