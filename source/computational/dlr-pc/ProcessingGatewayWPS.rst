.. _dlrpc_ProcessingGatewayWPS :

DLR processing gateway/WPS
==========================

Implementation software and configuration
-----------------------------------------

The DLR Processing Gateway and WPS provides a OGC service infrastructure with remote processing capabilities on the DLR Geofarm and DLR Calvalus Cluster 
The main purpose of this instance is to decouple the user-facing services from the actual processes that runs on the secured, intranet hosts and processing infrastructures.

The Portal browses and executes the available list of processes through the OGC WPS interfaces ( GetCapabilities, DescribeProcess, Execute ect). The results can then asynchronosly  be retrieve ‘as is’ in the original format via HTTP(S) download. They can also be accessed through WMS/WCS/WFS services.
The DLR Processing Gateway and WPS is responsible of receiving and caching the process execution requests. It forward them to the Apache Mesos Sheduler and handles the status updates and eventually streama the results to the client or the Portal. If the process generates geospatial data, then the Processing Gateway will also import and publish it through OGC services.
The Process sheduling, monitoring and implementation are run in their own secure host and infrastructure. Together with a “Remote WPS Agent” that runs as a daemon (pull interface), the Gateways requests can trigger the process execution with specific input parameters


State representation and persistent data
----------------------------------------

The Processing Gateway and WPS forwards all requests to the Apache Mesos sheduler. 


Computational service and functions
-----------------------------------

The computational services of the Processing Gateway and WPS comprises implementations of the WPS functions GetCapabilities, DescribeProcess, Execute, and GetStatus. 

 * For GetCapabilities and DescribeProcess it determines all configured processors and datasets accessible by the user (of group *urbantep*) and caches this information for repeated use. The computational service for these functions is the conversion into the WPS-specific structure. 
 * For Execute it submits one or several requests to Apache Mesos according to the workflow used.
 * For GetStatus it presents the status of a processing job  via WPS.
 * For the retrieval of result datasets it stages the data at the Online Data Access and provides HTTP(S) accesses the directories of the staging area.
 * For the upload of reference datasets and processor bundles it inserts the files into a user area of the HDFS EO Data and Processing Storage.

Interfaces and interface items
------------------------------

The external interfaces provided by the Processing Gateway/WPS are 

 * the WPS interface
 * the result access interface
 * the interface for upload of reference data and of processor bundles via HTTP

The subsystem-external interface used by the Processing Gateway/WPS is 

 * the catalogue interface of the Portal subsystem. 

Internally, the Processing Gateway/WPS uses 

 * the job submission and monitoring interface of the Apache Mesos Scheduling and Processing component
 * a http push interface to retrieve data for Online Access



Requirements for the design of DLR processing gateway/WPS
---------------------------------------------------------

.. req:: TS-FUN-640
  :show:

  (WPS interface) The Processing Request Gateway/WPS provides an OGC WPS 1.0 interface with functions GetCapabilities, DescribeProcess, Execute, and GetStatus.

.. req:: TS-FUN-645
  :show:

  (Processing mode) The Processing Request Gateway/WPS supports asynchronous requests and the retrieval of intermediate and final status with GetStatus.

.. req:: TS-FUN-650
  :show:

  (Process offerings) The Processing Request Gateway/WPS provides the set of processor offerings with parameters and input datasets with the functions GetCapabilities and DescribeProcess. Spatial and temporal selection is among the parameters of the Execute request.

.. req:: TS-FUN-680
  :show:

  (Deployment) Execute requests received are translated to Apache Mesos requests forwarded to Scheduling and Processing. This results into processing with the selected processor.

.. req:: TS-FUN-690
  :show:

  (Processing result provision) The Processing Request Gateway/WPS caches the results to the Online Data Access storage and provides them via HTTP(S).

.. req:: TS-FUN-700
  :show:

  (Catalogue entry) Either the Processing Request Gateway/WPS or Apache Mesos generates a metadata record and submits it to the Portal catalogue.

.. req:: TS-FUN-720
  :show:

  (Reference data upload) The Processing Request Gateway/WPS provides a HTTP(S) interface for the upload of reference data and caches it for the pickup of the processor (pull infrastructure).

.. req:: TS-FUN-740
  :show:

  (Software upload) The Processing Request Gateway/WPS provides a HTTP interface for the upload of (well-known) user-provided processors (probably in  form of docker images). Provided Processors will be vetted by Operator prior to deployment into Processing center. 

.. req:: TS-PER-610
  :show:

  (Response time) The Processing Request Gateway/WPS returns an Execute response with the identifier and an intermediate status upon submission of the Execute request.

.. req:: TS-SEC-610
  :show:

  (Authentication) A dedicated portal user is authorized to access the WPS and shedule executions and data retrival.

.. req:: TS-ICD-210
  :show:

  (GC Web Processing Service Interface)  WPS supports OGC WPS version 1.0 with functions GetCapabilities, DescribeProcess, Execute, and in addition GetStatus.

.. req:: TS-ICD-220 Result Access Interface
  :show:

  The Processing Request Gateway/WPS provides the result datasets stored in the staging area of Online Data Access via its HTTP(S) interface.

.. req:: TS-ICD-230
  :show:

  (Processor and Reference Data Upload Interface) The Processing Request Gateway/WPS provides a HTTPS interface for the upload of processor bundles by well-known users.

