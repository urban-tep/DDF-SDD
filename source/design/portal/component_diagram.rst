.. uml::

  !define DIAG_NAME Component Diagram

  !include includes/skins.iuml

  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2

  !include source/groups/group___r_w_p_s.iuml
  !include source/groups/group___open_search.iuml
  !include source/groups/group___s_q_l_connector.iuml
  !include source/groups/group___apel_reporting.iuml
  !include source/groups/group___geo_server_a_p_i.iuml
  !include source/groups/group___geo_node_a_p_i.iuml
  

  folder "Portal" [[../computational/portal/index.html]] {
    !include source/groups/group___t2_a_p_i.iuml
    folder "Urban Site" {
    
    }
    folder "Web Services" {
    
    }
    folder "Core" {

    }
    folder "Security" {

    } 
    folder "Tep Modules" {
    
    }
  }

  !include source/groups/group___urban_site.iuml
  !include source/groups/group___web_services.iuml
  !include source/groups/group___tep.iuml
  !include source/groups/group___security.iuml
  !include source/groups/group___core.iuml

  [group___auth___umsso]  --  [group___authentication] : implements
  [group___authentication]  ..>  [group___persistence] : []
  [group___authorisation]  ..>  [group___persistence] : []
  [group___authorisation]  ..>  [group___context] : uses
  [group___catalogue_editor]  --(  [group___t2_a_p_i] : connects
  [group___context]  ..>  [group___persistence] : []
  [group___context]  ..>  [group___authentication] : []
  [group___core_w_p_s]  ..>  [group___persistence] : []
  [group___core_w_p_s]  ..>  [group___authorisation] : []
  [group___core_w_p_s]  --(  [group___r_w_p_s] : connects
  [group___geo_browser]  --(  [group___t2_a_p_i] : connects
  [group___persistence]  --(  [group___s_q_l_connector] : connects
  [group___r_e_s_t]  ..>  [group___tep_accounting] : CRUD
  [group___r_e_s_t]  ..>  [group___tep_application] : CRUD
  [group___r_e_s_t]  ..>  [group___tep_community] : CRUD
  [group___r_e_s_t]  ..>  [group___tep_contents] : CRUD
  [group___r_e_s_t]  ..>  [group___tep_data] : CRUD
  [group___r_e_s_t]  ..>  [group___tep_service] : CRUD
  [group___r_e_s_t]  --  [group___t2_a_p_i] : implements
  [group___r_e_s_t]  --  [group___open_search] : implements
  [group___series]  --(  [group___open_search] : connects
  [group___series]  ..>  [group___persistence] : []
  [group___series]  ..>  [group___authorisation] : []
  [group___tep_accounting]  --(  [group___apel_reporting] : connects
  [group___tep_accounting]  ..>  [group___persistence] : []
  [group___tep_application]  ..>  [group___tep_data] : delegates
  [group___tep_application]  ..>  [group___tep_service] : delegates
  [group___tep_community]  ..>  [group___authorisation] : uses
  [group___tep_contents]  ..>  [group___persistence] : []
  [group___tep_data]  ..>  [group___authorisation] : uses
  [group___tep_data]  ..>  [group___series] : uses
  [group___tep_data]  --(  [group___geo_server_a_p_i] : connects
  [group___tep_data]  --(  [group___geo_node_a_p_i] : connects
  [group___tep_service]  ..>  [group___core_w_p_s] : uses
  [group___web_pages]  --(  [group___t2_a_p_i] : connects


