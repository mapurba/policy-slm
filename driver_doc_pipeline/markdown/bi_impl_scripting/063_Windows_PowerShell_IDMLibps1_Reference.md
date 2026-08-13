# C.5 Windows PowerShell (IDMLib.ps1) Reference

The scripts are written using Windows PowerShell. They are located in the scripts\powershell folder below the folder where the driver was installed (C:\Program Files\Novell\WSDriver by default).

Subscriber events are submitted to Subscriber.ps1, which then calls the script for the event. Modify the ps1 file corresponding to the event type: Add.ps1, Modify.ps1, ModifyPassword.ps1, Delete.ps1, Move.ps1, Rename.ps1. Queries of the external system should be handled in Query.ps1.

The Publisher calls Poll.ps1 periodically. The frequency of the poll is determined by the Polling Interval driver parameter (60 seconds by default). Edit Poll.ps1 to allow the driver to respond to events in the external account management system.

The Publisher calls Heartbeat.ps1 periodically to determine whether the external account management system is responding correctly.

Topics discussing the built-in functions in IDMLib.ps1 are categorized as follows:

* [General Functions](bf20v4l.html#bf20v4m)
* [Subscriber Functions](bf20v4l.html#bf20v4x)
* [Publisher Functions](bf20v4l.html#bf20v56)
* [Query Functions](bf20v4l.html#bf20v5d)
* [Heartbeat Functions](bf20v4l.html#bf20v5u)

## C.5.1 General Functions

* [function idm\_getdriverparam($paramname)](bf20v4l.html#bf20v4n)
* [function idm\_trace($message)](bf20v4l.html#bf20v4o)
* [function idm\_status($level, $message)](bf20v4l.html#bf20v4r)
* [function idm\_statussuccess($message)](bf20v4l.html#bf20v4s)
* [function idm\_statuswarning($message)](bf20v4l.html#bf20v4t)
* [function idm\_statusretry($message)](bf20v4l.html#bf20v4u)
* [function idm\_statuserror($message)](bf20v4l.html#bf20v4v)
* [function idm\_statusfatal($message)](bf20v4l.html#bf20v4w)

### function idm\_getdriverparam($paramname)

Returns the string value for the Driver parameter specified by the string $paramname.

### function idm\_trace($message)

Appends the specified message to the user-defined trace file.

### function idm\_status($level, $message)

Set the status level and message to return to the Identity Manager engine when the script completes.

### function idm\_statussuccess($message)

Set the status success message to return to the Identity Manager engine when the script completes.

### function idm\_statuswarning($message)

Set the status warning message to return to the Identity Manager engine when the script completes.

### function idm\_statusretry($message)

Set the status retry message to return to the Identity Manager engine when the script completes.

### function idm\_statuserror($message)

Set the status error message to return to the Identity Manager engine when the script completes.

### function idm\_statusfatal($message)

Set the status fatal message to return to the Identity Manager engine when the script completes.

## C.5.2 Subscriber Functions

* [function idm\_getsubscriberparam($paramname)](bf20v4l.html#bf20v4y)
* [function idm\_setcommand($command)](bf20v4l.html#bf20v4z)
* [function idm\_geteventvalues($name)](bf20v4l.html#bf20v50)
* [function idm\_geteventvalue($name)](bf20v4l.html#bf20v51)
* [function idm\_geteventvaluenames](bf20v4l.html#bf20v52)
* [function idm\_geteventattrnames](bf20v4l.html#bfcczk6)
* [function idm\_writevalues($name, $values)](bf20v4l.html#bf20v53)
* [function idm\_writevalue($name, $value)](bf20v4l.html#bf20v54)
* [function idm\_subgetnamedpassword($name)](bf20v4l.html#bf20v55)

### function idm\_getsubscriberparam($paramname)

Returns the string value for the Subscriber parameter specified by the string $paramname.

### function idm\_setcommand($command)

Sets the command that the Subscriber returns to the Identity Manager engine. This function must be called before using idm\_writevalue functions. If only a status needs to be returned, use one of the idm\_status functions (see above).

### function idm\_geteventvalues($name)

Returns an array of string values for the item specified by $name. If no values exist, $null is returned.

### function idm\_geteventvalue($name)

Returns the string value for the item specified by $name. If no values exist, $null is returned.

### function idm\_geteventvaluenames

Returns an array containing each value name for the event. This function can be used to iterate over every value.

### function idm\_geteventattrnames

Returns an array containing each attribute item for the event. This includes ADD\_attrname, REMOVE\_attrname and PASSWORD values.

### function idm\_writevalues($name, $values)

Sets an array of string values for the item specified by $name to be returned to the driver engine when the script completes. You must call idm\_setcommand or one of the idm\_status functions before calling this function.

### function idm\_writevalue($name, $value)

Sets a single string value for the item specified by $name to be returned to the driver engine when the script completes. You must call idm\_setcommand or one of the idm\_status functions before calling this function.

### function idm\_subgetnamedpassword($name)

Returns a named password specifed by $name from the Identity Manager engine. The value $null is returned if no such password exists.

## C.5.3 Publisher Functions

* [function idm\_getpublisherparam($paramname)](bf20v4l.html#bf20v57)
* [function idm\_publishinit($command)](bf20v4l.html#bf20v58)
* [function idmpublishvalues($name, $values)](bf20v4l.html#bf20v59)
* [function idm\_publishvalue($name, $value)](bf20v4l.html#bf20v5a)
* [function idm\_publish](bf20v4l.html#bf20v5b)
* [function idm\_pubgetnamedpassword($name)](bf20v4l.html#bf20v5c)

### function idm\_getpublisherparam($paramname)

Returns the string value for the Publisher parameter specified by the string $paramname.

### function idm\_publishinit($command)

Sets the Publisher command specified by $command to return to the driver engine when idm\_publish is called.

### function idmpublishvalues($name, $values)

Sets an array of string values for the item specified by $name to be returned to the driver engine when idm\_publish is called.

### function idm\_publishvalue($name, $value)

Sets a single string values for the item specified by $name to be returned to the driver engine when idm\_publish is called.

### function idm\_publish

Submit the command and item values specified above to the driver engine for Publication to the identity vault.

### function idm\_pubgetnamedpassword($name)

Returns a named password specified by $name from the Identity Manager engine. The value $null is returned if no such password exists.

## C.5.4 Query Functions

* [function idm\_queryinit](bf20v4l.html#bf20v5e)
* [function idm\_querysetassociation($association)](bf20v4l.html#bf20v5f)
* [function idm\_querysetsearchroot($searchroot)](bf20v4l.html#bf20v5g)
* [function idm\_queryaddsearchattr($name, $value)](bf20v4l.html#bf20v5h)
* [function idm\_queryaddreadattr($name)](bf20v4l.html#bf20v5i)
* [function idm\_querysetreadparent($readparent)](bf20v4l.html#bf20v5j)
* [function idm\_doquery](bf20v4l.html#bf20v5k)
* [function idm\_getqueryinstanceassociation](bf20v4l.html#bf20v5l)
* [function idm\_getqueryinstancedn](bf20v4l.html#bf20v5m)
* [function idm\_getqueryinstanceclass](bf20v4l.html#bf20v5n)
* [function idm\_getqueryinstanceparentassociation](bf20v4l.html#bf20v5o)
* [function idm\_getqueryinstanceparentDN](bf20v4l.html#bf20v5p)
* [function idm\_getqueryinstanceattrnames](bf20v4l.html#bf20v5q)
* [function idm\_getqueryinstanceattrcount](bf20v4l.html#bf20v5r)
* [function idm\_getqueryinstanceattrvalues($attrname)](bf20v4l.html#bf20v5s)
* [function idm\_getqueryinstanceattrvalue($attrname)](bf20v4l.html#bf20v5t)

### function idm\_queryinit

Initializes a query to be submitted to the identity vault with the idm\_doquery call. NOTE: Currently only queries that query a single object are supported.

### function idm\_querysetassociation($association)

Specifies the association of the identity vault object to query.

### function idm\_querysetsearchroot($searchroot)

Specifies the DN of the identity vault object to query. Either the object’s association or DN must be specified. If both are specified, the association value is used by the Identity Manager engine.

### function idm\_queryaddsearchattr($name, $value)

Specifies a search condition to be used for the query, of the form $name=$value. $name specifies an attribute, and $value specifies a value it must match. The query will return only objects matching all specified conditions.

### function idm\_queryaddreadattr($name)

Specifies an attribute name whose values should be returned by the query. By default, all attributes are returned.

### function idm\_querysetreadparent($readparent)

Specifies whether the association and DN of the parent of the queried object should be returned ($readparent is boolean). The default is $False.

### function idm\_doquery

Executes the query with the parameters specified by idm\_querysetXXX calls. The function returns $True if an object (called an instance) is returned.

### function idm\_getqueryinstanceassociation

Returns the association for the returned instance.

### function idm\_getqueryinstancedn

Returns the DN for the returned instance. The DN is in slash format, for example: \ACME\Users\Bob.

### function idm\_getqueryinstanceclass

Returns the class name for the returned instance.

### function idm\_getqueryinstanceparentassociation

Returns the association for instance’s parent object, if the $readparent flag was specified.

### function idm\_getqueryinstanceparentDN

Returns the DN for instance’s parent object, if the $readparent flag was specified.

### function idm\_getqueryinstanceattrnames

Returns an array containing the names of the attributes retrieved for the instance. Returns $null if no attributes were retrieved.

### function idm\_getqueryinstanceattrcount

Returns the number of attributes retrieved for the instance.

### function idm\_getqueryinstanceattrvalues($attrname)

Returns an array of values for the attribute with the specified $attrname. Returns $null if no values are available.

### function idm\_getqueryinstanceattrvalue($attrname)

Returns a string value for the attribute with the specified $attrname. If multiple values are available for the attribute, the first one is returned. If no values are available, $null is returned.

## C.5.5 Heartbeat Functions

* [function idmheartbeatsuccess($message)](bf20v4l.html#bf20v5v)
* [function idmheartbeaterror($message)](bf20v4l.html#bf20v5w)
* [function idmheartbeatwarning($message)](bf20v4l.html#bf20v5x)

### function idmheartbeatsuccess($message)

Use this function in the heartbeat.ps1 script to indicate a success status of the external application.

### function idmheartbeaterror($message)

Use this function in the heartbeat.ps1 script to indicate an error status of the external application.

### function idmheartbeatwarning($message)

Use this function in the heartbeat.ps1 script to indicate a warning status of the external application.
