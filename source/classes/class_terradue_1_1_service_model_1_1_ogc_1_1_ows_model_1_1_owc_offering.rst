.. _class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_offering:

OwcOffering
-----------


This datatype class defines the properties of a specific service binding or inline content for an offering. The service binding is primarily characterized by a series of parameters. The parameters valid for a specific type of service binding, e.g. WFS are defined outside of the OWS Context core specification. Each specific service binding is defined by a URI which references a requirement class. 





Properties
^^^^^^^^^^

.. cssclass:: propertiestable

+------------------------------------------------------------------------------------------------+------------+-----------------------------------------+
| Type                                                                                           | Name       | Summary                                 |
+================================================================================================+============+=========================================+
| :ref:`OwcOperation <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_operation>` | Operations | Operations used to invoke the service   |
+------------------------------------------------------------------------------------------------+------------+-----------------------------------------+
| :ref:`OwcContent <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_content>`     | Content    | inline content                          |
+------------------------------------------------------------------------------------------------+------------+-----------------------------------------+

