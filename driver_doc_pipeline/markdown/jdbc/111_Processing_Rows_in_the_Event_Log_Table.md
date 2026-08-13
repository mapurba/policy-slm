# D.3 Processing Rows in the Event Log Table

*Question:*
Why isn’t the driver processing rows in the Event Log Table?

*Answer:*
Do the following:

1. Check the perpetrator field of the rows in question and make sure that the value is set to something other than the driver’s database username.

   The Publisher channel checks the perpetrator field to detect loopback events if the Publisher channel Allow Loopback parameter is set to Boolean False (the default). See [Allow Loopback?](how-to-set-publication-parameters.html#bvw4x51).

   When the Allow Loopback parameter is set to Boolean False, the Publisher channel ignores all records where the perpetrator field value is equal to the driver’s database username. The driver’s database username is specified by using the Authentication ID parameter. See [Authentication ID](jdbc-driver-parameters.html#bvqz2y8).
2. Ensure that the record’s status field is set to N (new).

   Records with status fields set to something other than N will not be processed.
3. Make sure to explicitly commit changes.

   Changes are often tentative until explicitly committed.
