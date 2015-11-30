.. _bcpc_part1 :

BC HDFS EO data and processing storage
======================================

Implementation software and configuration
-----------------------------------------

The EO Data and Processing Storage component is based on Apache Hadoop (Calvalus Cluster) and centralized NFS datashare (Geofarm Cluster).
It is deployed on the DLR Calvalus infrastructure with 28 nodes, master node, and I/O node as a distributed hdfs Filesystem and to the 
It can push data to the Processing Gateway/WPS on request (pull request via XMPP and data transfer via http push or ftp push) 

For the TEP Urban 

The configuration specific for Urban TEP comprises:

 * access to certain EO datasets and to certain processor bundles for the group *urbantep*
 * storage area for result sets, reference data, and uploaded processor bundles

State representation and persistent data
----------------------------------------

The persistent data of this component is the Hadoop configuration and the file system content. The configuration of Hadoop is not Urban TEP-specific. The file system structures relevant for Urban TEP are:

 * directory ``/calvalus/eodata/MER_FSG_1P/v2013/`` of the MERIS full resolution geo-corrected input data
 * directory ``/calvalus/eodata/Landsat8/v1/`` of Landsat8 L1 input data
 * directory ``/calvalus/eodata/Sentinel2/v1/`` of Sentinel 2 input data
 * file ``/calvalus/eodata/product-sets.csv`` with the master table of datasets
 * directory ``/calvalus/software/1.0/urban-tep-1.0/`` an Urban TEP-specific processor bundle with index generation processors
 * file ``/calvalus/software/1.0/urban-tep-1.0/bundle-descriptor.xml`` with the description of all processors made available by this bundle and their parameters
 * directory ``/calvalus/software/1.0/...`` with other processor bundles for use in Urban TEP
 * directory ``/calvalus/projects/urban-tep/`` as space for bulk production with the Ingestion and Processing Control component
 * directory ``/calvalus/home/<user>/`` as space for results of on-demand processing
 * directory ``/calvalus/home/<user>/point-data/`` as space for reference data
 * directory ``/calvalus/home/<user>/software/`` as space for user-provided processor bundles

Access to the shared EO data and the processor bundles is granted by corresponding ACLs for the directories. Access to the project and the user directories is granted by group and user ownerships.

The directory structure information is in fact stored in a Hadoop database in the file system of the master. The file contents of the files is in fact organised in blocks stored in Unix file systems on volumes of the nodes.

Computational service and functions
-----------------------------------

The computational service of this component is that of a file system, i.e. the data storage in files, organisation in directories, the provision of access control rules, and the functions of reading files and writing files. The service is provided by two types of processes:

 * a namenode Unix process on the master node serving the file system structure and data organisation
 * the datanode Unix processes on all cluster nodes concurrently serving the file contents

Interfaces and interface items
------------------------------

There are two interfaces of the file system:

 * the HDFS protocol providing direct concurrent access to namenode and datanodes via a set of functions and data streams. There is a Java API to this interface.
 * an NFS protocol provided by a gateway service running on the I/O nodes of the cluster, providing a Posix-compliant interface

In addition there is an operator interface:

 * Web GUI of Hadoop for monitoring
 * command line interface of Hadoop for monitoring and control

Requirements for the design of BC HDFS EO data and processing storage
---------------------------------------------------------------------

.. req:: TS-FUN-610
  :show:

  (Data ingestion) The Urban TEP Processing and Ingestion Control inserts newly retrieved Landsat and Sentinel 2 data into the file system using NFS (systematic ingestion) or HDFS (bulk ingestion). The MERIS dataset has also been ingested this way.

.. req:: TS-FUN-611
  :show:

  (Settlement mask processing input) Urban TEP-specific datasets are stored in the project space /calvalus/projects/urbantep/ of HDFS if needed on Calvalus.

.. req:: TS-FUN-612
  :show:

  (GSI input processing input) Urban TEP-specific datasets are stored in the project space /calvalus/projects/urbantep/ of HDFS if needed on Calvalus.

.. req:: TS-FUN-613
  :show:

  (Population distribution processing input) Urban TEP-specific datasets are stored in the project space /calvalus/projects/urbantep/ of HDFS if needed on Calvalus.

.. req:: TS-FUN-614
  :show:

  (Administrative units processing input) Urban TEP-specific datasets are stored in the project space /calvalus/projects/urbantep/ of HDFS if needed on Calvalus.

.. req:: TS-FUN-615
  :show:

  (Socio-economic statistics processing input) Urban TEP-specific datasets are stored in the project space /calvalus/projects/urbantep/ of HDFS if needed on Calvalus.

.. req:: TS-FUN-660
  :show:

  (Subsetting processor) Subsetting is provided as processor for the Urban TEP input datasets in the urban-tep-1.0 bundle. A function of the Sentinel Toolbox or BEAM is used for it.

.. req:: TS-FUN-710
  :show:

  (Processing statistics) The used storage on HDFS is monitored regularily by Ingestion and Processing Control for the purpose of reporting.

.. req:: TS-RES-610
  :show:

  (Data storage for EO data) EO data is stored on HDFS below directory /calvalus/eodata.

.. req:: TS-RES-620
  :show:

  (Data storage for non-EO data) Urban TEP-specific non-EO data is stored on HDFS below directory /calvalus/projects/urbantep/ .

