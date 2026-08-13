# 7.18 Collecting Trace Files For Troubleshooting

While troubleshooting any issues, you require to view the required trace files to analyze the issue. Ensure the following trace files are collected to help you analyze any issue:

1. Fanout driver trace: This is a common trace file that can be configured using Designer or Identity Console.

   * To configure using Designer, go to Driver Properties > Trace and set the trace level and trace file name.
   * To configure using Identity Console, click the driver icon, then click the Log and Trace Configuration tab and configure the trace level and trace file path.
2. Fanout agent trace: This trace file contains the processing logs performed by the Fanout agent. The trace file is located at <fanout agent root directory>\logs.

   To configure the Fanout agent trace level and the trace path, modify the following parameter in the Fanout agent configuration file:

   *NOTE:*By default, trace level is set to 5 and file name is fanout\_trace.txt.

   * netiq.fanoutagent.trace.level=5
   * netiq.fanoutagent.trace.file=fanout\_trace.txt
3. JDBC driver instance trace: This trace contains the JDBC instance level tracing, that can be configured using Designer. These trace files are located in the server where the Fanout agent is installed.

   * To configure using Designer, provide the trace level and trace file path for the particular JDBC instance, while configuring the connection object.

     ```
     <trace-info>
                  <driverTraceFile>trace-file-path</driverTraceFile>
                  <driverTraceLevel>trace-level</driverTraceLevel>
                  <driverTraceFileSize>trace-file-size</driverTraceFileSize>
     </trace-info>
     ```
