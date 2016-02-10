.. _it4ipc_hpc_as_a_service :

IT4I HPC as a Service
=====================
The *HPC as a Service Middleware* is an IT4I in-house developed solution designed to simplify the access to HPC resources for internal and external applications. This solution unifies access to different HPC systems in the *IT4I Processing Infrastructure* through a simple object-oriented client-server interface using WCF services. It also ensures all necessary supporting functions like service management, job management, monitoring and reporting, user authentication and authorization, request/result data transfer and encryption and various notification mechanisms. It is therefore the main control component of the IT4I processing centre and integrates most of its processing workflow and configuration functionalities.

.. req:: TS-FUN-710
  :show:

  The *HPC as a Service Middleware* and its modules will maintain the list of processing jobs at the IT4I processing centre.

The *HPC as a Service Middleware* is a web-based .NET application that will be deployed on one virtual server in the IT4I virtualisation infrastructure. It will provide a REST-ful WCF service interface for processing all requests from the *GeoServer* and possibly from the *Urban TEP Portal* for non-WPS auxiliary services, and HTTPS administration interface for *IT4I Service Support Operators*. All workflow management and configuration data will be stored in a RDBMS that will be deployed on the same server.

The *HPC as a Service Middleware* defines several modules that cover different concerns of the solution and the most important modules for the Urban TEP platform will be described in the following subsections. These modules are already mostly implemented but will need customisation for the specific Urban TEP project requirements during Phase 2 of the project.


Service management module
-------------------------
The *Service Management Module* manages information and configuration of all processing services supported on the IT4I processing centre. Its main goal is to properly configure the processing jobs that will be submitted to the IT4I clusters based on user inputs and service configuration. It also ensures that service configurations are synchronised with the *WPS Provider* using the *Service Configuration Tool*. All service configurations are stored in the database and administered using the HTTPS administration interface of the *HPC as a Service Middleware*.

.. req:: TS-FUN-680
  :show:

  The *Service Management Module* will manage and synchronise configuration of all supported services at the IT4I processing centre.

.. req:: TS-FUN-700
  :show:

  The *Service Management Module* will generate a metadata record and submit it to the *Service Configuration Tool* that will submit it to the catalogue at the IT4I processing centre and subsequently generates a metadata record and submits it to the Urban TEP catalogue.


Processing job management module
--------------------------------
The *Job Management Module* contains functionality for managing processing jobs sent from the *Urban TEP Portal* on each supported HPC cluster in the IT4I processing infrastructure. This management contains submitting new jobs onto a specific cluster, cancelling a running or queued job on the cluster and getting actual information about individual user's jobs submitted to any managed cluster. Users have to be authenticated through the *User and Quota Management Module* before they can manage their jobs on the cluster. Information about all submitted jobs is stored in the database for monitoring and reporting purposes.

.. req:: TS-FUN-680
  :show:

  The *Processing Job Management Module* will submit jobs to execute any of the supported service processors at the IT4I processing centre.


User and quota management module
--------------------------------
The *User and Quota Management Module* is used for managing users that will be submitting jobs to supported clusters. The first part of this module is the administration part that manages the user database and their quotas for cluster usage. The second part is the authentication and authorisation part that checks access of all requests to the *HPC as a Service Middleware*, provides actual usage and quota information and provides the number of available resources that the user can use for processing.

This module allows flexible approach to user management between the Urban TEP Portal and the IT4I processing centre. It fully supports the currently planned approach of authentication and authorisation by the portal, but it can also support basic synchronisation of user databases between the portal and the HPC as a Service to further enhance the security, access control and quota management with finer granularity at the IT4I processing centre.

.. req:: TS-RES-630
  :show:

  The *User and Quota Management Module* will manage all user and access quotas at the IT4I processing centre.

.. req:: TS-SEC-610
  :show:

  The *User and Quota Management Module* will authenticate user request from the portal and authorise their access to supported processing services at the IT4I processing centre.


Package deployment manager
--------------------------
The *Package Deployment Manager* manages deployment of the user developed processors that have been packaged by the supported packaging tools and registered to the Portal. It takes the package sent by the user through the Portal, uploads it into the *IT4I Processing Infrastructure* with the help of the *HPC Data Storage Access Framework*, deploys it to the *Supported Service Processors* on the supported HPC clusters in the infrastructure using the *HPC Connection Framework* and registers it as a new service through the *Service Management Module*. This procedure ensures that processing with the packaged processor will be available as a WPS service in the IT4I Processing centre accessible from the Portal.

.. req:: TS-FUN-740
  :show:

  The *Package Deployment Manager* will support upload and deployment of user developed algorithms to the IT4I processing centre.

.. req:: TS-FUN-750
  :show:

  The *Package Deployment Manager* will support upload and deployment of user developed algorithms to the IT4I processing centre.


Resource allocation reporting module
------------------------------------
The *Resource Allocation Reporting Module* provides reporting functionality for cluster usage for individual users and projects. These usage reports can then be used for accounting and will contain information about corehours and type of computing resources used. These reports can be created individually for each user or each project. The *Resource Allocation Reporting Module* will also send the reports to the APEL reporting interface provided by the *Urban TEP Portal*.

.. req:: TS-FUN-710
  :show:

  The *Resource Allocation Reporting Module* will report resource allocation for submitted processing jobs to the portal at the IT4I processing centre.

.. req:: TS-ICD-260
  :show:

  The *Resource Allocation Reporting Module* will report resource allocation for submitted processing jobs at the IT4I processing centre to the APEL accounting interface.


HPC connection framework
------------------------
The *HPC Connection Framework* provides unified access to all supported IT4I clusters, takes into account specific connection requirements and protocols for each HPC cluster and ensures proper translation of service and processing job configurations to the selected cluster operating and scheduling system. This framework therefore encapsulates all communication between the *HPC as a Service Middleware* and IT4I HPC clusters, except for the file transfer that is managed by the *HPC Data Storage Access Framework*.

The *HPC Connection Framework* currently supports SSH connection to both *Anselm HPC* and *Salomon HPC* clusters along with Windows HPC API connection to internal Windows HPC clusters. The framework also houses the functionality to provide information about the total and currently available resources for each supported cluster.

.. req:: TS-RES-630
  :show:

  The *HPC Connection Framework* will manage and monitor all resources and queues for HPC clusters at the IT4I processing centre.


Virtual machine management framework
------------------------------------
The *Virtual Machine Management Framework* manages the whole life cycle and access to virtual machines (VMs), which serve as experimental development environments (Sandboxes) for Urban TEP users that want to create their own processors and register them in the Urban TEP platform (see :ref:`it4ipc_sandbox_vm`). The *Virtual Machine Management Framework* will ensure proper hosting of these VMs in the shared Salomon supercomputer infrastructure for well-known users and provide connection information and access credentials to the hosted machines, or provide them as VM images for download by the users to work on locally.

Each properly certified well-known user will have access to his own VM that will contain his data (in a specific folder) from previous Sandbox VM instances that were hosted on the IT4I infrastructure. More information about VM provisioning can be found in :ref:`develenv_processor_development_environment`.

.. req:: TS-FUN-750
  :show:

  The *Virtual Machine Management Framework* will support development of custom algorithms by providing and hosting VMs with experimental development environment.

.. req:: TS-ICD-270
  :show:

  The *Virtual Machine Management Framework* will provide connection information and access credentials to the VMs with experimental development environment.


HPC data storage access framework
---------------------------------
The *HPC Data Storage Access Framework* provides functions that ensure transferring files from the *Urban TEP Portal* or other Urban TEP processing centres to the user specific session on the HPC cluster that will be used to execute a processing service. The communication with the *Urban TEP Portal* includes sending input files of the job to the cluster, synchronizing changes in important files during the execution of the job on the cluster, sending all results from the cluster to the portal after the job finishes and possibly deleting files from the cluster to clean the user's session. When exchanging data with other processing centres, the *HPC Data Storage Access Framework* either sends proper data to the other processing centre or downloads necessary input data hosted on a different processing centre and caches them on the selected HPC cluster using, possibly deleting them after the processing is finished.

.. req:: TS-FUN-690
  :show:

  The *HPC Data Storage Access Framework* will provide the processing results to the portal at the IT4I processing centre.

.. req:: TS-FUN-720
  :show:

  The *HPC Data Storage Access Framework* will enable to upload reference data for validation purposes through the REST-ful WCF service interface at the IT4I processing centre.

.. req:: TS-ICD-220
  :show:

  The *HPC Data Storage Access Framework* will provide the connection to SCP/GridFTP interface for accessing processing results to the portal at the IT4I processing centre.


To avoid transferring big amounts of data through the *HPC as a Service Middleware* and overloading the server and network connection with unnecessary data transfer, the *HPC Data Storage Access Framework* is able to open a temporary authenticated connection with limited access directly to the *Shared Data Storage* of the selected HPC cluster and provide this connection to the client that wants to transfer the data, be it the *Urban TEP Portal* or other Urban TEP processing centre. In this way, it is possible to transfer big amounts of data directly to the cluster where the *HPC as a Service Middleware* only controls the connection. After the connection is used, it is automatically closed by the middleware.

.. req:: TS-FUN-630
  :show:

  The *HPC Data Storage Access Framework* will ensure the download of necessary datasets from other processing centres to the IT4I processing centre and will provide connection to the SCP and GridFTP interface of the *Shared Data Storage* that other processing centres can use to download the datasets they need from the IT4I processing centre.

.. req:: TS-ICD-250
  :show:

  The *HPC Data Storage Access Framework* will ensure the exchange interface with other processing centres by providing connection information to the direct SCP and GridFTP interface of the *Shared Data Storage*.


The *HPC Data Storage Access Framework* currently supports SCP transfer to *Anselm HPC* and *Salomon HPC* clusters along with network share/Samba interface for internal Windows HPC clusters. Connection functionalities to other Urban TEP processing centres will be added to the framework during Phase 2 of the project based on their specific interfaces.
