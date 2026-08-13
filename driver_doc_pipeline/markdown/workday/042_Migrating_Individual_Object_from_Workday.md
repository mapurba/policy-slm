# 8.2 Migrating Individual Object from Workday:

You may migrate individual user object either employee or Contingent worker with relation (Position). You may also migrate other object such as job profile, job family, location, organization including cost center, company, HR Company etc. To migrate these objects, use Identity Console’s Migrate into IDVault option. This process will update the IDV object with latest information.

* Migrating users with relation:

1. In Identity Console, click the IDM Administration tile. “Migrate into IDVault” option to migrate individual employee or contingent worker.
2. On the Driver Dashboard, locate the driver and click the driver icon.
3. Click the Data Transformation and Synchronization tab.
4. Click the Migrate into IDVault tab.
5. Click Edit migration criteria.
6. Select user as class and select Show all attributes > from all classes.
7. Select workforce ID and wd-workerIDType and provide the required data.

   wd-workerIDType can be Employee\_ID or Contingent\_Worker\_ID. Workforce ID is the unique ID in Workday.
8. Select OK.

* Migrating job profile:

1. In Identity Console navigate to the Migrate into IDVault tab to migrate job profile.
2. Select Edit migration criteria.
3. Select wd-Jobprofile as class and select Show all attributes > from all classes.

   *NOTE:*You have to first add wd-Jobprofile in the filter list.
4. Select wd-JobProfileID and provide the ID of the object to migrate.

* Migrating job family:

1. In Identity Console navigate to the Migrate into IDVault tab to migrate job family.
2. Select Edit migration criteria.
3. Select wd-Jobfamily as class and select Show all attributes > from all classes.
4. Select wd-JobFamilyID and provide the ID of the object to migrate.

* Migrating Location:

1. In Identity Console navigate to the Migrate into IDVault tab to migrate location.
2. Select Edit migration criteria.
3. Select wd-Location as class and select Show all attributes > from all classes.
4. Select wd-LocationID and provide the ID of the object to migrate.

* Migrating Organization – Cost center, company, HR company:

1. In Identity Console navigate to the Migrate into IDVault tab to migrate organization.
2. Select Edit migration criteria.
3. Select wd-organization as class and select Show all attributes > from all classes.
4. Select wd-OrganizationID and provide the ID of the object to migrate.

* Migrating user’s photo:

1. In Identity Console navigate to the Migrate into IDVault tab to migrate photo.
2. Select Edit migration criteria.
3. Select wd-Photo as class and select Show all attributes > from all classes.
4. Select wd-photoID and provide the ID of the object to migrate.
