# 9.6 Setting Paging Size Parameter Value

If Workday data is fetched using SOAP APIs such as Get\_Workers, Get\_JobProfiles etc., the data is fetched in chunks. The driver fetches data from Workday in pages to limit the number of records to be processed at a time. The Workday driver fetches one page at a time, processes and stores it in the cache, updates the driver storage, and then requests for the next page. The Paging Size value which is already set is directly proportional to the Java heap that is available to the driver, as it uses the heap for local storage of the data records returned by Workday until it is processed and stored in the driver cache as part of every poll request.

The Paging Size value is used for both the recurring and scheduled polling cycle and should be set as per the Java heap available to the driver.

If a smaller value is set as the page size, multiple pages with smaller chunks of data are processed as part of poll and the frequency of the driver processing and storing the data to the driver cache would increase.

You must also check and set the remote loader configuration for Java heap size and number of instances of remote loader running, as these parameter values would be limiting the actual virtual memory available for the Java heap.
