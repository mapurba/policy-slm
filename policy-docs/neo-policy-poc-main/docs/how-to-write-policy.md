Here's a comprehensive guide for DirXMLScript policy generation, drawing on the information from the provided sources:

## Comprehensive Guide for DirXMLScript Policy Generation

This document serves as a self-contained reference for creating DirXMLScript policies. It details the policy engine syntax and how various elements interact to define identity management logic.

### 1. How to Construct a Policy (Core Logic)

To create a functional DirXMLScript policy, you combine elements that define conditions and actions. The fundamental steps involve:

*   **Understanding the Policy Flow**: A **`<policy>`** is an ordered set of **`<rule>`** elements. Each **`<rule>`** itself consists of a set of **`<conditions>`** to be tested and an ordered set of **`<actions>`** to be performed if the conditions are met. The **`<policy>`** operates on an XDS document, examining and modifying it.
*   **Identify the Target Information**: Policies operate on a "current operation," which is any element that is a child of `<input>` or `<output>` in the XDS document. The "current object" is described by the `src-dn`, `src-entry-id`, `dest-dn`, `dest-entry-id`, and/or association from the current operation. When defining conditions or actions, you typically refer to attributes, DNs, or other properties of this "current operation" or "current object." For instance, you might want to test an attribute (`<if-attr>`, `<if-op-attr>`) or modify one (`<do-set-dest-attr-value>`).
*   **Define the Condition**: Conditions determine when a rule's actions are performed. The **`<conditions>`** element specifies these tests, typically in Conjunctive Normal Form (CNF) or Disjunctive Normal Form (DNF), meaning they are structured as logical "and"s (**`<and>`**) or "or"s (**`<or>`**). Individual condition tests are represented by elements of the form **`<if-* op="some operator">`**.
    *   The primary element for checking an attribute in the current operation is **`<if-op-attr>`**.
    *   You must know the correct operator (`op=`) for the comparison, as the type of test depends on it.
    *   For testing attributes in the source datastore, use **`<if-attr>`** or **`<if-src-attr>`**. For destination datastore attributes, use **`<if-dest-attr>`**.
    *   Other conditional checks include **`<if-class-name>`** (object class of current operation), **`<if-association>`** (association value of current operation/object), **`<if-dest-dn>`** (destination DN), **`<if-src-dn>`** (source DN), **`<if-entitlement>`** (entitlements of current object), **`<if-op-entitlement>`** (entitlements in current operation), **`<if-global-variable>`** (global configuration value), **`<if-local-variable>`** (local variable), **`<if-named-password>`** (named password), **`<if-op-property>`** (operation property), **`<if-operation>`** (name of current operation), **`<if-password>`** (password in current operation), **`<if-xml-attr>`** (XML attribute of current operation), and **`<if-xpath>`** (XPATH 1.0 expression).
*   **Specify the Action**: Actions are performed when the conditions of the enclosing rule are met. All individual actions are represented by an element of the form **`<do-*>`**.
    *   Examples include **`<do-veto>`** to stop the current operation or **`<do-set-dest-attr-value>`** to set an attribute's value in the destination datastore.
    *   Actions often take arguments that further describe the action to be taken. These arguments can be fixed strings (as attributes on the action element) or re-evaluated at runtime (as child elements of the form **`<arg-*>`**). The content of most **`<arg-*>`** elements consists of a set of tokens represented by elements of the form **`<token-*>`**.

### 2. DirXMLScript Policy Engine Documentation

This section details the structure and syntax of the DirXMLScript policy engine.
The DirXMLScript DTD defines a structured language for creating policies that govern how identity data is managed and synchronized between different datastores. A **<policy>** element represents a set of rules that examine and modify an XDS document, which typically describes an operation or event. Policies can also interact with external contexts and produce side effects not reflected in the result document.

Within a **<policy>**, there is an ordered set of **<rule>** elements. Each **<rule>** specifies a set of **<conditions>** to be tested and an ordered set of **<actions>** to be performed if those conditions are met. The **<conditions>** are evaluated using short-circuit logic, meaning that no further tests are performed once the overall boolean value of the conditions can be determined. **<actions>** are performed when the conditions of the enclosing rule are met.

Arguments for actions can either be fixed strings (represented by attributes on the action element) or dynamic values that can be re-evaluated at runtime (represented by child elements of the form `<arg-*>`). These dynamic arguments often contain **<token-*>** elements, which are expanded at runtime based on the rule evaluation context and concatenated to form the actual argument.

### Sample Policy to Check if User Last Name is Not Present

To check if a user's last name is not present, you would typically use an **<if-op-attr>** condition within a **<rule>**'s **<conditions>**. The **<if-op-attr>** element performs a test on attribute values in the current operation.

However, the provided sources indicate that the type of test performed by **<if-op-attr>** (and other **<if-*>** elements) depends on an `op` attribute, and state that a table showing the operators is available. **This table is not included in the provided excerpts.**

Based on the existence of the **<do-veto-if-op-attr-not-available>** action, it can be inferred that there is an operator (e.g., `op="not-available"`) that checks for the absence of an attribute. Therefore, the following sample policy assumes such an operator for **<if-op-attr>**:

```xml
<policy>
  <description>Policy to check if user last name is not present in the current operation</description>
  <rule>
    <description>Check for missing 'Surname' attribute</description>
    <conditions>
      <and>
        <!-- NOTE: The exact 'op' attribute values (e.g., "not-available") for if-op-attr are not detailed in the provided sources. This is an inferred operator. -->
        <if-op-attr name="Surname" op="not-available"/>
      </and>
    </conditions>
    <actions>
      <do-trace-message>
        <arg-string>
          <token-text>Warning: User's 'Surname' (Last Name) attribute is not present in the current operation.</token-text>
        </arg-string>
      </do-trace-message>
      <!-- You could add other actions here, for example: -->
      <!-- <do-veto/> to stop the operation if the attribute is critical -->
      <!-- <do-set-op-property name="missingLastName" value="true"/> to set a flag -->
    </actions>
  </rule>
</policy>
```
In this example:
*   The **<policy>** element encapsulates the entire policy logic.
*   The **<rule>** element contains a specific check.
*   **<conditions>** define when the rule's actions should run.
*   **<and>** specifies that all enclosed tests must be true.
*   **<if-op-attr name="Surname" op="not-available"/>** hypothetically checks if the "Surname" attribute is not present in the current operation.
*   **<actions>** define what happens if the conditions are met.
*   **<do-trace-message>** emits a trace message.
*   **<arg-string>** specifies the string argument for the trace message.
*   **<token-text>** provides constant text within the argument.

### More General Sample Policy

This general policy demonstrates combining multiple conditions using **<and>** and **<or>** elements, and performing various **<do-*>** actions based on the current operation's context, including dynamic values derived from tokens.

```xml
<policy>
  <description>A more general policy example for user provisioning and updates</description>
  <rule>
    <description>Rule 1: Process new user creation with specific class name and set initial attributes</description>
    <conditions>
      <and>
        <!-- NOTE: The exact 'op' attribute values (e.g., "equal") for if-operation and if-class-name are not detailed in the provided sources. This is an inferred operator. -->
        <if-operation op="equal">add</if-operation>
        <if-class-name op="equal">User</if-class-name>
      </and>
    </conditions>
    <actions>
      <do-add-association>
        <arg-dn>
          <token-src-dn/>
        </arg-dn>
        <arg-association>
          <token-unique-name/>
        </arg-association>
      </do-add-association>
      <do-set-dest-attr-value name="cn">
        <arg-value>
          <token-attr name="GivenName"/>
          <token-text> </token-text>
          <token-attr name="Surname"/>
        </arg-value>
      </do-set-dest-attr-value>
      <do-trace-message>
        <arg-string>
          <token-text>New 'User' object created and associated: </token-text>
          <token-src-dn/>
        </arg-string>
      </do-trace-message>
    </actions>
  </rule>

  <rule>
    <description>Rule 2: Handle password changes or specific attribute modifications for existing users</description>
    <conditions>
      <or>
        <!-- NOTE: The exact 'op' attribute values (e.g., "equal", "value-changed") for if-operation and if-op-attr are not detailed in the provided sources. These are inferred operators. -->
        <if-operation op="equal">modify</if-operation>
        <if-password op="set"/> <!-- Assumes an "set" operator for if-password to check if password is being set -->
      </or>
      <and>
        <if-operation op="equal">modify</if-operation>
        <if-op-attr name="description" op="value-changed"/> <!-- Checks if 'description' attribute value has changed -->
      </and>
    </conditions>
    <actions>
      <do-generate-event>
        <arg-string>
          <token-text>Significant change detected for object: </token-text>
          <token-src-dn/>
          <token-text>. Details: </token-text>
          <token-operation/>
        </arg-string>
      </do-generate-event>
      <do-send-email>
        <arg-string name="to">admin@example.com</arg-string>
        <arg-string name="subject">Identity Change Alert</arg-string>
        <arg-string name="body">
          <token-text>An operation of type ' </token-text>
          <token-operation/>
          <token-text>' occurred for: </token-text>
          <token-src-dn/>
        </arg-string>
      </do-send-email>
    </actions>
  </rule>
</policy>
```
In this general example:
*   **<rule>** elements are used to define distinct logical blocks of processing.
*   **<conditions>** can use **<and>** and **<or>** elements to combine multiple tests.
*   **<if-operation>** tests the name of the current operation (e.g., "add", "modify").
*   **<if-class-name>** tests the object class of the current operation (e.g., "User").
*   **<if-password>** tests the password in the current operation.
*   **<do-add-association>** associates the current object. It uses **<arg-dn>** and **<arg-association>**.
    *   **<token-src-dn/>** expands to a value derived from the source DN.
    *   **<token-unique-name/>** generates a unique name.
*   **<do-set-dest-attr-value>** sets the value of an attribute in the destination datastore. It uses **<arg-value>**.
    *   **<token-attr name="GivenName"/>** expands to the value of the 'GivenName' attribute from the current operation or source datastore.
*   **<do-generate-event>** generates a user-defined event.
*   **<do-send-email>** generates an email notification.
*   **<token-operation/>** expands to the name of the current operation.

**Important Note on Operators:** As mentioned, the provided sources frequently state that the type of test performed by **<if-*>** elements depends on an `op` attribute and that a table shows the specific operators. However, **these tables with the detailed operator values (like `equal`, `not-available`, `value-changed`, `set`) are not included in the provided excerpts.** The operators used in these examples (`op="not-available"`, `op="equal"`, `op="set"`, `op="value-changed"`) are inferred based on common XML DTD patterns and the general descriptions of the elements' functionalities. You may want to independently verify the exact syntax and available operators if implementing these policies.

#### `<policy>` Element

A **`<policy>`** element is the top-level container for defining identity synchronization and management logic. It consists of an ordered set of **`<rule>`** elements and can include rules from other policies via **`<include>`**. A **`<policy>`** can also have an optional **`<description>`**.

*   **Functionality**: A **`<policy>`** operates on an XDS document, primarily examining and modifying it. It can also gain additional context from outside the document and trigger side effects not reflected in the result document.
*   **Basic Operation**:
    *   The XDS document is divided into its constituent operations. An **operation** is any element that is a child of `<input>` or `<output>`.
    *   The **`<policy>`** is applied separately to each operation. As the policy is applied to each operation, that operation becomes the **current operation**.
    *   The object described by the `src-dn`, `src-entry-id`, `dest-dn`, `dest-entry-id`, and/or association from the current operation becomes the **current object**.
    *   Each **`<rule>`** within the **`<policy>`** is applied in order to the current operation.
    *   The **`<conditions>`** for the **`<rule>`** are tested, and if they are met, the **`<actions>`** are applied. Processing stops if an action causes subsequent rules to no longer apply.
*   **Variables**: DirXML Script supports two types of variables:
    *   **Global Variables**: These obtain their values from Global Configuration Values (GCVs) defined for the driver or driver set and are read-only.
    *   **Local Variables**: These are set by a policy and can exist in two scopes:
        *   **Policy Scope**: Visible only during the processing of the current operation by the policy that sets the variable.
        *   **Driver Scope**: Visible from all DirXML Script policies running within the same driver until the driver is stopped.
        *   If the same local variable exists in both policy and driver scope, the policy-scoped variable takes precedence.
    *   A variable name must be a legal XML Name.
    *   **Variable Expansion**: Many conditions, actions, and tokens support dynamic variable expansion. An embedded reference of the form `$*variable-name*$` is replaced with the value of the local or global variable. If the variable doesn't exist, an empty string is returned. To use a literal '$', it must be escaped with an additional '$' (e.g., `$$100.00`).
*   **Date/Time Parameters**: Tokens dealing with dates and times can specify format, language, and time zone. Formats starting with '!' are named formats, otherwise, they conform to `java.text.SimpleDateFormat` patterns. Language arguments conform to IETF RFC3066, and time zone arguments are identifiers recognizable by `java.util.TimeZone.getTimeZone()`.
*   **XPATH Evaluation**: Arguments to some conditions and actions take an XPATH 1.0 expression. The context for XPATH evaluation includes the current operation as the context node (unless specified otherwise), available variables (local policy, local driver, global GCVs with precedence), implicitly and explicitly defined namespaces, and built-in XPATH 1.0 functions, Java extension functions, and ECMAScript extension functions.

#### `<rule>` Element

A **`<rule>`** element specifies a set of **`<conditions>`** and a set of **`<actions>`** to be performed when those conditions are met. It can also include a **`<description>`** and **`<comment>`**.

*   **Parent Element**: **`<policy>`**.

#### `<conditions>` Element

The **`<conditions>`** element defines the tests under which the **`<actions>`** of the enclosing **`<rule>`** are performed. Conditions are specified in Conjunctive Normal Form (CNF) or Disjunctive Normal Form (DNF), meaning their content is either a disjunction of conjunctions (set of **`<and>`** elements) or a conjunction of disjunctions (set of **`<or>`** elements). The **`<actions>`** are performed only if the logical expression evaluates to `TRUE` or if no conditions are specified. Condition evaluation uses short-circuit logic.

*   **Allowed Content**: **`<and>`** (logical conjunction) and **`<or>`** (logical disjunction).
*   **Parent Element**: **`<rule>`**.

#### `<actions>` Element

The **`<actions>`** element contains the operations performed when the conditions of the enclosing **`<rule>`** are met. All individual actions are represented by elements of the form **`<do-*>`**.

*   **Argument Handling**:
    *   Arguments taking a fixed string are represented by attributes on the action element.
    *   Arguments that can be re-evaluated at run-time are represented by child elements of the form **`<arg-*>`**.
    *   The content of most **`<arg-*>`** elements consists of a set of tokens (**`<token-*>`**) which are expanded at run-time.
*   **Allowed Content (`do-*` elements)**: This element can contain a wide array of actions, including but not limited to:
    *   **Data Modification**: **`<do-add-dest-attr-value>`**, **`<do-add-src-attr-value>`**, **`<do-clear-dest-attr-value>`**, **`<do-clear-src-attr-value>`**, **`<do-remove-dest-attr-value>`**, **`<do-remove-src-attr-value>`**, **`<do-set-dest-attr-value>`**, **`<do-set-src-attr-value>`**, **`<do-reformat-op-attr>`**, **`<do-rename-op-attr>`**, **`<do-strip-op-attr>`**.
    *   **Object Management**: **`<do-add-dest-object>`**, **`<do-add-src-object>`**, **`<do-delete-dest-object>`**, **`<do-delete-src-object>`**, **`<do-move-dest-object>`**, **`<do-move-src-object>`**, **`<do-rename-dest-object>`**, **`<do-rename-src-object>`**.
    *   **Association and Identity Management**: **`<do-add-association>`**, **`<do-remove-association>`**, **`<do-find-matching-object>`**, **`<do-set-op-association>`**.
    *   **Password/Credential Management**: **`<do-set-dest-password>`**, **`<do-set-src-password>`**, **`<do-clear-sso-credential>`**, **`<do-set-sso-credential>`**, **`<do-set-sso-passphrase>`**, **`<do-remove-named-password>`**, **`<do-set-named-password>`**.
    *   **Role and Resource Management**: **`<do-add-role>`**, **`<do-remove-role>`**, **`<do-create-role>`**, **`<do-delete-role>`**, **`<do-modify-role>`**, **`<do-add-resource>`**, **`<do-remove-resource>`**, **`<do-create-resource>`**, **`<do-delete-resource>`**, **`<do-modify-resource>`**, **`<do-implement-entitlement>`**.
    *   **XML Manipulation**: **`<do-append-xml-element>`**, **`<do-append-xml-text>`**, **`<do-clone-xpath>`**, **`<do-set-xml-attr>`**, **`<do-strip-xpath>`**.
    *   **Control Flow & Logging**: **`<do-break>`** (stop processing), **`<do-if>`** (conditionally perform actions), **`<do-for-each>`** (repeat actions), **`<do-while>`** (repeat actions while conditions are true), **`<do-veto>`** (veto current operation), **`<do-veto-if-op-attr-not-available>`**, **`<do-trace-message>`**, **`<do-status>`** (report status).
    *   **Variables & Properties**: **`<do-set-local-variable>`**, **`<do-clear-op-property>`**, **`<do-set-op-class-name>`**, **`<do-set-op-dest-dn>`**, **`<do-set-op-property>`**, **`<do-set-op-src-dn>`**, **`<do-set-op-template-dn>`**.
    *   **External Interactions**: **`<do-generate-event>`**, **`<do-generate-xdas-event>`**, **`<do-send-email>`**, **`<do-send-email-from-template>`**, **`<do-invoke-rest-endpoint>`**, **`<do-start-workflow>`**.
*   **Parent Elements**: **`<rule>`**, **`<arg-actions>`**.

#### `<arg-*>` Elements (Arguments)

These elements define arguments for **`<do-*>`** actions and some **`<if-*>`** conditions. They specify the data to be used by the enclosing action or condition.

*   **`<arg-actions>`**: Specifies a set of actions for the enclosing action, differing from other arguments by containing actions instead of tokens.
    *   **Parent Elements**: **`<do-for-each>`**, **`<do-if>`**, **`<do-implement-entitlement>`**, **`<do-while>`**.
*   **`<arg-conditions>`**: Specifies conditions for the enclosing action, containing **`<and>`** or **`<or>`** elements.
    *   **Parent Elements**: **`<do-if>`**, **`<do-while>`**.
*   **`<arg-dn>`**: Specifies a DN value for the enclosing action, concatenating string values from enclosed tokens.
    *   **Parent Elements**: Various `do-*` actions like **`<do-add-association>`**, **`<do-add-dest-attr-value>`**, **`<do-add-dest-object>`**, **`<do-add-resource>`**, **`<do-add-role>`**, **`<do-add-src-object>`**, and conditional tests like **`<if-dest-attr>`**, **`<if-src-attr>`**.
*   **`<arg-node-set>`**: Specifies an XPATH 1.0 node-set for the enclosing action, adding nodes from token evaluations.
    *   **Parent Elements**: **`<do-for-each>`**, **`<do-implement-entitlement>`**, **`<do-set-local-variable>`**.
*   **`<arg-query-condition>`**: Specifies a logical conditional search expression for an action or token like **`<do-find-matching-object>`** or **`<token-query>`**. It can contain other **`<arg-query-condition>`** or **`<arg-match-attr>`** elements. It supports `and`, `or`, and `not` operations.
    *   **Parent Elements**: It can be nested within itself or be a child of **`<do-find-matching-object>`** or **`<token-query>`**.
*   **`<arg-string>`**: Specifies a string value for the enclosing action, concatenating results from enclosed tokens.
    *   **Parent Elements**: Numerous `do-*` actions like **`<do-add-resource>`**, **`<do-add-role>`**, **`<do-send-email>`**, **`<do-trace-message>`**, and tokens like **`<token-document>`**, **`<token-query>`**.
*   **`<arg-value>`**: Specifies an attribute value for the enclosing action. If `type="structured"`, it contains **`<component>`** elements; otherwise, it concatenates string values from enclosed tokens.
    *   **Parent Elements**: `do-*` actions related to attribute value manipulation like **`<do-add-dest-attr-value>`**, **`<do-add-src-attr-value>`**, **`<do-remove-dest-attr-value>`**, **`<do-remove-src-attr-value>`**, **`<do-set-dest-attr-value>`**, **`<do-set-default-attr-value>`**, **`<do-set-src-attr-value>`**, and **`<arg-match-attr>`**.

#### `<token-*>` Elements (Tokens)

Tokens are child elements of `<arg-*>` elements that expand to specific values at runtime based on the rule evaluation context. The results of token expansion are concatenated to form the argument's actual value.

*   **Examples**:
    *   **`<token-added-entitlement>`**: Expands to granted entitlement values in the current operation.
    *   **`<token-association>`**: Expands to the association value from the current operation.
    *   **`<token-attr>`**: Expands to attribute values of the current object in the current operation or source datastore.
    *   **`<token-char>`**: Expands to a unicode character specified by a code point.
    *   **`<token-class-name>`**: Expands to the object class name in the current operation.
    *   **`<token-xpath>`**: Expands to the result of an XPATH 1.0 expression.
    *   **`<token-xml-parse>`**: Parses enclosed tokens as XML and returns the document node.
    *   **`<token-xml-serialize>`**: Serializes the node-set result of enclosed tokens as XML.
*   **Common Functionality Tokens**: Many tokens offer common string or data manipulation functionalities, such as:
    *   **Encoding/Decoding**: **`<token-base64-decode>`**, **`<token-base64-encode>`**.
    *   **Case Conversion**: **`<token-lower-case>`**, **`<token-upper-case>`**.
    *   **String Manipulation**: **`<token-substring>`**, **`<token-replace-all>`**, **`<token-replace-first>`**, **`<token-split>`**, **`<token-join>`**.
    *   **DN/Object Related**: **`<token-dest-dn>`**, **`<token-src-dn>`**, **`<token-parse-dn>`**, **`<token-resolve>`**, **`<token-unique-name>`**, **`<token-query>`**.
    *   **Variables**: **`<token-global-variable>`**, **`<token-local-variable>`**.
    *   **Time/Date**: **`<token-convert-time>`**, **`<token-time>`**.

To write an XML policy in DirXMLScript DTD, you need to understand its fundamental structure, which is built upon policies, rules, conditions, and actions. The goal of a DirXMLScript policy is to examine and modify an XDS document, gather external context, and trigger side effects.

Here's a breakdown of how to construct an XML policy based on the DirXMLScript DTD:

### **1. Policy (`<policy>`)**

The top-level element in a DirXMLScript is the `<policy>` tag. A policy acts on an XDS document by processing its constituent operations, which are typically children of `<input>` or `<output>` elements. Each operation becomes the "current operation," and the object it describes (via `src-dn`, `src-entry-id`, `dest-dn`, `dest-entry-id`, or association) becomes the "current object".

A `<policy>` can contain:
*   An optional **`<description>`** element, which provides a description of the policy.
*   An optional sequence of **`<rule>`** or **`<include>`** elements.
    *   **`<rule>`**: Defines a set of conditions and actions.
    *   **`<include>`**: Allows you to incorporate rules from another policy.

### **2. Rule (`<rule>`)**

Within a `<policy>`, a `<rule>` is used to specify a set of conditions and a set of actions that will be performed if those conditions are met. Rules are applied sequentially to the current operation unless a prior action prevents further rule processing.

A `<rule>` must contain:
*   An optional **`<description>`**.
*   Zero or more **`<comment>`** elements for long descriptions.
*   Required **`<conditions>`**.
*   Required **`<actions>`**.

### **3. Conditions (`<conditions>`)**

The `<conditions>` element defines the criteria under which the actions of the enclosing rule will be executed. If no conditions are specified, the actions are performed by default.

Conditions are structured using either:
*   **Logical Conjunction (`<and>`)**: Specifies tests whose results are logically ANDed together. If multiple `<and>` elements are within `<conditions>`, they are ORed together.
*   **Logical Disjunction (`<or>`)**: Specifies tests whose results are logically ORed together. If multiple `<or>` elements are within `<conditions>`, they are ANDed together.

Individual condition tests are represented by elements of the form `<if-* op="some operator">`. These tests check various aspects of the current operation or objects in the datastores. Some common examples include:
*   **`if-association`**: Tests the association value of the current operation or object.
*   **`if-attr`**: Tests attribute values of the current object in the current operation or source datastore.
*   **`if-class-name`**: Tests the object class name in the current operation.
*   **`if-dest-attr`**: Tests attribute values of the current object or a specified object in the destination datastore.
*   **`if-dest-dn`**: Tests the destination DN of the current operation.
*   **`if-global-variable`**: Tests a global configuration value.
*   **`if-local-variable`**: Tests a local variable.
*   **`if-operation`**: Tests the name of the current operation.
*   **`if-password`**: Tests the password in the current operation.
*   **`if-src-attr`**: Tests attribute values of the current object or a specified object in the source datastore.
*   **`if-xpath`**: Tests the result of an XPATH 1.0 expression.

The evaluation of conditions uses short-circuit logic, meaning that testing stops as soon as the boolean outcome is determined.

### **4. Actions (`<actions>`)**

The `<actions>` element specifies the operations to be performed if the rule's conditions are met. All individual actions are represented by elements of the form `<do-*>`.

Actions often take arguments that further describe the operation. These arguments can be:
*   **Attributes**: Fixed string values that won't change at runtime.
*   **Child Elements (`<arg-*>`)**: Dynamically re-evaluated at runtime.

Common `<do-*>` actions include:
*   **Object Manipulation**:
    *   **`do-add-dest-object`**: Creates an object in the destination datastore.
    *   **`do-delete-dest-object`**: Deletes an object in the destination datastore.
    *   **`do-move-dest-object`**: Moves an object in the destination datastore.
    *   **`do-rename-dest-object`**: Renames an object in the destination datastore.
*   **Attribute Management**:
    *   **`do-add-dest-attr-value`**: Adds a value to an attribute in the destination datastore.
    *   **`do-set-dest-attr-value`**: Sets the value of an attribute in the destination datastore.
    *   **`do-clear-dest-attr-value`**: Clears all values of an attribute in the destination datastore.
    *   **`do-reformat-op-attr`**: Changes the format of attribute values in the current operation.
*   **Role and Resource Management**:
    *   **`do-add-role`**: Initiates a request to assign a Role to an Identity.
    *   **`do-add-resource`**: Initiates a request to assign a Resource to an Identity.
    *   **`do-create-role`**: Creates a role.
    *   **`do-delete-role`**: Deletes a role.
*   **Flow Control and Messaging**:
    *   **`do-break`**: Stops processing the current operation within the policy.
    *   **`do-if`**: Conditionally performs actions.
    *   **`do-for-each`**: Repeats actions for each node in a node-set.
    *   **`do-trace-message`**: Emits a trace message.
    *   **`do-veto`**: Vetoes (stops) the current operation.
    *   **`do-send-email`**: Generates an email notification.
    *   **`do-start-workflow`**: Starts a workflow.

### **5. Arguments (`<arg-*>`)**

As mentioned, many actions use `<arg-*>` child elements to specify dynamic values. These arguments are further detailed by their content:
*   **`arg-actions`**: Contains a set of `<do-*>` actions to be performed by the enclosing action (e.g., within a `do-if` or `do-for-each`).
*   **`arg-conditions`**: Contains `<and>` or `<or>` elements, specifying conditions for the enclosing action (e.g., for `do-if` or `do-while`).
*   **`arg-dn`**: Specifies a DN value for the enclosing action. Its content consists of concatenated string values from enclosed tokens.
*   **`arg-node-set`**: Specifies an XPATH 1.0 node-set. Enclosed tokens returning a node-set add nodes to the result; otherwise, a text node is created and added.
*   **`arg-string`**: Specifies a string value for the enclosing action by concatenating string values from enclosed tokens.
*   **`arg-value`**: Specifies an attribute value. If its `type` attribute is "structured", it contains `<component>` elements; otherwise, it concatenates string values from enclosed tokens.

### **6. Tokens (`<token-*>`)**

The content of most `<arg-*>` elements consists of a set of `<token-*>` elements. These tokens expand at runtime based on the rule evaluation context, and their expanded results are concatenated to form the actual argument value.

Examples of various tokens include:
*   **Contextual Information**:
    *   **`token-association`**: The association value from the current operation.
    *   **`token-attr`**: Attribute values from the current operation or current object in the source datastore.
    *   **`token-class-name`**: The object class name from the current operation.
    *   **`token-dest-dn`**: A value derived from the destination DN.
    *   **`token-operation`**: The name of the current operation.
    *   **`token-op-attr`**: Attribute values in the current operation.
*   **Variable Access**:
    *   **`token-global-variable`**: The value of a global variable.
    *   **`token-local-variable`**: The value of a local variable.
*   **String Manipulation**:
    *   **`token-lower-case`**: Converts a string to lower case.
    *   **`token-substring`**: Extracts a substring from a string.
    *   **`token-replace-all`**: Replaces all instances of a substring within a string.
*   **Data Conversion/Generation**:
    *   **`token-base64-decode`**: Decodes base64 data into a string.
    *   **`token-generate-password`**: Generates a random password.
    *   **`token-parse-dn`**: Parses and/or converts a DN.
*   **XML/JSON Processing**:
    *   **`token-xml-parse`**: Parses XML from enclosed tokens and returns a document node-set.
    *   **`token-xml-serialize`**: Serializes a node-set result from enclosed tokens as XML.
    *   **`token-json-array`**: Constructs a JSON array.
    *   **`token-json-object`**: Constructs a JSON string.
*   **XPATH**:
    *   **`token-xpath`**: Returns the result of evaluating an XPATH 1.0 expression.

### **7. Variables**

DirXML Script supports two types of variables:
*   **Global variables**: These are read-only and derive their values from Global Configuration Values defined for the driver or driverset.
*   **Local variables**: These are set by a policy and can have either a "policy" scope (visible only during the processing of the current operation by the setting policy) or a "driver" scope (visible across all DirXML Script policies within the same driver until it stops).

Variable names must be legal XML Names. Dynamic variable expansion is supported in many attributes or content using the format `$$variable-name$$`. To use a literal '$', it must be escaped with an additional '$' (e.g., `$$100.00`).

To write an XML policy using the DirXMLScript DTD, you need to understand its hierarchical structure, starting from the top-level `<policy>` element down to specific conditions and actions. This structure allows you to define how an XDS document (which represents identity events and data) is processed, modified, and used to trigger side effects.

Here's a breakdown of how to construct an XML policy, with examples:

### 1. The Policy (`<policy>`) Element

The `<policy>` element is the root of your DirXMLScript policy. Its primary purpose is to examine and modify an XDS document. It operates by applying itself to each "current operation" within the XDS document, which are typically children of `<input>` or `<output>` elements. The object described by the current operation becomes the "current object".

A `<policy>` can contain:
*   An optional **`<description>`** to explain the policy's purpose.
*   One or more **`<rule>`** elements, which define specific sets of conditions and actions.
*   Optional **`<include>`** elements to incorporate rules from other policies.

**Example of a Policy Structure:**

```xml
<policy xmlns:policy="http://www.novell.com/dirxml/policy">
  <description>This is a sample policy to manage user accounts.</description>

  <!-- Rules will be defined here -->
  <rule>
    <!-- Conditions and actions for this rule -->
  </rule>

  <!-- Or rules from another policy can be included -->
  <!-- <include src="path/to/another/policy.xml"/> -->
</policy>
```

### 2. The Rule (`<rule>`) Element

Within a `<policy>`, a `<rule>` specifies a set of conditions and the actions to be performed if those conditions are met. Rules are applied sequentially to the current operation unless an action in a preceding rule stops further processing.

A `<rule>` must contain:
*   An optional **`<description>`** for the rule.
*   Zero or more **`<comment>`** elements for longer descriptions.
*   A **`<conditions>`** element, which defines the criteria for the rule's actions.
*   An **`<actions>`** element, which specifies the operations to execute if conditions are met.

**Example of a Rule Structure:**

```xml
<rule>
  <description>Create a new user if the operation is 'add' and class is 'User'.</description>
  <comment>This rule ensures that only 'User' objects are created in the destination system.</comment>
  <conditions>
    <!-- Conditions will be defined here -->
  </conditions>
  <actions>
    <!-- Actions will be defined here -->
  </actions>
</rule>
```

### 3. Conditions (`<conditions>`) Element

The `<conditions>` element dictates when the actions of its enclosing rule are executed. If no conditions are specified, the actions are performed by default. Conditions are typically structured using logical conjunctions (`<and>`) or disjunctions (`<or>`).

*   **`<and>`**: Specifies tests whose results are logically ANDed together. If multiple `<and>` elements are within `<conditions>`, they are ORed together.
*   **`<or>`**: Specifies tests whose results are logically ORed together. If multiple `<or>` elements are within `<conditions>`, they are ANDed together.

Individual condition tests are represented by elements of the form `<if-* op="some operator">`. These tests check various aspects of the "current operation" or objects in the datastores.

Some common condition elements include:
*   **`if-association`**: Tests the association value.
*   **`if-attr`**: Tests attribute values of the current object in the current operation or source datastore.
*   **`if-class-name`**: Tests the object class name in the current operation.
*   **`if-dest-attr`**: Tests attribute values of the current object or a specified object in the destination datastore.
*   **`if-operation`**: Tests the name of the current operation.
*   **`if-xpath`**: Tests the result of an XPATH 1.0 expression.

**Example of Conditions:**

```xml
<conditions>
  <and>
    <if-operation op="equal">add</if-operation>
    <if-class-name op="equal">User</if-class-name>
  </and>
  <or>
    <if-dest-attr name="GivenName" op="not-available"/>
    <if-dest-attr name="Surname" op="not-available"/>
  </or>
</conditions>
```
This example defines a rule that will execute its actions if the operation is "add" AND the object class is "User", AND (GivenName is not available OR Surname is not available in the destination datastore).

### 4. Actions (`<actions>`) Element

The `<actions>` element specifies the operations to be performed if the rule's conditions are met. All individual actions are represented by elements of the form `<do-*>`.

Arguments to actions can be:
*   **Attributes**: Fixed string values that won't change at runtime.
*   **Child Elements (`<arg-*>`)**: Dynamically re-evaluated at runtime using tokens.

Common `<do-*>` actions include:
*   **`do-add-dest-object`**: Creates an object in the destination datastore.
*   **`do-set-dest-attr-value`**: Sets an attribute value in the destination datastore.
*   **`do-add-role`**: Requests assignment of a Role to an Identity.
*   **`do-send-email`**: Generates an email notification.
*   **`do-trace-message`**: Emits a trace message.
*   **`do-veto`**: Stops the current operation.
*   **`do-set-local-variable`**: Sets the value of a local variable.
*   **`do-if`**: Conditionally performs actions.
*   **`do-for-each`**: Repeats actions for each node in a node-set.

**Example of Actions:**

```xml
<actions>
  <do-add-dest-object class-name="User">
    <arg-dn>
      <token-text>Users\</token-text>
      <token-attr name="LastName"/>
      <token-text>_</token-text>
      <token-attr name="FirstName"/>
    </arg-dn>
  </do-add-dest-object>
  <do-set-dest-attr-value name="email">
    <arg-value>
      <token-attr name="FirstName"/>
      <token-text>.</token-text>
      <token-attr name="LastName"/>
      <token-text>@example.com</token-text>
    </arg-value>
  </do-set-dest-attr-value>
  <do-trace-message level="info">
    <arg-string>
      <token-text>New user </token-text>
      <token-attr name="FullName"/>
      <token-text> created.</token-text>
    </arg-string>
  </do-trace-message>
</actions>
```
This example shows actions to add a destination object with a constructed DN, set its email attribute, and log a trace message.

### 5. Arguments (`<arg-*>`) Elements

Arguments are used by actions to define dynamic values or nested logic.
*   **`arg-actions`**: Contains a set of `<do-*>` actions, used by actions like `do-if` or `do-for-each`.
*   **`arg-conditions`**: Contains `<and>` or `<or>` elements, specifying conditions for actions like `do-if` or `do-while`.
*   **`arg-dn`**: Specifies a DN value by concatenating string results from enclosed tokens.
*   **`arg-node-set`**: Specifies an XPATH 1.0 node-set; enclosed tokens returning a node-set add nodes, otherwise a text node is added.
*   **`arg-string`**: Specifies a string value by concatenating string results from enclosed tokens.
*   **`arg-value`**: Specifies an attribute value. If its `type` attribute is "structured", it contains `<component>` elements; otherwise, it concatenates string values from enclosed tokens.

**Example using `arg-actions` with `do-if`:**

```xml
<do-if>
  <arg-conditions>
    <and>
      <if-attr name="EmployeeType" op="equal">Full-Time</if-attr>
    </and>
  </arg-conditions>
  <arg-actions>
    <do-add-role role-id="FullTimeEmployeeRole">
      <arg-string name="reason">
        <token-text>Assigned based on EmployeeType</token-text>
      </arg-string>
    </do-add-role>
  </arg-actions>
</do-if>
```
This example shows how a `do-if` action uses `arg-conditions` to check if `EmployeeType` is "Full-Time", and if true, `arg-actions` specifies that the "FullTimeEmployeeRole" should be added.

### 6. Tokens (`<token-*>`) Elements

Tokens expand at runtime to provide dynamic values for arguments. The expanded results are concatenated to form the actual argument value.

Some common token elements include:
*   **`token-added-entitlement`**: Value(s) of an entitlement granted in the current operation.
*   **`token-association`**: Association value from the current operation.
*   **`token-attr`**: Attribute values of the current object in the current operation or source datastore.
*   **`token-class-name`**: Object class name from the current operation.
*   **`token-dest-dn`**: Value derived from the destination DN.
*   **`token-generate-password`**: Generates a random password.
*   **`token-global-variable`**: Value of a global variable.
*   **`token-local-variable`**: Value of a local variable.
*   **`token-lower-case`**: Converts a string to lower case.
*   **`token-operation`**: Name of the current operation.
*   **`token-substring`**: Extracts a substring from a string.
*   **`token-text`**: Constant text.
*   **`token-time`**: Current date/time.
*   **`token-unique-name`**: A generated unique name.
*   **`token-xml-parse`**: Parses XML from enclosed tokens and returns a document node-set.
*   **`token-xml-serialize`**: Serializes a node-set result from enclosed tokens as XML.
*   **`token-xpath`**: Result of an XPATH 1.0 expression.

**Example using `token-xpath`:**

```xml
<do-set-local-variable name="userStatus">
  <arg-node-set>
    <token-xpath expression="string(./@status)"/>
  </arg-node-set>
</do-set-local-variable>
```
This example sets a local variable named "userStatus" to the string value of the "status" attribute from the current operation using `token-xpath`.

### 7. Variables

DirXML Script supports two types of variables:
*   **Global variables**: Read-only, deriving their values from Global Configuration Values (GCVs) defined for the driver or driverset.
*   **Local variables**: Set by a policy, with either "policy" scope (visible only during current operation processing by the setting policy) or "driver" scope (visible across all policies within the same driver until it stops).
Variable names must be legal XML Names. Dynamic variable expansion uses the `$$variable-name$$` format, where `$$` escapes a literal `$`.

### 8. XPATH Evaluation

XPATH 1.0 expressions are evaluated with the current operation as the default context node. Identity Manager provides stylesheet parameters (e.g., `fromNDS`), global configuration values, and local policy variables as available variables. In case of name conflicts, local (policy scope) takes precedence, then local (driver scope), then global variables. Built-in XPATH 1.0 functions, Java extension functions, and ECMAScript extension functions are all available.

By combining these elements, you can build powerful and intricate XML policies to manage identity and data flows within your system.