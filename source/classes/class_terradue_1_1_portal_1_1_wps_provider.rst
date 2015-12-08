.. _class_terradue_1_1_portal_1_1_wps_provider:

WpsProvider
-----------


Represents a remote provider of a Web Processing :ref:`Service <class_terradue_1_1_portal_1_1_service>`.



This class is used as the computing resource on which WPS processes, which are equivalent to tasks, run.

Properties
^^^^^^^^^^

.. cssclass:: propertiestable

+------+-------+--------------------------------------------------+
| Type | Name  | Summary                                          |
+======+=======+==================================================+
| bool | Proxy | Define if the provider is to be proxied or not   |
+------+-------+--------------------------------------------------+

Methods
^^^^^^^

.. cssclass:: propertiestable

====================== ============================== ===============================================================
Type                   Name                           Summary
====================== ============================== ===============================================================
void                   StoreProcessOfferings()        Get and stores the process offerings from GetCapabilities url 

bool                   ExecuteTask()                  Executes the task. 

WPSCapabilitiesType    GetWPSCapabilitiesFromUrl()    Return a GetCapabilities object from GetCapabilities url 

ProcessDescriptionType GetWPSDescribeProcessFromUrl() Gets the WPS describe process from URL. 

bool                   GetTaskResult()                Gets the task result. 

WpsProcessOffering     GetProcessOffering()           Get all the process offering of the WPS provider 

====================== ============================== ===============================================================

