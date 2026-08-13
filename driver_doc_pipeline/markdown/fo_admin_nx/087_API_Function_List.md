# 14.2 API Function List

API routines are provided to perform the following functions:

* Initialize the environment.

  + *C:*
    [ASC\_INIT](babbgdde.html), [ASC\_INIT\_EXT](babiiiag.html)
  + *Java:*
    [init](chdiibfb.html#chdcajdd)
* Terminate the environment.

  + *C:*
    [ASC\_TERM](babeeidi.html)
  + *Java:*
    [destroy](chdiibfb.html#chdbbjah)
* Validate a user ID and password combination.

  + *C:*
    [ASC\_CHKPASSWD](chddejci.html)
  + *Java:*
    [checkPassword](chdiibfb.html#chddcbah)
* Change a user's password, given the current password.

  + *C:*
    [ASC\_CHGPASSWD](chdjhaec.html)
  + *Java:*
    [changePassword](chdiibfb.html#chdfdcdg)
* Reset a user's password as an administrative user.

  + *C:*
    [ASC\_ADMINRSTPASSWD](bcgdgeha.html)
  + *Java:*
    [adminResetPassword](chdiibfb.html#chdbiegf)
* Obtain the fully distinguished name for a user ID.

  + *C:*
    [ASC\_GETCONTEXT](chdfccfe.html)
  + *Java:*
    [getContext](chdiibfb.html#chdfdaha)
* Determine if a user has security equal to a given object.

  + *C:*
    [ASC\_SECEQUAL](chdcaaic.html)
  + *Java:*
    [securityEquals](chdiibfb.html#chdiedig)
* Determine if an object has the specified effective rights to the specified attribute of another object.

  + *C:*
    [ASC\_RIGHTS](chdibdjd.html)
  + *Java:*
    [effectiveRights](chdiibfb.html#chdjcfgj)
* Obtain a list of members of a group.

  + *C:*
    [ASC\_GRPMEM](chdgdbej.html)
  + *Java:*
    [groupMembers](chdiibfb.html#chdccghj)
* Obtain a list of security equivalences for a user.

  + *C:*
    [ASC\_LISTSEQV](chdgfafi.html)
  + *Java:*
    [listSecurityEquivalences](chdiibfb.html#chdbjjgh)
* Obtain attribute values for an object.

  + *C:*
    [ASC\_READATTR](chdgfhej.html)
  + *Java:*
    [readAttribute](chdiibfb.html#chdecaii)
* Determine if a given user is in the Include/Exclude list.

  + *C:*
    [ASC\_USER\_INCLUDE\_EXCLUDE](chdcjbca.html)
  + *Java:*
    [userIncludeExclude](chdiibfb.html#chdchaeg)
* Decode API return values.

  + *C:*
    [ASC\_STRERROR](babgiddd.html)
  + *Java:*
    [strError](chdiibfb.html#chdegceg)
* Convert number of seconds to number of days.

  + *C:*
    [ASC\_DAYS](chdjjggg.html)
  + *Java:*
    [secondsToDays](chdiibfb.html#chdfcchf)
