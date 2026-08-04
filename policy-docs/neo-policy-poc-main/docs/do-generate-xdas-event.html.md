DirXMLScript DTD: do-generate-xdas-event element



# do-generate-xdas-event

The **<do-generate-xdas-event>** action causes
an Identity Manager xdas event to be sent to
NetIQ Audit service. Identity Manager XDAS events are
definend in the Attributes table below.Valid event levels are
definend in the following table. The remaining event data fields
are provided by [<arg-string>](arg-string.html)
elements with name attributes.

> | Level | Description |
> | --- | --- |
> | log-emergency | Events that cause the Identity Manager metadirectory engine or driver to shutdown. |
> | log-alert | Events that require immediate attention. |
> | log-critical | Events that can cause parts of the Identity Manager metadirectory engine or driver to malfunction. |
> | log-error | Events describing errors which can be handled by the Identity Manager metadirectory engine or driver. |
> | log-warning | Negative events not representing a problem. |
> | log-notice | Events (positive or negative) an administrator can use to understand or improve use and operation. |
> | log-info | Positive events of any importance. |
> | log-debug | Events of relevance for support or engineers to debug operation of the Identity Manager metadirectory engine or driver. |

> | Tag | Description |
> | --- | --- |
> | Observer.Account.Domain | Text entered here will be stored in *Observer.Account.Domain* field in the XDAS event. |
> | Observer.Account.Name | Text entered here will be stored in *Observer.Account.Name* field in the XDAS event. |
> | Observer.Account.Id | Text entered here will be stored in *Observer.Account.Id* field in the XDAS event. |
> | Observer.Entity.SysAddr | Text entered here will be stored in *Observer.Entity.SysAddr* field in the XDAS event. |
> | Observer.Entity.SysName | Text entered here will be stored in *Observer.Entity.SysName* field in the XDAS event. |
> | Observer.Entity.SvcName | Text entered here will be stored in *Observer.Entity.SvcName* field in the XDAS event. |
> | Observer.Entity.SvcComp | Text entered here will be stored in *Observer.Entity.SvcComp* field in the XDAS event. |
> | Initiator.Account.Domain | Text entered here will be stored in *Initiator.Account.Domain* field in the XDAS event. |
> | Initiator.Account.Name | Text entered here will be stored in *Initiator.Account.Name* field in the XDAS event. |
> | Initiator.Account.Id | Text entered here will be stored in *Initiator.Account.Id* field in the XDAS event. |
> | Initiator.Entity.SysAddr | Text entered here will be stored in *Initiator.Entity.SysAddr* field in the XDAS event. |
> | Initiator.Entity.SysName | Text entered here will be stored in *Initiator.Entity.SysName* field in the XDAS event. |
> | Initiator.Entity.SvcName | Text entered here will be stored in *Initiator.Entity.SvcName* field in the XDAS event. |
> | Initiator.Entity.SvcComp | Text entered here will be stored in *Initiator.Entity.SvcComp* field in the XDAS event. |
> | Initiator.Assertions | Text entered here will be stored in *Initiator.Assertions* field in the XDAS event. |
> | Target.Account.Domain | Text entered here will be stored in *Target.Account.Domain* field in the XDAS event. |
> | Target.Account.Name | Text entered here will be stored in *Target.Account.Name* field in the XDAS event. |
> | Target.Account.Id | Text entered here will be stored in *Target.Account.Id* field in the XDAS event. |
> | Target.Entity.SysAddr | Text entered here will be stored in *Target.Entity.SysAddr* field in the XDAS event. |
> | Target.Entity.SysName | Text entered here will be stored in *Target.Entity.SysName* field in the XDAS event. |
> | Target.Entity.SvcName | Text entered here will be stored in *Target.Entity.SvcName* field in the XDAS event. |
> | Target.Entity.SvcComp | Text entered here will be stored in *Target.Entity.SvcComp* field in the XDAS event. |
> | Target.Data | Text entered here will be stored in *Target.Data* field in the XDAS event. |
> | Action.Event.CorrelationID | Text entered here will be stored in *Action.Event.CorrelationID* field in the XDAS event. |
> | Action.Event.Subevent | Text entered here will be stored in *Action.Event.Subevent* field in the XDAS event. |
> | Action.Time.Offset | Text entered here will be stored in *Action.Time.Offset* field in the XDAS event. |

### Example

> ```
>
> <do-generate-xdas-event name="Create Data Item" level="log-info">
>   <arg-string name="Observer.Entity.SysAddr">
>     <token-text>127.0.0.2</token-text>
>   </arg-string>
>   <arg-string name="Observer.Entity.SysName">
>     <token-text>Sri-SLES11.test.net</token-text>
>   </arg-string>
>   <arg-string name="Initiator.Entity.SvcName">
>     <token-text>CN=Sri-SLES11,O=novell</token-text>
>   </arg-string>
>   <arg-string name="Initiator.Entity.SvcComp">
>     <token-text>\\dxevent</token-text>
>   </arg-string>
>   <arg-string name="Target.Data">
>     <token-text>CgAAAAAAAAABAAAAGgAAAHEAdwBlAHIAdAAuAG4AbwB2AGUAbABsAAAAAAAAAAAAMwAAACIAAAAjAAAAJgAAACcAAAABAAAAAgAAAAMAAAAEAAAABQAAAAYAAAAHAAAACAAAAAkAAAAKAAAACwAAAAwAAAANAAAADgAAAA8AAAAQAAAAEQAAABIAAAATAAAAKQAAACoAAAAvAAAAKwAAACwAAAAoAAAALQAAAC4AAAAUAAAAFQAAABYAAAAXAAAAGAAAABkAAAAaAAAAGwAAABwAAAAdAAAAHgAAAB8AAAAgAAAAIQAAACQAAAAlAAAAMAAAADEAAAAyAAAARgAAAAA=</token-text>
>   </arg-string>
>   <arg-string name="Target.Entity.SvcName">
>     <token-text>CN=qwert,O=novell</token-text>
>   </arg-string>
>   <arg-string name="Target.Entity.SvcComp">
>     <token-text>DirXML-LogEvents</token-text>
>   </arg-string>
>   <arg-string name="Action.Event.Subevent">
>     <token-text>307D0</token-text>
>   </arg-string>
>   <arg-string name="Action.Time.Offset">
>     <token-text>1291895458</token-text>
>   </arg-string>
> </do-generate-event>
>
> ```

<details>
<summary><strong>Click to expand allowed content</strong></summary>

## 1. Allowed Content

> [**arg-string**](arg-string.html)
> :   string argument
>
> ---

## 2. Attributes

> | Attribute | Value(s) | Default Value |
> | --- | --- | --- |
> | **disabled** | true   |  false   *true* if this element is disabled | false |
> | **level** | log-emergency   |  log-alert   |  log-critical   |  log-error   |  log-warning   |  log-notice   |  log-info   |  log-debug   NetIQ Audit log level | log-info |
> | **name** | **CDATA**   Create Account | Delete Account | Disable Account | Enable Account | Query Account | Modify Account | Modify Security Token | Create Session | Terminate Session | Query Session | Modify Session | Create Data Item | Delete Data Item | Query Data Item Attribute | Modify Data Item Attribute | Install Service | Remove Service | Query Service Config | Modify Service Config | Disable Service | Enable Service | Invoke Service | Terminate Service | Query Process Context | Modify Process Context | Create Peer Association | Terminate Peer Association | Query Association Context | Modify Association Context | Receive Data Via Association | Send Data Via Association | Create Data Item Association | Terminate Data Item Association | Query Data Item Association | Modify Data Item Association | Query Data Item Content | Modify Data Item Content | Request Workflow Approval | Receive Workflow Approval | Escalate Workflow Approval | Send Workflow Notification | Create Role | Delete Role | Disable Role | Enable Role | Query Role | Modify Role | Start System | Shutdown System | Resource Exhaustion | Resource Corruption | Backup Datastore | Restore Datastore | Configure Audit Service | Audit Datastore Full | Audit Datastore Corrupt | Authentication Session | Unauthentication Session | Federate Identity | Unfederate Identity | Create Access Token | Destroy Access Token    XDAS Event Name | #REQUIRED |
> | **notrace** | true   |  false   *true*if this element should not be traced during execution of policy | false |
>
> ---

## 3. Content Rule

> ( [arg-string](arg-string.html) \* ) 
>
> ---


<details>
<summary>## 4. <strong>Parent Elements</strong></summary>

## 4. <strong>Parent Elements</strong>

> [**actions**](actions.html)
> :   actions that are performed by a <rule>
>
> [**arg-actions**](arg-actions.html)
> :   actions argument

---

[**Top Elements**](TOP-ELEM.html) ||
[**All Elements**](ALL-ELEM.html)
|| [**Tree**](DTD-TREE.html#do-generate-xdas-event)

---

[DirXMLScript DTD](index.html)

</details>


</details>
