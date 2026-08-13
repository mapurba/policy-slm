# D.1 Message Format

Each message written by the driver begins with a message identifier. The text of the message follows the message identifier. A diagnostic code, meaningful to the NetIQ product support team, follows the message text.

Example message:

```
OBJ010I Trawl complete. aas1625
```

In this example, the message identifier is OBJ010I. The message text is Trawl complete. The diagnostic code is aas1625.

The last character of the message identifier represents one of the following possible severity codes:

*Table D-1* Message Severity Codes

| D | Debugging |
| I | Informational |
| W | Warning |
| E | Error |

Each message identifier begins with a code of 3-5 characters associated with the driver component that generated the message. Message explanations in this reference are grouped according to these codes so you can find them quickly.

* [AGT Messages](bsqu70u.html)

  Messages beginning with AGT are issued by the Core Driver for Authentication Services.
* [AUDA Messages](bshp1so.html)

  Messages beginning with AUDA are issued by Audit Services for Authentication Services.
* [AUDG Messages](bshp1st.html)

  Messages beginning with AUDG are issued by Audit Services for general components.
* [AUDR Messages](bshp1t3.html)

  Messages beginning with AUDR are issued by Audit Services to report actions taken during Receiver script processing.
* [AXML Messages](bshp1tb.html)

  Messages beginning with AXML are issued by the Core Driver during interactions with the Identity Manager engine.
* [CFG Messages](bshp1tj.html)

  Messages beginning with CFG are issued by Platform Configuration file processing.
* [CFGA Messages](bshp1tk.html)

  Messages beginning with CFGA are issued during installation when migrating values from the asamcore.conf file to Driver object configuration parameters.
* [CFGP Messages](bshp1tl.html)

  Messages beginning with CFGP are issued by platform configuration file processing.
* [CRT Messages](bt6wbss.html)

  Messages beginning with CRT are issued by Certificate Services.
* [DIR Messages](bshp1tm.html)

  Messages beginning with DIR are issued by the Core Driver during LDAP directory access.
* [DOM Messages](bshp1tn.html)

  Messages beginning with DOM are issued by driver components as they communicate among themselves.
* [DRVCOM Messages](b48n3rn.html)

  Messages beginning with DRVCOM are issued by the include/exclude system.
* [EJS Messages](bshp1tr.html)

  Messages beginning with EJS are issued by Event Journal Services.
* [HES Messages](bshp1tv.html)

  Messages beginning with HES are issued by driver components as they use HTTP to communicate.
* [LWS Messages](bshp1u1.html)

  Messages beginning with LWS are issued by the Core Driver as it functions as an HTTP server.
* [NET Messages](bshp1u4.html)

  Messages beginning with NET are issued by driver components during verification of SSL certificates.
* [OAP Messages](bshp1u7.html)

  Messages beginning with OAP are issued by driver components when communicating among themselves.
* [OBJ Messages](bshp1ug.html)

  Messages beginning with OBJ are issued by Object Services.
* [PLS Messages](bshp1uq.html)

  Messages beginning with PLS are issued by Platform Services.
* [PRCV Messages](bshp1v1.html)

  Messages beginning with PRCV are issued by Platform Receivers.
* [RDXML Messages](b48n3tn.html)

  Messages beginning with RDXML are issued by the embedded Remote Loader.
* [W3LM Messages](bshp1v5.html)

  Messages beginning with W3LM are issued by Web Services.
