.. uml::

   !define DIAG_NAME Component Diagram

   !include includes/skins.iuml

   skinparam backgroundColor #FFFFFF
   skinparam componentStyle uml2

   !include source/groups/group___core.iuml
   !include source/groups/group___community.iuml
   !include source/groups/group___cloud.iuml
   !include source/groups/group___security.iuml
   !include source/groups/group___open_search.iuml
   !include source/groups/group___model.iuml
   !include source/groups/group___tep.iuml

   !include source/groups/group___auth___umsso.iuml
   !include source/groups/group___authentication.iuml
   !include source/groups/group___authorisation.iuml
   !include source/groups/group___context.iuml
   
   !include source/groups/group___cloud_appliance.iuml
   !include source/groups/group___cloud_provider.iuml
   !include source/groups/group___virtual_machine_template.iuml
   !include source/groups/group___one_cloud_appliance.iuml
   !include source/groups/group___one_cloud_provider.iuml
   !include source/groups/group___one_v_m_template.iuml
   !include source/groups/group___cloud_wps_factory.iuml
   !include source/groups/group___data_package.iuml
   !include source/groups/group___one_client.iuml
   !include source/groups/group___open_nebula_x_m_l_r_p_c.iuml
   !include source/groups/group___persistence.iuml
   !include source/groups/group___tep_user.iuml
   
   !include source/groups/group___series.iuml
   !include source/groups/group___service.iuml
   !include source/groups/group___s_q_l_connector.iuml
   !include source/groups/group___web_context.iuml
   !include source/groups/group___w_p_s.iuml
   !include source/groups/group___wps_provider.iuml
   !include source/groups/group___wps_service.iuml

   !include source/groups/group___o_w_s_context_atom_feed.iuml
   !include source/groups/group___o_w_s_context.iuml

   !include source/groups/group___syndication.iuml

   !include source/groups/group___github_profile.iuml
   !include source/groups/group___github_client.iuml
   

   !include source/groups/group___atom.iuml
   !include source/groups/group___open_search_engine.iuml
   !include source/groups/group___open_searchable.iuml

   !include source/groups/group_relations.iuml
   

  footer
    DIAG_NAME
    endfooter