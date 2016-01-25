.. _design_data_gateway:

Data Gateway
^^^^^^^^^^^^

General design
""""""""""""""

The Data Gateway is Data as a Service platform of Terradue to resolve the best location and access to the data.
It resolves the best location from the catalogue but also based on rules.


.. req:: TS-FUN-100
  :show:

  The data gateway mechanism is fully described in this section

Partnership Policies
""""""""""""""""""""

The Data Gateway implements 3 methods to access data from data providers:

- remote access either by user redirection or by piping the data request download
- caching the data resource on a custom data storage for a defined retention time
- mirroring the data resource on a custom data storage for an undefined time limit


Rule Based design
"""""""""""""""""

The Data Gateway implements a rule-based mechanism to control data partnership and access policies and scenario. 
The rules conditions are applicable to:
- origin of the data request (IP, user, processing center)
- location of the data as recorded in the catalogue
- data provider of the data
- the authorization applied to that resource at portal level

The rules are combinable.


Data Access Policies enforcement
""""""""""""""""""""""""""""""""

.. req:: TS-FUN-480
  :show:

  Data Access policies enforcement is described in this section

When a user or a third party system contacts the data gateway to fetch data that is under a restricted acccess policy in the context of the TEP,
the component apply a set of rules that allows or not the request.

To illustrate this mechanism, the 2 following figures describes 2 typical cases where such rules apply.

.. uml::
  :caption: Data Gateway - trusted originator access (IP based) sequence diagram

  actor "User" as U
  participant "Portal" as P
  participant "Data Gateway" as DG
  database "Catalogue" as C
  
  autonumber
  
  U -> P : Query authorized Collection with params (AOI, timespan, filters...)
  activate P
  P -> C : Query index of the restricted collection
  activate C
  C -> C : Control the rules (e.g. IP based)
  C -> P : Datasets metadata (atom, geojson...)
  deactivate C
  P -> U : Datasets metadata
  deactivate P
  U -> P : Download dataset
  activate P
  P -> DG : Query dataset download link for user IP
  activate DG
  DG -> DG : Control the rules (e.g. IP based)
  DG -> P : URL to file
  deactivate DG
  P -> U : redirection to url
  deactivate P


.. uml::
  :caption: Data Gateway - temporary access (token based) sequence diagram

  actor "User" as U
  participant "Portal" as P
  participant "Data Gateway" as DG
  participant "WPS Service" as WPS
  database "Catalogue" as C
  
  autonumber
  
  U -> P : submit data package for processing
  activate P
  P -> DG : query token for datapackage
  activate DG
  DG -> DG : Control the rules (e.g. IP based)
  DG -> DG : Generate and save temporary token
  DG -> P : datapackage URL with token
  deactivate DG
  P -> WPS : submit processing (dp URL with token)
  activate WPS
  WPS -> DG : query datapackages files (URL with token)
  activate DG
  DG -> DG : Control the rules (e.g. token based)
  DG -> WPS : datapackages files
  deactivate DG
  WPS -> WPS : execute processing
  WPS -> P : processing complete
  deactivate WPS
  deactivate P


SciHub
""""""

Data Gateway service implements a channel for harvesting and retrieving data from Copernicus Sentinels Scientific Hub (https://scihub.esa.int/).








