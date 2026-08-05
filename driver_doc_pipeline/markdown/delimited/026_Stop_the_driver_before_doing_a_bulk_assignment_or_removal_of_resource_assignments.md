# 10.1 Stop the driver before doing a bulk assignment or removal of resource assignments

If you don’t stop the driver before doing a bulk removal of resource assignments from the User Application, the driver creates multiple user entries in the output CSV file. It might display a warning message when you are deploying the driver for the first time.

To workaround this issue, stop the driver before doing such bulk revocations from the User Application, then restart the driver. This creates the output CSV file with one entry instead of multiple intermediate entries in it.
