# 10.4 Why does the rescind transaction not update the Future Full State Object?

Rescind process is an event that is triggered by the HR administrator to terminate a business process that was initiated for an expected worker to join the organization. The rescind event is triggered if the expected worker defers to join the organization. As the HR administrator would have started the upstream business process, a rescind event is triggered to terminate it.

To create a future state object, the business process and workflows are initiated based on the created future state event.

For example, assume a business process is initiated for hiring, and the full state object is created “x“ days prior to the effective date of hiring. In some cases, there may be changes to update the worker object, post the creation of full state object. These changes when incorporated to the worker object, they do not reflect in the full state object. Hence, there will be a difference between the worker object and the full state object.

So, depending on when a rescind event is triggered, the Workday driver ensures to update the changes to the associated object.

Consider the two scenarios for triggering the rescind event:

* If the rescind event is triggered before creation of the full state object:

  In this scenario, the full state object will include the rescind information. This is because, the rescind event was already triggered prior to the full state object creation. As a result of this, the future state object will not be created.
* If the rescind event is triggered after creation of the full state object:

  In this scenario, the full state object will not include the rescind information. As the rescind event was triggered post creation of the full state object, this event updates only the current state object, and not the full state object.
