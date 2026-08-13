# B.3 LAM Configuration Notes

IBM芒聙聶s proprietary Loadable Authentication Module (LAM) interface is an alternative to PAM on AIX systems. In fact, the Identity Manager Fan-Out Driver fully supports PAM only on AIX 5.3 and later.

If you use LAM with the Fan-Out Driver, be sure to include the following considerations in your configuration.

* [Locating the LAM Module](brk5h3s.html#brk6g17)
* [Enabling the LAM Module](brk5h3s.html#brk6gmr)
* [Associating Users With the LAM Module](brk5h3s.html#brk6hcs)
* [Other LAM Configuration Considerations](brk5h3s.html#brk6umy)

## B.3.1 Locating the LAM Module

The Fan-Out Driver芒聙聶s LAM module is named DCE and located here on your AIX system:

```
  /usr/lib/security/DCE
```

*NOTE:*IBM also has a deprecated LAM module named DCE, which is their implementation of the Distributed Computing Environment. IBM芒聙聶s DCE LAM module is unrelated to the Fan-Out Driver芒聙聶s DCE LAM module.

## B.3.2 Enabling the LAM Module

To enable the DCE LAM module as an available authentication mechanism, you must add it to the methods.cfg configuration file located here on your AIX system:

```
  /usr/lib/security/methods.cfg
```

A sample methods.cfg file is included in /usr/local/ASAM/bin/PlatformServices.

## B.3.3 Associating Users With the LAM Module

The DCE LAM module can be made the default authentication method for all users, or it can be associated with particular users, via the user file located here on your AIX system:

```
  /etc/security/user
```

Two sample user files are included in /usr/local/ASAM/bin/PlatformServices:

* user.sample shows how to make DCE the default authentication mechanism.
* user.sample2 shows how to make DCE the default authentication mechanism with fail-over to local authentication if DCE authentication is unavailable.

Alternatively, the DCE LAM module can be explicitly associated with Fan-Out Driver managed users by adding the SYSTEM and registry attributes to the mkuser command in the Fan-Out Driver芒聙聶s adduser.sh script as follows:

```
  COMMAND="/usr/bin/mkuser -R files SYSTEM=\"DCE\" registry=DCE "
```

## B.3.4 Other LAM Configuration Considerations

### AIX 5.3 and later

To enable LAM on AIX 5.3 and later, you also need to modify the login.cfg file located here on your AIX system:

```
  /etc/security/login.cfg
```

In this file, make sure that auth\_type is set to STD\_AUTH.

### Using SSH

Finally, to use ssh with the DCE LAM module, you will need to check your sshd\_config file located here on your AIX system:

```
  /etc/ssh/sshd_config
```

In this file, it is important for PasswordAuthentication to have the default setting of yes .
