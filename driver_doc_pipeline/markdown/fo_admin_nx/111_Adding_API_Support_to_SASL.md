# 17.3 Adding API Support to SASL

SASL, the Simple Authentication and Security Layer, is a generic authentication protocol. Many connection-based protocols, such as SMTP, LDAP, IMAP, and POP3, support SASL. New authentication mechanisms that support SASL are automatically supported by those protocols. Furthermore, protocols that use SASL for authentication support Kerberos\* authentication through the Generic Security Services Application Programming Interface (GSSAPI).

A common open-source SASL library is Cyrus SASL, which is available at ftp://ftp.andrew.cmu.edu/pub/cyrus-mail.

Directions for modifying Cyrus SASL to use the AS Client API for authentication can be found in the ASAM/bin/PlatformServices/PlatformClient/sasl directory created by the Platform Services installation process.
