.. uml::
  :caption: Data Agency component diagram
  :align: center


  !include includes/skins.iuml

  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2

  !include source/groups/group___open_search.iuml
  interface "Data Gateway API" as datagatewayAPI

  folder "Data Agency" [[../architecture/dataagency/index.html]] {

      !include source/architecture/dataagency/datagateway.iuml

      

    folder "Catalogue" [[../architecture/catalogue/index.html]] {

      !include source/groups/group___geosquare.iuml

      !include source/architecture/dataagency/elasticsearch.iuml
    }

     group___elastic_cas -- group___geosquare_a_p_i : expose
     group___elastic_cas -- elasticsearch
     group___elastic_cas -- group___open_search 

     datagateway -up-( group___open_search : query
     datagateway -up-( datagatewayAPI : cache/stream/redirect
     datagateway --( group___geosquare_a_p_i : locate
  }



  
  

