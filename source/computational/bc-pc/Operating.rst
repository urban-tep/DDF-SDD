.. _bcpc_part1 :

BC Urban TEP Operating
======================

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

.. req:: TS-FUN-750 Custom algorithm upload support
  :show:

  Urban TEP Processing Centre Operating shall support the implementation of custom algorithms. 

.. req:: TS-FUN-760 Issue tracking
  :show:

  Urban TEP Processing Centre Operating shall make use of the portal Issue Tracker Interface and handle issues addressed to the Processing Centre.

.. req:: TS-FUN-620 Data ingestion monitoring
  :show:

  The Urban TEP Processing and Ingestion Control shall provide the status of data ingestion to the Catalogue Entry Interface.

.. req:: TS-FUN-630 Dataset exchange
  :show:

  The Online Data Access/FTP from one Processing Centre shall exchange datasets from the other Processing Centres. 


.. req:: TS-FUN-670 Processing
  :show:

  The Scheduling and Processing shall perform the requested operation based on the specified configurations.

.. req:: TS-FUN-680 Deployment
  :show:

  Scheduling and Processing shall run Urban TEP processors provided in the Urban TEP Config & Processor Repo triggered by a request from the Processing Request Gateway/WPS. 

.. req:: TS-FUN-690 Processing result provision
  :show:

  The Processing Request Gateway/WPS or the Online Data Access/FTP shall provide the processing result to the users and the portal for online access. 

.. req:: TS-FUN-710 Processing statistics
  :show:

  The Urban TEP Processing and Ingestion Control shall maintain a list of processing jobs performed with information on users and used resources, such as CPU hours, input data size, and storage capacity. This component shall report this information to the Reporting Interface of the portal.

.. req:: TS-FUN-720 Reference data upload
  :show:

  The Processing Request Gateway/WPS may allow users to upload reference data for validation purpose.

.. req:: TS-FUN-740 Software upload
  :show:

  The processing centres shall support the upload of custom processors by well-known users. As baseline the external user sends the agreed algorithm code to the Urban TEP Processing Centre Operating and they validate and make it available for processing in Urban TEP Config and Processor Repo.

.. req:: TS-FUN-770 Processing in external cloud
  :show:

  Urban TEP project shall demonstrate the capability to migrate one of its processing workflows into an external cloud. The result dataset shall be made available in the portal.

.. req:: TS-RES-630 Subsystem configuration
  :show:

  The Urban TEP Config and Processor Repo shall store all processors and processor versions used for Urban TEP in this Processing Centre as well as all system configurations, like user, queue resources, online data access quotas, and systematic workflows.

.. req:: TS-SEC-610 Authentication
  :show:

  Processing Centre User Management shall accept a dedicated portal user for authentication.



.. req:: TS-ICD-240 Email Interface

  The Urban TEP Processing Centre Operating shall expose an email interface to:

.. req:: TS-ICD-250 Processor and Data Exchange Interface

  The Online data access/FTP shall expose an (S)FTP interface to exchange data and processors between processing centres.

.. req:: TS-ICD-350 Resource utilization reporting interface

  The processing centre shall send resource utilization reports to the Urban TEP Portal centralized APEL accounting interface.

.. req:: TS-ICD-080 Accounting collection API	

  Urban TEP portal shall expose an accounting interface based on APEL technology to record usage of the internal or third party resource provid-ers.

.. req:: TS-ICD-090 OGC Web Services Context Document (OWS Context)
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
 	 	 
.. req:: TS-ICD-140 Issue Tracking web widget	

  rban TEP platform geobrowser shall integrate quick helper to submit issues or requests to the operation team. This shall create a new ticket in the support system hosted by Terradue. The follow up of the issue shall be done on this latter third party system.	 
