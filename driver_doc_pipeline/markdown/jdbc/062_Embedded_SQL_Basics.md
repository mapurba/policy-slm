# 12.2 Embedded SQL Basics

* [Elements](basics-of-embedded-sql-for-jdbc-driver.html#b9fxkvb)
* [Namespaces](basics-of-embedded-sql-for-jdbc-driver.html#b9fxkvc)
* [Embedded SQL Example](basics-of-embedded-sql-for-jdbc-driver.html#b9fxkvd)

## 12.2.1 Elements

SQL is embedded in XDS events through the <jdbc:statement> and <jdbc:sql> elements. The <jdbc:statement> element can contain one or more <jdbc:sql> elements.

## 12.2.2 Namespaces

The namespace prefix jdbc used throughout this section is implicitly bound to the namespace urn:dirxml:jdbc when referenced outside of an XML document.

You must use namespace-prefixed embedded SQL elements and attributes. Otherwise, the driver does not recognize them. In all examples in this section, the prefix used is jdbc. In practice, the prefix can be whatever you want it to be, as long as it is bound to the namespace value urn:dirxml:jdbc.

The following XML example illustrates how to use and properly namespace-prefix embedded SQL elements. In the following example, the namespace declaration and namespace prefixes are bolded:

```
<input xmlns:jdbc="urn:dirxml:jdbc">
     <add class-name="usr">
         <add-attr name="lname">
             <value>Doe</value>
         </add-attr>
     </add>
     <jdbc:statement>
         <jdbc:sql>UPDATE indirect.usr SET fname = 'John'          </jdbc:sql>
     </jdbc:statement>
</input>
```

## 12.2.3 Embedded SQL Example

The following XML example illustrates how to use the <jdbc:statement> and <jdbc:sql> elements and their interpretation. In the following example, embedded SQL elements are bolded:

```
<input xmlns:jdbc="urn:dirxml:jdbc">
     <add class-name="usr">
         <add-attr name="lname">
             <value>Doe</value>
         </add-attr>
     </add>
     <jdbc:statement>
         <jdbc:sql>UPDATE indirect.usr SET fname = 'John'          </jdbc:sql>
     </jdbc:statement>
</input>
```

Because the Subscriber channel resolves <add> events to one or more INSERT statements, the XML shown above resolves to:

```
SET AUTOCOMMIT OFF
INSERT INTO indirect.usr(lname)VALUES('Doe');
COMMIT; --explicit commit
UPDATE indirect.usr SET fname = 'John';
COMMIT; --explicit commit
```
