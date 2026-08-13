# 3.1 Common Response Parameters

The following list contains the parameters whose values are returned in response JSON by all actions pertaining to obtaining events. Any action-specific parameters are listed in the topic for that action.

* size - Specifies the number of records returned. Type: String
* hasMore - Returns true if there are additional events. Otherwise, it returns false. Type: Boolean
* pageId - Specifies the ID of the page containing the events. If you configure the client to manually remove the read events, use this parameter to delete the page containing the events. Type: String
