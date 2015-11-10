.. _class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_operation:

Terradue::ServiceModel::Ogc::OwsModel::OwcOperation
---------------------------------------------------

Definition of the operation either to get the information or to get the capabilities. Note that service specific extension requirements may mandate more than one owc:operation. 


.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/classes/class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_operation.iuml



Properties
^^^^^^^^^^

.. cssclass:: propertiestable

+--------------------------------------------------------------------------------------------+------------+---------------------------------+
| Type                                                                                       | Name       | Summary                         |
+============================================================================================+============+=================================+
| Uri                                                                                        | RequestURL | Service Request URL             |
+--------------------------------------------------------------------------------------------+------------+---------------------------------+
| :ref:`OwcContent <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_content>` | Request    | Optional request body content   |
+--------------------------------------------------------------------------------------------+------------+---------------------------------+

