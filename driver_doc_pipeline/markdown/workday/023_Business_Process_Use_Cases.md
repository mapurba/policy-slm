# 4.1 Business Process Use Cases

As a part of lifecycle business process, the following use cases are supported for a worker:

* Hire Business Process:

  + Hiring an employee for future date: This use case helps to manage the worker details for workers hired for a future date.For example, if a worker is being hired for a future date, the hiring company will have the worker's generic information updated for the record, which is partial. To have the complete information (which includes employee ID, official email ID, etc) updated, you must specify the number of days prior to keep the worker record ready.

    Having this information ready and available helps to prevent any on-boarding issues. Hence, the advance number of days is specified (in the field Future Object Creation Days in Advance) with respect to the hiring date, so that a future state object of the worker is created to execute a seamless on-boarding process.

    For more information, see [Configuring Business Process](t4f47egfqot3.html).
  + Hire Contingent worker for future date: For a Contingent worker to be hired on a future date, you can acquire and have all the required information updated. All the future state objects (such as worker details and position details) are created in advance to the effective hiring date.
* Rehire Business Process:

  + Rehire employee for future date: You can set the number of days in advance to acquire and update all the information for hiring an ex-employee. Identity Manager creates all the future state objects as per the number of days set in advance with respect to the effective hiring date of the ex-employee.
  + Rehire Contingent worker for future date: Similar to the rehire employee, you can set the number of days in advance for the future state objects to be created for a contingent worker.
  + Convert Contingent worker to employee: You can set the number of days in advance to convert a contingent worker to a regular employee. Identity Manager acquires and updates all the required information and creates the future state objects in advance to the conversion effective date.
* Terminate Business Process:

  + Terminate Employee: You can set the number of days in advance to deactivate the worker’s details, due to termination of an employee.
  + Contract closure for Contingent worker: You can set the number of days in advance to deactivate the worker’s details, due to expiry of the contract period.
  + Employee Retirement: When the employee qualifies for retirement, you can set the number of days in advance to deactivate the employee’s details.
* Attribute Management of Contact Information: You can manage the attributes of the workers contact information such as, home address etc.
