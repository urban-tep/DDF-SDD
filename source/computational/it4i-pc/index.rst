.. _it4ipc_components_list :

IT4I Processing Center Computational Components
===============================================

The Urban TEP subsystem of the IT4I processing centre consists of several functional components and interfaces that are described in this section of the design document. The following figure shows the components used by the IT4I processing centre to support processes of the Urban TEP platform.

.. figure:: img/design_components.png
   :align: center

   *IT4I processing centre with Anselm and Salomon clusters, other shared components, and Urban TEP-specific components*

Before describing the components the main functions with their initiation and workflows may help to understand the role of each of the elements. These main functions are:

 * To provide processing offerings, which involves
     - the *Geoserver* that publishes supported processing services via the GetCapabilities and DescribeProcess WPS functions,
     - the configured datasets and processors in the *Service Processor Repository* deployed to the Processing Infrastructure as *Supported Service Processors* on the selected HPC cluster,
     - and their configuration managed by the *HPCaaS Service Management Module*.
 * To receive and handle processing requests, which involves
     - the *Geoserver* that provides the Execute and GetStatus WPS functions,
     - the modules of *HPCaaS Middleware* to manage the proper job deployment and execution on the processing infrastructure,
     - the "Supported Service Processor" stored in the *Shared Data Storage* of the selected HPC cluster used for processing,
     - the input EO data available in the *Shared Data Storage* of the selected HPC cluster,
     - the storage of intermediates and outputs in the *Shared Data Storage* of the selected HPC cluster,
     - the staging of results through the *SCP/GridFTP* interface,
     - the *HPCaaS HPC Data Storage Access Framework* to provide access to the staged results via SCP/GridFTP,
     - the *HPCaaS Service Management Module* with the help of the *Service Configuration Tool* and *Geoserver* for catalogue entry generation.
 * To ingest input data
     - the *IT4I Service Support Operator* to monitor ingestion,
     - the *Data Mirroring / Caching Tool* on the *Salomon Login Nodes* for configuration and systematic or one-time ingestion of data from external data providers using their interfaces.
 * To upload reference data
     - the *HPCaaS Middleware* and its *HPC Data Storage Access Framework* with a WCF REST-ful interface for reference data upload,
     - the *Shared Data Storage* of the selected HPC cluster for storage of the reference data in a user-specific space.
 * To upload processor bundles
     - the *IT4I Helpdesk* with a HTTPS interface to receive a request to deploy a processor bundle,
     - the *Service Processor Repository* with a SFTP/SCP interface for the processor bundle upload,
     - the *IT4I Service Support Operator* to validate and deploy the uploaded processor bundle to the selected HPC cluster and to the *HPCaaS Service Management Module* using the HPCaaS Administration interface to be used by the specific user/group,
     - the *Shared Data Storage* of the selected HPC cluster for storage of the processor bundle in a user-specific space,
     - optionally the *IT4I Service Support Operator* to release the use of the uploaded processor, or the publication of the processor to be used by other users via the *HPCaaS Service Management Module* using the HPCaaS Administration interface.
 * To report on resource usage
     - the *HPCaaS Resource Allocation Reporting Module* to generate the report for Urban TEP,
     - the *IT4I Service Support Operator* to verify and release the report.

Individual packages and their components are described in more detail in the following subsections.

.. toctree::
   :maxdepth: 1
   
   WPS Provider <wps_provider>
   HPC as a Service (HPCaaS) <hpc_as_a_service>
	 Processing Infrastructure <processing_infrastructure>
   Service Support <service_support>

