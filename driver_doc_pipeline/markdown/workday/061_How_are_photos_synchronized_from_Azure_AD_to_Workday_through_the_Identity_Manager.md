# 10.5 How are photos synchronized from Azure AD to Workday through the Identity Manager?

Azure AD supports photo synchronization in Identity Manager User container. However, Workday supports photo synchronization through a different container called wd-Photo.

Follow the procedure given below to complete the synchronization:

1. In Identity Console, click the IDM Administration tile.
2. On the Driver Dashboard, click the Workday Driver icon.
3. Click the Data Transformation and Synchronization tab.
4. Click the Filter in the Subscriber channel, add the Azure attribute jpegPhoto. To add:

   1. Select User as class and click Add Attribute.
   2. Click Show All Attribute to display the list of attributes applicable for the class.
   3. Add jpegPhoto, and save.
   4. Select the attribute from the class list and set the following:

   * Publisher: Ignore
   * Subscriber: Notify
5. For the Workday attribute wd-Photo class, set the Subscriber channel to Synchronize.
6. Place the following policy in the subscriber etp after NETQWDDCFG-sub-etp-SupportedOperations-users:

   ```
   <?xml version="1.0" encoding="UTF-8"?><policy>
       <rule>
           <description>subPhotoSync</description>
           <comment xml:space="preserve">SubPhotoSynz</comment>
           <conditions>
               <and>
                   <if-class-name mode="nocase" op="equal">User</if-class-name>
                   <if-op-attr name="jpegPhoto" op="changing"/>
               </and>
           </conditions>
           <actions>
               <do-set-local-variable name="workerID" scope="policy">
                   <arg-string>
                       <token-attr name="workforceID"/>
                   </arg-string>
               </do-set-local-variable>
               <do-set-local-variable name="eType" scope="policy">
                   <arg-string>
                       <token-attr name="wd-WorkerIDType"/>
                   </arg-string>
               </do-set-local-variable>
               <do-set-local-variable name="photoVal" scope="policy">
                   <arg-string>
                       <token-op-attr name="jpegPhoto"/>
                   </arg-string>
               </do-set-local-variable>
               <do-add-dest-attr-value class-name="wd-Photo" name="photo" when="after">
                   <arg-association>
                       <token-local-variable name="workerID"/>
                       <token-text xml:space="preserve">-</token-text>
                       <token-local-variable name="eType"/>
                   </arg-association>
                   <arg-value type="octet">
                       <token-local-variable name="photoVal"/>
                   </arg-value>
               </do-add-dest-attr-value>
           </actions>
       </rule>
   </policy>
   ```
