# 7.17 Manually Deleting the Unused ActiveMQ Queues

When an instance is stopped in the Fanout Agent, the Fanout Agent does not automatically delete the corresponding instance queue in ActiveMQ. This is because if an instance queue contains an unprocessed event, deleting the queue results in loss of that event. However, you can manually delete an unused queue of a stopped instance.

* Log in as administrator into Apache ActiveMQ.
* Click Manage ActiveMQ broker, then click Queues.
* Click Delete in the operations column for the queue that you want to delete.
