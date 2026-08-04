DirXMLScript DTD: conditions element



# conditions

The **<conditions>** under which the [<actions>](actions.html) of the
enclosing [<rule>](rule.html) are performed.
The <conditions> are always specified in [Conjunctive Normal
Form](http://mathworld.wolfram.com/ConjunctiveNormalForm.html) (CNF) or [Disjunctive Normal
Form](http://mathworld.wolfram.com/DisjunctiveNormalForm.html) (DNF). As such the content of
<conditions> is either a disjunction of
conjunctions specified by a (possibly empty) set of
[<and>](and.html)'s
or a conjunction of disjunctions specified by a
(possibly empty) set of [<or>](or.html)'s. The [<actions>](actions.html) of the
enclosing [<rule>](rule.html) are only
performed when the logical expression represented
in CNF or DNF evaluates to TRUE or when no
conditions are specified.

The evaluation of the conditions uses short circuit
logic such that no additional tests are performed
once it is possible to determine the resultant
boolean value of the <conditions>.

All individual condition tests are represented by
an element of the form <if-\* op="some
operator">.

Some condition tests have a mode parameter that
indicates the algorithm to use for comparisons. The
following table details the modes that are
available.

> | mode | Description |
> | --- | --- |
> | case | Character by character case sensitive comparison. |
> | nocase | Character by character case insensitive comparison. |
> | regex | Regular expression match of entire string. Case insensitive by default, but may be changed by an escape in the expression.  See <http://java.sun.com/j2se/1.4/docs/api/java/util/regex/Pattern.html> and [http://java.sun.com/j2se/1.4/docs/api/java/util/regex/Matcher.html#matches()](http://java.sun.com/j2se/1.4/docs/api/java/util/regex/Matcher.html#matches%28%29).  Note that pattern option CASE\_INSENSITIVE, DOTALL, and UNICODE\_CASE are used but can be reversed using the appropriate embedded escapes. |
> | src-dn | Compare using semantics appropriate to the DN format for the source datastore. |
> | dest-dn | Compare using semantics appropriate to the DN format for the destination datastore. |
> | numeric | Compare numerically. |
> | octet | Compare octet (Base64 encoded) values. |
> | structured | Compare structured attribute according to the comparison rules for the structured syntax of the attribute. |

### Example

> See **[<policy>](policy.html).**

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**and**](and.html)
> :   logical conjunction
>
> [**or**](or.html)
> :   logical disjunction
>
> ---

## 2. No Attributes

## 3. Content Rule

> ( [and](and.html) \* | [or](or.html) \* ) 
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
|| [**Tree**](DTD-TREE.html#conditions)

---

[DirXMLScript DTD](index.html)

</details>


</details>
