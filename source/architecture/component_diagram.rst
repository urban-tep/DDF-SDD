.. uml::
  :width: 16cm
  :caption: General overview component diagram

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
      backgroundColor<<accounting>> Yellow
      borderColor<<accounting>> DarkYellow
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

    interface "redmine" <<http>>
    interface "support" as SUP <<email>>
    

    node "Data Agency" {
      interface "Dataset Search" as OS1 <<OGC OpenSearch>>
      interface "Dataset ingestion" as gsapi <<OGC OpenSearch>>
    }

    node PUMA {
      interface "Web UI" as PUMAWEBUI <<UI>>
      interface "GeoServer API" as PUMAGeoServerAPI <<http>>
      interface "WMS" as PUMAWMS <<http>>
    }

    node "Portal" {
      interface "Web UI" as WEBUI <<UI>>
      interface "Dataset search proxy" as OS2 <<OGC OpenSearch>>
      interface "Service Search" as OSS <<OGC OpenSearch>>
      interface "Processs Request proxy" as WPS2 <<OGC WPS>>
      interface "Portal mgmt" as T2API <<http>>
      database "Tep database" as TEPDB
    }

    node "Accounting" {
      interface "accounting report" as ACR <<reporting>>
      interface "accounting" as AC <<accounting>>
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

    node PUMA {
      [GeoNode] as PUMAGeoNode
      [GeoServer] as PUMAGeoServer
      database "PUMA" as PUMADB
      PUMAGeoServer -- PUMAWMS
      PUMAGeoServer -- PUMAGeoServerAPI
      PUMAGeoNode -- PUMAWMS
      PUMAWEBUI --( PUMAWMS
      PUMAWEBUI -- PUMADB
      PUMAGeoServer -- PUMADB
      PUMAGeoNode -- PUMADB
    }

    node "Portal" {
      WEBUI -down-( OSS
      WEBUI -down-( OS2
      WEBUI -down-( WPS2
      WEBUI -down-( T2API
      WEBUI --( redmine
      WEBUI --( PUMAWMS
      [Web Server] -down-( OS1 : find series
      [Web Server] -up- OS2 : expose series
      [Web Server] -up- WPS2 : handle request
      [Web Server] -up- OSS : expose services
      [Web Server] -up- T2API : expose
      [Web Server] --( WPS1 : find service
      [Web Server] --( WPS1 : submit request
      [Web Server] -right- TEPDB
      [Web Server] --( PUMAGeoServerAPI : publishes results
      [Web Server] --( PUMAWEBUI : redirects
      [Web Server] -right- ACR
      [Web Server] -down-( gsapi : register dataset
    }

    node "Accounting" {
      database "accounting" as ACC
      ACC -down- AC : store usage
      ACC -up- ACR : produce report
    }

    node "Data Agency" {
      [Catalogue] -right- OS1 
      [Catalogue] -down- [Dataset Indices]
      database "Dataset Indices"
      [Dataset Indices] -right- [Data Gateway] : manage dataset with data policies
      [Data Gateway] -down-( DI : harvest metadata
      [Data Gateway] -down-( PRA : stream / copy
    }

    node "Processing Centers" {

      node "Services" { 
        [Accounting reporter] as AccClient
        AccClient -up-( AC : record usage
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
        PCS -up-( gsapi : registers dataset

      }

      PCWPS -left- Processor : submits processing

      
    }

    redmine -up- SUP
  }






  @enduml
