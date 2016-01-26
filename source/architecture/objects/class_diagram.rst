.. uml::
   :align: center

   !define DIAG_NAME Business Objects

   !include includes/skins.iuml

   skinparam backgroundColor #FFFFFF
   skinparam componentStyle uml2

   set namespaceSeparator ::

   !include source/classes/class_terradue_1_1_portal_1_1_entity.iuml
   !include source/classes/class_terradue_1_1_portal_1_1_feature.iuml
   !include source/classes/class_terradue_1_1_portal_1_1_group.iuml
   !include source/classes/class_terradue_1_1_portal_1_1_series.iuml
   !include source/classes/class_terradue_1_1_portal_1_1_service.iuml
   !include source/classes/class_terradue_1_1_portal_1_1_user.iuml
   !include source/classes/class_terradue_1_1_portal_1_1_wps_process_offering.iuml
   !include source/classes/class_terradue_1_1_portal_1_1_wps_provider.iuml

   !include source/classes/class_terradue_1_1_tep_1_1_account.iuml
   !include source/classes/class_terradue_1_1_tep_1_1_collection.iuml
   !include source/classes/class_terradue_1_1_tep_1_1_data_package.iuml
   !include source/classes/class_terradue_1_1_tep_1_1_group_tep.iuml
   !include source/classes/class_terradue_1_1_tep_1_1_user_tep.iuml
   !include source/classes/class_terradue_1_1_tep_1_1_rates.iuml
   !include source/classes/class_terradue_1_1_tep_1_1_role_tep.iuml
   !include source/classes/class_terradue_1_1_tep_1_1_thematic_application.iuml

   !include source/classes/class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_application.iuml
   !include source/classes/class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_content.iuml
   !include source/classes/class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_creator.iuml
   !include source/classes/class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_display.iuml
   !include source/classes/class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_offering.iuml
   !include source/classes/class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_operation.iuml
   !include source/classes/class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_resource.iuml
   !include source/classes/class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_ows_context.iuml

   !include source/classes/class_relations.iuml

   (GroupTep, UserTep) .. RoleTep
   (DataPackage, Collection) .. Filters

  footer
    DIAG_NAME
    endfooter