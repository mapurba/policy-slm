# C.2 Perl (IDMLib.pm) Reference

These scripts are written for the Linux and UNIX Perl interpreter. They are located in the scripts folder below the folder where the driver was installed (/opt/novell/usdrv/ by default).

Subscriber events are submitted to subscriber.pl, which then calls the script for the event. Modify the Perl script file corresponding to the event type: add.pl, modify.pl, modify-password.pl, delete.pl, move.pl, rename.pl. Queries of the external system should be handled in query.pl.

The Publisher calls poll.pl periodically. The frequency of the poll is determined by the Polling Interval driver parameter (60 seconds by default). Edit poll.pl to allow the driver to respond to events in the external account management system.

The Publisher calls heartbeat.pl periodically to determine whether the external account management system is responding correctly.

The built-in functions below are defined in IDMLib.pm.

## C.2.1 General Functions

* [idmgetvar($ParamName)](b8nqjm3.html#b8nqjm5)
* [idmtrace($Message)](b8nqjm3.html#b8nqjm6)
* [exec($Command)](b8nqjm3.html#b8nqjm7)
* [status($Level, $Message)](b8nqjm3.html#b8nqjm8)
* [status\_success($Message)](b8nqjm3.html#b8nqjm9)
* [status\_warning($Message)](b8nqjm3.html#b8nqjma)
* [status\_retry($Message)](b8nqjm3.html#b8nqjmb)
* [status\_error($Message)](b8nqjm3.html#b8nqjmc)
* [status\_fatal($Message)](b8nqjm3.html#b8nqjmd)

### idmgetvar($ParamName)

Returns the string value for the Driver parameter specified by the string ParamName.

### idmtrace($Message)

Appends the specified message to the user-defined trace file.

### exec($Command)

Executes an external program using the specified command line, and returns its numerical exit code on completion.

### status($Level, $Message)

Sends a status document with given level and message to return to the Identity Manager engine when the script completes.

The status document as seen by the engine looks like the following:

```
  <status level="success">This is a message</status>
```

### status\_success($Message)

Sends a status document with a success level and message to return to the Identity Manager engine when the script completes.

### status\_warning($Message)

Sends a status document with a warning level and message to return to the Identity Manager engine when the script completes.

### status\_retry($Message)

Sends a status document with a retry level and message to return to the Identity Manager engine when the script completes.

### status\_error($Message)

Sends a status document with a error level and message to return to the Identity Manager engine when the script completes.

### status\_fatal($Message)

Sends a status document with a fatal level and message to return to the Identity Manager engine when the script completes.

## C.2.2 Subscriber Functions

* [idmgetsubvar($ParamName)](b8nqjm3.html#b8nqjmf)
* [idmgetvar($Name)](b8nqjm3.html#b8nqjmg)
* [idmsetvar($Name, $Value)](b8nqjm3.html#b8nqjmh)

### idmgetsubvar($ParamName)

Returns the string value for the Subscriber parameter specified by the string ParamName.

### idmgetvar($Name)

Returns a string value for the item specified by Name through standard output. If no values exist, Empty is returned. If the value is multi-valued, each value is separated by a newline character.

### idmsetvar($Name, $Value)

Sets a single string value for the item specified by Name to be returned to the driver engine.

## C.2.3 Publisher Functions

* [idmgetpubvar($ParamName)](b8nqjm3.html#b8nqjmj)

### idmgetpubvar($ParamName)

Returns the string value for the Publisher parameter specified by the string ParamName.

## C.2.4 Query Functions

* [idmquery($ClassName, $Association, $ReadAttrs)](b8nqjm3.html#b8nqjml)
* [idmgetqva($ParamName)](b8nqjm3.html#b8nqjmm)

### idmquery($ClassName, $Association, $ReadAttrs)

Performs a query to the engine with the given ClassName, Association and ReadAttrs.

### idmgetqva($ParamName)

Retrieves a string value for the query result item, specified by ParamName, through standard output. If no values exist, Empty is returned. If the value is multi-valued, each value is separated by a newline character.

## C.2.5 Heartbeat Functions

* [heartbeat\_success($Message)](b8nqjm3.html#b8nqjmo)
* [heartbeat\_error($Message)](b8nqjm3.html#b8nqjmp)
* [heartbeat\_warning($Message)](b8nqjm3.html#b8nqjmq)

### heartbeat\_success($Message)

Use these functions in the heartbeat.sh script to indicate the status of the external application. Heartbeat documents are sent to the engine in following format:

```
  <status level="success" type="heartbeat">This is a heartbeat message</status>
```

### heartbeat\_error($Message)

Use these functions in the heartbeat.sh script to indicate the status of the external application. Heartbeat documents are sent to the engine in following format:

```
  <status level="success" type="heartbeat">This is a heartbeat message</status>
```

### heartbeat\_warning($Message)

Use these functions in the heartbeat.sh script to indicate the status of the external application. Heartbeat documents are sent to the engine in following format:

```
  <status level="success" type="heartbeat">This is a heartbeat message</status>
```
