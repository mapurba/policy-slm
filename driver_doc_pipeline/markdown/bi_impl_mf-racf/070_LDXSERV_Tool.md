# C.3 LDXSERV Tool

LDXSERV is a TSO command tool that serves several functions. For the driver shim, it allows the started task to set a loopback token in its address space memory in order to prevent the Exit routines from logging its activity to the change log. From the user's perspective, LDXSERV can be used as a verification tool to investigate whether the Exits are in place correctly. It can also be used to query information from the change log queue and even modify the queue, if necessary.

The syntax for LDXSERV is as follows:

```
  LDXSERV < STATUS | GETNEXT | [MARKDONE <EVENT(event-id)>] >
```

## C.3.1 STATUS

The STATUS operand reports back to the user an XML document describing the installed Event Subsystem. It provides several pieces of information, including the build date and version of each component, the state of each Exit, the number of events queued through each Exit, and the size and location of the log file.

```
  ldxserv status
  <ldx>
    <source>
      <product build="20210103" instance="ldxserv" version="4.83">
        Novell IDM RACF Driver Version 4.8.3.0
      </product>
      <contact>NetIQ Corporation</contact>
    </source>
    <output>
      <status level="success">
        <exit name="LDXRIX02" state="enabled" version="4.83" build-date="20210103"
          times-called="584" events-queued="2" info="ok"/>
        <exit name="LDXEVX01" state="enabled" version="4.83" build-date="20210103"
          times-called="20" events-queued="7" info="ok"/>
        <queue version="4.83" state="active" created-by="LDXRIX02" entries="0"/>
        <logger version="4.83" state="active" taskid="LDXLOGRP"
          logfilename="LDX.LOGFILE"/>
        <logfile name="LDX.LOGFILE" state="0% used"/>
      </status>
    </output>
  </ldx>
```

## C.3.2 GETNEXT

The GETNEXT operand reports back to the user an XML document describing the first event in the change log queue. Inside the XML document, you may view the type of event and details about the event, including the user that issued the event, the date and time of the event.

```
  ldxserv getnext
  <ldx>
    <source>
      <product build="20210103" instance="ldxserv" version="4.83">
        Novell IDM RACF Driver Version 4.8.3.0
      </product>
      <contact>NetIQ Corporation</contact>
    </source>
    <output>
      <modify-password date="2021-01-15" time=" 7:18" event-id="7006">
        <association>USER\JAVIER</association>
        <password>********</password>
      </modify-password>
      <status level="success">
        <description>ok</description>
      </status>
    </output>
  </ldx>
```

## C.3.3 MARKDONE

The MARKDONE operand instructs LDXSERV to remove the event in the queue, described by the EVENTID operand. The event-id must match the event-id found by the GETNEXT command. When complete, it reports back an XML document describing the success or error of the instruction.

```
  ldxserv markdone event(7006)
  <ldx>
    <source>
      <product build="20210103" instance="ldxserv" version="4.83">
        Novell IDM RACF Driver Version 4.8.3.0
      </product>
      <contact>NetIQ Corporation</contact>
    </source>
    <output>
      <status level="success">
        <description>ok</description>
      </status>
    </output>
  </ldx>
```
