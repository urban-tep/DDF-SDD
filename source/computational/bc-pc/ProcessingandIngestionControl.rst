.. _bcpc_part1 :

BC Processing and ingestion control
===================================

Implementation software and configuration
-----------------------------------------

State representation and persistent data
----------------------------------------

Computational service and functions
-----------------------------------

Interfaces and interface items
------------------------------

...

Requirements
------------

.. req:: TS-FUN-610 Data ingestion
  :show:

  The Urban TEP Processing and Ingestion Control shall systematically harvest data from ESA Sentinel data hub, Landsat archives (ESA, Google, USGS) and MERIS archive (BC).

.. req:: TS-FUN-620 Data ingestion monitoring
  :show:

  The Urban TEP Processing and Ingestion Control shall provide the status of data ingestion to the Catalogue Entry Interface.

.. req:: TS-FUN-690 Processing result provision
  :show:

  The Processing Request Gateway/WPS or the Online Data Access/FTP shall provide the processing result to the users and the portal for online access. 

.. req:: TS-FUN-700 Catalogue entry
  :show:

  The Processing Request Gateway/WPS shall send the metadata of the resulting product(s) to the catalogue entry interface.

.. req:: TS-FUN-710 Processing statistics
  :show:

  The Urban TEP Processing and Ingestion Control shall maintain a list of processing jobs performed with information on users and used resources, such as CPU hours, input data size, and storage capacity. This component shall report this information to the Reporting Interface of the portal.

.. req:: TS-RES-630 Subsystem configuration
  :show:

  The Urban TEP Config and Processor Repo shall store all processors and processor versions used for Urban TEP in this Processing Centre as well as all system configurations, like user, queue resources, online data access quotas, and systematic workflows.

.. req:: TS-ICD-350 Resource utilization reporting interface
  :show:

  The processing centre shall send resource utilization reports to the Urban TEP Portal centralized APEL accounting interface.

.. req:: TS-ICD-080 Accounting collection API	
  :show:

  Urban TEP portal shall expose an accounting interface based on APEL technology to record usage of the internal or third party resource provid-ers.

.. req:: TS-ICD-090 OGC Web Services Context Document (OWS Context)
  :show:

  TEP Urban system shall exchange metadata internally and with remote third party systems using the OWS Context conceptual model in its extent.
  This specification shall be applicable to:
  - Dataset / Product / Series / Collection / Data Packages
  - Services (WPS)
  - Job 
  The system shall support the following mime-type for the representation at interface level:
  - ATOM (RFC4287)
  - GeoJson
  - KML	 
  The OGC OWS Context conceptual model is described in [OGC-12-80r2] and is fully specified for ATOM encoding in [OGC-12-84r2]. 
  In annex A, there is a catalogue entry example that is OWS context compliant document describing 1 entry with many options.
 	 	 
