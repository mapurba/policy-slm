# D.0 REST Endpoints

[Table D-1](the-jdbc-fan-out-rest-endpoints.html#b1i8cys6) lists the endpoints that the Fanout agent exposes for performing basic monitoring and management tasks.

*Table D-1* REST endpoints

| Path | Method | Parameter(s) | Description |
| /fanoutagent/config | PUT | {“KEY”:”VALUE”,…}  Key-value pair of the parameters received through the GET method call to this endpoint (refer (3)) | Used to set or update the parameter values for the Fanout agent.  Clients to this endpoint should provide the changed/modified value pairs only.  Password updates cannot be done through this endpoint. Due to the alternate handling of sensitive data, different endpoints are available for password updates. |
| /fanoutagent/config | GET | {}None | Provides the current configuration values of the Fanout agent. |
| /fanoutagent/config/setpassword | PUT | {“OLD\_SHIM\_PASSWD”:”...”,“NEW\_SHIM\_PASSWD”:”...”,“OLD\_AGENT\_PASSWD”:“”,“NEW\_AGENT\_PASSWD”:“”}All the values must be provided | Used to set the agent and the shim password on the Fanout agent.  *NOTE:*Both the password pairs must be provided. Otherwise, the agent might be locked down that can result in an error at startup. This is because one of the passwords is used for encrypting the other and hence the dependency.  There are no endpoints for fetching the password. |
| /fanoutagent/config/setkspassword | PUT | {“PASSWORD”:“...”} | Sets the keystore password for the command server.  The keystore contains a self-signed certificate created by the Fanout agent at the initial startup.  A user provided keystore with a certificate can also be used.  The certificate is used for securing the endpoint transport. An option exists to disable the SSL, which is not the recommended/default option. |
| /fanoutagent/service | GET | {}None | Retrieves the list of connected system services (shims) in the Fanout agent. Both running and stopped shims are reported in the response of this endpoint. |
| /fanoutagent/service/{state} | GET | {}NonePossible values for state are RUNNING or STOPPED | Provides the list of connected system services (shims) in the Fanout agent based on the service state.  *NOTE:*Legal values are RUNNING and STOPPED. |
| /fanoutagent/service/cmd/stop/{serviceId} | PUT | {}NoneServiceId returned by the GET service endpoint | Used to start a currently stopped service. |
| /fanoutagent/service/cmd/start/{serviceId} | PUT | {}NoneServiceId returned by the GET service endpoint | Used to start a currently stopped service. |
| /fanoutagent/shutdown | PUT | {}None | Used to shutdown a Fanout agent instance.  *NOTE:*When this endpoint is invoked, the agent instance will shutdown.  This means that all further communication with the agent will cease. Further communication will resume only after the agent is started by logging into the computer hosting the agent. |
| /config/setEncryptionkey |  |  |  |
