# 5.1 ID Client

The ID client can be used inside of DirXML style sheets calling the getNextID function of the com.novell.ncs.idsrv.IDClient Java class.

xmlns:id=http://www.novell.com/nxsl/java/com.novell.idm.idprovider.IDClient

To obtain the next available ID from an ID Policy object in the Identity Vault, the ID client uses the following parameters to communicate with the ID Provider driver:

| Parameter | Description | Sample |
| $RMIServer | RMI server host address. | localhost |
| $RMIPort | RMI server port. | 1099 |
| $UIDRule | ID Policy object name to retrieve an ID from. | uniqueCN |
| $IDClient | ID Client name to identify this client at the RMI server. | Client-No2 |
| $Tracelevel | Trace level.  You use the trace level setting to see specific trace information in the DirXML ID Servers main screen.  The trace level is a bit mask and can be combined.  Trace values and levels:   * 0 = off * 1 = low * 2 = medium * 3 = high * 4 = exceptions | 1 |

To generate the IDs by the XPATH expression, use the following command:

```
id: getNextID('IP_OF_RMI_SERVER','PORT','POLICY_NAME','CLIENT_NAME',TRACE_LEVEL
```

The XPATH expression will look like this:

```
<arg-string>
    <token-xpath expression="id:getNextID('172.17.1.3','1199','MYUID','DBUSERS',0)"/>
</arg-string>
```
