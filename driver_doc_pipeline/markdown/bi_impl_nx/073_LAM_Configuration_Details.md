# C.5 LAM Configuration Details

PAM is supported by AIX beginning with AIX 5.3, but earlier versions use the IBM Loadable Authentication Module (LAM) technology instead of PAM. The Linux and UNIX driver LAM module implements password publishing in the LAM environment for files mode only. The LAM module is not supported for NIS or NIS+ on AIX.

You can install and optionally configure the LAM module at any time using the installation program. For details, see [Installing the PAM or LAM Module](b3xfnmq.html).

After it is installed, you can configure the LAM module with the nxdrv-config command. For details, see [Using the nxdrv-config Command](b4339kg.html).

The installation script installs the LAM module NXDRV into the /usr/lib/security directory of the connected AIX system. If you respond to the prompt to configure the LAM module, the installation script adds an NXDRV stanza to /usr/lib/security/methods.cfg. The nxdrv-config command also adds this stanza.

You can edit your /usr/lib/security/methods.cfg file manually. The following example shows the driver LAM stanza:

```
NXDRV:
   program = /usr/lib/security/NXDRV
   options = db=BUILTIN
```

If the LAM module is installed, the default AIX files-mode scripts cause AIX users to be associated with the LAM module via individual user stanzas in /etc/security/user. Alternatively, you can change the global stanza in /etc/security/user to use the LAM module by default, and change the scripts so that they don’t assign NXDRV SYSTEM and registry attributes to files-mode users. More fine-tuned configurations are also possible and are referenced in the add-user.sh script file.
