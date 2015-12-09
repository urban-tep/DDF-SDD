.. _dlrpc_part1 :

DLR TEP Urban Operating
=======================

.. req:: TS-FUN-750
  :show:

  (Custom algorithm upload support) TEP Urban Processing Centre Operating provides support for the integration of user-provided processors on request via the Portal Issue Tracking system.

.. req:: TS-FUN-760
  :show:

  (Issue tracking) Urban TEP Processing Centre Operating regularily handles issues assigned to the DLR processing centre in the Portal Issue Tracking system.

.. req:: TS-FUN-620
  :show:

  (Data ingestion monitoring) Operating initiates and monitors ingestion of systematic or on demand datasets from data providers via their interfaces.

.. req:: TS-FUN-630
  :show:

  (Dataset exchange) Operating performs the exchange of datasets and processors with the other Processing Centres


.. req:: TS-FUN-670
  :show:

  (Processing) Operating monitors processing jobs.

.. req:: TS-FUN-680
  :show:

  (Deployment) Operating maintains the versions of Urban TEP thematic processors and verfies they are deployable to the Geofarm and/or DLR Calvalus Cluster. 

.. req:: TS-FUN-690
  :show:

  (Processing result provision) Operating performs cleanup of results stored at Online Data Access/FTP for a certain time. Operating is also involved in the process of releasing a dataset as permanent (like an input or a reference dataset).

.. req:: TS-FUN-710
  :show:

  (Processing statistics) Operating initiates and verifies the generated reports.

.. req:: TS-FUN-720
  :show:

  (Reference data upload) Operating supports reference data ingestion if the data is provided by FTP/SCP/HTTP.

.. req:: TS-FUN-740
  :show:

  (Software upload) Operating verifies user-provided thematic processors and deploys them for public (other TEP Urban users)  or private use.

.. req:: TS-RES-630
  :show:

  (Subsystem configuration) Operating maintains the Urban TEP processors and processor versions, system configurations for queue resources, online data access space, and systematic workflows.
.. req:: TS-ICD-240
  :show:

  (Email Interface) Operating has a dedicated email account TBD .

.. req:: TS-ICD-350
  :show:

  (Resource utilization reporting interface) Operating initiates and verifies accounting reports.

.. req:: TS-ICD-090
  :show:

  The operator monitors - and initiates for bulk processing - the generation of catalogue entries for new EO Datasets.
       
.. req:: TS-ICD-140
  :show: 

  (Issue Tracking)  TEP Urban Processing Centre Operating regularily handles issues assigned to the DLR processing centre in the Portal Issue Tracking system. 
  
  .. req:: TS-FUN-610
  :show:

  (EO Data ingestion) Monitor and develop systematic and ondemand ingestion system from the ESA Sentinel data hub and ESA, Google and USGS for Landsat. 

.. req:: TS-ICD-080
  :show:

  Operation maintains scripts to generate accounting reports, verify them and transder reports to the Reporting component of the Portal. 



Personnel
----------

The DLR TEP Urban processing centre will be managed by an operator with some Urban TEP-specific activities. 

 * An email account serves as communication endpoint.
 * The DLR processing centre monitors an account in the TEP Urban portal issue tracking system.

Information persistence
-----------------------

Operators exchange information that is kept persistent:

 * The issue tracking keeps track of all communication activities regarding the DLR processing centre. 
 * The record of emails keeps track of bilateral communication.

Service and functions
---------------------

Activities of the Operator comprise:

 * monitoring and configuration of systematic or one-time ingestion of data from external data providers using their interfaces
 * communication with data providers, configuration for new ingestion sources (new datasets, different extent, different time interval)
 * monitoring of processing and delivery
 * analysis of failures in production flow 
 * support of users in questions partaining to the DLR Processing center 
 * support vetted users in adapting their processors to DLR Processing center standards 
 * communication with the Portal Operating and with Operating of the other processing centres, exchange of datasets and processors
 * generating and verification of usage reports

Interfaces and interface items
------------------------------

The external interfaces provided or used by Operating are:

 * Operating provides an email interface
 * Operating uses the issue tracking interface of the Portal
 * Operating uses the online data access interfaces of the BC Processing center to exchange processors and/or replicate EO Data

The internal interfaces within the DLR processing centre used by Operating are:

 * Registering and maintaing necessary production users in DLR Infrastructure 
 * Control and Monitor production systems and all components
 * Shell access to all relevant machines in the DLR Geofarm and DLR Calvalus
 * Access to internal Dockerhub to version and deploy thematic processors
 * Rights management on all TEP Urban relevant storage

