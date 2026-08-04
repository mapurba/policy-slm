DirXMLScript DTD: and element



# and

**<and>** specifies a set of tests that
are to be performed and whose results are to be
logically and'ed together. A set of <and>'s
enclosed by a [<conditions>](conditions.html) are
or'ed together.

### Example

> See **[<policy>](policy.html).**

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**if-association**](if-association.html)
> :   test association
>
> [**if-attr**](if-attr.html)
> :   test an attribute in the current operation or
>     current object in the source datastore
>
> [**if-class-name**](if-class-name.html)
> :   test the object class of the current operation
>
> [**if-dest-attr**](if-dest-attr.html)
> :   test an attribute of the current object or specified object in the
>     destination datastore
>
> [**if-dest-dn**](if-dest-dn.html)
> :   test the destination DN of the current operation
>
> [**if-entitlement**](if-entitlement.html)
> :   test an entitlement of the current object
>
> [**if-op-entitlement**](if-op-entitlement.html)
> :   test an entitlement of the current object in the current operation
>
> [**if-global-variable**](if-global-variable.html)
> :   test a global variable
>
> [**if-local-variable**](if-local-variable.html)
> :   test a local variable
>
> [**if-named-password**](if-named-password.html)
> :   test a named password
>
> [**if-op-attr**](if-op-attr.html)
> :   test an attribute in the current operation
>
> [**if-op-property**](if-op-property.html)
> :   test an operation property
>
> [**if-operation**](if-operation.html)
> :   test the name of the current operation
>
> [**if-password**](if-password.html)
> :   test the password of the current operation
>
> [**if-src-attr**](if-src-attr.html)
> :   test an attribute of current object or specified object in the source
>     datastore
>
> [**if-src-dn**](if-src-dn.html)
> :   test the source DN of the current operation
>
> [**if-xml-attr**](if-xml-attr.html)
> :   test an XML attribute of the current operation
>
> [**if-xpath**](if-xpath.html)
> :   test an xpath expression
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
>
> ---

## 3. Content Rule

> ( [if-association](if-association.html) | [if-attr](if-attr.html) | [if-class-name](if-class-name.html) | [if-dest-attr](if-dest-attr.html) | [if-dest-dn](if-dest-dn.html) |
> [if-entitlement](if-entitlement.html) | [if-op-entitlement](if-op-entitlement.html) | [if-global-variable](if-global-variable.html) |
> [if-local-variable](if-local-variable.html) | [if-named-password](if-named-password.html) | [if-op-attr](if-op-attr.html) | [if-op-property](if-op-property.html) |
> [if-operation](if-operation.html) | [if-password](if-password.html) | [if-src-attr](if-src-attr.html) | [if-src-dn](if-src-dn.html) | [if-xml-attr](if-xml-attr.html) |
> [if-xpath](if-xpath.html) ) \* 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**arg-conditions**](arg-conditions.html)
> :   conditions argument
>
> [**conditions**](conditions.html)
> :   conditions under which the actions of a
>     <rule> are performed

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#and)

---

[DirXMLScript DTD](index.html)

</details>


</details>
