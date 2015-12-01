.. _dlrpc_part1 :

DLR EO data and processing storage
==================================

Implementation software and configuration
-----------------------------------------

The EO Data and Processing Storage component is based on Apache Hadoop (Calvalus Cluster) and centralized NFS datashare (Geofarm Cluster). Both systems are interconnected by 10GB link to quickly shift processing depending on available ressources and data storage
It is deployed on the DLR Calvalus infrastructure with 28 nodes, master node, and I/O node as a distributed hdfs Filesystem. The HDFS Filesystem spans the 28 nodes and has a total capacity of 390TB. A flexibel part of this storage is allocated to the TEP Urban depending on demand. 
The DLR Geofarm cloudsystem has a end capacity of 1.9PB attached via Infiniband to the virtual machines. Parts of this storage will be allocated to the TEP Urban conntect according to demand. Furthermore it contains 100TB SAS for intermediate data with high IO demands. 
The EO Data and Processing Storage component can push data to the Processing Gateway/WPS on request (pull request via XMPP and data transfer via http push or ftp push due to security constraints) 


The configuration specific for Urban TEP comprises:

 * access to EO datasets and to certain thematic processors developed for TEP Urban
 * storage space area for result sets, reference data, and user provided thematic processors
 
State representation and persistent data
----------------------------------------

The persistent data of this component is file system content in the tep Urban specific Storage Areas these comprise

 * Storage on the HDFS Filesystem for Input, intermediary and output data for DLR Calvalus Processing
 * Storage on the (tiered) NFS/local Filesystem provided by the DLR Geofarm 
 * storage in the DLR docker registry to manage, version and deploy thematic processors 
   
 Access to the shared EO data is granted by corresponding ACLs for the directories. Access to the project and the user directories is granted by group and user ownerships.


Computational service and functions
-----------------------------------

The computational service of this component is that of a file system, i.e. the data storage in files, organisation in directories, the provision of access control rules, and the functions of reading files and writing files. The service is provided by two types of processes:

 * a namenode Unix process on the master node serving the file system structure and data organisation for the Calvalus system
 * the datanode Unix processes on all cluster nodes concurrently serving the file contents on Calvalus
 * on the geofarm dedicated IO-Machines shares the data via NFS with the Processing Nodes for input data and results. Intermediate data is stored localy.

Interfaces and interface items
------------------------------

There are two interfaces of the Calvalus file system:

 * the HDFS protocol providing direct concurrent access to namenode and datanodes via a set of functions and data streams. There is a Java API to this interface.
 * an NFS protocol provided by a gateway service running on the I/O nodes of the cluster, providing a Posix-compliant interface
 
 The Geofarm filesysem is only accesible via NFS


Requirements for the design of BC HDFS EO data and processing storage
---------------------------------------------------------------------

.. req:: TS-FUN-610
  :show:

  (Data ingestion) The Urban TEP Processing and Ingestion Control inserts newly retrieved Landsat and Sentinel 2 data into the file system.

.. req:: TS-FUN-611
  :show:

  (Settlement mask processing input) Urban TEP-specific datasets are stored in the project storage.

.. req:: TS-FUN-612
  :show:

  (GSI input processing input) Urban TEP-specific datasets are stored in the project data storage.

.. req:: TS-FUN-613
  :show:

  (Population distribution processing input) Urban TEP-specific datasets are stored in the project storage.

.. req:: TS-FUN-614
  :show:

  (Administrative units processing input) Urban TEP-specific datasets are stored in the project storage

.. req:: TS-FUN-615
  :show:

  (Socio-economic statistics processing input) Urban TEP-specific datasets are stored in the project storage.

.. req:: TS-FUN-660
  :show:

  
  (Processing statistics) The used storage on the TEP Urban storage is monitored regularily for the purpose of reporting.

.. req:: TS-RES-610
  :show:

  (Data storage for EO data) EO data is stored on the HDFS below directory /calvalus/eodata/tepUrban and /net/eodata/tepUrban on the Geofarm

.. req:: TS-RES-620
  :show:

  (Data storage for non-EO data) Urban TEP-specific non-EO data is stored on HDFS below directory /calvalus/projects/tepUrban/ and under /net/auxdata/tepUrban on the Geofarm.

