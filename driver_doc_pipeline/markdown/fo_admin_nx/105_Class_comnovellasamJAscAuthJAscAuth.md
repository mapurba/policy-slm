# Class com.novell.asam.JAscAuth.JAscAuth

Provides the methods you use to access the AS Client API.

## Constructor

```
public JAscAuth()
```

## Fields

The following fields map the AS Client API return codes. For more information about return codes from the AS Client API, see [Section C.0, Troubleshooting the API](br7ugbs.html).

```
public static int AS_OK     = 0
```

```
public static int AS_NO     = 1
```

```
public static int AS_NOUSER     = 2
```

```
public static int AS_NOAGENT    = 3
```

```
public static int AS_NOSERVER   = 3
```

```
public static int AS_BADCLIENT  = 4
```

```
public static int AS_REVOKED    = 5
```

```
public static int AS_INTRUDER    = 6
```

```
public static int AS_INVALIDARGS  = 7
```

```
public static int AS_INVALIDOBJ  = 8
```

```
public static int AS_INVALIDOBJLEN  = 9
```

```
public static int AS_PASSDUPLICATE  = 10
```

```
public static int AS_PASSTOOSHORT  = 11
```

```
public static int AS_TOOSMALL    = 12
```

```
public static int AS_ATTRNOTFOUND  = 13
```

```
public static int AS_WSOCKUP    = 14
```

```
public static int AS_WSOCKDOWN  = 15
```

```
public static int AS_NOAUTHENV  = 16
```

```
public static int AS_PRODUCTEXPIRED   = 17
```

```
public static int AS_INCLUDED    = 18
```

```
public static int AS_EXCLUDED    = 19
```

```
public static int AS_NOMATCH    = 20
```

```
public static int AS_NOLICENSE  = 21
```

```
public static int AS_INVALIDREQ  = 22
```

```
public static int AS_KEYEXPIRED  = 23
```

## Methods

The following methods invoke the API functions:

* [adminResetPassword](chdiibfb.html#chdbiegf)
* [changePassword](chdiibfb.html#chdfdcdg)
* [checkPassword](chdiibfb.html#chddcbah)
* [destroy](chdiibfb.html#chdbbjah)
* [effectiveRights](chdiibfb.html#chdjcfgj)
* [getContext](chdiibfb.html#chdfdaha)
* [getLastReturnCode](chdiibfb.html#chdfabai)
* [groupMembers](chdiibfb.html#chdccghj)
* [init](chdiibfb.html#chdcajdd)
* [listSecurityEquivalences](chdiibfb.html#chdbjjgh)
* [readAttribute](chdiibfb.html#chdecaii)
* [secondsToDays](chdiibfb.html#chdfcchf)
* [securityEquals](chdiibfb.html#chdiedig)
* [strError](chdiibfb.html#chdegceg)
* [userIncludeExclude](chdiibfb.html#chdchaeg)

### adminResetPassword

Performs an administrative reset of a user's password. The new password is marked as being expired unless it is non-expiring.

You must call the init method to initialize the JAscAuth environment before calling adminResetPassword. For more information about init, see [init](chdiibfb.html#chdcajdd).

For details about the exceptions that can be thrown, see [Exception Classes in com.novell.asam.JAscAuth](chdgfcih.html).

#### Syntax

```
public void adminResetPassword(
 java.lang.String adminUser,
 java.lang.String adminPass,
 java.lang.String user,
 java.lang.String pass)
```

#### Parameters

| adminUser | The Enterprise User ID of an administrative user with rights to change the target user's password |
| adminPass | The password of the administrative user |
| user | The Enterprise User ID whose password is to be changed |
| pass | The new password for the user |

### changePassword

Changes the password of a user.

You must call the init method to initialize the JAscAuth environment before calling changePassword. For more information about init, see [init](chdiibfb.html#chdcajdd).

For details about the exceptions that can be thrown, see [Exception Classes in com.novell.asam.JAscAuth](chdgfcih.html).

#### Syntax

```
public void changePassword(
 String user,
 String oldPass,
 String newPass)
```

#### Parameters

| user | The Enterprise User ID whose password is to be changed |
| oldPass | The old password for the user |
| newPass | The new password for the user |

### checkPassword

Verifies the password of a user.

You must call the init method to initialize the JAscAuth environment before calling checkPassword. For more information about init, see [init](chdiibfb.html#chdcajdd).

The checkPassword method can optionally return information about the user and password in a JAscUser object. For details about the contents of JAscUser, see [Classes Used by checkPassword](chdhhaad.html).

For details about the exceptions that can be thrown, see [Exception Classes in com.novell.asam.JAscAuth](chdgfcih.html).

#### Syntax

```
public void checkPassword(
 String user,
 String pass)
```

```
public void checkPassword(
 String user,
 String pass,
 JAscUser ascuser)
```

#### Parameters

| user | The Enterprise User ID whose password is to be verified |
| pass | The password to be verified for the user |
| ascuser | A JAscUser object to be filled with information about the user and password |

### destroy

Destroys the JAscAuth environment and frees its underlying resources.

#### Syntax

```
public void destroy()
```

#### See Also

[init](chdiibfb.html#chdcajdd)

### effectiveRights

Checks the effective rights of one object over another for a specific attribute.

You must call the init method to initialize the JAscAuth environment before calling effectiveRights. For more information about init, see [init](chdiibfb.html#chdcajdd).

For details about the exceptions that can be thrown, see [Exception Classes in com.novell.asam.JAscAuth](chdgfcih.html).

#### Syntax

```
public void effectiveRights(
 String user,
 String object,
 String attribute,
   String rights)
```

#### Parameters

| user | The Enterprise User ID or fully distinguished object name whose effective rights are to be tested |
| object | The Enterprise User ID or fully distinguished object name for which access by user is to be tested |
| attribute | The name of an attribute of object for which the effective rights of user are tested. The special attribute names All Attributes Rights, Entry Rights, and SMS Rights can also be specified. |
| rights | The rights to test. The characters specified must be in the following set: [S,C,R,W,A]. These correspond to Supervisor, Compare, Read, Write, and Add Self. |

### getContext

Returns the fully distinguished object name from the Census for a given user.

You must call the init method to initialize the JAscAuth environment before calling getContext. For more information about init, see [init](chdiibfb.html#chdcajdd).

For details about the exceptions that can be thrown, see [Exception Classes in com.novell.asam.JAscAuth](chdgfcih.html).

#### Syntax

```
public String getContext(String user)
```

#### Parameters

| user | The Enterprise User ID whose context is to be returned |

### getLastReturnCode

Returns the return code from the last call to the AS Client API.

For details about return codes from the AS Client API, see [Section C.0, Troubleshooting the API](br7ugbs.html).

#### Syntax

```
public int getLastReturnCode()
```

#### See Also

[strError](chdiibfb.html#chdegceg)

### groupMembers

Returns an enumeration of all members of a given Group.

You must call the init method to initialize the JAscAuth environment before calling groupMembers. For more information about init, see [init](chdiibfb.html#chdcajdd).

For details about the exceptions that can be thrown, see [Exception Classes in com.novell.asam.JAscAuth](chdgfcih.html).

#### Syntax

```
public Enumeration groupMembers(String group)
```

#### Parameters

| group | The Enterprise Group or fully distinguished Group object name whose members are to be returned |

### init

Initializes the JAscAuth environment using the platform configuration file.

You can optionally specify the location of the platform configuration file to be used. If you do not specify the location of the platform configuration file, the default platform configuration file is used.

Call the destroy method to free the JAscAuth environment and its underlying resources when you are finished. For more information about destroy, see [destroy](chdiibfb.html#chdbbjah).

#### Syntax

```
public void init()
```

```
public void init(java.lang.String filename)
```

#### Parameters

| filename | The path name of the platform configuration file to use |

### listSecurityEquivalences

Returns an enumeration of a given user's security equivalences.

You must call the init method to initialize the JAscAuth environment before calling listSecurityEquivalences. For more information about init, see [init](chdiibfb.html#chdcajdd).

For details about the exceptions that can be thrown, see [Exception Classes in com.novell.asam.JAscAuth](chdgfcih.html).

#### Syntax

```
public Enumeration listSecurityEquivalences(String user)
```

#### Parameters

| user | The Enterprise User ID whose Security Equals attribute values are to be returned |

### readAttribute

Returns an enumeration of the values of a specified attribute for a given object.

You must call the init method to initialize the JAscAuth environment before calling readAttribute. For more information about init, see [init](chdiibfb.html#chdcajdd).

For details about the exceptions that can be thrown, see [Exception Classes in com.novell.asam.JAscAuth](chdgfcih.html).

#### Syntax

```
public Enumeration readAttribute(
 String object,
 String attribute)
```

#### Parameters

| object | The Enterprise User ID or fully distinguished object name of the object whose attribute values are to be returned |
| attribute | The single-valued attribute whose value is to be returned for the object. Only the Home Directory attribute of a User object is supported at this time. |

### secondsToDays

Returns the integer number of days for the given number of seconds.

#### Syntax

```
public long secondsToDays(long secs)
```

### securityEquals

Checks to see if a user has security equivalence to the specified object.

You must call the init method to initialize the JAscAuth environment before calling securityEquals. For more information about init, see [init](chdiibfb.html#chdcajdd).

For details about the exceptions that can be thrown, see [Exception Classes in com.novell.asam.JAscAuth](chdgfcih.html).

#### Syntax

```
public void securityEquals(
 String user,
 String object)
```

#### Parameters

| user | The Enterprise User ID to be tested |
| object | The fully distinguished object name for which the security equivalence of user is to be tested |

### strError

Returns the string representation of the given AS Client API return code.

#### Syntax

```
public String strError(int rc)
```

#### Parameters

| rc | The AS Client API return code value whose string representation is to be returned |

#### See Also

[getLastReturnCode](chdiibfb.html#chdfabai)

### userIncludeExclude

Determines if a given user matches an AS.USER.INCLUDE or AS.USER.EXCLUDE statement in the platform configuration file.

#### Syntax

```
public int userIncludeExclude(String user)
```

#### Parameters

| user | The Enterprise User ID of the user to be checked |

#### Return Values

| AS\_NOMATCH | The user does not match any INCLUDE/EXCLUDE statement. Because AS.USER.INCLUDE \* is implicit in the absence of AS.USER.EXCLUDE \*, the user is included. |
| AS\_INCLUDED | User matches an AS.USER.INCLUDE statement. |
| AS\_EXCLUDED | User matches an AS.USER.EXCLUDE statement or an entry in the built-in standard exclude list. |
