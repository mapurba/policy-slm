# 7.5 Changing the Driver Shim Trace Level

To change the trace level setting for the driver shim, issue the following operator command with the desired trace level:

```
  MODIFY ACF2DRV,APPL='CTL(desired_trace_level)'
```

*Example 7-1* For example

```
  MODIFY ACF2DRV,APPL='CTL(9)'
```

For details about the trace file and trace levels, see [The Trace File](b3xzdtn.html#b3xzpa5).
