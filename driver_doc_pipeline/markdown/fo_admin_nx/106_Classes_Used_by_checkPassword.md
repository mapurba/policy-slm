# Classes Used by checkPassword

The following topics describe classes used by the checkPassword method of JAscAuth to return information.

## Class com.novell.asam.JAscAuth.JAscUser

The checkPassword method of JAscAuth optionally returns a JAscUser object with information about the user being authenticated.

### Constructor

```
public JAscUser()
```

### Fields

| public JAscLoginRestrict login | Contains the user's login disabled flag |
| public JAscPassRestrict pass | Contains the user's password expiration information |

## Class com.novell.asam.JAscAuth.JAscLoginRestrict

The checkPassword method of JAscAuth optionally returns a JAscUser object with information about the user being authenticated. One of the fields in JAscUser is a JAscLoginRestrict object, which contains the user's login disabled flag.

### Constructor

```
public JAscLoginRestrict()
```

### Fields

| public int disabled | The user's login disabled flag |

### Methods

| public int getDisabled() | Returns the user's login disabled flag |

## Class com.novell.asam.JAscAuth.JAscPassRestrict

The checkPassword method of JAscAuth optionally returns a JAscUser object with information about the user being authenticated. One of the fields in JAscUser is a JAscPassRestrict object, which contains password expiration information.

### Constructor

```
public JAscPassRestrict()
```

### Fields

| public long interval | The password change interval in seconds (or -1 if the password does not expire) |
| public long expire | The number of seconds until the password expires (or -1 if the password does not expire) |

### Methods

| public long getInterval() | Returns the password change interval in seconds (or -1 if the password does not expire) |
| public long getExpire() | Returns the number of seconds until the password expires (or -1 if the password does not expire) |
