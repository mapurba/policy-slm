# 5.3 Modifying Policies

You can modify the existing driver policies to perform additional functionality.

* [Specifying the GroupWise Post Office](modify-policies.html#ad8q7uj)
* [Configuring the GroupWise UserID](modify-policies.html#ad8a401)
* [Creating Mappings for Additional Attributes](modify-policies.html#ad8svzj)
* [Getting a Record Count from a Query](modify-policies.html#br4u4ut)
* [Creating a GroupWise Nickname](modify-policies.html#ae01co4)
* [Creating a GroupWise Nickname Record](modify-policies.html#br586mk)
* [Controlling Creation of GroupWise Accounts](modify-policies.html#adn4u96)
* [Moving Users from One Post Office to Another Post Office](modify-policies.html#adn4w5c)
* [Adding Additional Attributes to Be Synchronized](modify-policies.html#adstxu1)
* [Renaming Users](modify-policies.html#adn50u8)
* [Creating a Gateway Alias](modify-policies.html#agg2agx)
* [Using the Wildcard Query](modify-policies.html#b1kfnbsz)
* [Querying for a Nickname](modify-policies.html#agg2dl1)
* [Querying for a Email Address from a Nickname](modify-policies.html#b1knuqh5)
* [Querying for a Gateway Alias](modify-policies.html#agg2gtm)
* [Querying for Internet Email Address](modify-policies.html#agg2hn2)
* [Synchronizing GroupWise External Users](modify-policies.html#akxyufc)
* [Verifying if an E-Mail Address or Gateway Alias Is Unique](modify-policies.html#b4ua4el)
* [Converting String Attributes to Structured Attributes](modify-policies.html#b1ey3xc1)

## 5.3.1 Specifying the GroupWise Post Office

By default, the GroupWise Subscriber Placement policy puts all new users in the same post office. The Placement policy can also determine the post office based on an attribute value or the Identity Vault user container.

The following example shows the policies needed to place users in the Sales container into PO1 and users in the Engineering container into PO2.

```
<rule>
  <description>Users in Sales container are placed in Post Office PO1</description>
  <conditions>
   <and>
    <if-class-name op="equal">User</if-class-name>
    <if-src-dn op="in-container">data\users\Sales</if-src-dn>
   </and>
  </conditions>
  <actions>
   <do-set-op-dest-dn>
    <arg-dn>
     <token-text xml:space="preserve">GWDomain.PO1</token-text>
    </arg-dn>
   </do-set-op-dest-dn>
   <do-break/>
  </actions>
 </rule>
 <rule>
  <description>Users in Engineering container are placed in Post Office PO2</description>
  <conditions>
   <and>
    <if-class-name op="equal">User</if-class-name>
    <if-src-dn op="in-container">data\users\Engr</if-src-dn>
   </and>
  </conditions>
  <actions>
   <do-set-op-dest-dn>
    <arg-dn>
     <token-text xml:space="preserve">GWDomain.PO2</token-text>
    </arg-dn>
   </do-set-op-dest-dn>
   <do-break/>
  </actions>
 </rule>
```

## 5.3.2 Configuring the GroupWise UserID

The CN attribute in the Identity Vault is used to name the GroupWise account. You must include this in the Create policy as a required attribute. The CN value from the Identity Vault can be ignored in the Subscriber Create policy and a CN based on other attributes can be generated. An example of Create policy is shown below. If you make modifications to this policy, the modify events coming from the engine also need to be modified.

When an attribute used to construct the CN is modified, a GroupWise Rename event should be generated via the policies. The UserID must be unique within a post office. If UserID is used to generate Internet EMail Address, it must be unique in the entire GroupWise system. The UserID contains 1 to 256 characters, and cannot contain the ( ) @ . : , { } \* " characters. The UserID must be unique within its namespace (UserID shares the same namespace as nicknames.) Do not use “mapi” (reserved ID) for this value.

An Output Transformation or Event Transformation policy can monitor the attributes used to build the CN. If one of these attributes changes, a Rename event should also be generated. Any attributes used here need to be added to the list of required attributes. In this case, Rename events should still be forwarded to the driver with an empty <newname> element. See [Renaming Users](modify-policies.html#adn50u8) for more information.

```
<rule>
  <description> Use Given Name for GroupWise Account Name</description>
  <conditions>
    <and>
      <if-class-name op="equal">User</if-class-name>
    </and>
  </conditions>
  <actions>
    <!-- 'CN' and 'Given Name' must be present -->
    <do-veto-if-op-attr-not-available name="CN"/>
    <do-veto-if-op-attr-not-available name="Given Name"/>
    <!-- replace current CN value with the 'Given Name' value -->
    <do-reformat-op-attr name="CN">
      <arg-value type="string">
        <token-op-attr name="Given Name"/>
      </arg-value>
    </do-reformat-op-attr>
  </actions>
</rule>
```

## 5.3.3 Creating Mappings for Additional Attributes

You can synchronize any attribute that can be represented as a string in the Identity Vault with one of twenty GroupWise generic attributes. You specify the Identity Vault attribute you want to map in the filter. In addition, the Identity Vault and GroupWise attribute names must be connected in the Schema Mapping policy.

The Schema Mapping rule code segment below connects the Identity Vault attribute Location with the GroupWise attribute 55003.

```
<attr-name class-name="User">
     <nds-name>Location</nds-name>
     <app-name>55003</app-name>
</attr-name>
```

The twenty GroupWise attribute names are 50106 through 50115 and 55002 through 55011. Address book labels can be assigned to these GroupWise attributes through the GroupWise Web Console. You should configure the same mappings in GroupWise as you do in the driver mappings.

## 5.3.4 Getting a Record Count from a Query

The following query, sent to the driver, returns the number of users in dom1.po1.

```
<nds dtdversion="2.0" ndsversion="8.x">
       <input>
                 <query event-id="query-groupwise" scope="subtree">
          <search-class class-name="User"/>

                     <!-- Referenced Domain Name -->
                     <search-attr attr-name="50035">
                            <value>dom1</value>
                     </search-attr>

                     <!-- Referenced Post Office Name -->
          <search-attr attr-name="50062">
                              <value>po1</value>
                 <search-attr>

                     <!-- return Record Count-->
                     <read-attr attr-name="Record Count"/>
                </query>
       </input>
</nds>
```

If you remove the post office <search-attr>, it returns the number of users in dom1. If you remove the domain <search attr>, it returns the number of users in the GroupWise system. This search can be altered to apply to other search criteria.

## 5.3.5 Creating a GroupWise Nickname

GroupWise nicknames can be automatically created when an Identity Vault User is renamed or when a GroupWise account is moved. This is controlled in Identity Console on the driver through the Global Configuration Value page. When you set this option to True, nicknames are automatically created when an Identity Vault rename occurs or when a GroupWise account is moved. When you set this option to False, nicknames are not created.

## 5.3.6 Creating a GroupWise Nickname Record

The following examples show two ways to create a nickname record. The first specifies the post office in which the nickname is created in the <dest-dn> attribute (this implies the domain). The second example uses <add-attr> nodes to specify the domain and post office.

The nickname can contain 1 to 256 characters, and cannot contain the ()@.:,{}\*" characters. It must be unique within its namespace (nicknames share the same namespace as users.)

### Example 1

```
<add class-name="GroupWise Nickname" dest-dn="domain.po" event-id="0" >
     <!-- Domain of user this nickname refers to -->
       <add-attr attr-name="50068" >
          <value type="string">xmlDom</value>
       </add-attr>
     <!-- Post Office of user this nickname refers to  -->
       <add-attr attr-name="50069" >
          <value type="string">xmlPO</value>
        </add-attr>
     <!--  user this nickname refers to  -->
       <add-attr attr-name="50070" >
          <value type="string">Usern1</value>
       </add-attr>
     <!-- name of nickname record -->
       <add-attr attr-name="50073" >
          <value type="string">nn1</value>
       </add-attr>
</add>
```

### Example 2

```
<add class-name="GroupWise Nickname" event-id="0" >
        <!-- Domain of user this nickname refers to -->
          <add-attr attr-name="50068" >
              <value type="string">xmlDom</value>
          </add-attr>
        <!-- Post Office of user this nickname refers to -->
          <add-attr attr-name="50069" >
              <value type="string">xmlPO</value>
          </add-attr>
        <!-- user this nickname refers to -->
          <add-attr attr-name="50070" >
              <value type="string">Usern1</value>
          </add-attr>
        <!-- Domain of nickname record -->
          <add-attr attr-name="50035" >
             <value type="string">xmlDom</value>
          </add-attr>
        <!-- Post Office of nickname record -->
          <add-attr attr-name="50062" >
             <value type="string">xmlPO</value>
          </add-attr>
        <!-- name of nickname record -->
          <add-attr attr-name="50073" >
             <value type="string">nn1</value>
          </add-attr>
</add>
```

## 5.3.7 Controlling Creation of GroupWise Accounts

There might be situations where an Identity Vault user is created and you do not want to create a corresponding GroupWise account. In addition, not all Identity Vault users initially have a GroupWise account. You can use the driver to control the creation of GroupWise accounts.

NetIQ recommends that you use the UserAccount entitlement to control the creation of an account. When this entitlement is granted, the driver provides an enabled logon account. When this entitlement is revoked, the driver either disables or deletes the logon account, depending on the GCV configuration of entitlements.

Alternatively, you can control the creation of an account by triggering the account creation through an extended attribute such as createGroupWiseAccount.

The Identity Vault schema must be extended to include the createGroupWiseAccount attribute. When the createGroupWiseAccount attribute is set to True, the GroupWise account is created. When the createGroupWiseAccount attribute is set to False, the GroupWise account is not created. Changing the value from False to True causes the GroupWise account to be created.

The createGroupWiseAccount attribute must be added to the Create policy as a required attribute and also added to the Subscriber Filter.

```
<rule>
  <description>Require createGroupWiseAccount attribute</description>
  <conditions>
    <and>
      <if-class-name op="equal">User</if-class-name>
    </and>
  </conditions>
  <actions>
    <do-veto-if-op-attr-not-available name="createGroupWiseAccount"/>
  </actions>
</rule>
<rule>
  <description>Check createGroupWiseAccount attribute</description>
  <conditions>
    <and>
      <if-class-name op="equal">User</if-class-name>
      <if-op-attr name="createGroupWiseAccount" op="not-equal">true</if-op-attr>
    </and>
  </conditions>
  <actions>
    <do-veto/>
  </actions>
</rule>
```

## 5.3.8 Moving Users from One Post Office to Another Post Office

When the Output Transformation style sheet is configured to move GroupWise accounts, NetIQ recommends that user moves be made in the Identity Vault and that the driver assigns the object to a new post office in GroupWise. The DirXML script code segment for the Output Transformation policy is shown below. The dest-dn attribute on the parent element specifies the new post office.

```
<rule>
  <description>Move User to GW Post Office</description>
  <conditions>
    <and>
      <if-operation op="equal">move</if-operation>
      <if-class-name op="equal">User</if-class-name>
    </and>
  </conditions>
  <actions>
    <do-if>
      <arg-conditions>
        <and>
          <if-xpath op="true">parent/@src-dn="\GWDRIVERTREE\Novell\Users\Sales"</if-xpath>
        </and>
      </arg-conditions>
      <arg-actions>
        <do-set-xml-attr expression="parent" name="dest-dn">
          <arg-string>
            <token-text xml:space="preserve">GWDomain.salesPO</token-text>
          </arg-string>
        </do-set-xml-attr>
      </arg-actions>
    </do-if>
    <do-if>
      <arg-conditions>
        <and>
          <if-xpath op="true">parent/@src-dn="\GWDRIVERTREE\Novell\Users\Engineering"</if-xpath>
        </and>
      </arg-conditions>
      <arg-actions>
        <do-set-xml-attr expression="parent" name="dest-dn">
          <arg-string>
            <token-text xml:space="preserve">GWDomain.engineeringPO</token-text>
          </arg-string>
        </do-set-xml-attr>
      </arg-actions>
    </do-if>
  </actions>
</rule>
```

The following example shows how to move a user to a new post office based on an attribute change:

```
<rule>
  <description>Post Office Move</description>
  <conditions>
   <or>
    <if-class-name mode="nocase" op="equal">User</if-class-name>
   </or>
   <or>
    <if-op-attr name="Description" op="changing-to">NYC</if-op-attr>
   </or>
  </conditions>
  <actions>
   <do-move-dest-object class-name="User">
    <arg-dn>
     <token-text xml:space="preserve">domain.po</token-text>
    </arg-dn>
   </do-move-dest-object>
  </actions>
 </rule>
```

## 5.3.9 Adding Additional Attributes to Be Synchronized

You can map up to twenty user Identity Vault attributes to generic GroupWise attributes and display them in the address book. For these attributes, you use the ranges 50106-50115 and 55002-55011. You must add these Identity Vault attributes to the filter and Schema Mapping policy.

## 5.3.10 Renaming Users

NetIQ recommends that you rename users by changing the naming attribute in the Identity Vault and letting the driver rename the GroupWise account. When CN is the naming attribute (this is the default), no special style sheet coding is required for a rename process. However, the GroupWise MailboxID can be built from attributes other than CN. When one of these attributes is modified, the GroupWise account should also be renamed.

In Example 1 below, the Identity Vault attribute Given Name is used to name the GroupWise account. When Given Name is modified, a GroupWise rename is generated. In Example 2 below, the Identity Vault User object is renamed. Even though the GroupWise account is not renamed, the rename event must pass to the driver.

### Example 1

```
(placed in the subscriber event transform, or subscriber command transform)

<rule>
  <description>Rename User if Given Name is changing</description>
  <conditions>
    <and>
      <if-operation op="equal">modify</if-operation>
      <if-op-attr name="Given Name" op="changing"/>
      <if-class-name op="equal">User</if-class-name>
    </and>
  </conditions>
  <actions>
    <do-rename-dest-object>
      <arg-string>
        <token-op-attr name="Given Name"/>
      </arg-string>
    </do-rename-dest-object>
  </actions>
</rule>
```

### Example 2

```
(placed in the subscriber event transform)

<rule>
  <description>Veto Rename User operations</description>
  <conditions>
    <and>
      <if-operation op="equal">rename</if-operation>
      <if-class-name op="equal">User</if-class-name>
    </and>
  </conditions>
  <actions>
    <do-veto/>
  </actions>
</rule>
```

## 5.3.11 Creating a Gateway Alias

The following DirXML Script code segment shows how to create a gateway alias in the Output Transformation policy. Your code is responsible for generating the value of attributes 50140 and 50077.

```
<rule>
  <description>Create GW Gateway Alias attribute for new user</description>
  <conditions>
    <and>
      <if-operation op="equal">add</if-operation>
      <if-class-name op="equal">User</if-class-name>
    </and>
  </conditions>
  <actions>
    <do-add-dest-attr-value class-name="User" name="Gateway Alias">
      <arg-value type="structured">
        <arg-component name="50140">
          <token-text xml:space="preserve">SMTP</token-text>
        </arg-component>
        <arg-component name="50077">
          <token-text xml:space="preserve">UserOne@novell.com</token-text>
        </arg-component>
      </arg-value>
    </do-add-dest-attr-value>
  </actions>
</rule>
```

where SMTP specifies the gateway alias type and UserOne@novell.com is the gateway alias address.

## 5.3.12 Using the Wildcard Query

Wildcard (\*) query is supported for all attributes except Internet Email Address and Email Address.

### Code Sample

```
<nds dtdversion="4.0" ndsversion="8.x">
  <source>
    <product edition="Advanced" version="4.5.0.0">DirXML</product>
    <contact>NetIQ Corporation</contact>
  </source>
<input>
    <query class-name="User" event-id="0" scope="subtree">
      <search-class class-name="User"/>
      <search-attr attr-name="50089">
        <value type="string">AAA*</value>
      </search-attr>
      <read-attr attr-name="50089"/>
    </query>
  </input>
</nds>
```

### Result

```
<nds dtdversion="2.0" ndsversion="8.x">
  <source>
    <product build="20160208_0216" instance="GroupWise REST Driver"version="4.0.2.0">DirXML Driver for GroupWise</product>
    <contact>NetIQ Corporation</contact>
  </source>
<output>
   <instance class-name="User" event-id="0" src-dn="gwdomain.po1.user1">
      <association>gwdomain.po1.user1{106}{B1D8F380-1429-0000-B673-757234396331}6012EC01-18B5-0000-8300-1F8D6C64A072</association>
      <attr attr-name="OU">
        <value type="string">AAA-ENGINEERING</value>
      </attr>
    </instance>
    <instance class-name="User" event-id="0" src-dn="gwdomain.po1.user2">
      <association>gwdomain.po1.user2{106}{3AC06E00-1595-0000-B673-757234396331}6012EC01-18B5-0000-8300-1F8D6C64A072</association>
      <attr attr-name="OU">
        <value type="string">AAA-SALES</value>
      </attr>
    </instance>
    <status event-id="0" level="success"/>
  </output>
</nds>
```

*NOTE:*Groupwise Rest API returns an error if the search-attr contains ?(question mark) or =(equals to) literals.

## 5.3.13 Querying for a Nickname

The following Output Transformation policy shows how to query for GroupWise nicknames. The search-attrs in this style sheet are optional. They are used to scope the search. When you specify a post office name (50069), you must also specify a domain name (50068). More than one nickname can be returned.

For example, User2a is renamed to User2b, then renamed to User2c. This creates two nickname records (User2a and User2b) that both reference User2c. The following DirXML Script sample code queries the User of the current event for nicknames.

### Code Sample

```
<rule>
  <description>Query for User's GroupWise Nicknames</description>
  <conditions>
    <and>
      <if-operation op="equal">modify</if-operation>
      <if-class-name op="equal">User</if-class-name>
    </and>
  </conditions>
  <actions>
    <do-set-local-variable name="gw-user-name">
      <arg-node-set>
        <token-query class-name="User" scope="entry">
          <arg-association>
            <token-association/>
          </arg-association>
          <arg-string>
            <token-text xml:space="preserve">50035</token-text>
          </arg-string>
          <arg-string>
            <token-text xml:space="preserve">50062</token-text>
          </arg-string>
          <arg-string>
            <token-text xml:space="preserve">50073</token-text>
          </arg-string>
        </token-query>
      </arg-node-set>
    </do-set-local-variable>
    <do-set-local-variable name="gw-nickname">
      <arg-node-set>
        <token-query class-name="GroupWise Nickname">
          <arg-match-attr name="50068">
            <arg-value>
              <token-xpath expression="$gw-user-name//attr[@attr-name='50035']/value"/>
            </arg-value>
          </arg-match-attr>
          <arg-match-attr name="50069">
            <arg-value>
              <token-xpath expression="$gw-user-name//attr[@attr-name='50062']/value"/>
            </arg-value>
          </arg-match-attr>
          <arg-match-attr name="50070">
            <arg-value>
              <token-xpath expression="$gw-user-name//attr[@attr-name='50073']/value"/>
            </arg-value>
          </arg-match-attr>
          <arg-string>
            <token-text xml:space="preserve">50035</token-text>
          </arg-string>
          <arg-string>
            <token-text xml:space="preserve">50062</token-text>
          </arg-string>
          <arg-string>
            <token-text xml:space="preserve">50073</token-text>
          </arg-string>
        </token-query>
      </arg-node-set>
    </do-set-local-variable>
  </actions>
</rule>
```

### Result

```
<nds dtdversion="4.0" ndsversion="8.x">
   <output>
   <instance class-name="GroupWise Nickname" event-id="0">
        <attr attr-name="50035">
            <value type="string">TaoDom</value>
        </attr>
        <attr attr-name="50062">
            <value type="string">TaoPO</value>
        </attr>
        <attr attr-name="50073">
            <value type="string">User2b</value>
          </attr>
    </instance>
    <instance class-name="GroupWise Nickname" event-id="0">
          <attr attr-name="50035">
            <value type="string">TaoDom</value>
    </attr>
    <attr attr-name="50062">
        <value type="string">TaoPO</value>
    </attr>
    <attr attr-name="50073">
        <value type="string">User2a</value>
    </attr>
    </instance>
    <status level="success"/>
    </output>
</nds>
```

## 5.3.14 Querying for a Email Address from a Nickname

The following DirXML script code segment shows how to query the email address from a user nickname.

### Code Sample

```
<nds dtdversion="4.0" ndsversion="8.x">
  <source>
  <product edition="Advanced" version="4.5.3.0">DirXML</product>
    <contact>NetIQ Corporation</contact>
    </source>
  <input>
    <query class-name="User" event-id="0" scope="subtree">
    <search-class class-name="User"/>
  <search-attr attr-name="Internet EMail Address">
  <value>user@domain.com</value>
    </search-attr>
    <read-attr attr-name="Internet EMail Address"/>
  <read-attr attr-name="50073"/>
  </query>
  </input>
  </nds>
```

### Result

```
<nds dtdversion="2.0" ndsversion="8.x">
   <source>
    <product build="20160208_0216" instance="GroupWise REST Driver"version="4.0.2.0">DirXML Driver for GroupWise</product>
   <contact>NetIQ Corporation</contact>
   </source>
   <output><instance class-name="User" event-id="0" src-dn="gwdomain1.po1.user1">
   <association>gwdomain1.po1.user1{106}{98A43B80-129F-0000-8A67-777838626530}1975BF80-18BE-0000-BA4E-0D7666A11154</association>
   <attr attr-name="Internet EMail Address">
   <value type="string">user@domain.com</value>
    </attr>
    <attr attr-name="CN">
  <value type="string">user</value></attr>
    </instance><status event-id="0" level="success"/>
   </output>
  </nds>
```

## 5.3.15 Querying for a Gateway Alias

The following DirXML Script code segment shows how to query in the Output Transformation policy for a gateway alias.

### Code Sample

```
<rule>
  <description>Query for User's GroupWise Gateway Alias</description>
  <conditions>
    <and>
      <if-operation op="equal">modify</if-operation>
      <if-class-name op="equal">User</if-class-name>
      <if-association op="associated"/>
    </and>
  </conditions>
  <actions>
    <do-set-local-variable name="gw-alias">
      <arg-node-set>
        <token-query class-name="User" scope="entry">
          <arg-association>
            <token-association/>
          </arg-association>
          <arg-string>
            <token-text xml:space="preserve">Gateway Alias</token-text>
          </arg-string>
        </token-query>
      </arg-node-set>
    </do-set-local-variable>
  </actions>
</rule>
```

### Result

```
<nds dtdversion="4.0" ndsversion="8.x">
    <output>
         <instance class-name="User" event-id="0" src-dn="TaoDom.TaoPO.User1{106}{640D4300-049C-0000-9F67-777433313534}50D4B180-061B-0000-9A29-2264EBF4B491">
            <association>TaoDom.TaoPO.User1{106}{640D4300-049C-0000-9F67-777433313534}50D4B180-061B-0000-9A29-2264EBF4B491</association>
            <attr attr-name="Gateway Alias">
                 <value type="structured">
                     <component name="50140">SMTP</component>
                     <component name="50077">UserOne@novell.com</component>
                 </value>
            </attr>
         </instance>
         <status level="success"/>
     </output>
</nds>
```

## 5.3.16 Querying for Internet Email Address

The following DirXML Script code segment shows how to query in the Output Transformation policy for the Internet Email Address generated by GroupWise.

### Code Sample

```
<rule>
  <description>Query for User's GroupWise Internet E-mail Address</description>
  <conditions>
    <and>
      <if-operation op="equal">modify</if-operation>
      <if-class-name op="equal">User</if-class-name>
    </and>
  </conditions>

  <actions>
    <do-set-local-variable name="gw-email-address">
      <arg-node-set>
        <token-query class-name="User" scope="entry">
          <arg-association>
            <token-association/>
          </arg-association>
          <arg-string>
            <token-text xml:space="preserve">Internet EMail Address</token-text>
          </arg-string>
        </token-query>
      </arg-node-set>
    </do-set-local-variable>
  </actions>
</rule>
```

### Results

```
<nds dtdversion="4.0" ndsversion="8.x">
    <output>
       <instance class-name="User" event-id="0"
          src-dn="TaoDom.TaoPO.User2{106}{640D4300-049C-0000-9F67-777433313534}50D4B180-061B-0000-9A29-2264EBF4B491">                              <association>TaoDom.TaoPO.User2{106}{640D4300-049C-0000-9F67-777433313534}50D4B180-061B-0000-9A29-2264EBF4B491</association>
            <attr attr-name="Internet EMail Address">
                  <value type="string">User2@domain.com</value>
            </attr>
        </instance>
        <status level="success"/>
    </output>
</nds>
```

## 5.3.17 Synchronizing GroupWise External Users

In your business, you might have several different e-mail applications. Although not all employees have GroupWise e-mail accounts, you want the GroupWise address book to contain all employee information. The driver has the ability to create GroupWise external users, which enables the driver to obtain data from other e-mail systems (via the Identity Vault) and display it in the GroupWise address book. The users in the Identity Vault can be assigned to a GroupWise external post office.

To synchronize data between external e-mail systems and GroupWise, your implementation must meet the following conditions:

* External users must be assigned to or be created in an external post office. These users do not have a GroupWise mailbox.
* External post offices must belong to a non-GroupWise domain.

The following sections explain how to implement this functionality:

* [Creating External Users](modify-policies.html#akxyvi4)
* [Specifying an External Post Office in an Add Event](modify-policies.html#akxywo5)
* [Creating External Post Offices](modify-policies.html#akxz989)

### Creating External Users

There are three ways you can specify placement when creating external users:

* In the Placement rule, you can specify the DN of an Identity Vault object associated with the external post office. For additional information, refer to [Creating External Post Offices](modify-policies.html#akxz989).
* Identify the external post office by [Specifying an External Post Office in an Add Event](modify-policies.html#akxywo5).
* Create a user in an organizational unit associated with the External GroupWise Post Office.

When you create accounts in the Identity Vault for a non-GroupWise user, make sure that gw:classification=“external” attribute is part of the Add event. The attribute can be used on the User object and on the Post Office object. If you have selected the options of [Synchronize eDir OrgUnit to GroupWise External Post Office](global-configuration-values.html#bryot46) during the configuration of the driver, the attribute is automatically part of the Add event.

You can modify the Schema Mapping policy or Output Transformation policy so that it modifies the class name of the user based on some criterion, such as the parent container name. The external users were formerly a separate class. The preferred method is to add the attributes instead of adding a new class. These two methods are mutually exclusive.

When a new GroupWise external user is added to GroupWise, the driver creates an association on the User object in the Identity Vault. If the non-GroupWise user’s information changes in the Identity Vault, the driver synchronizes those changes to GroupWise. If the association key is altered or deleted, the connection is broken, and the driver does not synchronize any changes made to the User object in the Identity Vault to GroupWise.

### Specifying an External Post Office in an Add Event

If you do not use the driver to create an external post office, you need to generate the following information in the XML Add event. You must replace the external post office name and non-GroupWise domain values with names specific to your system.

```
<!--   The external post office name to which the user belongs. -->
       <add-attr attr-name="50062">
               <value type="string"><![CDATA[External post office name]]></value>
     </add-attr>
```

```
<!-- The non-GroupWise domain name to which the external post office belongs. -->
       <add-attr attr-name="50035">
           <value type="string"><![CDATA[Non-GroupWise domain name]></value>
      </add-attr>
```

*NOTE:*If you include the additional XML in the Add event, the value in your Placement policy is overridden.

### Creating External Post Offices

There are two ways you can create external post offices:

* Let the driver create a GroupWise external post office and associate it to an Identity Vault object, such as an Organizational Unit (recommended). Select [Synchronize eDir OrgUnit to GroupWise External Post Office](global-configuration-values.html#bryot46) during the configuration of the driver.
* Create an external post office through GroupWise Web administration console.

*NOTE:*Before you can create an external post office, you must create a non-GroupWise domain.

To specify placement when creating external post offices, specify the name of the non-GroupWise domain in which to create the external post office in the Placement policy.

## 5.3.18 Verifying if an E-Mail Address or Gateway Alias Is Unique

The GroupWise driver has a special query that allows you to see if a proposed Internet e-mail address or gateway alias is unique. Use the following example to first query if an e-mail address is in use, then based on the query results, it tests if it was in use or not.

```
<rule>
  <description> Query to see if e-mail address is unique in GroupWise</description>
    <actions>
    <do-set-local-variable name="PROPOSED-EMAIL" scope="policy">
      <arg-string>
        <token-text xml:space="preserve">Lee.Kristen@KristensRUs.com</token-text>
      </arg-string>
    </do-set-local-variable>
    <do-set-local-variable name="EMAIL" scope="policy">
      <arg-node-set>
        <token-query class-name="User">
          <arg-match-attr name="Internet EMail Address">
            <arg-value type="string">
              <token-local-variable name="PROPOSED-EMAIL"/>
            </arg-value>
          </arg-match-attr>
          <arg-string>
            <token-text xml:space="preserve">50035</token-text>
          </arg-string>
          <arg-string>
            <token-text xml:space="preserve">50062</token-text>
          </arg-string>
          <arg-string>
            <token-text xml:space="preserve">50073</token-text>
          </arg-string>
        </token-query>
      </arg-node-set>
    </do-set-local-variable>
    <do-if>
      <arg-conditions>
        <and>
          <if-xpath op="true">$EMAIL</if-xpath>
        </and>
      </arg-conditions>
      <arg-actions>
        <do-trace-message>
          <arg-string>
            <token-text xml:space="preserve">Email address is in use by the user </token-text>
            <token-xpath expression="$EMAIL/@src-dn"/>
          </arg-string>
        </do-trace-message>
      </arg-actions>
      <arg-actions>
        <do-trace-message>
          <arg-string>
            <token-text xml:space="preserve">Email address not found, you are free to use it.</token-text>
          </arg-string>
        </do-trace-message>
      </arg-actions>
    </do-if>
  </actions>
</rule>
```

## 5.3.19 Converting String Attributes to Structured Attributes

GroupWise supports some of the attributes only in the structured format. You need to convert them to the structured type that GroupWise supports. For example, attributes 50045. The attribute 50045 looks similar to the following in the JSON format:

```
"internetDomainName":{

  "inherited":false,

  "value":"some value",

  "exclusive":false

}
```

The true or false value for the inherited and exclusive components of this attribute depends on the configuration of the GroupWise system. For example,

```
<add-attr attr-name="50045">
        <value type="structured">
          <component name="inherited">true</component>
          <component name="value">company.com</component>
          <component name="exclusive">false</component>
        </value>
</add-attr>
```

For more information about how GroupWise handles these attributes, see [GroupWise SDK: Administration REST API Guide](https://www.novell.com/documentation/groupwise2014/gwsdk_gwadminweb/data/bookinfo.html).

To transform a string attribute type to a structured type, create a Transformation policy similar to the example shown below and add it to the Output Transformation policy of the driver. Also, ensure that you add the structured attributes to the Schema Mapping policy and the Subscriber filter of the driver.

The following example converts the 50045 attribute from a string value to a structured value. To override the preferred Internet domain name that the post office has inherited from its domain, the component inherited is set to false.

```
<rule>
   <description>Convert 50045 attribute from string to structured format</description>
            <comment xml:space="preserve">The GroupWise REST interface requires this attribute in the structured format.</comment>
              <conditions>
                  <and>
                      <if-op-attr name="50045" op="changing"/>
                      <if-xpath op="true">node()[@attr-name='50045']//value/ @type='string'</if-xpath>
                  </and>
               </conditions>
                <actions>
                  <do-reformat-op-attr name="50045">
                    <arg-value type="structured">
                       <arg-component name="inherited">
                          <token-text xml:space="preserve">false</token-text>
                        </arg-component>
                        <arg-component name="value">
                           <token-local-variable name="current-value"/>
                        </arg-component>
                        <arg-component name="exclusive">
                            <token-text xml:space="preserve">false</token-text>
                         </arg-component>
                    </arg-value>
                   </do-reformat-op-attr>
                </actions>
</rule>
```

*NOTE:*In the GroupWise driver, you can set the Exclusive Use of Internet Domain Name by using the attribute 50045. In the legacy GroupWise driver, it could be done by using the attribute 50157. To set the Exclusive Use of Internet Domain Name by using the attribute 50045, set the component exclusive to true for the 50045 attribute in the above example policy.
