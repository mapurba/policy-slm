# C.1 Tips for Synchronizing Millions of User Records on the Publisher Channel

For successfully synchronizing millions of user records, change the following settings using Designer:

1. Click the driver set that contains this driver and change the Java Maximum heap size to 256 MB. This change will be applicable to all the drivers under this driver set.
2. Under the Driver Settings tab, change the Show the compatibility parameters? option to show to display the Show backward compatibility parameters? option. Change it to show, then change the Enable the Table Referential attribute support? to No.
3. Under the Publisher Settings tab, change the Show polling-related parameters? option to show to display the Batch Size, then change it to 128.
