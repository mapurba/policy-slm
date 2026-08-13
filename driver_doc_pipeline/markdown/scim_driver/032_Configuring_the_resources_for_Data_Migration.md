# C.1 Configuring the resources for Data Migration

1. Login to Identity Console.
2. Go to IDM Administrator.
3. Select the required Driver Sets.
4. Click the SCIM Driver icon.
5. Go to Data Transformation and Synchronization and click Schema Mapping in the fish bone diagram.
6. Click the available policy.
7. Add the following mapping attribute:

   ```
   <attr-name class-name="User">

           <nds-name>nspmDistributionPassword</nds-name>

           <app-name>password</app-name>

       </attr-name>
   ```
8. Click Save.
9. Again, go to Data Transformation and Synchronization and click Filter in the fish bone diagram.
10. Select the User resource and click Add Attribute.
11. Select nspmDistributionPassword attribute and save.
12. Change the status to Synchronize for both publisher and subscriber channel.
13. Click the Save icon.
