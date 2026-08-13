# 8.5 Driver Security Certificates

SSL uses security certificates to control, encrypt, and authenticate communications.

Ensure that the security certificate directory /usr/local/nxdrv/keys is appropriately protected. The installation program sets secure file permissions for this directory.

The Driver Shim and the Identity Manager engine communicate through SSL using a certificate created in the Identity Vault and retrieved by the driver shim during the installation process. For more information on this certificate and how to renew or install third-party certificates, refer to the Identity Manager Administration Guide.

The Embedded Remote Loader web interface uses a dynamically generated, self-signed certificate for SSL communication. The details of this certificate are as follows:

*Table 8-1* Security Certificate Details (Embedded Remote Loader)

| Property Name | Values / Parameters |
| Subject | SSL Server |
| Issuer | SSL Server |
| Validity | 1 year |
| Serial Number | 0 |
| Key | 1024-bit RSA |

Renewal of this certificate automatically occurs every time the driver shim is restarted on the connected platform.

If you have configured your Driver Shim to provide remote NIS or NIS+ clients with password publishing, a certificate is generated during installation for SSL authorization and communication. This certificate is a self-signed certificate authority with the following certificate properties:

*Table 8-2* Security Certificate Details (Driver Shim)

| Property Name | Values / Parameters |
| Subject | soap api certificate authority |
| Issuer | soap api certificate authority |
| Validity | 10 year |
| Serial Number | 0 |
| Key | 4096-bit RSA |

These properties can be configured and renewed at any time. For information on how to configure these properties, refer to [The Remote Publisher Configuration File](b4dwo69.html).

When remote NIS or NIS+ clients are configured to publish passwords, they retrieve a certificate from the Driver Shim and use this for SSL communication and client authorization. The client certificates contain the following certificate properties:

*Table 8-3* Security Certificate Details (NIS or NIS+ clients)

| Property Name | Values / Parameters |
| Subject | soap api client |
| Issuer | soap api certificate authority |
| Validity | 2 year |
| Serial Number | [starts at 1000] |
| Key | 2048-bit RSA |

For more information on how to configure these certificate properties, refer to [The Remote Publisher Configuration File](b4dwo69.html).
