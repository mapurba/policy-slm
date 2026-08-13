# 3.4 Getting the Installation Files

1. Obtain the most recent distribution of the Identity Manager 4.8 Driver for RACF from the [NetIQ Downloads Web site](https://dl.netiq.com/index.jsp).

   At the time of this Implementation Guide’s release, the -driver was included in the following ISO package:

   ```
     NIdM_Integration_Module_4.8_Mainframes_Midrange.iso
   ```
2. Based on the version of the Identity Manager Metadirectory engine you are using, determine which files you will need to copy from the software distribution.

   1. Regardless of the Metadirectory engine version you are running, the following files are required for all installations:

      ```
        SAMPLIB.XMT
        IDMLOAD.XMT
        RACFEXEC.XMT
      ```

      These files are located under bidirectional/RACF.
3. Copy the files the files you will need (see Step 2) onto the workstation you will use for the installation. You will use this workstation to set up the driver on the Metadirectory server and to FTP files to the target system.
