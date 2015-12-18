.. _it4ipc_processing_infrastructure :

IT4I Processing Infrastructure
==============================
The *IT4I Processing Infrastructure* contains two Linux-based HPC clusters - *Anselm* and *Salomon* - and a supporting infrastructure for accessing and managing these clusters. The *Salomon HPC cluster* is the more powerful one of the two and will be primarilly used in the platform, with *Anselm HPC cluster* serving as a possible reserve during high utilisation of the *Salomon HPC cluster* or for executing processors accelerated with GPGPUs (as *Salomon* does not contain any GPGPU accelerators). As both these clusters have similar structure, their main components will be described together in the following subsections.


Login Nodes
-----------
Each cluster contains login nodes that are used for accessing the cluster environment and managing jobs. These login nodes serve as a single point for accessing the computational resources on the cluster and executing processing services. They are accessible through the SSH interface and the *HPCaaS HPC Connection Framework* uses this interface to submit processing jobs on the clusters. All processing requests in the Urban TEP platform has to go through the *HPC as a Service Middleware*, so the connections to *Login Nodes* are not provided to the *Urban TEP Portal* or any other part of the platform.

.. req:: TS-ICD-330
  :show:

  The *Login Nodes* will provide the SSH interface for accessing experimental environment by the user at the IT4I processing centre. The connection to this interface will be provided by the *IT4I Service Support Operators* based on the approved request on the *Urban TEP Service Desk* escalated to the *IT4I Helpdesk*.

All login nodes for both *Salomon* and *Anselm* clusters are running the *PBS Pro Scheduler* software, which efficiently distributes workloads across the computing resources on the related HPC cluster. These schedulers are independent, so jobs submitted on the *Salomon* cluster are only scheduled on *Salomon* and not on *Anselm* and vice versa. The *HPCaaS Middleware* therefore needs to know, which cluster is relevant for each processed service and submitted job. The *HPCaaS HPC Connection Framework* then uses the *PBS Pro Scheduler* to queue the processing jobs and monitor their status. By reconfiguring used queues in the *PBS Pro Scheduler* it is possible to dedicate a part of the cluster for executing Urban TEP services or let them compete over resources with other projects. It is also possible to change the configuration of the queues during runtime to react to the demand.

The final Urban TEP related component on the *Login Nodes* is the *Data Mirroring / Caching Tool* that is currently present only on the *Salomon HPC*. This component connects to the external data providers and downloads service related data for long-term mirroring or short-term caching. It is deployed directly on the *Login Nodes* to have direct access to the *Shared Data Storage* on the *Salomon HPC* and store the data directly on the processing environment. This component is currently implemented to mirror LandSat data and will be extended with other data providers during Phase 2 of the Urban TEP project.

.. req:: TS-FUN-610
  :show:

  The *Data Mirroring / Caching Tool* will mirror the LandSat data and mirror or cache Sentinel data and data from other providers on the IT4I processing infrastructure as necessary.

.. req:: TS-FUN-620
  :show:

  The *Data Mirroring / Caching Tool* will provide the status of data ingestion on the IT4I processing infrastructure to the *HPC as a Service Middleware* that will update the service description using the *Service Configuration Tool*.


Shared Data Storages
--------------------
Both clusters contain a *Shared Data Storage* specific for each cluster that is shared between all computing nodes of the specific cluster. This storage is used for the long-term mirrored data, short-term cached data, configuration and processing data of currently submitted jobs and processing results of finished jobs that were not yet downloaded by the *Urban TEP Portal* and deleted from the processing infrastructure.

The *Shared Data Storage* of each cluster is accessible by the SCP and GridFTP interface and access to this interface is managed by the *HPCaaS HPC Data Storage Access Module*, that can open a temporary authenticated connection with limited access and provide it to the client that wants to transfer the data, be it the *Urban TEP Portal* or other Urban TEP processing centre. In this way, the *Urban TEP Portal* can for example download processing results of specific job without transferring the data through the *HPCaaS Middleware*, but it first needs to send an authenticated request to the middleware so that it can open and provide the connection.

.. req:: TS-FUN-630
  :show:

  The *HPCaaS HPC Data Storage Access Module* will ensure the download of necessary datasets from other processing centres and will provide connection to the SCP and GridFTP interface of the *Shared Data Storage* that other processing centres can use to download the datasets they need.

.. req:: TS-RES-610
  :show:

  The *Salomon Shared Data Storage* will store EO data at the IT4I processing centre to be available for processing on the *Salomon HPC Cluster*.

.. req:: TS-RES-620
  :show:

  The *Salomon Shared Data Storage* will store non-EO data at the IT4I processing centre to be available for processing on the *Salomon HPC Cluster*.

.. req:: TS-ICD-320
  :show:

  The *Shared Data Storage* will provide the SCP/GridFTP interface for accessing processing results to the portal at the IT4I processing centre. The connection to this interface will be provided by the *HPCaaS HPC Data Storage Access Module*.

.. req:: TS-ICD-330
  :show:

  The *Shared Data Storage* will provide the SCP interface for uploading development versions of the user-developed processors to the experimental environment at the IT4I processing centre. The connection to this interface will be provided by the *IT4I Service Support Operators* based on the approved request on the *Urban TEP Service Desk* escalated to the *IT4I Helpdesk*.


As the storages are not shared between clusters, when executing processing services on the *Anselm HPC cluster*, the necessary input data have to be transferred from the *Salomon HPC cluster* first.


Supported Service Processors
----------------------------
The *Supported Service Processors* are applications that are responsible for the computations performed in the platform. The processors that will be supported by the IT4I processing centre will be deployed on the *Salomon Shared Data Storage* and possibly *Anselm Shared Data Storage* and will be directly available on the computing resources on these clusters. They will be deployed as basic Linux-based applications and will be able to use all languages, runtime environments, libraries and tools installed on the processing infrastructure.

.. req:: TS-FUN-660
  :show:

  The *Supported Service Processors* will include a processor for subsetting the GUF and GSI input dataset at the IT4I processing centre.

.. req:: TS-FUN-671
  :show:

  The *Supported Service Processors* will include a processor for generating the statistics at the IT4I processing centre.

.. req:: TS-FUN-672
  :show:

  The *Supported Service Processors* will include a processor for generating the binary settlement mask at the IT4I processing centre.

.. req:: TS-FUN-673
  :show:

  The *Supported Service Processors* will include a processor for generating the imperviousness/urban greenness layer at the IT4I processing centre.

.. req:: TS-FUN-674
  :show:

  The *Supported Service Processors* will include a processor for generating the functional urban areas at the IT4I processing centre.



HPC Clusters
------------
The HPC clusters themselves are used for computing by executing processing service processors. The structure of both clusters is similar but with significant differences in the number and power of their computing nodes.

The *Salomon HPC cluster* is currently (November 2015) the top 48th supercomputer in the TOP500 list1 and consists of 1008 computational nodes of which 576 are regular compute nodes and 432 accelerated nodes. Each node is a powerful x86-64 computer, equipped with 24 cores (two twelve-core Intel Xeon E5-2680v3 processors) and 128GB RAM. The accelerated nodes are additionally equipped with Intel Xeon Phi 7120P MIC accelerators. All nodes are interconnected by 7D Enhanced hypercube InfiniBand network. All nodes share 0.5PB NFS disk storage to store the user files and a DDN Lustre shared storage with a capacity of 1.69 PB, which is available for the temporary processing data. The total theoretical peak performance of the Salomon cluster is 2011 Tflop/s.

The *Anselm HPC cluster* consists of 209 computational nodes, of which 180 are regular computing nodes, 23 are GPU Kepler K20 accelerated nodes, 4 are MIC Xeon Phi 5110 accelerated nodes and 2 are fat nodes. Each node is an x86-64 computer, equipped with 16 cores (two eight-core Intel Sandy Bridge E5-2665 or E5-2470 processors), at least 64GB RAM, and local hard drive. The nodes are interlinked by high speed InfiniBand QDR, fully non-blocking, fat-tree network. All nodes share 320TB disk storage to store the user files and 146TB shared storage for temporary processing data. The total theoretical peak performance of the Anselm cluster is 94 Tflop/s.

As GPGPU accelerated nodes are only present on the Anselm HPC cluster, any service processors that are accelerated by GPGPUs have to be executed on the *Anselm HPC cluster*.

.. req:: TS-FUN-670
  :show:

  The *HPC Clusters* will perform the processing of supported services at the IT4I processing centre.

.. req:: TS-FUN-680
  :show:

  The *HPC Clusters* will execute the supported service processors at the IT4I processing centre.

