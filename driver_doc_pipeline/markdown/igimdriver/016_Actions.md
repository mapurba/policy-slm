# 3.2 Actions

The following actions are supported:

* [Add a Consumer](rest-apis-exposed-by-netiq-igim-driver.html#add-a-consumer-rest-api-exposed-by-idm-igim-driver)
* [Get the Registered Consumers](rest-apis-exposed-by-netiq-igim-driver.html#fetch-details-of-registered-consumers-rest-api-exposed-by-idm-igim-driver)
* [Get a Consumer’s Details](rest-apis-exposed-by-netiq-igim-driver.html#obtain-consumer-details-rest-api-exposed-by-idm-igim-driver)
* [Modify a Consumer](rest-apis-exposed-by-netiq-igim-driver.html#modify-consumer-details-rest-api-exposed-by-idm-igim-driver)
* [Delete a Consumer](rest-apis-exposed-by-netiq-igim-driver.html#delete-a-consumer-rest-api-exposed-by-idm-igim-driver)
* [Get Events](rest-apis-exposed-by-netiq-igim-driver.html#get-events-rest-api-exposed-by-idm-igim-driver)
* [Flush All Events](rest-apis-exposed-by-netiq-igim-driver.html#delete-all-events-rest-api-exposed-by-idm-igim-driver)
* [Flush Events for a Consumer](rest-apis-exposed-by-netiq-igim-driver.html#delete-events-for-a-consumer-rest-api-exposed-by-idm-igim-driver)
* [Flush Events on a Page for a Consumer](rest-apis-exposed-by-netiq-igim-driver.html#delete-a-cached-page-event-for-a-consumer-rest-api-exposed-by-idm-igim-driver)
* [Obtain the Driver Filter](rest-apis-exposed-by-netiq-igim-driver.html#get-the-driver-filter-details-for-a-consumer-rest-api-exposed-by-idm-igim-driver)
* [Get the Driver Attribute Filter for an Object Class](rest-apis-exposed-by-netiq-igim-driver.html#get-driver-filter-details-for-an-object-class-rest-api-exposed-by-idm-igim-driver)
* [Restart the Driver](rest-apis-exposed-by-netiq-igim-driver.html#restart-the-driver-rest-api-exposed-by-idm-igim-driver)

## 3.2.1 Add a Consumer

Request Type
:   POST

API
:   /idv/driver/consumer

Sample URL
:   https://<hostname>:<port>/idv/driver/consumer

Description
:   Adds a consumer.

    A consumer represents a view in the application. For example, Identity Governance. You can add multiple consumers for the same set of object classes or attributes. The driver filter is constructed from the classes or attributes registered for each consumer. Direct update to the filter is not available.

    To eliminate the need for issuing multiple REST calls for flushing events and restarting the driver, specify the following parameters in the request payload:

    * purgeParam: Purges the cached events of all or specific consumers.
    * restartParam: Restarts the driver automatically after the duration specified for the parameter. This is a mandatory parameter because the changes will not be applied to the consumer until the driver is restarted.

Sample1 Request
:   ```
    POST https://192.168.0.1:7708/idv/driver/consumer
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    Content-Type: application/json
    {
    "consumer": {
    "consumerName": "Acme",
    "filter": [{
    "className": "inetorgperson",
    "attributes": [
    "cn",
    "sn",
    "givenname"
    ]
    }]
    }
    }
    ```

Sample1 Response
:   ```
    200 OK
    Content-Type: application/json
    Date: Wed, 10 Oct 2018 08:26:44 GMT
    Server: Jetty(9.4.z-SNAPSHOT)
    Transfer-Encoding: chunked
    {
    "consumerName": "Acme",
    "consumerId": "2119f87e-899a-4e91-97e0-c7c4e28daf09",
    "filter": [{
    "className": "inetorgperson",
    "attributes": ["cn", "sn", "givenname"]
    }]
    }
    ```

Sample2 Request
:   ```
    POST https://192.168.0.1:7708/idv/driver/consumer
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    Content-Type: application/json
    {
       "consumer":{
          "consumerName":"LooneyCorporation",
          "filter":[
             {
                "className":"inetorgperson",
                "attributes":[
                   "cn",
                   "fullName",
                   "title"
                ]
             }
          ]
       },
       "restartParam":{
    "initialDelay":5000
    },
       "purgeParam":{"purgeConsumers":["2119f87e-899a-4e91-97e0-c7c4e28daf09"]
       }
    }
    ```

    NOTE:

    * The purgeConsumers parameter accepts the set of consumer IDs for which all the cached events are purged. To purge all cached events for all consumers, specify the purgeParam parameter in the request payload in the following syntax:

      ```

                            "purgeParam":{ "purgeAll":true}
      ```
    * The restartParam parameter uses the value of initialDelay in milliseconds after that the driver is restarted.

Sample2 Response
:   ```
    200 OK
    Content-Type: application/json
    Server: Jetty(9.4.z-SNAPSHOT)
    Transfer-Encoding: chunked
    {
    "consumerName": "LooneyCorporation",
    "consumerId": "6c0f26da-c83e-4c1f-a90d-7f8de2ff3129",
    "filter": [
            {
                "className": "inetorgperson",
                "attributes": [
                    "cn",
                    "fullName",
                    "title"
                ]
            }
        ]
    }
    ```

Authentication
:   Yes

Error Codes
:   * 200 - OK
    * 204 - No response, OK
    * 400 - Bad Request, ERROR
    * 401 - Authentication Failure, ERROR
    * 404 - Not Found, ERROR
    * 500 - Driver Error, ERROR

## 3.2.2 Get the Registered Consumers

Request Type
:   GET

API
:   /idv/driver/consumer

Sample URL
:   https://<hostname>:<port>/idv/driver/consumer

Description
:   Obtains the details of registered consumers.

Sample Request
:   ```
    GET https://192.168.0.1:7708/idv/driver/consumer
    ```

    ```
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    ```

Sample Response
:   ```
    200 OK
    Content-Type: application/json
    Date: Wed, 10 Oct 2018 08:30:17 GMT
    Server: Jetty(9.4.z-SNAPSHOT)
    Transfer-Encoding: chunked
    {
    "consumers": [{
    "consumerName": "Acme",
    "consumerId": "2119f87e-899a-4e91-97e0-c7c4e28daf09",
    "filter": [{
    "className": "inetorgperson",
    "attributes": ["cn", "sn", "givenname"]
    }]
    }, {
    "consumerName": "LooneyCorporation",
    "consumerId": "6c0f26da-c83e-4c1f-a90d-7f8de2ff3129",
    "filter": [{
    "className": "inetorgperson",
    "attributes": ["cn", "fullName", "title"]
    }]
    }]
    }
    ```

Authentication
:   Yes

Error Codes
:   * 200 - OK
    * 204 - No response, OK
    * 400 - Bad Request, ERROR
    * 401 - Authentication Failure, ERROR
    * 404 - Not Found, ERROR
    * 500 - Driver Error, ERROR

## 3.2.3 Get a Consumer’s Details

Request Type
:   GET

API
:   ```

                    /idv/driver/consumer/{consumerId}
    ```

Sample URL
:   ```
    https://<hostname>:<port>/idv/driver/consumer/{consumerId}
    ```

Description
:   Obtains the details of a consumer.

Sample Request
:   ```
    GET https://192.168.0.1:7708/idv/driver/consumer/2119f87e-899a-4e91-97e0-c7c4e28daf09
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    ```

Sample Response
:   ```
    200 OK
    Content-Type: application/json
    Date: Wed, 10 Oct 2018 08:30:57 GMT
    Server: Jetty(9.4.z-SNAPSHOT)
    Transfer-Encoding: chunked
    {
    "consumerName": "Acme",
    "consumerId": "2119f87e-899a-4e91-97e0-c7c4e28daf09",
    "filter": [{
    "className": "inetorgperson",
    "attributes": ["cn", "sn", "givenname"]
    }]
    }
    ```

Authentication
:   Yes

Error Codes
:   * 200 - OK
    * 204 - No response, OK
    * 400 - Bad Request, ERROR
    * 401 - Authentication Failure, ERROR
    * 404 - Not Found, ERROR
    * 500 - Driver Error, ERROR

## 3.2.4 Modify a Consumer

Request Type
:   PUT

API
:   ```

                    /idv/driver/consumer
    ```

Sample URL
:   ```
    https://<hostname>:<port>/idv/driver/consumer
    ```

Description
:   Updates a consumer.

    To eliminate the need for issuing multiple REST calls for flushing events and restarting the driver, specify the following parameters in the request payload:

    * purgeParam: Purges the cached events of all or specific consumers.
    * restartParam: Restarts the driver automatically after the duration specified for the parameter. This is a mandatory parameter because the changes will not be applied to the consumers until the driver is restarted.

Sample Request
:   ```
    PUT https://192.168.0.1:7708/idv/driver/consumer
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    Content-Type: application/json
    {
       "consumer":{
          "consumerName":"Acme",
          "filter":[
             {"className":"inetorgperson",
                "attributes":["givenname"]
             }
          ]
       },
       "restartParam":{
    "initialDelay":5000
       },
       "purgeParam":{"purgeConsumers":["2119f87e-899a-4e91-97e0-c7c4e28daf09"]
       }
    }
    ```

Sample Response
:   ```
    200 OK
    Content-Type: application/json
    Server: Jetty(9.4.z-SNAPSHOT)
    Transfer-Encoding: chunked
    {
    "consumerName": "Acme",
    "consumerId": "2119f87e-899a-4e91-97e0-c7c4e28daf09",
    "filter": [
            {
                "className": "inetorgperson",
                "attributes": ["givenname"]
            }
        ]
    }
    ```

Authentication
:   Yes

Error Codes
:   * 200 - OK
    * 204 - No response, OK
    * 400 - Bad Request, ERROR
    * 401 - Authentication Failure, ERROR
    * 404 - Not Found, ERROR
    * 500 - Driver Error, ERROR

## 3.2.5 Delete a Consumer

Request Type
:   DELETE

API
:   ```

                    /idv/driver/consumer/{consumerId}
    ```

Sample URL
:   ```
    https://<hostname>:<port>/idv/driver/consumer/{consumerId}
    ```

Description
:   Deletes a consumer.

Sample Request
:   ```
    DELETE https://192.168.0.1:7708/idv/driver/consumer/2119f87e-899a-4e91-97e0-c7c4e28daf09
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    ```

Sample Response
:   ```
    204 No Content
    Content-Type: application/json
    Date: Wed, 10 Oct 2018 08:54:11 GMT
    Server: Jetty(9.4.z-SNAPSHOT)
    ```

Authentication
:   Yes

Error Codes
:   * 200 - OK
    * 204 - No response, OK
    * 400 - Bad Request, ERROR
    * 401 - Authentication Failure, ERROR
    * 404 - Not Found, ERROR
    * 500 - Driver Error, ERROR

## 3.2.6 Get Events

Request Type
:   GET

API
:   /idv/events/{consumerId}

Query Parameters
:   pageSize

    * Default: 25
    * Min: 1
    * Max: 500

Sample URL
:   ```
    https://<hostname>:<port>/idv/events/{consumerId}
    ```

Description
:   Obtains a page of cached events for the specified consumer. If you are registering a consumer, it returns a consumerId for the consumer.

Sample Request
:   ```
    GET https://192.168.0.1:7708/idv/events/6c0f26da-c83e-4c1f-a90d-7f8de2ff3129

    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    ```

Sample Response
:   ```
    200 OK
    Content-Type: application/json
    Date: Thu, 11 Oct 2018 08:11:22 GMT
    Server: Jetty(9.4.z-SNAPSHOT)
    Transfer-Encoding: chunked
    {
    "events": [{
    "eventType": "modify",
    "objectClass": "inetorgperson",
    "srcDn": "CN=ab4,OU=engg,OU=users,O=data",
    "association": "uv8QJqFRUkSxObr\/ECahUQ==",
    "attributes": {
    "cn": {
    "removeAllValues": true,
    "addValue": ["ab4"]
    },
    "fullName": {
    "removeAllValues": true,
    "addValue": ["ab4 ab4"]
    },
    "title": {
    "removeAllValues": true
    }
    }
    }, {
    "eventType": "move",
    "objectClass": "inetorgperson",
    "srcDn": "CN=ab4,OU=engg,OU=users,O=data",
    "cachedTime": "20171012042831.471Z",
    "oldSrcDn": "CN=ab4,OU=users,O=data",
    "association": "uv8QJqFRUkSxObr\/ECahUQ==",
    "parent": {
    "srcDn": "OU=engg,OU=users,O=data"
    }
    }],
    "size": 2,
    "hasMore": false,
    "pageId": "a763bf7d-6b3b-4f5f-8881-ecad91483f50"
    }
    ```

    In Manual flush mode, the cached events are cleaned up by the Flush API. The API returns an empty response in absence of change events.

Authentication
:   Yes

Error Codes
:   * 200 - OK
    * 204 - No response, OK
    * 400 - Bad Request, ERROR
    * 401 - Authentication Failure, ERROR
    * 404 - Not Found, ERROR
    * 500 - Driver Error, ERROR

## 3.2.7 Flush All Events

Request Type
:   DELETE

API
:   /idv/events

Sample URL
:   https://<hostname>:<port>/idv/events

Description
:   Deletes all cached events.

Sample Request
:   ```
    DELETE http://192.168.0.1:7708/idv/events
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    ```

Sample2 Response
:   ```
    204 No Content
    Content-Type: application/json
    Date: Wed, 12 Sep 2018 08:55:50 GMT
    Server: Jetty(9.4.z-SNAPSHOT)
    ```

Authentication
:   Yes

Error Codes
:   * 204 - No response, OK
    * 401 - Authentication Failure, ERROR
    * 500 - Driver Error, ERROR

## 3.2.8 Flush Events for a Consumer

Request Type
:   DELETE

API
:   ```
    /idv/events/{consumerId}
    ```

Sample URL
:   ```
    https://<hostname>:<port>/idv/events/{consumerId}
    ```

Description
:   Deletes all cached events for a consumer.

Sample Request
:   ```
    DELETE http://192.168.0.1:7708/idv/events/6c0f26dac83e-4c1f-a90d-7f8de2ff3129
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    ```

Sample Response
:   ```
    204 No Content
    Content-Type: application/json
    Date: Wed, 10 Oct 2018 09:28:12 GMT
    Server: Jetty(9.4.z-SNAPSHOT)
    ```

Authentication
:   Yes

Error Codes
:   * 204 - No response, OK
    * 401 - Authentication Failure, ERROR
    * 500 - Driver Error, ERROR

## 3.2.9 Flush Events on a Page for a Consumer

Request Type
:   DELETE

API
:   ```
    /idv/events/{consumerId}/{pageId}
    ```

Sample URL
:   ```
    https://<hostname>:<port>/idv/events/{consumerId}/{pageId}
    ```

Description
:   Deletes a cached event page for a consumer.

Sample Request
:   ```
    DELETE http://192.168.0.1:7708/idv/events/6c0f26dac83e-4c1f-a90d-7f8de2ff3129/bf4dcbf8-31a8-4701-a9e4-4fc2ad7d40d4
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    ```

Sample Response
:   ```
    204 No Content
    Content-Type: application/json
    Date: Wed, 12 Sep 2018 08:54:39 GMT
    Server: Jetty(9.4.z-SNAPSHOT)
    ```

Authentication
:   Yes

Error Codes
:   * 204 - No response, OK
    * 401 - Authentication Failure, ERROR
    * 404 - Not Found, ERROR
    * 500 - Driver Error, ERROR

## 3.2.10 Obtain the Driver Filter

Request Type
:   GET

API
:   ```
    /idv/driver/filter
    ```

Sample URL
:   ```
    https://<hostname>:<port>/idv/driver/filter
    ```

Description
:   Obtains details of the driver filter.

Sample Request
:   ```
    GET http://192.168.0.1:7708/idv/driver/filter
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    ```

Sample Response
:   ```
    {
        "objectClasses": {
            "className": "inetorgperson",
            "attributes": [
    "cn","fullName","title"
            ]
        }
    }
    ```

Authentication
:   Yes

Error Codes
:   * 200 - OK
    * 204 - No response, OK
    * 401 - Authentication Failure, ERROR
    * 404 - Not Found, ERROR
    * 500 - Driver Error, ERROR

## 3.2.11 Get the Driver Attribute Filter for an Object Class

Request Type
:   GET

API
:   ```
    /idv/driver/filter/{objectclass}
    ```

Sample URL
:   ```
    https://<hostname>:<port>/idv/driver/filter/{objectclass}
    ```

Description
:   Obtains details of attribute filter of an object class.

Sample Request
:   ```
    GET
    http://192.168.0.1:7708/idv/driver/filter/inetorgperson
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    ```

Sample Response
:   ```
    {
        "className": "inetorgperson",
        "attributes": [
    "cn","fullName","title"
            ]
    }
    ```

Authentication
:   Yes

Error Codes
:   * 200 - OK
    * 204 - No response, OK
    * 401 - Authentication Failure, ERROR
    * 404 - Not Found, ERROR
    * 500 - Driver Error, ERROR

## 3.2.12 Restart the Driver

Request Type
:   PUT

API
:   ```
    /idv/driver/restart
    ```

Sample URL
:   ```
    https://<hostname>:<port>/idv/driver/restart
    ```

Description
:   Restarts the driver.

Sample Request
:   ```
    PUT http://192.168.0.1:7708/idv/driver/restart
    Authorization: Basic Y249YWRtaW4sb3U9c2Esbz1zeXN0ZW06bm92ZWxs
    Content-Type: application/json
    {
    "initialDelay":10000
    }
    ```

Sample Response
:   ```
    200 OK
    Content-Type: application/json
    Date: Mon, 10 Sep 2018 08:22:54 GMT
    Server: Jetty(9.4.z-SNAPSHOT)
    Transfer-Encoding: chunked
    {
    "submitted": true
    }
    ```

Authentication
:   Yes

Error Codes
:   * 200 - OK
    * 401 - Authentication Failure, ERROR
    * 500 - Driver Error, ERROR
