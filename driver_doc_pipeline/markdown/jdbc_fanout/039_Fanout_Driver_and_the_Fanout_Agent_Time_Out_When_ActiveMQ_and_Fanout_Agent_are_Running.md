# 7.2 Fanout Driver and the Fanout Agent Time Out When ActiveMQ and Fanout Agent are Running

When the Fanout driver does not receive response within a specified time, it displays a time out warning message and processes the subsequent event.The response for the previous event will be processed when it is available.

It is safe to ignore the warning as this does no cause any functionality loss.
