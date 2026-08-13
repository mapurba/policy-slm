# 6.1 The Scriptable Framework

The driver provides a comprehensive scriptable framework that you can use to add to the built-in support for the security system, and to add support for other applications and security system fields that have been customized for a particular installation.

The driver’s scriptable framework includes components that simplify the job of extending the driver to support new applications and fields.

* Embedded Remote Loader

  + Full SSL support, and an installer to easily configure the certificates
  + Web access to debugging information from the embedded Remote Loader
* Encrypted change log that stores changes from the application to the Identity Vault if there is a communication problem
* Loopback detection system to prevent subscribed events from being published back to the Identity Vault
* z/OS name/token callable services helper programs that provide for securely passing large variables to and from the REXX execs
* Easily extendable connected system schema file to support any application
* Include/exclude file for simplified testing and deployment by the platform administrator
* Event support, both for applications that have exits or callouts, and for applications that must be polled for changes

The names of objects and attributes in the REXX execs are the names specified in the connected system schema file.

The following tables describe the major REXX execs.

*Table 6-1* Identity Vault Command Processing Execs

| REXX Exec | Identity Vault Event |
| IDMADDG | Add Group |
| IDMADDU | Add User |
| IDMDELG | Delete Group |
| IDMDELU | Delete User |
| IDMMODG | Modify Group |
| IDMMODU | Modify User |
| IDMMODPW | Password Change |
| IDMQUERY | Query |
| IDMCHOPW | Check Password |

*Table 6-2* Other Execs

| REXX Exec | Purpose |
| IDMSUB | Calls the appropriate command processing exec based on the type of event and object. This is executed for every Subscriber event. |
| IDMPOLL | Not used for ACF2. You can use this exec as needed to support your own applications if they do not generate events when changes are made. |
| IDMHRTBT | Heartbeat exec. |
| IDMGLBLS | Holds configurable options that all REXX execs can use during event processing. |
| IDMSTATS | Sends a status document to report the health of the application. |
| IDMTSOEX | Executes a TSO command and returns the command return code and command output. |
| SETPWDS | Sets the Remote Loader and Driver object passwords, which are used to authenticate and authorize the connection between the driver shim started task and the Metadirectory system. |
| SETCERT | Retrieves the certificate authority for the Metadirectory engine that uses SSL to communicate with the driver shim started task. |

## 6.1.1 Modifying a REXX Exec

Each of the REXX execs that come with the driver is designed with a common format, which makes it easy to read, edit, and maintain. Following are functional descriptions of the standard sections included in each exec:

* Retrieve subscriber shim variables, using IDMGETV sub.
* Retrieve event data variables, using IDMGETV event.
* Trace a useful message to be logged to the TSO print file.
* Provide comments instructing where to insert custom code before the TSO command is executed.
* Execute the TSO command stored in variable ACF2CMD, which performs the basic action.
* Provide comments instructing where to insert custom code after the TSO command has been executed.
* Return of status document, using the IDMSTATS function.

### Retrieving and Returning Information with IDMGETV and IDMSETV

The REXX execs use IDMGETV to obtain information about the event and about the properties configured on the ACF2 driver. The REXX execs use IDMSETV to return information to the driver shim or Metadirectory engine for processing. Both IDMGETV and IDMSETV are utilities, found in the distribution LOAD library, which transport information between REXX variables and memory storage. When information is retrieved using IDMGETV, the REXX variables will be created and populated and a special variable, VariableList, will also be created to contain a list of the available REXX variables from the shim.

To check for the existence of a REXX variable, set by IDMGETV, use:

```
  if wordpos("VariableName", VariableList) > 0; then do;
    /* REXX variable, VariableName exists and was created by IDMGETV */
  end;
```

Where VariableName is the name of the variable of interest. Event variables will contain the prefix ADD\_ or REMOVE\_ to indicate that this attribute has been added or removed from the object in question. For example, to check if the REVOKE field has been removed:

```
  if wordpos("REMOVE_REVOKED", VariableList) > 0; then do;
    /* User had REVOKED value removed */
  end;
```

For example, if the following XDS document is sent to the ACF2 driver shim:

```
  <modify class-name="User" event-id="12345">
    <association>IBMUSER</association>
    <modify-attr attr-name="NAME">
      <remove-value>
        <value>IBMUSER</value>
      </remove-value>
      <add-value>
        <value>THE IBMUSER</value>
      </add-value>
    </modify-attr>
  </modify>
```

The resulting REXX variables would look like:

```
  COMMAND=modify
  CLASS_NAME=User
  EVENT_ID=12345
  ASSOCIATION=IBMUSER
  REMOVE_NAME=IBMUSER
  ADD_NAME=THE IBMUSER
```

When attributes are mapped to REXX variables, all invalid REXX variable characters are converted into underscore (“\_”) characters. These include “-”, “@” and “...”.

### Multivalued (Stem) Variables

When attributes are multivalued, IDMGETV assigns a suffix to the variable name to index its values. The count of the number of values is represented by suffix.0 and the values are represented from .1 to .n, where n is the total count. For example, if the variable CLASSES was multivalued with values: CLS1, CLS2, CLS3, the following variables would be created:

```
  CLASSES.0=3
  CLASSES.1=CLS1
  CLASSES.2=CLS2
  CLASSES.3=CLS3
```

To iterate over each value, use a REXX do loop:

```
  do i = 1 to CLASSES.0
    class = CLASSES.i
  end;
```

### Returning Status Documents Using IDMSTATS

Identity Manager uses status documents, returned by the driver, to investigate whether an event was processed by the driver shim. Therefore, it’s important for the REXX execs to return a status document indicating whether the event was successful or resulted in an error. Use the supplied REXX exec, IDMSTATS, to return a status document:

```
  x = IDMSTATS("success", "Event was processed successfully", EVENT_ID);
```

The IDMSTATS script takes three parameters: level, message and event id. The level must be one of: success, error, warning, retry or fatal.

```
  <status level="success" event-id="12345">
    Event was processed successfully
  </status>
```

### Understanding the ACF2CMD Variable

Before an XDS command is sent to the driver shim, the Output Transformation policy converts the XDS document into a ACF2 TSO administrative command and stores the result in the attribute, ACF2CMD. This process avoids adding parsing logic inside the REXX execs to build the command, making the REXX execs cleaner, shorter, and easier to read. Therefore the default action of each REXX exec is to look for the ACF2CMD variable, which may be multivalued, and execute the command by default.

### Using IDMTRACE To Print Messages

IDMTRACE is another REXX exec, supplied by the driver distribution, that allows you to simply trace a message to the TSO print file (SYSTSPRT), allocated by the ACF2DRV JCL. It will only trace messages if ENABLE\_TRACE is set to true in IDMGLBLS. It will also print the date and time before the message for convenience.

```
  x = IDMTRACE("IDMADDU is running for user <"ADD_LID">.");
```

### Global Settings in member IDMGLBLS

The REXX exec IDMGLBLS is a simple script containing global settings that all scripts may use. It provides a common repository of variables you may change to alter the behavior of the other REXX execs. There are four variables of interest:

* SUBCOMMAND\_SEPARATOR: Defines the character to be recognized as a delimiter between lines of output received from TSO when executing commands that produce output. The default is the EBDIC newline character.
* MESSAGE\_PREFIX: Defines a string that precedes lines in the TSO print file (SYSTSPRT) in which a TSO command is about to be executed. The default is -->TSO:
* DISPLAY\_TSO\_OUTPUT: A boolean variable that controls whether TSO output received from a command should be displayed in the TSO print file (SYSTSPRT). The default is true.
* ENABLE\_TRACE: A boolean variable that controls whether IDMTRACE messages should be displayed. The default is true.

  *NOTE:*Enabling trace can be useful for troubleshooting and log collecting; however, disabling trace can reduce the amount of output that is saved in the SYSTSPRT file.

### Using IDMTSOEX To Execute A TSO Command

In REXX, a TSO command can be evaluated simply by entering the command on its own line:

```
  cmd = "ALU IBMUSER NAME(IBMUSER)IDMTRACE");
  cmd;
```

The IDMTSOEX exec, also supplied by the distribution, will provide a few other options:

```
  x = IDMSOEX(cmd);
```

* Log the command (password sanitized) using IDMTRACE
* Trap the output and return code from the command
* Return the code and output of the command to the caller

It's convenient to use this output to display a message back to the engine through a status document:

```
  response = IDMTSOEX("ALU IBMUSER NAME(IBMUSER)");

  /* first word is the return code */
  if word(cmd_response) > 0 then do;
    x = IDMSTATS("error", response, EVENT_ID);
  end;
  else do;
    x = IDMSTATS("success", response, EVENT_ID);
  end;
```

### Putting It All Together

The following code sample illustrates how the IMMADDU exec can be modified to additionally create an OMVS home directory:

```
  /* retrieve subscriber variables */
  "IDMGETV sub";

  /* retrieve event variables */
  "IDMGETV event";

  /* trace a message to SYSTSPRT */
  x = idmtrace("IDMADDU running for user <"ADD_LID">.");

  /*
     INSERT CUSTOM CODE HERE

     Add any custom code here that needs to be executed before
     creating the user in the ACF2 database.
  */

  /* Add the user to the ACF2 database using a TSO command */
  if wordpos("ADD_ACF2CMD.0", variablelist) <= 0; then do;
    /* we did not get a ACF2CMD from the event document */
    success = IDMSTATS("error", "No ACF2 command found", EVENT_ID);
    exit 0;
  end;

  do i = 1 to ADD_ACF2CMD.0
    tsocmd = ADD_ACF2CMD.i
    /* For an event, multiple TSO commands may be generated */
    cmd_response = IDMTSOEX(tsocmd);
    /* check the return code from our command */
    if word(cmd_response, 1) > 0 then do;
      /* an error occurred, report an error and exit from script */
      success = IDMSTATS("error", cmd_response, EVENT_ID);
      exit 0;
    end;
    else do;
      success = IDMSTATS("success", cmd_response, EVENT_ID);
    end;
  end;

  /*
  INSERT CUSTOM CODE HERE
  Add any custom code here that needs to be executed after
  creating the user in the ACF2 database.
  */

  /* check for the home directory attribute and create it */
  if wordpos("ADD_OMVSHOME", VariableList) > 0; then do
    makeDir = "oshell mkdir '"ADD_OMVS_HOME"'";
    response = IDMTSOEX(makeDir);
    if word(response, 1) > 0 then do;
      x = IDMSTATS("warning", response, EVENT_ID);
    end;
  end;

  /* All is successful, so we need to return an association
   for this user. */

  parse upper var ADD_LID ASSOCIATION;
  "IDMSETV MODIFY NAME(COMMAND) VALUE(ADD_ASSOCIATION)";
  "IDMSETV MODIFY NAME(ASSOCIATION) VALUE("ASSOCIATION")";
  "IDMSETV MODIFY NAME(EVENT_ID) VALUE("EVENT_ID")";

  if SRC_DN <> "SRC_DN"; then
    "IDMSETV MODIFY NAME(DEST_DN) VALUE("SRC_DN")";
  end;

  if SRC_ENTRY_ID <> "SRC_ENTRY_ID"; then
    "IDMSETV MODIFY NAME(DEST_ENTRY_ID) VALUE("SRC_ENTRY_ID")";
  end;

  /* Exit the script with return code 0 (no error) */
  exit 0;
```
