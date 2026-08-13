# 4.1 Customizing the Referenced Attributes Using Policies

Referenced attributes can be handled by customizing the policies in ServiceNow. Company, Location, and Building are examples of some of the referenced attributes in ServiceNow.

Identity Manager allows you to customize the referenced attributes by modifying the policies. For example, you can update the Company attribute for a user on the Subscriber channel by adding a custom policy to the driver using Designer.

To add a custom policy:

1. In Designer, add the Company attribute to the ServiceNow driver filter and select Synchronize under the Subscribe settings.
2. Right-click the Output Transformation Policy, click New, and then click DirXML Script.
3. Add the below DirXML script to the policy you just created.

   ```
   <rule>
     <description>Company attribute Verification</description>
     <conditions>
      <and>
       <if-class-name op="equal">sys_user</if-class-name>
       <if-attr name="company" op="available"/>
       <if-operation mode="nocase" op="equal">modify</if-operation>
      </and>
     </conditions>
     <actions>
      <do-set-local-variable name="companyName" scope="policy">
       <arg-string>
        <token-xpath expression="./modify-attr[@attr-name=&apos;company&apos;]/add-value/value/text()&#xd;&#xa;"/>
       </arg-string>
      </do-set-local-variable>
      <do-set-local-variable name="companyInstance" scope="policy">
       <arg-node-set>
        <token-query class-name="core_company" scope="entry">
         <arg-match-attr name="name">
          <arg-value>
           <token-local-variable name="companyName"/>
          </arg-value>
         </arg-match-attr>
        </token-query>
       </arg-node-set>
      </do-set-local-variable>
      <do-if>
       <arg-conditions>
        <and>
         <if-xpath op="not-true">$companyInstance/../instance</if-xpath>
        </and>
       </arg-conditions>
       <arg-actions>
        <do-add-dest-object class-name="core_company" when="before">
         <arg-dn>
          <token-text xml:space="preserve">Companyattr</token-text>
         </arg-dn>
        </do-add-dest-object>
        <do-add-dest-attr-value class-name="core_company" name="name" when="before">
         <arg-dn>
          <token-text xml:space="preserve">Companyattr</token-text>
         </arg-dn>
         <arg-value type="string">
          <token-xpath expression="./modify-attr[@attr-name='company']/add-value/value/text()"/>
         </arg-value>
        </do-add-dest-attr-value>
        <do-add-dest-attr-value class-name="sys_user" name="company">
         <arg-value type="string">
          <token-xpath expression="./modify-attr[@attr-name='company']/add-value/value/text()"/>
         </arg-value>
        </do-add-dest-attr-value>
       </arg-actions>
       <arg-actions/>
      </do-if>
     </actions>
    </rule>
   ```
4. Deploy the driver along with the policy.

In the above example, when the driver is deployed to the Identity Vault, the policy checks whether the company name exists in the ServiceNow database and performs one of the following actions:

* If the company name exists, the policy links the company with the user.
* If the company name does not exist in the database, the policy updates ServiceNow with the company name and links it with the user.
