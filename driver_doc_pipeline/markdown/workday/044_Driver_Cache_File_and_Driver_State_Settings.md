# 9.1 Driver Cache File and Driver State Settings

As part of cache management, the shim develops sets of cache files. It compares the attribute value after conversion from SOAP response and passes only changed value to the driver channel. The driver will develop these cache files either on the server where Identity Manager engine is running (in Native setup) or at the remote loader server where the driver shim is running. You may delete these files in the case of corruption (If any). After deletion, the driver will redevelop these files but the driver will lose all caches and has to build up cache again from the beginning.

The Driver state setting file keeps the information about the last poll timestamp and also the pages fetched in the initial migration. A sample state file is shown below:

state\_\_u5fTREEu5fSLES\_system\_driverset1\_workdayu20v25.xml
