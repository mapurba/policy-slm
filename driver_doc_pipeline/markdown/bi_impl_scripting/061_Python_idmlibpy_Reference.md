# C.3 Python (idmlib.py) Reference

These scripts are written for the Linux and UNIX Python interpreter. They are located in the scripts folder below the folder where the driver was installed (/opt/novell/usdrv/ by default).

Subscriber events are submitted to subscriber.py, which then calls the script for the event. Modify the Python script file corresponding to the event type: add.py, modify.py, modify-password.py, delete.py, move.py, rename.py. Queries of the external system should be handled in query.py.

The Publisher calls poll.py periodically. The frequency of the poll is determined by the Polling Interval driver parameter (60 seconds by default). Edit poll.py to allow the driver to respond to events in the external account management system.

The Publisher calls heartbeat.py periodically to determine whether the external account management system is responding correctly.

The built-in functions below are defined in idmLib.py.

## C.3.1 General Functions

* [idmgetvar(VariableName)](bf1m36m.html#bf1m36o)
* [idmtrace(Message)](bf1m36m.html#bf1m36p)
* [exec(Command)](bf1m36m.html#bf1m36q)
* [status(Level, Message)](bf1m36m.html#bf1m36r)
* [status\_success(Message)](bf1m36m.html#bf1m36s)
* [status\_warning(Message)](bf1m36m.html#bf1m36t)
* [status\_retry(Message)](bf1m36m.html#bf1m36u)
* [status\_error(Message)](bf1m36m.html#bf1m36v)
* [status\_fatal(Message)](bf1m36m.html#bf1m36w)

### idmgetvar(VariableName)

Returns the string value for the Driver parameter specified by the string ParamName.

### idmtrace(Message)

Appends the specified message to the user-defined trace file.

### exec(Command)

Executes an external program using the specified command line, and returns its numerical exit code on completion.

### status(Level, Message)

Sends a status document with given level and message to return to the Identity Manager engine when the script completes.

### status\_success(Message)

Sends a status document with a success level and message to return to the Identity Manager engine when the script completes.

### status\_warning(Message)

Sends a status document with a warning level and message to return to the Identity Manager engine when the script completes.

### status\_retry(Message)

Sends a status document with a retry level and message to return to the Identity Manager engine when the script completes.

### status\_error(Message)

Sends a status document with a error level and message to return to the Identity Manager engine when the script completes.

### status\_fatal(Message)

Sends a status document with a fatal level and message to return to the Identity Manager engine when the script completes.

## C.3.2 Subscriber Functions

* [idmgetsubvar(VariableName)](bf1m36m.html#bf1m36y)
* [idmgetvar(Name)](bf1m36m.html#bf1m36z)
* [idmsetvar(Name, Value)](bf1m36m.html#bf1m370)

### idmgetsubvar(VariableName)

Returns the string value for the Subscriber parameter specified by the string VariableName.

### idmgetvar(Name)

Returns a string value for the item specified by Name through standard output. If no values exist, Empty is returned. If the value is multi-valued, each value is separated by a newline character.

### idmsetvar(Name, Value)

Sets a single string value for the item specified by Name to be returned to the driver engine.

## C.3.3 Publisher Functions

* [idmgetpubvar(VariableName)](bf1m36m.html#bf1m372)

### idmgetpubvar(VariableName)

Returns the string value for the Publisher parameter specified by the string VariableName.

## C.3.4 Query Functions

* [idmquery(ClassName, Association, ReadAttrs)](bf1m36m.html#bf1m374)
* [idmgetqva(ParamName)](bf1m36m.html#bf1m375)

### idmquery(ClassName, Association, ReadAttrs)

Performs a query to the engine with the given ClassName, Association and ReadAttrs.

### idmgetqva(ParamName)

Retrieves a string value for the query result item, specified by ParamName, through standard output. If no values exist, Empty is returned. If the value is multi-valued, each value is separated by a newline character.

## C.3.5 Heartbeat Functions

* [heartbeat\_success(Message)](bf1m36m.html#bf1m377)
* [heartbeat\_error(Message)](bf1m36m.html#bf1m378)
* [heartbeat\_warning($Message)](bf1m36m.html#bf1m379)

### heartbeat\_success(Message)

Use these functions in the heartbeat.py script to indicate the status of the external application. Heartbeat documents are sent to the engine in following format:

```
  <status level="success" type="heartbeat">This is a heartbeat message</status>
```

### heartbeat\_error(Message)

Use these functions in the heartbeat.py script to indicate the status of the external application. Heartbeat documents are sent to the engine in following format:

```
  <status level="success" type="heartbeat">This is a heartbeat message</status>
```

### heartbeat\_warning($Message)

Use these functions in the heartbeat.py script to indicate the status of the external application. Heartbeat documents are sent to the engine in following format:

```
  <status level="success" type="heartbeat">This is a heartbeat message</status>
```
