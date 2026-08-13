# 12.14 Calling Stored Procedures and Functions

The JDBC driver enables you to use stored procedures. The ability to use the <jdbc:call-procedure> and <jdbc:call-function> elements to call stored procedures from a policy has been tested only against Oracle and is supported only on that platform.

* [Using Embedded SQL to Call Stored Procedures or Functions](how-to-call-stored-procedures-and-functions.html#b87snuq)
* [Using the jdbc:call-procedure Element](how-to-call-stored-procedures-and-functions.html#b87suy1)
* [Using the jdbc:call-function Element](how-to-call-stored-procedures-and-functions.html#b886mfz)

## 12.14.1 Using Embedded SQL to Call Stored Procedures or Functions

You can call stored procedures or functions in one of two ways:

* Call the procedure or function by using a Statement object.
* Call the procedure by using a Callable Statement object.

#### Example 1: Calling a Stored Procedure by Using a Statement

```
     <!-- call syntax is Oracle -->
     <jdbc:statement>
          <jdbc:sql>CALL schema.procedure-name</jdbc:sql/>
     </jdbc:statement>
```

#### Example 2: Calling a Stored Procedure as a CallableStatement

```
     <!-- call syntax is vendor agnostic -->
     <jdbc:statement>
      <jdbc:call-procedure jdbc:name="schema.procedure-name"/>
     </jdbc:statement>
```

#### Example 3: Calling a Function by Using a Statement

```
     <!-- call syntax is Informix -->
     <jdbc:statement>
       <jdbc:sql>EXECUTE FUNCTION schema.function-name</jdbc:sql/>
```

```
     </jdbc:statement>
```

#### Example 4: Calling a Function as a CallableStatement

```
     <!-- call syntax is vendor agnostic -->
     <jdbc:statement>
          <jdbc:call-function jdbc:name="schema.function-name"/>
     </jdbc:statement>
```

The principle advantage of using the CallableStatement interface is that you do not need to know the proprietary call syntaxes of each database vendor or JDBC implementation. Other advantages include the following:

* It's much easier to build procedure or function calls in the Policy Builder.
* You can differentiate between Null and empty string parameter values.
* You can call functions on all database platforms.

  Oracle, for instance, doesn't support calling functions by using a statement.
* You can retrieve Out parameter values from stored procedure calls.

## 12.14.2 Using the jdbc:call-procedure Element

Stored procedures do not necessarily require parameters. Only a name is required. If a database supports schemas, we recommend that you schema-qualify the name. If a schema qualifier isn't provided, how names are resolved depends upon your third-party JDBC implementation and might change, depending upon driver configuration settings.

The jdbc:call-procedure element must be wrapped in a jdbc:statement element.

* [Specifying a Procedure Name](how-to-call-stored-procedures-and-functions.html#b87tt30)
* [Passing In or In Out Parameter Values](how-to-call-stored-procedures-and-functions.html#b87tvm2)
* [Handling Out or In Out Parameters](how-to-call-stored-procedures-and-functions.html#b87uog6)
* [Example Complex Stored Procedure Calls](how-to-call-stored-procedures-and-functions.html#b886br1)

### Specifying a Procedure Name

<jdbc:call-procedure jdbc:name="schema.procedure-name"/>

### Passing In or In Out Parameter Values

The number of jdbc:param elements specified must match the number of param elements declared in the procedure. Only jdbc:param elements corresponding to In or In Out procedure parameters can have values. Out parameters (those that can't be passed values) must be represented by an empty jdbc:param element.

* [Calling a Procedure with No Parameters](how-to-call-stored-procedures-and-functions.html#b87u9nx)
* [Calling a Procedure with a Null Parameter](how-to-call-stored-procedures-and-functions.html#b87uawc)
* [Calling a Procedure with an Empty String Parameter](how-to-call-stored-procedures-and-functions.html#b87uaz7)
* [Calling a Procedure with a Literal Value](how-to-call-stored-procedures-and-functions.html#b87ugjd)
* [Calling a Procedure with an Out Parameter](how-to-call-stored-procedures-and-functions.html#b87ugje)

#### Calling a Procedure with No Parameters

```
     <jdbc:statement>
          <jdbc:call-procedure jdbc:name="schema.procedure-name"/>
     </jdbc:statement>
```

#### Calling a Procedure with a Null Parameter

```
     <jdbc:call-procedure jdbc:name="schema.procedure-name">
          <!-- no value element = pass null -->
          <jdbc:param/>
     </jdbc:call-procedure>
```

#### Calling a Procedure with an Empty String Parameter

```
     <jdbc:call-procedure jdbc:name="schema.procedure-name">
          <!-- empty value element = pass empty string -->
          <jdbc:param>
               <jdbc:value/>
          </jdbc:param>
     <jdbc:param>
```

Literals can be passed only to procedure parameters declared as In or In Out. Passed literals must be type-compatible with declared procedure parameters.

#### Calling a Procedure with a Literal Value

```
     <jdbc:call-procedure jdbc:name="schema.procedure-name">
          <!-- non-empty value element = pass literal -->
          <jdbc:param>
               <jdbc:value>literal</jdbc:value>
          </jdbc:param>
     <jdbc:param>
```

#### Calling a Procedure with an Out Parameter

Assuming that a procedure has two parameters, the first Out and the second In, you invoke the procedure as follows:

```
     <jdbc:call-procedure jdbc:name="schema.procedure-name">
          <!-- the OUT param place -->
          <jdbc:param/>
            <!-- the IN param -->
          <jdbc:param>
               <jdbc:value>literal</jdbc:value>
          </jdbc:param>
     <jdbc:param>
```

### Handling Out or In Out Parameters

Stored procedures with Out or In Out parameters can return values. These values are returned by the driver and are accessible to policies. Out or In Out parameters values are returned at the same position as their corresponding declared parameter.

Also, to facilitate correlation of procedure calls and output parameter values, Out parameters contain the same event-ID value as the procedure call that generated them. This is particularly useful when multiple calls are made in the same document.

* [Null or No Return Value](how-to-call-stored-procedures-and-functions.html#b8862sq)
* [Empty String Return Value](how-to-call-stored-procedures-and-functions.html#b886csz)
* [Literal Return Value](how-to-call-stored-procedures-and-functions.html#b886ct0)

#### Null or No Return Value

Assuming that a procedure has a single Out or In parameter, the following output is generated:

```
     <output>
         <!-- no value element = OUT param returned null or IN param -->
        <jdbc:out-parameters event-id="0" jdbc:number-of-params="1">
             <jdbc:param/>
        </jdbc:out-parameters>
        <status event-id="0" level="success"/>
     </output>
```

#### Empty String Return Value

Assuming that a procedure has a single Out or In Out parameter, the following output is generated:

```
     <output>
         <!-- empty value element = returned empty string -->
         <jdbc:out-parameters event-id="0" jdbc:number-of-params="1">
             <jdbc:param>
                 <jdbc:value/>
             </jdbc:param>
          </jdbc:out-parameters>
          <status event-id="0" level="success"/>
     </output>
```

#### Literal Return Value

Assuming that a procedure has a single Out or In Out parameter, the following output is generated:

```
     <output>
         <!-- no-empty value element = returned literal value -->
         <jdbc:out-parameters event-id="0" jdbc:number-of-params="2">
             <jdbc:param>
                 <jdbc:value>literal<jdbc:value>
             </jdbc:param>
         </jdbc:out-parameters>
         <status event-id="0" level="success"/>
     </output>
```

### Example Complex Stored Procedure Calls

* [Procedure Declaration](how-to-call-stored-procedures-and-functions.html#b886cew)
* [Procedure Call from Policy](how-to-call-stored-procedures-and-functions.html#b886ct1)
* [Procedure Output to Policy](how-to-call-stored-procedures-and-functions.html#b886ct2)

#### Procedure Declaration

This procedure uses Oracle PSQL syntax.

```
CREATE PROCEDURE indirect.p1(i1 IN VARCHAR2, io2 IN OUT VARCHAR2, o3 OUT INTEGER, i4 IN VARCHAR2)
AS
BEGIN
    SELECT 'literal' INTO io2 FROM DUAL;
    SELECT 1 INTO o3 FROM DUAL;
END p1;
```

#### Procedure Call from Policy

```
<input>
     <jdbc:statement event-id="0">
         <jdbc:call-procedure jdbc:name="indirect.p1">
              <!-- i1 IN VARCHAR2 -->
              <jdbc:param>
                   <!-- pass empty string -->
                   <jdbc:value/>
              </jdbc:param>
              !-- io2 IN OUT VARCHAR2 -->
              <jdbc:param>
                   <!-- pass literal -->
                   <jdbc:value>literal</jdbc:value>
              </jdbc:param>
              <!-- o3 OUT INTEGER -->
              <!-- param placeholder -->
              <jdbc:param/>
              <!-- o4 IN VARCHAR2 -->
              <!-- pass null -->
              <jdbc:param/>
          </jdbc:call-procedure>
     </jdbc:statement>
</input>
```

#### Procedure Output to Policy

```
<output>
     <jdbc:out-parameters event-id="0" jdbc:number-of-params="2">
          <jdbc:param/>
          <jdbc:param jdbc:name="IO2"
                    jdbc:param-type="INOUT"
                    jdbc:position="2"
                    jdbc:sql-type="java.sql.Types.VARCHAR">
               <jdbc:value>literal</jdbc:value>
          </jdbc:param>
          <jdbc:param jdbc:name="O3"
                    jdbc:param-type="OUT"
                    jdbc:position="3"
                    jdbc:sql-type="java.sql.Types.DECIMAL">
                <jdbc:value>1</jdbc:value>
          </jdbc:param>
          <jdbc:param/>
     </jdbc:out-parameters>
     <status event-id="0" level="success"/>
</output>
```

## 12.14.3 Using the jdbc:call-function Element

Functions do not necessarily require parameters. Only a name is required. If a database supports schemas, we recommend that you schema-qualify the name. If a schema qualifier isn't provided, how names are resolved depends upon your third-party JDBC implementation and might change depending upon driver configuration settings.

The jdbc:call-function element must be wrapped in a jdbc:statement element.

* [Specifying a Function Name](how-to-call-stored-procedures-and-functions.html#b886plk)
* [Passing In Parameter Values](how-to-call-stored-procedures-and-functions.html#b887upa)
* [Calling a Function with No Parameter](how-to-call-stored-procedures-and-functions.html#b887upb)
* [Calling a Function with a Null Parameter](how-to-call-stored-procedures-and-functions.html#b887upc)
* [Calling a Function with an Empty String Parameter](how-to-call-stored-procedures-and-functions.html#b887upd)
* [Calling a Function with a Literal Value](how-to-call-stored-procedures-and-functions.html#b887upe)
* [Handling Function Results](how-to-call-stored-procedures-and-functions.html#b887upf)
* [Example Complex Function Calls](how-to-call-stored-procedures-and-functions.html#b888j98)

### Specifying a Function Name

```
     <jdbc:call-function jdbc:name="schema.function-name"/>
```

### Passing In Parameter Values

The number of jdbc:param elements specified must match the number of params declared in the function.

### Calling a Function with No Parameter

```
     <jdbc:call-function jdbc:name="schema.function-name"/>
```

### Calling a Function with a Null Parameter

```
     <jdbc:call-function jdbc:name="schema.function-name">
          <!-- no value element = null -->
          <jdbc:param/>
     </jdbc:call-procedure>
```

### Calling a Function with an Empty String Parameter

```
     <jdbc:call-function jdbc:name="schema.function-name">
          <!-- empty value element = pass empty string -->
          <jdbc:param>
               <jdbc:value/>
          </jdbc:param>
     <jdbc:param>
```

Literals can be passed to function parameters declared as In. Passed literals must be type-compatible with declared function parameters.

### Calling a Function with a Literal Value

```
     <jdbc:call-function jdbc:name="schema.function-name">
          <!-- non-empty value element = pass literal -->
          <jdbc:param>
               <jdbc:value>literal</jdbc:value>
          </jdbc:param>
     <jdbc:param>
```

### Handling Function Results

Unlike stored procedures, functions do not support Out or In Out parameters. They can, however, return a single, scalar value (such as an integer or string) or return a result set. Also, to facilitate correlation of function calls and results, results contain the same event-id value as the function call that generated them. This is particularly useful when multiple calls are made in the same document.

* [Scalar Return Value](how-to-call-stored-procedures-and-functions.html#b887upg)
* [Empty Set](how-to-call-stored-procedures-and-functions.html#b88830p)
* [Non-Empty Results Set](how-to-call-stored-procedures-and-functions.html#b8886yh)
* [Multiple Result Sets](how-to-call-stored-procedures-and-functions.html#b8886yi)
* [Oracle Results Set](how-to-call-stored-procedures-and-functions.html#b8888jg)
* [Returning Result Sets as Out Parameters](how-to-call-stored-procedures-and-functions.html#b8886yj)
* [Special Attributes](how-to-call-stored-procedures-and-functions.html#b8886yk)

#### Scalar Return Value

Scalar return values are returned by using the same syntax as stored procedure Out parameters. The scalar return value is always returned in the first parameter position.

```
<output>
     <jdbc:out-parameters event-id="0" jdbc:number-of-params="1">
          <jdbc:param jdbc:name="return value"
```

```
                    jdbc:param-type="OUT"
                    jdbc:position="1"
                    jdbc:sql-type="java.sql.Types.VARCHAR">
               <jdbc:value>1</jdbc:value>
          </jdbc:param>
     </jdbc:out-parameters>
     <status event-id="0" level="success"/>
</output
```

#### Empty Set

Assuming that a function returns no results set or an empty result set, the following output is generated:

```
<output>
     <jdbc:result-set event-id="0" jdbc:number-of-rows="0"/>
     <status event-id="0" level="success"/>
</output>
```

#### Non-Empty Results Set

Assuming a function returns a non-empty result set, output similar to the following is generated:

```
<output>
     <jdbc:result-set event-id="0" jdbc:number-of-rows="1">
          <jdbc:row jdbc:number="1">
               <jdbc:column jdbc:name="SYSDATE"
                         jdbc:position="1
                         jdbc:type="java.sql.Types.TIMESTAMP">
                    <jdbc:value>2007-01-03 14:52:20.0</jdbc:value>
               </jdbc:column>
          </jdbc:row>
     </jdbc:result-set>
     <status event-id="0" level="success"/>
</output>
```

#### Multiple Result Sets

Multiple result sets are returned in the order returned by the function. They all share a common event-id value.

```
<output>
     <jdbc:result-set event-id="0" jdbc:number-of-rows="0"/>
     <jdbc:result-set event-id="0" jdbc:number-of-rows="0"/>
     <status event-id="0" level="success"/>
</output>
```

#### Oracle Results Set

Oracle's JDBC implementation uses a proprietary mechanism to return a single result set from a function. To return a result set from an Oracle function, you need to explicitly set the [jdbc:return-type](how-to-call-stored-procedures-and-functions.html#b889hg3) value to OracleTypes.CURSOR on the jdbc:call-function element.

#### Returning Result Sets as Out Parameters

See the special attribute [jdbc:return-format](how-to-call-stored-procedures-and-functions.html#b889gww).

#### Special Attributes

#### jdbc:return-format

This attribute can be placed on the jdbc:call-function element to format the first row of a returned results set as stored procedure Out parameters of the result.

This works only when the jdbc:return-type attribute isn't used.

```
<input>
     <jdbc:statement>
          <jdbc:call-function jdbc:name="schema.function-name"
                    jdbc:return-format="return value">
               </jdbc:call-function>
     </jdbc:statement>
</input>
```

#### jdbc:return-type

This attribute can be placed on the jdbc:call-function element to allow Oracle functions to return a result set.

```
<input>
     <jdbc:statement>
          <jdbc:call-function jdbc:name="schema.function"
               jdbc:return-type="OracleTypes.CURSOR">
          </jdbc:call-function>
     </jdbc:statement>
</input>
```

### Example Complex Function Calls

* [Function Declaration](how-to-call-stored-procedures-and-functions.html#b888jiq)
* [Function Call from a Policy](how-to-call-stored-procedures-and-functions.html#b888l57)
* [Function Results to a Policy](how-to-call-stored-procedures-and-functions.html#b888l58)

#### Function Declaration

This declaration is for Oracle PSQL syntax.

```
CREATE OR REPLACE FUNCTION indirect.f1(i1 IN VARCHAR2, i2 IN INTEGER)
  RETURN VARCHAR2
AS
  o_idu VARCHAR2(32);
BEGIN
  SELECT 'literal' INTO o_idu FROM DUAL;
  RETURN o_idu;
END f1;
```

#### Function Call from a Policy

```
<input>
     <jdbc:statement>
```

```
          <jdbc:call-function jdbc:name="indirect.f1">
               <jdbc:param>
                    <jdbc:value>literal</jdbc:value>
               </jdbc:param>
               <jdbc:param>
                    <jdbc:value>1</jdbc:value>
               </jdbc:param>
           </jdbc:call-function>
     </jdbc:statement>
</input>
```

#### Function Results to a Policy

```
<output>
     <jdbc:out-parameters event-id="0" jdbc:number-of-params="1">
          <jdbc:param jdbc:name="return value"
                    jdbc:param-type="OUT"
                    jdbc:position="1"
                    jdbc:sql-type="java.sql.Types.VARCHAR">
               <jdbc:value>literal</jdbc:value>
          </jdbc:param>
     </jdbc:out-parameters>
     <status event-id="0" level="success"/>
</output>
```
