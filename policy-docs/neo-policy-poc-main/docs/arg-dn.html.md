DirXMLScript DTD: arg-dn element



# arg-dn

The **<arg-dn>** argument specifies a DN
value for the enclosing action. Each of the
enclosed tokens is evaluated and the resulting
string values are concatenated to form a DN value.

### Example

> See **[<do-add-association>](do-add-association.html).**

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**token-added-entitlement**](token-added-entitlement.html)
> :   the value(s) of an entitlement granted in the
>     current operation
>
> [**token-association**](token-association.html)
> :   the association value from the current operation
>
> [**token-attr**](token-attr.html)
> :   the value(s) of an attribute in the current
>     operation or current object in the source datastore
>
> [**token-base64-decode**](token-base64-decode.html)
> :   decode base64 data into a string
>
> [**token-base64-encode**](token-base64-encode.html)
> :   encode a string into base64 data
>
> [**token-char**](token-char.html)
> :   a unicode character
>
> [**token-class-name**](token-class-name.html)
> :   the object class name from the current operation
>
> [**token-convert-time**](token-convert-time.html)
> :   convert a date/time from one format to another
>
> [**token-dest-attr**](token-dest-attr.html)
> :   the value(s) of an attribute of current object in
>     the destination datastore
>
> [**token-dest-dn**](token-dest-dn.html)
> :   a value derived from the destination DN from the
>     current operation
>
> [**token-dest-name**](token-dest-name.html)
> :   the unqualified RDN derived from destination DN
>     from the current operation
>
> [**token-document**](token-document.html)
> :   read an XML document
>
> [**token-entitlement**](token-entitlement.html)
> :   the value(s) of a granted entitlement of the
>     current object
>
> [**token-escape-for-dest-dn**](token-escape-for-dest-dn.html)
> :   convert a string for use in a destination DN
>
> [**token-escape-for-src-dn**](token-escape-for-src-dn.html)
> :   convert a string for use in a source DN
>
> [**token-generate-password**](token-generate-password.html)
> :   generate a random password
>
> [**token-global-variable**](token-global-variable.html)
> :   the value of a global variable
>
> [**token-join**](token-join.html)
> :   join a node-set into a string
>
> [**token-json-object**](token-json-object.html)
> :   constructs a JSON string
>
> [**token-json-array**](token-json-array.html)
> :   constructs a JSON array
>
> [**token-local-variable**](token-local-variable.html)
> :   the value of a local variable
>
> [**token-lower-case**](token-lower-case.html)
> :   convert a string to lower case
>
> [**token-named-password**](token-named-password.html)
> :   the value of the named password
>
> [**token-map**](token-map.html)
> :   map a string through a mapping table
>
> [**token-op-attr**](token-op-attr.html)
> :   the value(s) of an attribute in the current
>     operation
>
> [**token-op-property**](token-op-property.html)
> :   the value of an operation property
>
> [**token-operation**](token-operation.html)
> :   the name of the current operation
>
> [**token-parse-dn**](token-parse-dn.html)
> :   parse and/or convert a DN
>
> [**token-password**](token-password.html)
> :   the value of the password in current operation
>
> [**token-query**](token-query.html)
> :   query the source or destination datastore
>
> [**token-removed-attr**](token-removed-attr.html)
> :   the value(s) of an attribute removed in the current
>     operation
>
> [**token-removed-entitlement**](token-removed-entitlement.html)
> :   the value(s) of an entitlement revoked in the
>     current operation
>
> [**token-replace-all**](token-replace-all.html)
> :   replace all instances of a substring within a
>     string
>
> [**token-replace-first**](token-replace-first.html)
> :   replace a single instance of a substring within a
>     string
>
> [**token-resolve**](token-resolve.html)
> :   resolve a DN to an association key or an
>     association key to a DN.
>
> [**token-split**](token-split.html)
> :   split a string into a node-set
>
> [**token-src-attr**](token-src-attr.html)
> :   the value(s) of an attribute of current object in
>     the source datastore
>
> [**token-src-dn**](token-src-dn.html)
> :   a value derived from the source DN from the current
>     operation
>
> [**token-src-name**](token-src-name.html)
> :   the unqualified RDN derived from source DN from the
>     current operation
>
> [**token-substring**](token-substring.html)
> :   substring of a string
>
> [**token-text**](token-text.html)
> :   constant text
>
> [**token-time**](token-time.html)
> :   the current date/time
>
> [**token-unique-name**](token-unique-name.html)
> :   a generated unique name
>
> [**token-unmatched-src-dn**](token-unmatched-src-dn.html)
> :   a DN relative to the one matched by if-src-dn
>
> [**token-upper-case**](token-upper-case.html)
> :   convert a string to upper case
>
> [**token-xml-parse**](token-xml-parse.html)
> :   parse XML
>
> [**token-xml-serialize**](token-xml-serialize.html)
> :   serialize XML
>
> [**token-xpath**](token-xpath.html)
> :   the result of an XPATH expression
>
> ---

## 2. No Attributes

## 3. Content Rule

> ( [token-added-entitlement](token-added-entitlement.html) | [token-association](token-association.html) | [token-attr](token-attr.html) |
> [token-base64-decode](token-base64-decode.html) | [token-base64-encode](token-base64-encode.html) | [token-char](token-char.html) |
> [token-class-name](token-class-name.html) | [token-convert-time](token-convert-time.html) | [token-dest-attr](token-dest-attr.html) |
> [token-dest-dn](token-dest-dn.html) | [token-dest-name](token-dest-name.html) | [token-document](token-document.html) | [token-entitlement](token-entitlement.html) |
> [token-escape-for-dest-dn](token-escape-for-dest-dn.html) | [token-escape-for-src-dn](token-escape-for-src-dn.html) |
> [token-generate-password](token-generate-password.html) | [token-global-variable](token-global-variable.html) | [token-join](token-join.html) |
> [token-json-object](token-json-object.html) | [token-json-array](token-json-array.html) | [token-local-variable](token-local-variable.html) |
> [token-lower-case](token-lower-case.html) | [token-named-password](token-named-password.html) | [token-map](token-map.html) | [token-op-attr](token-op-attr.html) |
> [token-op-property](token-op-property.html) | [token-operation](token-operation.html) | [token-parse-dn](token-parse-dn.html) | [token-password](token-password.html) |
> [token-query](token-query.html) | [token-removed-attr](token-removed-attr.html) | [token-removed-entitlement](token-removed-entitlement.html) |
> [token-replace-all](token-replace-all.html) | [token-replace-first](token-replace-first.html) | [token-resolve](token-resolve.html) | [token-split](token-split.html) |
> [token-src-attr](token-src-attr.html) | [token-src-dn](token-src-dn.html) | [token-src-name](token-src-name.html) | [token-substring](token-substring.html) |
> [token-text](token-text.html) | [token-time](token-time.html) | [token-unique-name](token-unique-name.html) | [token-unmatched-src-dn](token-unmatched-src-dn.html) |
> [token-upper-case](token-upper-case.html) | [token-xml-parse](token-xml-parse.html) | [token-xml-serialize](token-xml-serialize.html) | [token-xpath](token-xpath.html)
> ) \* 
>
> ---


<details>
<summary><strong>Parent Elements</strong></summary>


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
> [**do-add-resource**](do-add-resource.html)
> :   request the assignment of a Resource to an Identity
>
> [**do-add-role**](do-add-role.html)
> :   request the assignment of a Role to an Identity
>
> [**do-add-src-attr-value**](do-add-src-attr-value.html)
> :   add a value to an attribute in the source datastore
>
> [**do-add-src-object**](do-add-src-object.html)
> :   add an object in the source datastore
>
> [**do-clear-dest-attr-value**](do-clear-dest-attr-value.html)
> :   clear all values of an attribute in the destination
>     datastore
>
> [**do-clear-src-attr-value**](do-clear-src-attr-value.html)
> :   clear all values of an attribute in the source
>     datastore
>
> [**do-clear-sso-credential**](do-clear-sso-credential.html)
> :   clear a credential in an SSO credential store
>
> [**do-delete-dest-object**](do-delete-dest-object.html)
> :   delete an object in the destination datastore
>
> [**do-delete-src-object**](do-delete-src-object.html)
> :   delete an object in the source datastore
>
> [**do-find-matching-object**](do-find-matching-object.html)
> :   automatically associate the current object
>
> [**do-move-dest-object**](do-move-dest-object.html)
> :   move an object in the destination datastore
>
> [**do-move-src-object**](do-move-src-object.html)
> :   move an object in the source datastore
>
> [**do-remove-dest-attr-value**](do-remove-dest-attr-value.html)
> :   remove a value from an attribute in the destination
>     datastore
>
> [**do-remove-named-password**](do-remove-named-password.html)
> :   Remove a Named Password
>
> [**do-remove-resource**](do-remove-resource.html)
> :   request the revocation of a Resource for an Identity
>
> [**do-remove-role**](do-remove-role.html)
> :   request the revocation of a Role from an Identity
>
> [**do-remove-src-attr-value**](do-remove-src-attr-value.html)
> :   remove a value from an attribute in the source
>     datastore
>
> [**do-rename-dest-object**](do-rename-dest-object.html)
> :   rename an object in the destination datastore
>
> [**do-rename-src-object**](do-rename-src-object.html)
> :   rename an object in the source datastore
>
> [**do-set-dest-attr-value**](do-set-dest-attr-value.html)
> :   set the value of an attribute in the destination
>     datastore
>
> [**do-set-dest-password**](do-set-dest-password.html)
> :   set the password for an object in the destination
>     datastore
>
> [**do-set-named-password**](do-set-named-password.html)
> :   Set/Create a Named Password
>
> [**do-set-op-dest-dn**](do-set-op-dest-dn.html)
> :   set the destination DN for the current operation
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
> [**do-start-workflow**](do-start-workflow.html)
> :   start a workflow
>
> [**if-dest-attr**](if-dest-attr.html)
> :   test an attribute of the current object or specified object in the
>     destination datastore
>
> [**if-src-attr**](if-src-attr.html)
> :   test an attribute of current object or specified object in the source
>     datastore
>
> [**token-dest-attr**](token-dest-attr.html)
> :   the value(s) of an attribute of current object in
>     the destination datastore
>
> [**token-query**](token-query.html)
> :   query the source or destination datastore
>
> [**token-resolve**](token-resolve.html)
> :   resolve a DN to an association key or an
>     association key to a DN.
>
> [**token-src-attr**](token-src-attr.html)
> :   the value(s) of an attribute of current object in
>     the source datastore
>
> [**token-unique-name**](token-unique-name.html)
> :   a generated unique name

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#arg-dn)

---

[DirXMLScript DTD](index.html)

</details>


</details>
