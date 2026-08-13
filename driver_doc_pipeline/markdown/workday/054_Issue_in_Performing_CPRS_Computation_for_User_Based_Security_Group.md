# 9.11 Issue in Performing CPRS Computation for User-Based Security Group

Workaround: Prior to using the CPRS feature, you must migrate all users from Workday to the Identity Vault atleast once post upgrading to Workday driver 1.3. During the migration process, a cache mapping for user-name and worker-id is created. This mapping is used for displaying the assignments in CPRS. The mapping information is available in user-name-worker-id-mapping.txt file under cache folder.
