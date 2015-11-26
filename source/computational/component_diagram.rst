.. uml::

   !include includes/skins.iuml

   skinparam backgroundColor #FFFFFF
   skinparam componentStyle uml2

  skinparam interface {
      backgroundColor<<UI>> Green
      borderColor<<UI>> DarkGreen
      backgroundColor<<email>> Green
      borderColor<<email>> DarkGreen
      backgroundColor<<OGC OpenSearch>> Blue
      borderColor<<OGC OpenSearch>> DarkBlue
      backgroundColor<<OGC WPS>> Blue
      borderColor<<OGC WPS>> DarkBlue
      backgroundColor<<reporting>> Yellow
      borderColor<<reporting>> DarkYellow
      backgroundColor<<APEL>> Yellow
      borderColor<<APEL>> DarkYellow
      backgroundColor<<ODATA>> Blue
      borderColor<<ODATA>> DarkBlue
      backgroundColor<<http/ftp>> Blue
      borderColor<<http/ftp>> DarkBlue
      backgroundColor<<http>> Blue
      borderColor<<http>> DarkBlue
      backgroundColor<<ftp>> Blue
      borderColor<<ftp>> DarkBlue
      backgroundColor<<OGC WPS internal>> Red
      borderColor<<OGC WPS internal>> DarkRed
      backgroundColor<<http/ftp internal>> Red
      borderColor<<http/ftp internal>> DarkRed
  }

  package "Urban TEP" {
    node "Catalogue" {
      interface "Dataset Search" as OS1 <<OGC OpenSearch>>
    }

    node "Portal" {
      interface "Web UI" as WEBUI <<UI>>
      interface "Dataset search proxy" as OS2 <<OGC OpenSearch>>
      interface "Service Search" as OSS <<OGC OpenSearch>>
      interface "Processs Request proxy" as WPS2 <<OGC WPS>>
      interface "accounting report" as ACR <<reporting>>
      interface "accounting" as AC <<APEL>>
      interface "support" as SUP <<email>>
      database "Tep database" as TEPDB
    }

    node "Processing Centers" {
      node "Services" { 
        interface "Processor result access" as PRA <<http/ftp internal>>
        interface "Process Request" as WPS1 <<OGC WPS internal>>
        interface "Processor Deployment" as PD1 <<http/ftp>>
      }
    }

  }

  node "N" <<Data Provider>> {
    interface "Dataset Search" as DI <<http>>
    interface "Dataset download" as DPD <<http/ftp>>
  }

  package "Urban TEP" {

    node "Portal" {
      WEBUI -down- OSS
      WEBUI -down- OS2
      WEBUI -down- WPS2
      WEBUI -down- ACR
      WEBUI -down- [Ticket System]
      [Dataset Series] -down-( OS1 : find series
      [Dataset Series] -up- OS2 : expose series
      [Services] -up- WPS2 : handle request
      [Services] -up- OSS : expose services
      [Services] --( WPS1 : find service
      [Services] --( WPS1 : submit request
      [Services] -right- TEPDB 
      [Dataset Series] -right- TEPDB
      database "accounting" as ACC
      ACC -down- AC : store usage
      ACC -up- ACR : produce report
      [Ticket System] -up- SUP

    }

    node "Catalogue" {
      [Search Engine] -right- OS1 
      [Search Engine] -down- [Dataset Indices]
      database "Dataset Indices"
      [Dataset Indices] -right- [Data Agent] : manage dataset with data policies
      [Data Agent] -down-( DI : harvest metadata
      
      [Data Agent] -( PRA : stream / copy
    }

    node "Processing Centers" {

      node "Services" { 
        [Apel Client] as APELClient
        APELClient -up-( AC : record usage
        [WPS Server] as PCWPS
        PCWPS -up- WPS1
      }

      cloud "ICT resources" {
        [Processor]
        Processor -up- PD1 : deploys
        Processor -left-( OS1 : resolve dataset reference
        
        database "Storage" as PCS
        Processor -- PCS : download data for processing
        PRA -- PCS : access results
        [PCS] --( DPD : stream / copy

      }

      PCWPS -left- Processor : submits processing

      
    }


      note top of OS1 : Atom, OWS, GeoJson...
  }






  @enduml
