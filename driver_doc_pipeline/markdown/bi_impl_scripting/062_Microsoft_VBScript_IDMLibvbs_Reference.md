# C.4 Microsoft VBScript (IDMLib.vbs) Reference

The scripts are written using Microsoft VBScript. They are located in the scripts folder below the folder where the driver was installed (C:\Program Files\Novell\WSDriver by default).

Subscriber events are submitted to Subscriber.wsf, which then calls the script for the event. Modify the VBS file corresponding to the event type: Add.vbs, Modify.vbs, ModifyPassword.vbs, Delete.vbs, Move.vbs, Rename.vbs. Queries of the external system should be handled in Query.vbs.

The Publisher calls Poll.wsf periodically. The frequency of the poll is determined by the Polling Interval driver parameter (60 seconds by default). Edit Poll.wsf to allow the driver to respond to events in the external account management system.

The Publisher calls Heartbeat.wsf periodically to determine whether the external account management system is responding correctly.

Topics discussing the built-in functions in IDMLib.vbs are categorized as follows:

* [General Functions](b8nqqta.html#b8nqqtb)
* [Subscriber Functions](b8nqqta.html#b8nqqtl)
* [Publisher Functions](b8nqqta.html#b8nqqtp)
* [Query Functions](b8nqqta.html#b8nqqtr)
* [Heartbeat Functions](b8nqqta.html#b8nqqtu)

## C.4.1 General Functions

* [Function IDMGetDriverParam(ParamName)](b8nqqta.html#b8nqqtc)
* [Sub IDMTrace Message](b8nqqta.html#b8nqqtd)
* [Function IDMExecute(Command)](b8nqqta.html#b8nqqte)
* [Function IDMExecuteIO(Command, Input)](b8nqqta.html#b8wfptf)
* [Sub IDMStatus(Level, Message)](b8nqqta.html#b8nqqtf)
* [Sub IDMStatusSuccess(Message)](b8nqqta.html#b8nqqtg)
* [Sub IDMStatusWarning(Message)](b8nqqta.html#b8nqqth)
* [Sub IDMStatusRetry(Message)](b8nqqta.html#b8nqqti)
* [Sub IDMStatusError(Message)](b8nqqta.html#b8nqqtj)
* [Sub IDMStatusFatal(Message)](b8nqqta.html#b8nqqtk)

### Function IDMGetDriverParam(ParamName)

Returns the string value for the Driver parameter specified by the string ParamName.

### Sub IDMTrace Message

Appends the specified message to the user-defined trace file.

### Function IDMExecute(Command)

Executes an external program using the specified command line, and returns its numerical exit code on completion.

### Function IDMExecuteIO(Command, Input)

Executes an external program using the specified command line, submits the strings from array Input on standard input, and returns output from standard output and standard error as an array. You can specify Empty for the Input parameter. The function returns when the program completes. The first element of the returned array is the program exit code. Subsequent elements (if any) are strings, one for each line that was output to standard output and standard error.

### Sub IDMStatus(Level, Message)

Set the status level and message to return to the Identity Manager engine when the script completes.

### Sub IDMStatusSuccess(Message)

Set the status level and message to return to the Identity Manager engine when the script completes.

### Sub IDMStatusWarning(Message)

Set the status level and message to return to the Identity Manager engine when the script completes.

### Sub IDMStatusRetry(Message)

Set the status level and message to return to the Identity Manager engine when the script completes.

### Sub IDMStatusError(Message)

Set the status level and message to return to the Identity Manager engine when the script completes.

### Sub IDMStatusFatal(Message)

Set the status level and message to return to the Identity Manager engine when the script completes.

## C.4.2 Subscriber Functions

* [Function IDMGetSubscriberParam(ParamName)](b8nqqta.html#b8nqugv)
* [Sub IDMSetCommand(Command)](b8nqqta.html#b8nqv5y)
* [Function IDMGetEventValueCount(Name)](b8nqqta.html#b8nqvc5)
* [Function IDMGetEventValues(Name)](b8nqqta.html#b8nqvhs)
* [Function IDMGetEventValue(Name)](b8nqqta.html#b8nqvow)
* [Sub IDMWriteValue(Name, Value)](b8nqqta.html#b8nqw24)
* [Sub IDMWriteValues(Name, Values)](b8nqqta.html#b8nqx0k)
* [Function IDMSubGetNamedPassword(Name)](b8nqqta.html#b8nqwtk)

### Function IDMGetSubscriberParam(ParamName)

Returns the string value for the Subscriber parameter specified by the string ParamName.

### Sub IDMSetCommand(Command)

Sets the command that the Subscriber return to the Identity Manager engine. This function must be called before using IDMWriteValue functions. If only a status needs to be returned, use one of the IDMStatus functions (see above).

### Function IDMGetEventValueCount(Name)

Returns the number of values for the item specified by Name. (Items include event information and attribute changes.)

### Function IDMGetEventValues(Name)

Returns an array of string values for the item specified by Name. If no values exist, Empty is returned.

### Function IDMGetEventValue(Name)

Returns the string value for the item specified by Name. If multiple values exist for the item, it returns the first value. If no values exist, Empty is returned.

### Sub IDMWriteValue(Name, Value)

Sets a single string value for the item specified by Name to be returned to the driver engine when the script completes. You must call IDMSetCommand or one of the IDMStatus functions before calling this function.

### Sub IDMWriteValues(Name, Values)

Sets an array of string values for the item specified by Name to be returned to the driver engine when the script completes. You must call IDMSetCommand or one of the IDMStatus functions before calling this function.

### Function IDMSubGetNamedPassword(Name)

Returns a named password specifed by Name from the Identity Manager engine. The value Empty is returned if no such password exists.

## C.4.3 Publisher Functions

* [Function IDMGetPublisherParam(ParamName)](b8nqqta.html#b8nqqtq)
* [Sub IDMPublishInit(Command)](b8nqqta.html#b8nqy7v)
* [Sub IDMPublishValue(Name, Value)](b8nqqta.html#b8nqz27)
* [Sub IDMPublishValues(Name, Values)](b8nqqta.html#b8nqyeh)
* [Function IDMPublish](b8nqqta.html#b8nqyta)
* [Function IDMPubGetNamedPassword(Name)](b8nqqta.html#b8nr0dl)

### Function IDMGetPublisherParam(ParamName)

Returns the string value for the Publisher parameter specified by the string ParamName.

### Sub IDMPublishInit(Command)

Sets the Publisher command specified by Command to return to the driver engine when IDMPublish is called.

### Sub IDMPublishValue(Name, Value)

Sets a single string value for the item specified by Name to be returned to the driver engine when IDMPublish is called.

### Sub IDMPublishValues(Name, Values)

Sets an array of string values for the item specified by Name to be returned to the driver engine when IDMPublish is called.

### Function IDMPublish

Submit the command and item values specified above to the driver engine for Publication to the identity vault.

### Function IDMPubGetNamedPassword(Name)

Returns a named password specified by Name from the Identity Manager engine. The value Empty is returned if no such password exists.

## C.4.4 Query Functions

* [Sub IDMQueryInit](b8nqqta.html#b8nqqts)
* [Sub IDMQuerySetAssociation(Association)](b8nqqta.html#b8nr1ut)
* [Sub IDMQuerySetSearchRoot(SearchRoot)](b8nqqta.html#b8nr23q)
* [Sub IDMQueryAddSearchAttr(Name, Value)](b8nqqta.html#b8nr2eq)
* [Sub IDMQueryAddReadAttr(Name)](b8nqqta.html#b8nr2mz)
* [Sub IDMQuerySetReadParent(ReadParent)](b8nqqta.html#b8nr2tf)
* [Function IDMQuery](b8nqqta.html#b8nr2zh)
* [Function IDMGetQueryInstanceAssociation](b8nqqta.html#b8nr3ga)
* [Function IDMGetQueryInstanceDN](b8nqqta.html#b8nr3m9)
* [Function IDMGetQueryInstanceClass](b8nqqta.html#b8nr3vm)
* [Function IDMGetQueryInstanceParentAssociation](b8nqqta.html#b8nr43g)
* [Function IDMGetQueryInstanceParentDN](b8nqqta.html#b8nr4b4)
* [Function IDMGetQueryInstanceAttrNames](b8nqqta.html#b8nr4j1)
* [Function IDMGetQueryInstanceAttrCount](b8nqqta.html#b8nr4ot)
* [Function IDMGetQueryInstanceAttrValues(AttrName)](b8nqqta.html#b8nr4wr)
* [Function IDMGetQueryInstanceAttrValue(AttrName)](b8nqqta.html#b8nr53r)

### Sub IDMQueryInit

Initializes a query to be submitted to the identity vault with the IDMQuery call. NOTE: Currently only queries that query a single object are supported.

### Sub IDMQuerySetAssociation(Association)

Specifies the association of the identity vault object to query.

### Sub IDMQuerySetSearchRoot(SearchRoot)

Specifies the DN of the identity vault object to query. Either the object’s association or DN must be specified. If both are specified, the association value is used by the Identity Manager engine.

### Sub IDMQueryAddSearchAttr(Name, Value)

Specifies a search condition to be used for the query, of the form Name=Value. Name specifies an attribute, and Value specifies a value it must match. The query will return only objects matching all specified conditions.

### Sub IDMQueryAddReadAttr(Name)

Specifies an attribute name whose values should be returned by the query. By default, all attributes are returned.

### Sub IDMQuerySetReadParent(ReadParent)

Specifies whether the association and DN of the parent of the queried object should be returned (ReadParent is boolean). The default is False.

### Function IDMQuery

Executes the query with the parameters specified by IDMQuerySetXXX calls. The function returns True if an object (called an instance) is returned.

### Function IDMGetQueryInstanceAssociation

Returns the association for the returned instance.

### Function IDMGetQueryInstanceDN

Returns the DN for the returned instance. The DN is in slash format, such as \ACME\Users\Bob.

### Function IDMGetQueryInstanceClass

Returns the class name for the returned instance.

### Function IDMGetQueryInstanceParentAssociation

Returns the association for instance’s parent object, if the ReadParent flag was specified.

### Function IDMGetQueryInstanceParentDN

Returns the DN for instance’s parent object, if the ReadParent flag was specified.

### Function IDMGetQueryInstanceAttrNames

Returns an array containing the names of the attributes retrieved for the instance. Returns Empty if no attributes were retrieved.

### Function IDMGetQueryInstanceAttrCount

Returns the number of attributes retrieved for the instance.

### Function IDMGetQueryInstanceAttrValues(AttrName)

Returns an array of values for the attribute with the specified AttrName. Returns Empty if no values are available.

### Function IDMGetQueryInstanceAttrValue(AttrName)

Returns a string value for the attribute with the specified AttrName. If multiple values are available for the attribute, the first one is returned. If no values are available, Empty is returned.

## C.4.5 Heartbeat Functions

* [Sub IDMHeartbeatSuccess(Message)](b8nqqta.html#b8nqqtv)
* [Sub IDMHeartbeatError(Message)](b8nqqta.html#b8nqqtw)
* [Sub IDMHeartbeatWarning(Message)](b8nqqta.html#b8nqqtx)

### Sub IDMHeartbeatSuccess(Message)

Use these functions in the heartbeat.wsf script to indicate the status of the external application.

### Sub IDMHeartbeatError(Message)

Use these functions in the heartbeat.wsf script to indicate the status of the external application.

### Sub IDMHeartbeatWarning(Message)

Use these functions in the heartbeat.wsf script to indicate the status of the external application.
