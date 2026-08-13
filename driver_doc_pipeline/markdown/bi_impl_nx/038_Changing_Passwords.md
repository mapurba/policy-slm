# 7.5 Changing Passwords

To publish password change information, you must change passwords with a method that uses PAM or LAM. The driver obtains password change information through PAM and LAM.

To set a password, use passwd, not yppasswd or passwd -r. yppasswd and passwd -r bypass the authentication module.

Do not specify a password with useradd. This bypasses the authentication module.

For more information about the driver PAM and LAM modules, see [PAM Configuration Details](b3yj5z9.html) and [LAM Configuration Details](b3yj64d.html).
