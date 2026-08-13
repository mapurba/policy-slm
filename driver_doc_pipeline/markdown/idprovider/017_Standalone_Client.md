# 5.2 Standalone Client

The standalone client is run as a Java process that calls the main function of the com.novell.ncs.idsrv.IDClient Java class.

%JRE\_HOME%\java -noverify -classpath %CLASSPATH% com.novell.idm.idprovider.IDClient <parameters>

To obtain the next available ID from an ID Policy objects in the Identity Vault, the client uses the following parameters to communicate with the driver:

| Parameter | Description | Sample |
| -h | RMI server host address. | -h localhost |
| -p | RMI server port. | -p 1099 |
| -o | ID Policy object name to retrieve an ID from. | -o uniqueCN |
| -c | ID Client name to identify this client at the RMI server. | -c Client-No1 |
| -t | Trace level.  You use the trace level setting to see specific trace information in the DirXML ID Servers main screen.  The trace level is a bit mask and can be combined.  Trace values and levels:   * 0 = off * 1 = low * 2 = medium * 3 = high * 4 = exceptions | -t 1 |
| -m | Remote RMI server command to be executed at the RMI server console | -m reinitialize |

```
%JRE_HOME%\java -noverify -classpath %CLASSPATH% com.novell.idm.idprovider.IDClient -h localhost -p 1099 -o Policy -t 1 -c Client -l 1
```
