DirXMLScript DTD: token-query element



# token-query

**<token-query>** causes a [<query>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/ndsdtd/query.html) to be
performed in the source or destination datastore
and returns the resulting [<instance>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/ndsdtd/instance.html)'s.

The datastore to search is specified by
*datastore.*

The base of the query is specified by either [<arg-dn>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-dn.html)
or [<arg-association>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-association.html).
If neither are specified, then the base will be the
root of the datastore.

The scope of the query is specified by
*query*.

The class of the query is specified by
*class-name*. If omitted the query will look
for all classes.

The set of attributes to search for is specified by
the [<arg-match-attr>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-match-attr.html)'s.

When there is only one [<arg-query-condition>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-query-condition.html) element, only objects that satisfy the given condition will be selected.

When there are a combination of [<arg-query-condition>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-query-condition.html) and [<arg-match-attr>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-match-attr.html) elements, only the objects that satisfy the conditions defined in the [<arg-query-condition>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-query-condition.html) elements **and** match all the attribute values specified in the [<arg-match-attr>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-match-attr.html) elements will be selected.

The set of attributes to return is specified by the
[<arg-string>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-string.html)'s.
If no [<arg-string>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-string.html) are
specified then no attributes will be read. If one
of the [<arg-string>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-string.html)
evaluates to the asterisk character, then all
attributes will be read.

If *max-result-count* is specified, then [<query-ex>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/ndsdtd/query-ex.html)
will be issued instead of a [<query>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/ndsdtd/query-ex.html)
and the results will be returned in batches. When
used in the context of a [<do-for-each>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/do-for-each.html)
subsequent batches (if any) will be automatically
retrieved.

If *get-token* is specified as false, then token is not fetched in the query-ex. This is done, in case the query-ex is fired within a do-for-each loop and the expected result is a one time query. This was introduced to prevent needlessly fetching tokens for one time queries.Default behavior is to always fetch the token.

Refer [<token-text>](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-text.html) for limitations on using special characters in search values.

### Example

> ```
> <token-query class-name="User" datastore="dest" scope="subordinates">
>   <arg-dn>
> 	<token-text>Users/</token-text>
> 	<token-attr name="OU"/>
>   </arg-dn>
>   <arg-match-attr name="CN"/>
>   <arg-match-attr name="Title"/>
>   <arg-query-condition name="or">
> 	<arg-match-attr name="L">
> 	  <arg-value>
> 		<token-text>Provo</token-text>
> 	  </arg-value>
> 	</arg-match-attr>
> 	<arg-match-attr name="L">
> 	  <arg-value>
> 		<token-text>Bangalore</token-text>
> 	  </arg-value>
> 	</arg-match-attr>
>   </arg-query-condition>
>   <arg-string>
> 	<token-text>Surname</token-text>
>   </arg-string>
>   <arg-string>
> 	<token-text>Given Name</token-text>
>   </arg-string>
> </token-query>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-dn.html)
> :   DN argument
>
> [**arg-association**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-association.html)
> :   association argument
>
> [**arg-match-attr**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-match-attr.html)
> :   match attribute argument
>
> [**arg-query-condition**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-query-condition.html)
> :   query condition argument
>
> [**arg-string**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-string.html)
> :   string argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **class-name** | **CDATA**   class name of target object  *supports variable expansion*   the class name of the query  *supports variable expansion* | #IMPLIED |
> | **datastore** | src   |  dest   the datastore to be queried | dest |
> | **max-result-count** | **CDATA**   the maximum number of results to return per batch | #IMPLIED |
> | **notrace** | true   |  false   *true* if this element should not be traced during execution of policy | false |
> | **get-token** | true   |  false   *false* if the query-ex is a one time query running within a loop. This would prevent tokens from getting fetched. Setting it to true is the default behavior of query-ex.Default behavior is to always fetch the token. | true |
>   
> | **scope** | entry   |  subordinates   |  subtree   the scope of the query | subtree |
>
> ---

## 3. Content Rule

> (( [arg-dn](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-dn.html) | [arg-association](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-association.html) ) ? ,
> ( [arg-match-attr](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-match-attr.html) | [arg-query-condition](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-query-condition.html) ) \* , [arg-string](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-string.html) \* ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**arg-association**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-association.html)
> :   association argument
>
> [**arg-component**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-component.html)
> :   component argument
>
> [**arg-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-dn.html)
> :   DN argument
>
> [**arg-node-set**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-node-set.html)
> :   node set argument
>
> [**arg-password**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-password.html)
> :   password argument
>
> [**arg-string**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-string.html)
> :   string argument
>
> [**arg-value**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/arg-value.html)
> :   value argument
>
> [**token-base64-decode**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-base64-decode.html)
> :   decode base64 data into a string
>
> [**token-base64-encode**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-base64-encode.html)
> :   encode a string into base64 data
>
> [**token-convert-time**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-convert-time.html)
> :   convert a date/time from one format to another
>
> [**token-escape-for-dest-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-escape-for-dest-dn.html)
> :   convert a string for use in a destination DN
>
> [**token-escape-for-src-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-escape-for-src-dn.html)
> :   convert a string for use in a source DN
>
> [**token-join**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-join.html)
> :   join a node-set into a string
>
> [**token-lower-case**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-lower-case.html)
> :   convert a string to lower case
>
> [**token-map**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-map.html)
> :   map a string through a mapping table
>
> [**token-map-source-col**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-map-source-col.html)
> :   used in token-map to have multiple source columns
>
> [**token-parse-dn**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-parse-dn.html)
> :   parse and/or convert a DN
>
> [**token-replace-all**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-replace-all.html)
> :   replace all instances of a substring within a
>     string
>
> [**token-replace-first**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-replace-first.html)
> :   replace a single instance of a substring within a
>     string
>
> [**token-split**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-split.html)
> :   split a string into a node-set
>
> [**token-substring**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-substring.html)
> :   substring of a string
>
> [**token-upper-case**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-upper-case.html)
> :   convert a string to upper case
>
> [**token-xml-parse**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-xml-parse.html)
> :   parse XML
>
> [**token-xml-serialize**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/token-xml-serialize.html)
> :   serialize XML

---

[**Top Elements**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/TOP-ELEM.html) ||
[**All Elements**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/ALL-ELEM.html)
|| [**Tree**](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/DTD-TREE.html#token-query)

---

[DirXMLScript DTD](https://www.netiq.com/documentation/identity-manager-developer/dtd-documentation/dirxmlscript/index.html)

</details>


</details>
