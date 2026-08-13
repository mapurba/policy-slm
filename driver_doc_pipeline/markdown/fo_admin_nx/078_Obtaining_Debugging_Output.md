# 13.1 Obtaining Debugging Output

Identity Manager Fan-Out Driver components support the option to produce extensive debugging output. Although this output is intended primarily for use by NetIQ Technical Support, you might find it useful for your own troubleshooting efforts.

Because debugging mode adversely affects performance, it should not be used for routine operations.

## 13.1.1 Debugging the Linux/UNIX Platform Services Process and Platform Receiver

To obtain debugging output for the Platform Services Process or Platform Receiver on Linux/UNIX:

1. Add a DEBUGLOGFILE statement or DEBUGTOSTDOUT statement to the platform configuration file.

   For details about the platform configuration file, see [Section 10.0, The Platform Configuration File](beibfiae.html).
2. Specify the debugging command line parameter when you start the Platform Services Process or Platform Receiver.

   To obtain full debugging output, specify -d \\* on the command line.

   To obtain debugging output limited to messages exchanged with Core Drivers, specify the -d dom parameter.
