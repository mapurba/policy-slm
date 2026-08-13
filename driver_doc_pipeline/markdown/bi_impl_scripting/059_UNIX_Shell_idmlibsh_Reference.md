# C.1 UNIX Shell (idmlib.sh) Reference

The scripts are written for the Linux and UNIX Bourne Shell. They are located in the scripts folder below the folder where the driver was installed (/opt/novell/usdrv/ by default).

Subscriber events are submitted to subscriber.sh, which then calls the script for the event. Modify the shell script file corresponding to the event type: add.sh, modify.sh, modify-password.sh, delete.sh, move.sh, rename.sh. Queries of the external system should be handled in query.sh.

The Publisher calls poll.sh periodically. The frequency of the poll is determined by the Polling Interval driver parameter (60 seconds by default). Edit poll.sh to allow the driver to respond to events in the external account management system.

The Publisher calls heartbeat.sh periodically to determine whether the external account management system is responding correctly.

The built-in functions below are defined in idmlib.sh.

## C.1.1 General Functions

* [IDMGETDRVVAR ParamName](b8npkdf.html#b8nqasb)
* [TRACE Message](b8npkdf.html#b8nqb43)
* [EXEC Command](b8npkdf.html#b8nqcay)
* [STATUS Level Message](b8npkdf.html#b8nqcaz)
* [STATUS\_SUCCESS Message](b8npkdf.html#b8nqe4l)
* [STATUS\_WARNING Message](b8npkdf.html#b8nqe8u)
* [STATUS\_RETRY Message](b8npkdf.html#b8nqetl)
* [STATUS\_ERROR Message](b8npkdf.html#b8nqfbm)
* [STATUS\_FATAL Message](b8npkdf.html#b8nqfbn)

### IDMGETDRVVAR ParamName

Returns the string value for the Driver parameter specified by the string ParamName.

### TRACE Message

Appends the specified message to the user-defined trace file.

### EXEC Command

Executes an external program using the specified command line, and returns its numerical exit code on completion.

### STATUS Level Message

Sends a status document with given level and message to return to the Identity Manager engine when the script completes.

The status document as seen by the engine looks like the following:

```
  <status level="success">This is a message</status>
```

### STATUS\_SUCCESS Message

Sends a status document with a success level and message to return to the Identity Manager engine when the script completes.

### STATUS\_WARNING Message

Sends a status document with a warning level and message to return to the Identity Manager engine when the script completes.

### STATUS\_RETRY Message

Sends a status document with a retry level and message to return to the Identity Manager engine when the script completes.

### STATUS\_ERROR Message

Sends a status document with a error level and message to return to the Identity Manager engine when the script completes.

### STATUS\_FATAL Message

Sends a status document with a fatal level and message to return to the Identity Manager engine when the script completes.

## C.1.2 Subscriber Functions

* [IDMGETSUBVAR ParamName](b8npkdf.html#b8nqg82)
* [IDMGETVAR Name](b8npkdf.html#b8nqg83)
* [IDMSETVAR Name Value](b8npkdf.html#b8nqg84)

### IDMGETSUBVAR ParamName

Returns the string value for the Subscriber parameter specified by the string ParamName.

### IDMGETVAR Name

Returns a string value for the item specified by Name through standard output. If no values exist, Empty is returned. If the value is multi-valued, each value will be separated by a newline character.

### IDMSETVAR Name Value

Sets a single string value for the item specified by Name to be returned to the driver engine.

## C.1.3 Publisher Functions

Only one function exists in this category.

### IDMGETPUBVAR ParamName

Returns the string value for the Publisher parameter specified by the string ParamName.

## C.1.4 Query Functions

* [IDMQUERY ClassName Association ReadAttrs](b8npkdf.html#b8nqhha)
* [IDMGETQVAR ParamName](b8npkdf.html#b8nqhhb)

### IDMQUERY ClassName Association ReadAttrs

Performs a query to the engine with the given ClassName, Association and ReadAttrs

### IDMGETQVAR ParamName

Retrieves a string value for the query result item, specified by ParamName, through standard output. If no values exist, Empty is returned. If the value is multi-valued, each value is separated by a newline character.

## C.1.5 Heartbeat Functions

* [HEARTBEAT\_SUCCESS Message](b8npkdf.html#b8nqist)
* [HEARTBEAT\_ERROR Message](b8npkdf.html#b8nqisu)
* [HEARTBEAT\_WARNING Message](b8npkdf.html#b8nqisv)

### HEARTBEAT\_SUCCESS Message

Use these functions in the heartbeat.sh script to indicate the status of the external application. Heartbeat documents are sent to the engine in following format:

```
  <status level="success" type="heartbeat">This is a heartbeat message</status>
```

### HEARTBEAT\_ERROR Message

Use these functions in the heartbeat.sh script to indicate the status of the external application. Heartbeat documents are sent to the engine in following format:

```
  <status level="success" type="heartbeat">This is a heartbeat message</status>
```

### HEARTBEAT\_WARNING Message

Use these functions in the heartbeat.sh script to indicate the status of the external application. Heartbeat documents are sent to the engine in following format:

```
  <status level="success" type="heartbeat">This is a heartbeat message</status>
```
