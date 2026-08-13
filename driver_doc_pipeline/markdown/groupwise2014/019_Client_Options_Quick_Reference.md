# 5.5 Client Options Quick Reference

The following sections contain a summary of all of the GroupWise Client options that are currently enabled for the driver.

* [Environment](b9q9on5.html#b9qbgfx)
* [Send](b9q9on5.html#b9qbjmm)
* [Calendar](b9q9on5.html#b9qbkir)

## 5.5.1 Environment

The environment options allow you to change how a users interacts with the GroupWise client. These options control views, access, appearance, junk mail settings, retention, and cleanup. [Table 5-1](b9q9on5.html#b12cugux) shows the GroupWise Administration console options with a with their corresponding XML field names.

*Table 5-1* Client Options: Environment

| Client Option | XML Field |
| General > Check spelling before send | [autoSpellCheck](setting-groupwise-client-options.html#b9qp74p) |
| General > Allow shared folder creation | [allowSharedFolders](setting-groupwise-client-options.html#b9qp84y) |
| General > Allow shared address book creation | [allowSharedAddressBooks](setting-groupwise-client-options.html#b9qp8lf) |
| General > Allow use of POP and IMAP accounts in the Online Mailbox | [allowPOP\_IMAPAccounts](setting-groupwise-client-options.html#b9qp8t1) |
| General > Allow use of news (NNTP) accounts in the Online Mailbox | [allowNNTPAccounts](setting-groupwise-client-options.html#b9qp99e) |
| General > Show Messenger presence | [showIMPresence](setting-groupwise-client-options.html#b9qp9ls) |
| Client Access > Client Licensing | [clientLicense](setting-groupwise-client-options.html#b9qpc4z) |
| Views > Allowable Read Views | [allowableViewRead](setting-groupwise-client-options.html#b9qptg8) |
| Views > Allowable Read Views > Set Default | [defaultViewRead](setting-groupwise-client-options.html#b9qpx8k) |
| Views > Allowable Compose Views | [alloableViewCompose](setting-groupwise-client-options.html#b9qpue7) |
| Cleanup > Empty Trash | [trashPurge](setting-groupwise-client-options.html#b9qre7e) |
| Cleanup > Empty Trash > days | [trashDays](setting-groupwise-client-options.html#b9tt5jq) |

## 5.5.2 Send

The send options allows you to change how users send mail, appointments, notes, and tasks. [Table 5-2](b9q9on5.html#b9qbk1p) shows the GroupWise Administration console options with their corresponding XML field names.

*Table 5-2* GroupWise Client Options: Send

| Client Option | XML Field |
| Send Options > Classification | [sendSecurity](setting-groupwise-client-options.html#b9qrf06) |
| Send Options > Delay delivery | [delayDelivery](setting-groupwise-client-options.html#b9qrf7o) |
| Send Options > Convert attachments | [itemConversions](setting-groupwise-client-options.html#b9qrfea) |
| Send Options > Wildcard Addressing | [asteriskSendRestriction](setting-groupwise-client-options.html#b9qrfka) |
| Send Options > Allow reply rules to loop | [allowRuleReplyMoreThanOnce](setting-groupwise-client-options.html#b9qrg3f) |
| Send Options > Allow use of Internet mail tracking | [internetStatusTracking](setting-groupwise-client-options.html#b9qrgej) |
| Send Options > Priority | [mailPriority](setting-groupwise-client-options.html#b9qrhfq) |
| Send Options > Reply requested | [mailReplyRequested](setting-groupwise-client-options.html#b9qrhqt) |
| Send Options > Expiration date | [mailExpireDays](setting-groupwise-client-options.html#b9qri27) |
| Send Options > Notify recipients | [notifyRecipient](setting-groupwise-client-options.html#b9qri9b) |
| Mail > Create a sent item to track information | [outboxInsert](setting-groupwise-client-options.html#b9qrjpj) |
| Mail > Create a sent item to track information > option | [mailStatusInfo](setting-groupwise-client-options.html#b9tczny) |
| Mail > Auto-delete sent item | [mailAutoDelete](setting-groupwise-client-options.html#b9tvzrd) |
| Mail > Return Notification > When opened | [mailReturnOpen](setting-groupwise-client-options.html#b9qrkxw) |
| Mail > Return Notification > When deleted | [mailReturnDelete](setting-groupwise-client-options.html#b9qrm5i) |
| Appt > Create a sent item to track information options | [appointmentStatusInfo](setting-groupwise-client-options.html#b9qrnqn) |
| Appt > Return Notification > When opened | [appointmentReturnOpen](setting-groupwise-client-options.html#b9qroq2) |
| Appt > Return Notification > When deleted | [appointmentReturnDelete](setting-groupwise-client-options.html#b9qrp7x) |
| Appt > Return Notification > When accepted | [appointmentReturnAccept](setting-groupwise-client-options.html#b9qrpr3) |
| Task > Create a sent item to track information options | [taskStatusInfo](setting-groupwise-client-options.html#b9qrryx) |
| Task > Return Notification > When opened | [taskReturnOpen](setting-groupwise-client-options.html#b9qrtw0) |
| Task > Return Notification > When accepted | [taskReturnAccepted](setting-groupwise-client-options.html#b9qruo9) |
| Task > Return Notification > When deleted | [taskReturnDelete](setting-groupwise-client-options.html#b9qru5j) |
| Task > Return Notification > When completed | [taskReturnCompleted](setting-groupwise-client-options.html#b9qruwe) |
| Note > Create a sent item to track information options | [noteStatusInfo](setting-groupwise-client-options.html#b9qrvlr) |
| Note > Return Notification > When opened | [noteReturnOpen](setting-groupwise-client-options.html#b9qrwef) |
| Note > Return Notification > When deleted | [noteReturnDelete](setting-groupwise-client-options.html#b9qrwwp) |
| Note > Return Notification > When accepted | [noteReturnAccept](setting-groupwise-client-options.html#b9qrxeq) |
| Security > Conceal Subject | [concealedSubject](setting-groupwise-client-options.html#b9qry4c) |
| Security > Require password to complete routed item | [routePasswordRequired](setting-groupwise-client-options.html#b9qryb4) |
| Security > Secure Item Options > Do not allow use of S/MIME | [disallowSMIME](setting-groupwise-client-options.html#b9qryx9) |
| Security > Secure Item Options > Encrypt for recipients | [encryptMessages](setting-groupwise-client-options.html#b9qrz8m) |
| Disk Space Mgmt > User Limits | [userLimitSet](setting-groupwise-client-options.html#b9qrzwd) |
| Disk Space Mgmt > Mailbox size limit | [boxSizeLimit](setting-groupwise-client-options.html#b9qs0fr) |
| Disk Space Mgmt > Threshold for warning users | [boxThresholdLimit](setting-groupwise-client-options.html#b9qs0x3) |
| Disk Space Mgmt > Limit apply to cache | [boxLimitAppliesToCache](setting-groupwise-client-options.html#b9qs294) |
| Disk Space Mgmt > Notify the administrator when threshold limit is exceeded | [enableBoxThresholdNotification](setting-groupwise-client-options.html#b9qs2jv) |
| Disk Space Mgmt > Notify the administrator when size limit is exceeded | [enableBoxSizeNotification](setting-groupwise-client-options.html#b9qs2zw) |

## 5.5.3 Calendar

The Calendar options allows you to control how the calendar is displayed, and how busy searches are conducted. [Table 5-3](b9q9on5.html#b9qbmap) shows the GroupWise Administration console options with their corresponding XML field names.

*Table 5-3* GroupWise Client Option: Calendar

| Client Options | XML Field |
| General > Month Display Option > First of week | [firstDay](setting-groupwise-client-options.html#b9qs3uf) |
| General > Month Display Option > Highlight day | [hilightDaysOfWeek](setting-groupwise-client-options.html#b9qs42b) |
| General > Month Display Option > Show week number | [showWeekNumber](setting-groupwise-client-options.html#b9qs4ag) |
| General > Appointment Options > Include myself on new appointments | [appointmentIncludeSelf](setting-groupwise-client-options.html#b9qs4ii) |
| General > Appointment Options > Default length | [appointmentDefaultLength](setting-groupwise-client-options.html#b9qs4t1) |
| General > Work Schedule > Start time | [startOfWorkday](setting-groupwise-client-options.html#b9qs533) |
| General > Work Schedule > End time | [endOfWorkday](setting-groupwise-client-options.html#b9qs5b8) |
| General > Work Schedule > Work days | [workdays](setting-groupwise-client-options.html#b9qs5jc) |
| General > Alarm Options > Set alarm when accepted | [appointmentAlarmSet](setting-groupwise-client-options.html#b9qp3je) |
| General > Alarm Options > Default alarm time | [appointmentAlarmMinutes](setting-groupwise-client-options.html#b9qp3vi) |
| Busy Search > Range and Time to Search > From | [busyStartTime](setting-groupwise-client-options.html#b9qbpah) |
| Busy Search > Range and Time to Search > To | [busyEndTime](setting-groupwise-client-options.html#b9qbpmi) |
| Busy Search > Appointment Length | [busyInterval](setting-groupwise-client-options.html#b9qbpz4) |
| Busy Search > Days to Search | [busyDays](setting-groupwise-client-options.html#b9qbqgf) |
