# 6.1 Creating a Keystore and a Truststore

1. Create a certificate for the broker by using the keytool.

   keytool -genkey -alias broker -keyalg RSA -keystore broker.ks
2. Export the broker's certificate to share with clients.

   keytool -export -alias broker -keystore broker.ks -file broker\_cert
3. Create a certificate/keystore for the client.

   keytool -genkey -alias client -keyalg RSA -keystore client.ks
4. Create a truststore for the client and import the broker's certificate. This establishes that the client "trusts" the broker.

   keytool -import -alias broker -keystore client.ts -file broker\_cert
5. Export the client's certificate so it can be shared with broker:

   keytool -export -alias client -keystore client.ks -file client\_cert
6. Create a truststore for the broker, and import the client's certificate. This establishes that the broker "trusts" the client:

   keytool -import -alias client -keystore broker.ts -file client\_cert

*NOTE:*You must use the same passwords that were used for creating the keystores to configure the Fanout components for SSL. For more information about creating certificates, see [Setting up the Key and Trust Stores](http://activemq.apache.org/how-do-i-use-ssl.html).
