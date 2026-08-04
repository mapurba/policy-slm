DirXMLScript DTD: component element



# component

The **<component>** provides values for
components of the enclosing condition if the
mode attribute of that condition is "structured".

### Example

> See **[<if-attr>](if-attr.html).**

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> #PCDATA
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **name** | **CDATA**   name of the component  *supports variable expansion* | #REQUIRED |
>
> ---

## 3. Content Rule

> ( #PCDATA ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**if-attr**](if-attr.html)
> :   test an attribute in the current operation or
>     current object in the source datastore
>
> [**if-dest-attr**](if-dest-attr.html)
> :   test an attribute of the current object or specified object in the
>     destination datastore
>
> [**if-op-attr**](if-op-attr.html)
> :   test an attribute in the current operation
>
> [**if-src-attr**](if-src-attr.html)
> :   test an attribute of current object or specified object in the source
>     datastore

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#component)

---

[DirXMLScript DTD](index.html)

</details>


</details>
