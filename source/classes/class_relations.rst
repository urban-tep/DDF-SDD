.. _class_relations:

Class Relationships
-------------------



- :ref:`class_terradue_1_1_portal_1_1_wps_process_offering` 



- :ref:`class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_creator` created on :ref:`OwcApplication <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_application>` at the moment the ows document was generated 

- :ref:`class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_creator` displayed on :ref:`OwcDisplay <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_display>` at the moment the ows document was generated 

- :ref:`class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_offering` offers :ref:`OwcOperation <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_operation>` as a list of operations available to invoke the service

- :ref:`class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_offering` offers :ref:`OwcContent <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_content>` as a list of inline contents 

- :ref:`class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_operation` is invoked with :ref:`OwcContent <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_content>` that is the body of the requets to send along with service invokation

- :ref:`class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_resource` exposes :ref:`OwcOffering <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_offering>` as services or inline contents for the resource

- :ref:`class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_ows_context` references :ref:`OwcCreator <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_creator>` as the the tool or application used to create the context document and its properties.

- :ref:`class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_ows_context` contains :ref:`OwcResource <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_resource>` that describe resources and their access parameters and configuration

- :ref:`class_terradue_1_1_tep_1_1_controller_1_1_data_package` The owner.



- :ref:`class_terradue_1_1_tep_1_1_controller_1_1_data_package` The colelctions.



- :ref:`class_terradue_1_1_tep_1_1_controller_1_1_group_tep` The members.



- :ref:`class_terradue_1_1_tep_1_1_controller_1_1_thematic_application` The collections.



- :ref:`class_terradue_1_1_tep_1_1_controller_1_1_thematic_application` The WPS services.



- :ref:`class_terradue_1_1_tep_1_1_controller_1_1_user_tep` 


