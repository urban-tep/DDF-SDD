.. uml::

  !define DIAG_NAME Component Diagram

  !include includes/skins.iuml

  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2

  !include source/groups/group___r_w_p_s.iuml
  !include source/groups/group___open_search.iuml
  !include source/groups/group___s_q_l_connector.iuml
  !include source/groups/group___apel_accounting.iuml

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
  !include source/groups/group___apel.iuml
  !include source/groups/group_relations.iuml

  folder "Apel" {
      database "Accounting Storage" as AAS [[accounting/storage.html]]
      group___apel_server -down- AAS
  }

  hide group___elastic_cas
  hide group___geosquare_a_p_i


