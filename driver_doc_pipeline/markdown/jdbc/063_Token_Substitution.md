# 12.3 Token Substitution

Rather than require you to parse field values from an association, the Subscriber channel supports token substitution in embedded SQL statements. In the following examples, tokens and the values they reference are bolded:

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <modify class-name="usr">
        <association>idu=1,table=usr,schema=indirect</association>
        <modify-attr name="lname">
            <add-value>
                <value>DoeRaeMe</value>
            </add-value>
        </modify-attr>
    </modify>
    <jdbc:statement>
           <jdbc:sql>UPDATE indirect.usr SET fname = 'John' WHERE
                     idu = {$idu}</jdbc:sql>
    </jdbc:statement>
</input>
```

Token placeholders must adhere to the XSLT attribute value template syntax {$field-name}. Also, the referenced association element must precede the <jdbc:statement> element in the XDS document, or must be present as a child of the <jdbc:statement> element. Alternatively, instead of copying the association element as child of the <jdbc:statement> element, you could copy the src-entry-id of the element containing the association element onto the <jdbc:statement> element. Both approaches are bolded in the following examples:

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <modify class-name="usr">
        <association>idu=1,table=usr,schema=indirect</association>
        <modify-attr name="lname">
            <add-value>
                <value>DoeRaeMe</value>
            </add-value>
        </modify-attr>
    </modify>
    <jdbc:statement>
           <association>idu=1,table=usr,schema=indirect</association>
           <jdbc:sql>UPDATE indirect.usr SET fname = 'John' WHERE
                     idu = {$idu}</jdbc:sql>
    </jdbc:statement>
```

```
</input>
```

```
<input xmlns:jdbc="urn:dirxml:jdbc">
    <modify class-name="usr" src-entry-id="0">
        <association>idu=1,table=usr,schema=indirect</association>
        <modify-attr name="lname">
            <add-value>
                <value>DoeRaeMe</value>
            </add-value>
        </modify-attr>
    </modify>
    <jdbc:statement src-entry-id="0">
           <jdbc:sql>UPDATE indirect.usr SET fname = 'John' WHERE
                     idu = {$idu}</jdbc:sql>
    </jdbc:statement>
</input>
```

The {$field-name} token must refer to one of the naming RDN attribute names in the association value. The above examples have only one naming attribute: idu.

An <add> event is the only event where an association element is not required to precede embedded SQL statements with tokens because the association has not been created yet. Additionally, any embedded SQL statements using tokens must follow, not precede, the <add> event. For example:

```
<input xmlns:jdbc="urn:dirxml:jdbc">
     <add class-name="usr">
          <add-attr name="lname">
               <value>Doe</value>
          </add-attr>
     </add>
     <jdbc:statement>
          <jdbc:sql>UPDATE indirect.usr SET fname = 'John' WHERE
                    idu = {$idu}</jdbc:sql>
     </jdbc:statement>
</input>
```

To prevent tracing of sensitive information, you can use the {$$password} token to refer to the contents of the immediately preceding <password> element within the same document. In the following example, the password token and the value it refers to are bolded:

```
<input xmlns:jdbc="urn:dirxml:jdbc">
     <add class-name="usr">
          <password>some password</password>
          <add-attr name="fname">
              <value>John</value>
          </add-attr>
          <add-attr name="lname">
              <value>Doe</value>
          </add-attr>
     </add>
     <jdbc:statement>
          <jdbc:sql>CREATE USER jdoe IDENTIFIED BY
                    {$$password}</jdbc:sql>
     </jdbc:statement>
</input>
```

Furthermore, you can also refer to the driver’s database authentication password specified by the Application Password parameter as {$$$driver-password}. See [Application Password](jdbc-driver-parameters.html#bvqz3f5). Named password substitution is not yet supported.

Just as with association elements, the referenced password element must precede the <jdbc:statement> element in the XDS document or must be present as a child of the <jdbc:statement> element. Alternatively, instead of copying the password element as child of the <jdbc:statement> element, you could copy the src-entry-id of the element containing the password element onto the <jdbc:statement> element. Both approaches are bolded in the following examples:

```
<input xmlns:jdbc="urn:dirxml:jdbc">
     <add class-name="usr">
          <password>some password</password>
          <add-attr name="fname">
              <value>John</value>
          </add-attr>
          <add-attr name="lname">
              <value>Doe</value>
          </add-attr>
     </add>
     <jdbc:statement>
          <password>some password</password>
          <jdbc:sql>CREATE USER jdoe IDENTIFIED BY
                    {$$password}</jdbc:sql>
     </jdbc:statement>
</input>
```

```
<input xmlns:jdbc="urn:dirxml:jdbc">
     <add class-name="usr" src-entry-id="0">
          <password>some password</password>
          <add-attr name="fname">
              <value>John</value>
          </add-attr>
          <add-attr name="lname">
              <value>Doe</value>
          </add-attr>
     </add>
     <jdbc:statement src-entry-id="0">
          <jdbc:sql>CREATE USER jdoe IDENTIFIED BY
                    {$$password}</jdbc:sql>
     </jdbc:statement>
</input>
```
