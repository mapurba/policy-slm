# 1.1 How the Driver Works

The IGIM driver does not connect to a target application. The driver allows consumers and clients to register for change events for specific classes or attributes, or both. You can register a consumer through a REST API by specifying a unique name and an attribute filter for the consumer. For more information, see [Add a Consumer](rest-apis-exposed-by-netiq-igim-driver.html#add-a-consumer-rest-api-exposed-by-idm-igim-driver).

The driver is initially configured with a skeletal filter, which contains only those attributes that are required by the driver to function. The filter is dynamically updated based on the consumer registration data. Therefore, you must not directly modify the filter. Multiple consumers can be registered with the driver.

![](../graphics/igim_architecture.png)

When a change occurs for any classes or attributes specified in the driver filter, the driver caches the change and makes it available to the REST APIs. The application collector uses these REST APIs to obtain the changes.
