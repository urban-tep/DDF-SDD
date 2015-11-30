.. uml::

  !define DIAG_NAME Catalogue Component Diagram

  !include includes/skins.iuml

  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2

  folder "Catalogue" [[../computational/catalogue//index.html]] {
    folder "Geosquare" {
        [elasticsearch]
    }
    [datagateway]
  }

  !include source/groups/group___geosquare.iuml
  !include source/computational/catalogue/elasticsearch.iuml
  !include source/computational/catalogue/datagateway.iuml

