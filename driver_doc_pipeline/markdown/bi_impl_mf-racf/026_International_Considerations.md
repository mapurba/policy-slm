# 5.5 International Considerations

The Identity Manager driver for RACF assumes the RACF system is using the EBCDIC Latin 1 (Open Systems) codepage for translating data to and from the Identity Manager Metadirectory engine. This codepage, IBM-1047, is configured in the SAMPLIB member RACFDRV, the JCL for starting the RACF driver shim. If your system uses a codepage other than IBM-1047, you will need to change the JCL for starting the RACF driver to ensure correct character translation.

The following line, specified in the SAMPLIB(RACFDRV) member, illustrates how the environment is configured for the default codepage IBM-1047:

```
  //  SET ENV='ENVAR("LC_CTYPE=IBM-1047")'
```

You may change this text to reflect the codepage of your RACF system. The format is IBM-CCSID, where CCSID is a coded character set identifier, represented in decimal.

For a list of valid codepage identifiers, see the [IBM CCSID reference table](http://www-01.ibm.com/software/globalization/ccsid/ccsid_registered.jsp). The following table lists a subset of sample values:

| Codepage | Description |
| IBM-858 | IBM-PC |
| IBM-1047 | Latin 1 (Open Systems) |
| IBM-1140 | US/Canada |
| IBM-1141 | Austria/Germany |
| IBM-1142 | Denmark/Norway |
| IBM-1143 | Finland/Sweden |
| IBM-1144 | Italy |
| IBM-1145 | Spain/Spanish Latin America |
| IBM-1146 | UK |
| IBM-1147 | France |
| IBM-1148 | International |
| IBM-1149 | Iceland |
