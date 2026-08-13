# C.1 Customizing the Publisher Channel

The Publisher channel of the Oracle EBS drivers is enabled by default. To change the default driver configuration, use Designer.

The following sections provide information about customizing the Publisher channel to synchronize additional attributes from the different Oracle modules with which the drivers synchronize attributes.

* [Using the Oracle E-Business Events](customizing-the-publisher-channel.html#b1ftxibe)
* [Polling the Oracle EBS System Tables](customizing-the-publisher-channel.html#b1fx4da6)
* [Verifying the Changes](customizing-the-publisher-channel.html#b1fxjh6h)

## C.1.1 Using the Oracle E-Business Events

The Publisher channel of the driver is enabled by default unless you change this setting during driver configuration in Designer. The driver starts when the Oracle EBS system starts and internally starts the HTTP jetty server and listens on the specified port for the Publisher events from the Oracle EBS system. The PL/SQL script securely transports the events to the http://<driver IP address>:<Port> URL, then the driver submits the XML documents to the Identity Manager engine to publish the XML documents in the Identity Vault.

The following are sample XML documents for User Add and Modify operations supported in the Publisher channel. You can customize them to suit your environment.

*Example C-1*  Publisher XML Request for a User Add Event

```
<EBS_EVENT>
         <EVENT_NAME>oracle.apps.fnd.user.insert</EVENT_NAME>
         <EVENT_KEY>$user id</EVENT_KEY>
         <OBJECT type="user">
                 <USER_NAME></USER_NAME>
                 <EMAIL_ADDRESS></EMAIL_ADDRESS>
                 <DESCRIPTION></DESCRIPTION>
                         .
                         .
                         .
                         .
                 <LOGIN_DISABLED>false</LOGIN_DISABLED>
         </OBJECT>
</EBS_EVENT>
```

*Example C-2*  Publisher XML Request for a User Modify Event

```
<EBS_EVENT>
   <EVENT_NAME>oracle.apps.fnd.user.update</EVENT_NAME>
   <EVENT_KEY>$user id</EVENT_KEY>
   <OBJECT type="user">
       <USER_NAME></USER_NAME>
       <EMAIL_ADDRESS></EMAIL_ADDRESS>
       <DESCRIPTION></DESCRIPTION>
          .
          .
          .
          .
       <LOGIN_DISABLED>false</LOGIN_DISABLED>
   </OBJECT>
   <OLD_OBJECT type="user">
       <USER_NAME></USER_NAME>
       <EMAIL_ADDRESS></EMAIL_ADDRESS>
       <DESCRIPTION></DESCRIPTION>
          .
          .
          .
          .
          .
          .
          .
        <LOGIN_DISABLED>false</LOGIN_DISABLED>
   </OLD_OBJECT>
</EBS_EVENT>
```

The Oracle E-Business events post the user attribute changes from the Oracle EBS system to the driver. Subscribe to these events to add or modify the users in the Identity Vault. You can write specific PL/SQL methods and then subscribe to the business events for receiving user information modifications. Otherwise, modify the PL/SQL scripts shipped with the driver.

By default, the driver can synchronize all attributes from the FND\_USER, ER\_ALL\_PEOPLE\_F and HZ\_PARTIES tables. You need not modify the PL/SQL scripts to add new attributes. However, you need to modify the IDM\_DRIVER.PUBLISH\_EVENT\_TO\_ IDM PL/SQL script to synchronize attributes from the different tables in the Oracle EBS system.

NetIQ recommends that you add the new attributes as XML tags under the <OBJECT> tag and also add them to the driver Schema Mapping policy in the Identity Manager.

## C.1.2 Polling the Oracle EBS System Tables

Another way of synchronizing the columns of other tables from the Oracle EBS system is to create a new PL/SQL procedure in the IDMDRIVER package, then modify the XML document and add it to the newly created PL/SQL procedure.

To synchronize an attribute from the PER\_ADDRESSES table with Identity Manager, perform the following actions:

1. Construct the driver understandable XML document by creating a new FIND\_PER\_ADDRESSES\_ADD\_EVENTS procedure.

   This procedure should be similar to the FIND\_EMPLOYEE\_ADD\_EVENTS procedure.
2. Post the XML document to the driver.
3. Call the new PL/SQL method as part of the driver polling cycle by adding the FIND\_PER\_ADDRESSES\_ADD\_EVENTS procedure in the IDMDRIVER.SYNCH\_EVENTS\_WITH\_IDM procedure.
4. Modify the schema mapping policy for the driver to add the new attributes in Identity Manager.
5. Restart the driver.

Sample XML code for the Publisher Channel

1. Create a temporary table IDMUSRMGT.IDM\_PER\_ADDRESSES in the Oracle EBS system.
2. Identify the differences in the value between the temporary table and the Oracle EBS table using the below SQL query:

   ```
   sql>CREATE TABLE IDMUSRMGT.IDM_ PER_ADDRESSES
     AS (SELECT *
            FROM PER_ADDRESSES
            WHERE ADDRESS_ID< 0);
   ```
3. Create a new procedure to read the user address.

   ```
   PROCEDURE FIND_PER_ADDRESSES_ADD_EVENTS

   IS
     HR_EVENT_DOC CLOB := NULL;
     clob_locator CLOB;
     v_person_id NUMBER(15) :=100;
     CURSOR PER_ADDRESSES_CUR
     IS
       SELECT *
       FROM (
         (SELECT unique PERSON_ID
         FROM PER_ADDRESSES
         WHERE CREATED_BY!=-1
         AND CREATION_DATE BETWEEN (SELECT START_DATE FROM IDMUSRMGT.IDM_SYNC_START_DATE) AND SYSDATE
       MINUS
       SELECT PERSON_ID FROM IDMUSRMGT.IDM_PER_ADDRESSES
         ));
       PER_ALL_PEOPLE_REC PER_ADDRESSES_CUR%rowtype;
     BEGIN
       OPEN PER_ADDRESSES_CUR;
       LOOP
         FETCH PER_ADDRESSES_CUR INTO PER_ALL_PEOPLE_REC;
         EXIT
       WHEN PER_ADDRESSES_CUR%NOTFOUND;
         v_person_id    := PER_ALL_PEOPLE_REC.PERSON_ID;
         HR_EVENT_DOC :='<EBS_EVENT><EVENT_NAME>oracle.apps.fnd.user.insert</EVENT_NAME><OBJECT type="user"><LOGIN_DISABLED>false</LOGIN_DISABLED></OBJECT></EBS_EVENT>';
         SELECT dbms_xmlquery.getxml('SELECT * FROM PER_ADDRESSES where PERSON_ID='
           ||v_person_id,10)
         INTO clob_locator
         FROM DUAL;
         DBMS_LOB.COPY(HR_EVENT_DOC, to_clob('<EMPLOYEE></EMPLOYEE>'), 21 ,INSTR(HR_EVENT_DOC,'</EBS_EVENT>', -1), 1);
         DBMS_LOB.COPY(HR_EVENT_DOC, CLOB_LOCATOR, INSTR(CLOB_LOCATOR,'</ROW>',                                -1)- INSTR(CLOB_LOCATOR,'<ROW num="1">')-14 ,INSTR(HR_EVENT_DOC,'</EMPLOYEE>', -1), INSTR(CLOB_LOCATOR,'<ROW num="1">')+14);
         DELETE FROM IDMUSRMGT.IDM_PER_ADDRESSES WHERE PERSON_ID=v_person_id;
         INSERT INTO IDMUSRMGT.IDM_PER_ADDRESSES
         SELECT * FROM PER_ADDRESSES WHERE PERSON_ID=v_person_id;
         HR_EVENT_DOC:=HR_EVENT_DOC||'</EMPLOYEE></EBS_EVENT>';
         PERSISTS_EVENT( 'oracle.apps.fnd.user.insert','EMPLOYEE_ADD',NULL,HR_EVENT_DOC,NULL,'NEW',SYSDATE);
         commit;
         END LOOP;
     END;
   ```
4. Add the newly created procedure to the existing method.

   ```
   PROCEDURE SYNCH_EVENTS_WITH_IDM(
       request IN VARCHAR2 )
   IS
   BEGIN
     FIND_EMPLOYEE_ADD_EVENTS();
        :
        :
        :
        :
        :
        :
     FIND_PER_ADDRESSES_ADD_EVENTS();
     PUBLISH_EVENTS();
   END;
   ```

## C.1.3 Verifying the Changes

1. Create a user/employee in the Oracle EBS system with the recently added attributes.
2. Modify the attributes.
3. Verify if the attributes are synchronised with the Identity Manager.
