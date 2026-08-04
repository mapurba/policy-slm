DirXMLScript DTD: do-find-matching-object element



# do-find-matching-object

The **<do-find-matching-object>** action
causes a query to be performed in the destination
datastore and an appropriate dest-dn or an
appropriate dest-dn <association> to be added
to the [current
operation](policy.html#current_operation). It replaces the functionality
available via <matching-rule> in DirXML 1.x.
It is only valid when the [current
operation](policy.html#current_operation) is <add>.

[<arg-dn>](arg-dn.html) is required
when scope="entry" and optional otherwise.

At least one [<arg-match-attr>](arg-match-attr.html)
or [<arg-query-condition>](arg-query-condition.html)
is required when scope="subtree" or
scope="subordinates". Note that since it is
undefined what <query> does with
<search-attr> when scope="entry", it is also
undefined what <do-find-matching-object> will
do.

The <query> generated will have a scope
attribute based on the scope attribute of the
<do-find-matching-object>. It will have a
dest-dn attribute set to the content of [<arg-dn>](arg-dn.html),
if any. It will have a class-name attribute and
<search-class> based on the class-name
attribute from the [current
object](policy.html#current_object). For each [<arg-match-attr>](arg-match-attr.html)
there will be a <search-attr> for the same
attribute, populated with either the [<arg-value>](arg-value.html) content
of [<arg-match-attr>](arg-match-attr.html)
(if it exists) or the value(s) available in the [current
operation](policy.html#current_operation). If no value is available, then no
query will be performed and the action will not
find a match.

Any <instance> elements returned from the
query will be considered matches.

If the destination datastore is the application,
then an association will be added to the [current
operation](policy.html#current_operation) for each <instance> that is returned.
No query will be performed if the [current
operation](policy.html#current_operation) already has a non-empty association, thus allowing multiple
<do-find-matching-object> actions to be strung together in the same rule.
If no more than one instance is returned, then the local variable
*error.do-find-matching-object* will be unavailable. If more than one
<instance> is returned, then the local variable
*error.do-find-matching-object* will be set to a node-set containing the
list of src-dn's from the instances if they are available,
or the list of associations if the src-dn's are not available.

If the destination datastore is eDirectory, then the dest-dn
attribute for the [current
operation](policy.html#current_operation) will be set. No query will be performed if
the [current
operation](policy.html#current_operation) already has a non-empty dest-dn attribute,
thus allowing multiple <do-find-matching-object> action to be strung
together in the same rule. If only a single <instance> is
returned and that <instance> is not already associated
then the dest-dn of the [current
operation](policy.html#current_operation) is set to the src-dn of
the <instance> and the local variable *error.do-find-matching-object*
will be unavailable. If only a single <instance> is returned and
that <instance> is already associated then the dest-dn of the
[current
operation](policy.html#current_operation) is set to the single character &#xFFFC; and the local variable
*error.do-find-matching-object* will be set to the src-dn from that <instance>.
If multiple <instance>'s are returned then the dest-dn of
the [current
operation](policy.html#current_operation) is
set to the single character &#xFFFD; and the local variable *error.do-find-matching-object*
will be set to a node-set containing the src-dn's from those <instance>'s.

The operation property *error.do-find-matching-object* for
the [current
operation](policy.html#current_operation) will also be set to the value of the local variable
*error.do-find-matching-object*.

When the attribute **return-on-first-match = true** , this attribute will be appended to the resultant <query>, the Driver Shim or
Engine will interprest this query into multiple search criteria*(i.e each of <search-condition> or <search-attr> will be treated as a seperate search criteria and expected to have the attribute search-criteria-id set)* and are executed sequentially in the same order as received.  
As and when a non-empty result is received for particular search criteria or sub query, the associated search-criteria-id will be appended to the instance documents and returned. We exit from the query execution i.e we will not proceed to the next search-criteria when a match has been found.   
**Note:** The support for return-on-first-match depends on the implementation in the target Driver Shim.

### Example

> ```
> <do-find-matching-object scope="subordinates">
>   <arg-dn>
> 	<token-text>Users/</token-text>
> 	<token-attr name="OU"/>
>   </arg-dn>
>   <arg-match-attr name="CN"/>
>   <arg-match-attr name="L">
> 	<arg-value>
> 	  <token-text>Provo</token-text>
> 	</arg-value>
>   </arg-match-attr>
>   <arg-query-condition name="or">
> 	<arg-match-attr name="Given Name"/>
> 	<arg-query-condition name="not">
> 	  <arg-match-attr name="Title">
> 		<arg-value type="string">
> 		  <token-text xml:space="preserve">SSE</token-text>
> 		</arg-value>
> 	  </arg-match-attr>
> 	</arg-query-condition>
>   </arg-query-condition>
> </do-find-matching-object>
>
> <do-find-matching-object return-on-first-match="true" scope="subtree">
>   <arg-match-attr name="L" search-criteria-id="locationMatch">
> 	<arg-value type="string">
>       <token-text xml:space="preserve">Bangalore</token-text>
> 	</arg-value>
>   </arg-match-attr>
>   <arg-query-condition name="and" search-criteria-id="requiredAttributeCombination">
> 	<arg-match-attr name="Surname"/>
> 	<arg-match-attr name="Given Name"/>
>   </arg-query-condition>
> </do-find-matching-object>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-dn**](arg-dn.html)
> :   DN argument
>
> [**arg-match-attr**](arg-match-attr.html)
> :   match attribute argument
>
> [**arg-query-condition**](arg-query-condition.html)
> :   query condition argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
> | **return-on-first-match** | true   |  false   determines the behavior of the resultant query | false |
> | **scope** | entry   |  subordinates   |  subtree   the scope to be searched | subtree |
>
> ---

## 3. Content Rule

> (( [arg-dn](arg-dn.html) ? ,
> ( [arg-match-attr](arg-match-attr.html) | [arg-query-condition](arg-query-condition.html) ) + ) |
> ( [arg-dn](arg-dn.html) ,
> ( [arg-match-attr](arg-match-attr.html) | [arg-query-condition](arg-query-condition.html) ) \* ) ) 
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
|| [**Tree**](DTD-TREE.html#do-find-matching-object)

---

[DirXMLScript DTD](index.html)

</details>


</details>
