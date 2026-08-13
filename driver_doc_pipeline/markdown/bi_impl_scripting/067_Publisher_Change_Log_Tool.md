# D.3 Publisher Change Log Tool

The publisher channel might submit events to be published, using the change log tool usclh (on UNIX) or idmevent.exe (on Windows). These tools will create an event, which will be picked up by the driver shim on a polling interval and published to the Identity Manager engine, where it can be processed by Policy. The change log tool can be invoked at anytime on the application system. One commonly-used technique is to call the changelog tool from the polling script, which is executed on the polling interval as well. In such a scenario, the polling script can determine what changed and submit the changes to the change log to be processed immediately after the polling script terminates. However, if you wish to invoke the change log tool from another mechanism, events will be queued in the changelog and published on intervals when necessary.

The syntax for the change log tool on UNIX, usclh, is as follows:

```
usclh -t <type>
        [-c class]
        [-e event-id]
        [-a association]
        [-s src-dn]
        [-o old-src-dn]
        [-p password]
        [-w old-password]
        [-n new-name]
        [-r]
        [-y old-association]
        [-z new-association]
        [-l status-level]
        [-m status-message]
        [-1 | -2]
        [-?]
```

Where each option is described in the following table:

*Table D-3* Options

| Name | Description |
| type | The command type, which could be one of the following: add, delete, modify, modify-password, rename, modify-association, status, xds. When using the xds type, a raw XML document can be passed to the tool to be published as is. |
| event-id | The event-id of the document to be published. Typically, this is a timestamp or a counter. If none is specified, a default timestamp will be used. |
| association | The association string value for which the event being published describes. |
| src-dn | The source distinguished name of the object being published, if this object resides in a hierarchical directory structure. |
| old-src-dn | If the published event is a move or rename, the old-src-dn specifies the old distinguished name before the move or rename event. |
| password | The new password of the object being published. This is only valid for add or modify-password events. |
| old-password | The old password of the object being published. This is only valid for modify-password events. |
| new-name | The new name of an object being published during a rename event. |
| -r | If specified, instructs the event to remove the old name during a rename event. |
| old-association | Specifies the name of the old association value, during a modify-association event. |
| new-association | Specifies the name of the new association value, during a modify-association event. |
| status-level | Specifies the status level for a status message. Valid levels are: success, error, warning, retry, fatal. |
| status-message | Specifies the text messages that should be included for a status document. |
| -1 | Specifies that the event should be put on hold (do not publish), until a release is issued. |
| -2 | Specifies that all events on hold should be released (publishable). |
| -? | This help menu. |

When invoked, the changelog utility waits for input on standard input until an EOF (end of file) character is received. If entered on the command-line, you can terminate it with the Ctl-d meta character. Additional name/value pairs can then be passed to this tool to supply additional event information such as attribute values being added or removed.

When invoked from a script, you can use a “here-is” document format to pass standard input to the changelog tool. When passing input to a command-line utility through standard input, you have the advantage that the information is protected from the environment, adding security to your publisher. When using command-line arguments, these options will appear in cleartext to the outside environment with tools such as “ps”.

Examples from a script:

```
usclh -t add -c User -a bob <<EOF
ADD_CN=bob
ADD_Login Disabled=true
EOF

usclh -t modify -c User -a bob <<EOF
ADD_CN=bob
ADD_Login Disabled=true
EOF

usclh -t modify-password -c User -a bob <<EOF
OLD_PASSWORD=secret
PASSWORD=newsecret
EOF

usclh -t rename -c User -a bob -n bob2 -r <<EOF

EOF
```

Examples from a command line:

```
usclh -t add -c User -a bob
ADD_CN=bob
ADD_Login Disabled=true
^d

usclh -t delete -c User -a bob
^d

usclh -t modify-password -c User -a bob -w secret -p newsecret
^d

# ./usclh -t xds
<nds dtdversion="1.1" ndsversion="8.6">
<input>
<modify class-name="User" event-id="12345">
  <association>bob</association>
  <modify-attr attr-name="MyAttr">
    <remove-all-values/>
    <add-value>
      <value>some new value</value>
    </add-value>
  </modify-attr>
</modify>
</input>
</nds>
^d
```
