# B.2 Beyond Default Configuration for PAM

To use SSHD (secure shell daemon) to authenticate users through the PAM interface, your version of SSHD must be PAM-compliant. It is also recommended that you include the following directives in sshd\_config, the configuration file for SSHD:

```
  PasswordAuthentication yes
  ChallengeResponseAuthentication no
  UsePAM yes
```

For more information on SSHD configuration directives, consult the sshd\_config man pages.
