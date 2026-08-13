# 7.10 Adding a Group To a Specific Instance

To add a group to a specific instance perform the following actions:

1. You can either map an existing attribute or you can extend the schema to add new attribute for reading connection-dns.

   *NOTE:*The policy is written assuming that the created attribute name as conn-dn. You need to modify the policy as per the created attribute name.
2. Click Filter and add the created or existing attribute from the list of attributes.

   1. Click OK.
   2. Select the created or existing attribute and the Subscriber option as Notify.
3. Add the policy under Event Transformation Policies:

   ```
   <?xml version="1.0" encoding="UTF-8"?><policy>
       <rule>
           <description>Check for GroupAdd With ConnDn</description>
           <conditions>
               <and>
                   <if-class-name mode="nocase" op="equal">Group</if-class-name>
                   <if-operation mode="nocase" op="equal">add</if-operation>
                   <if-op-attr name="conn-dn" op="available"/>
               </and>
           </conditions>
           <actions>
                   <do-set-local-variable name="conn-dn" scope="policy">
                       <arg-node-set>
                           <token-xpath expression="add-attr[@attr-name='conn-dn']/value"/>
                       </arg-node-set>
                   </do-set-local-variable>
                   <do-strip-op-attr name="conn-dn"/>
                   <do-for-each>
                       <arg-node-set>
                           <token-local-variable name="conn-dn"/>
                       </arg-node-set>
                       <arg-actions>
                 <do-set-local-variable name="addDoc" scope="policy">
                       <arg-node-set>
                                   <token-xml-parse>
                                       <token-text xml:space="preserve">&lt;add>&lt;/add></token-text>
                                   </token-xml-parse>
                       </arg-node-set>
                               </do-set-local-variable>
                               <do-clone-xpath dest-expression="$addDoc/add" src-expression="@*"/>
                               <do-set-xml-attr expression="$addDoc/add" name="connection-dn">
                                       <arg-string>
                                           <token-xpath expression="$current-node/text()"/>
                                       </arg-string>
                               </do-set-xml-attr>
                               <do-clone-xpath dest-expression=".." src-expression="$addDoc/node()"/>
                       </arg-actions>
                   </do-for-each>
                   <do-strip-xpath expression="."/>
           </actions>
       </rule>
   </policy>
   ```
4. Restart the driver.
5. Add a group using the ldapadd command.

   The following is a sample ldif file for group add:

   ```
   dn: cn=group_sync_inst,ou=groups,o=data
   objectClass: groupOfNames
   conn-dn: instance1
   conn-dn: instance2
   description: group is a collection of users
   ```

   *NOTE:*By using this ldif file, the group (group\_sync\_1inst) is synchronised with the instances (instance1 and instance2).
