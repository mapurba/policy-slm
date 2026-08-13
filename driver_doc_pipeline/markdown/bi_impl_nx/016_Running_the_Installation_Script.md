# 3.5 Running the Installation Script

Several of the installation procedures described in the sections that follow include running the installation script on a Linux or UNIX system.

To run the installation script:

1. Log in to the target server as root.
2. Enter one of the following commands as appropriate for your operating system and architecture:

   ```
   sh linux_x86_driver_install.bin
   sh linux_x86_64_driver_install.bin
   sh linux_s390x_driver_install.bin
   sh solaris_sparc_driver_install.bin
   sh solaris_x86_driver_install.bin
   sh aix_driver_install.bin
   sh hpux_ia64_driver_install.bin
   ```

   These installation commands are self-extracting files, natively executable by the shell.
3. Optionally enter a language choice.
4. Read and accept the license agreement.
5. At the prompt, enter the installation type as directed by the procedure.

   ```
   Select the type of installation:
    1) Install Driver Shim on Linux or UNIX system
    2) Install only PAM Module

   Installation Type [1]:
   ```
6. Respond to the subsequent prompts as appropriate for the selected installation type.
