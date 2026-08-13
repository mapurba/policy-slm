# 7.6 Cannot Run Two Instances of the Fanout Agent Using the Same Queue Names

For multiple Fanout agents, you require equal number of ActiveMQs. In case the same ActiveMQ is used for multiple Fanout agents, manually clean the ActiveMQ queues before using a different Fanout agent.
