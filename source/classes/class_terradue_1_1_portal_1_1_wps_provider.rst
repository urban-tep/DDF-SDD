.. _class_terradue_1_1_portal_1_1_wps_provider:

WPS Provider
------------


Represents a remote provider of a Web Processing :ref:`Service <class_terradue_1_1_portal_1_1_service>`. 
This class is used as the computing resource on which WPS processes, which are equivalent to tasks, run.
"" 






The following properties define the object

.. cssclass:: propertiestable

+------+-------+--------------------------------------------------+
| Type | Name  | Summary                                          |
+======+=======+==================================================+
| bool | Proxy | Define if the provider is to be proxied or not   |
+------+-------+--------------------------------------------------+

The following functions are applicable to the object

.. cssclass:: propertiestable

============================== ===============================================================
Name                           Summary
============================== ===============================================================
StoreProcessOfferings          Get and stores the process offerings from GetCapabilities url 

ExecuteTask                    Executes the task. 

GetWPSCapabilitiesFromUrl      Return a GetCapabilities object from GetCapabilities url 

GetWPSDescribeProcessFromUrl   Gets the WPS describe process from URL. 

GetTaskResult                  Gets the task result. 

GetProcessOffering             Get all the process offering of the WPS provider 

============================== ===============================================================

