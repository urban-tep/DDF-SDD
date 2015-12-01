.. _dlrpc_components_list :

DLR Processing Center Computational Components
==============================================
The TEP Urban subsystem of the DLR processing centre consists of several functional components and interfaces.
This gives a quick overview while the they are explained in more detail in their sections

 * to provide processing offerings, which involves
     - the *Processing Gateway* with its WPS functions GetCapabilities and DescribeProcess
     - the configured datasets and thematic processors in *EO Data Storage* 
 * to receive and handle processing requests from the portal , which involves
     - the *Processing Gateway/WPS* with its functions Execute and GetStatus
     - the *Mesos Scheduling and Processing System* to run one or several jobs
     - the supported thematic processors autodeployed to the Cores
     - the input EO data available in *EO Data Storage*
     - the storage of intermediates and outputs in *EO Data Storage*
     - the pushing of results to the *Processing Gateway/WPS* for delivery via HTTPS, FTP or WMS
     - the *Processing Gateway/WPS* to update the catalogue 
  * to ingest input data
     - the *Operator* to monitor on demand and mirroring ingestion
     - the *Operator* for configuration and monitoring of systematic or one-time ingestion of data from external data providers using their interfaces
 * to upload reference data
     - the *Processing Gateway/WPS* with a REST-ful interface for reference data upload
     - the *EO Data Storage* for storage of the reference data in TEP Urban storage space
 * to deploy thematic processors
     - the *Mesos Scheduling and Processing System* to deploy thematic processors to the clusters
      - optionally the *Operator* to verify and deploy thematic processors from ohter processing centers or trusted users to the clusters
 * to report on resource usage
     - the *Mesos Scheduling and Processing System* to generate the APEL report for TEP Urban portal 
     - the *Operator* to verify and release the reports
     - the *Processing Gateway/WPS* to upload the reporst to the portal via APEL


The following figure shows the decomposition into its components and the subsystem-external interfaces. 

.. figure:: dlr_pc.png
   :scale: 100
   :align: center

   *DLR processing centre decomposition with Calvalus cluster, Geofarm cluster, other shared components*


.. toctree::
   :maxdepth: 1
   
   Processing Gateway/WPS <ProcessingGatewayWPS>
   Mesos Scheduling and Processing System <MesosSchedulingandProcessing>
   EO Data Storage <EODataandProcessingStorage>
   Operating <Operating>

