# 10.1 How to confirm successful establishment of JWT connection?

The successful JWT connection with all required parameters can now be confirmed from the log in level 3, as shown below:

```
Workday Ent PT:Workday Ent: Creating new OAuth Connection...
Workday Ent PT:Workday Ent: Extracting private key from the keystore file...
Workday Ent PT:Workday Ent: JWT Bearer Token initialized with
OAuth2 Client Id: ZmE1NjNhOGYtZWY1Mi00Yzg2LTlmZmUtOGJjOTAyNjhjYjEy
Workday Integration Username: idmuser2
Public-Private-Key Keystore File: /home/JWTkeystore.jks
Workday Ent PT:Workday Ent: Sending Request to Workday...
Workday Ent PT:
<soapenv:Envelope xmlns:bsvc="urn:com.workday/bsvc" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Body>
    <bsvc:Server_Timestamp_Get bsvc:version="v32.0"/>
  </soapenv:Body>
</soapenv:Envelope>
Workday Ent PT:Workday Ent: Generating signed JWT...
Workday Ent PT:Workday Ent: Requesting new access token...
Workday Ent PT:Workday Ent: Fetching Page 1 of 1 Pages.
Workday Ent PT:Workday Ent: Received Response from Workday with response code: 200
```
