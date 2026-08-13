# Exception Classes in com.novell.asam.JAscAuth

The following exceptions, along with java/lang/NullPointerException, are the exceptions that are thrown by the methods of JAscAuth.

## InvalidJAscException

Thrown when a method requires an authentication environment, but a valid authentication environment does not exist.

Most methods of com.novell.asam.JAscAuth.JAscAuth require that you call the init method before you call them. InvalidJAscException is thrown if you do not do so.

Corresponds to a return code of 16, AS\_NOAUTHENV, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscAttrNotFoundException

Thrown when the attribute specified to the readAttr method was not found for the specified object.

Corresponds to a return code of 13, AS\_ATTRNOTFOUND, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscAuthenticationException

Thrown when the password specified to the checkPassword method is not valid.

Corresponds to a return code of 1, AS\_NO, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscBadClientException

Thrown when the network address used by the platform to contact a Core Driver for a method call does not match the network address listed in the Platform Configuration object in the ASAM System container.

Corresponds to a return code of 4, AS\_BADCLIENT, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscChangePasswordException

Thrown by changePassword when the password cannot be changed.

Also thrown by changePassword if the old password given is not valid.

Corresponds to a return code of 1, AS\_NO, and a return code of 4, AS\_BADCLIENT, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscException

Thrown by most method calls when an unexpected or indeterminate error condition occurs.

## JAscInsufficientRightsException

Thrown by adminResetPassword if the administrative user does not exist, if the administrative user password specified is not valid, or if the administrative user does not have rights to change the password.

Also thrown by adminResetPassword if the network address used by the platform to contact a Core Driver does not match the network address listed in the Platform Configuration object in the ASAM System container.

Corresponds to a return code of 24, AS\_INSUFFICIENTRIGHTS from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscIntruderException

Thrown by checkPassword and changePassword when the specified user is locked because of intruder detection.

Corresponds to a return code of 6, AS\_INTRUDER, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscInvalidArgsException

Thrown when a parameter passed to a method is null or not valid.

Corresponds to a return code of 7, AS\_INVALIDARGS, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscInvalidObjException

Thrown when an object passed to a method is not found or is not of the correct type.

Corresponds to a return code of 8, AS\_INVALIDOBJ, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscInvalidObjLenException

Thrown when an object name passed to a method is longer than the maximum allowable name.

Corresponds to a return code of 9, AS\_INVALIDOBJLEN, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscInvalidReqException

Thrown when a method call is not known by the Core Driver.

Corresponds to a return code of 22, AS\_INVALIDREQ, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscKeyExpiredException

Thrown when the DES encryption key used by a non-SSL platform has expired.

Corresponds to a return code of 23, AS\_KEYEXPIRED, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscNoAgentException

Thrown when no Core Driver could be contacted to process a method call.

Corresponds to a return code of 3, AS\_NOAGENT, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscNoUserException

Thrown when the user specified to a method call is inactive or not in the Census.

Corresponds to a return code of 2, AS\_NOUSER, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscPassDuplicateException

Thrown by changePassword when the new password has been previously used for the user object, and the user is required to use unique passwords.

Corresponds to a return code of 10, AS\_PASSDUPLICATE, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscPassTooShortException

Thrown by changePassword when the new password is shorter than the minimum password length set for the user.

Corresponds to a return code of 11, AS\_PASSTOOSHORT, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscProductExpiredException

Thrown when the expiration date for the platform has passed.

Corresponds to a return code of 17, AS\_PRODUCTEXPIRED, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).

## JAscRevokedException

Thrown by checkPassword and changePassword when the specified user is disabled.

Corresponds to a return code of 5, AS\_REVOKED, from the AS Client API. For more information, see [Section C.0, Troubleshooting the API](br7ugbs.html).
