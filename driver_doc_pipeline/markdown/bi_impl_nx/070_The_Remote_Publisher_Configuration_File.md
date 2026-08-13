# C.2 The Remote Publisher Configuration File

The /usr/local/nxdrv/conf/remote-publisher.conf file on the connected Linux or UNIX system controls the issuing of security certificates to remote publishing clients. It is used when a remote client is configured.

Enter configuration statements, one per line.

## C.2.1 Comments

Lines that begin with an octothorpe (#) are comments.

#### Example

```
# This is a comment line.
```

## C.2.2 CA-DELAY Statement

The CA-DELAY statement specifies the number of days that the Certificate Authority remains valid.

#### Syntax

```
CA-DELAY=days
```

#### Example

```
CA-DELAY=3650
```

## C.2.3 CLIENT-DELAY Statement

The CLIENT-DELAY statement specifies the number of days that the client certificate remains valid.

#### Syntax

```
CLIENT-DELAY=days
```

#### Example

```
CLIENT-DELAY=1025
```

## C.2.4 VERIFY-SERIAL-NUMBERS Statement

The VERIFY-SERIAL-NUMBERS statement specifies whether the driver shim verifies that the certificate serial number of a connecting client matches the serial number specified for it in a CLIENT statement.

#### Syntax

```
VERIFY-SERIAL-NUMBERS={true|false}
```

#### Example

```
VERIFY-SERIAL-NUMBERS=true
```

## C.2.5 NEXT-SERIAL-NUMBER Statement

The NEXT-SERIAL-NUMBER statement specifies the next unused client certificate serial number.

#### Syntax

```
NEXT-SERIAL-NUMBER=number
```

#### Example

```
NEXT-SERIAL-NUMBER=1000
```

## C.2.6 CLIENT Statements

CLIENT statements are written by the driver shim when a remote client is configured, and are used by the driver shim to verify a client when it connects to publish a password.

#### Syntax

```
CLIENT ADDRESS=address1,address2, . . . SERIAL=serialNumber
```

#### Example

```
CLIENT ADDRESS=192.168.17.41,192.168.17.42,192.168.17.46 SERIAL=1952
```
