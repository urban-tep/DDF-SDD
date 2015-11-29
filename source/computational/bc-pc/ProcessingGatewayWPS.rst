.. _bcpc_ProcessingGatewayWPS :

BC processing gateway/WPS
=========================

Implementation software and configuration
-----------------------------------------

The Processing Gateway and WPS is based on an Apache Tomcat and a WPS 1.0 implementation of BC. The Tomcat will be deployed on a virtual machine of the BC infrastructure in a protected network. It will be accessible via the Apache HTTP server at www.brockmann-consult.de that serves as a proxy.

The configuration specific for Urban TEP comprises:

 * the virtual machine *urbantep* hosting the Tomcat service
 * the rewrite rule of the Apache HTTP server for the context *https://www.brockmann-consult.de/urban-tep/*
 * the LDAP configuration of Tomcat to use the BC ldap for authentication of WPS and result access calls
 * the WPS configuration to allow users of the *urbantep* group to access the service
 * the WPS configuration to access the BC HDFS and YARN as backend, including retrival of datasets and processors configured for use by *urbantep* and storage area for result sets, reference data, and uploaded processor bundles
 * the allocation of the staging area for Urban TEP on the BC Online Data Access storage

State representation and persistent data
----------------------------------------

The Processing Gateway and WPS maintains a database of submitted and running asynchronous requests and their status. They are maintained in a HSQL database on the *urbantep* virtual machine.


Computational service and functions
-----------------------------------

The computational services of the Processing Gateway and WPS comprises implementations of the WPS functions GetCapabilities, DescribeProcess, Execute, and GetStatus. 

 * For GetCapabilities and DescribeProcess it determines all configured processors and datasets accessible by the user (of group *urbantep*) and caches this information for repeated use. The computational service for these functions is the conversion into the WPS-specific structure. 
 * For Execute it submits one or several requests to YARN according to the workflow used, and enters the request into the persistent local database. The conversion in this case is the other way round, e.g. to determine the input dataset from the input dataset name. It furhter monitors the status of the request and updates the database accordingly. 
 * For GetStatus it presents the status in the WPS structure.
 * For the retrieval of result datasets it stages the data at the Online Data Access and provides HTTP accesses the directories of the staging area.
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

 * the file system interface of the HDFS EO Data and Processing Storage
 * the job submission and monitoring interface of the YARN Scheduling and Processing component
 * the LDAP interface of the BC user management
 * the the file system interface of the Online Data Access

The internal interface of the Processing Gateway/WPS provided is

 * the plain Tomcat interface (logging, monitoring and control) for Operating

The OGC WPS interface items are defined in the OGC specification. Example interface items for Urban TEP are the following:

Example GetCapabilities response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: urban-tep-wps-GetCapabilities-sample-response.xml
   :language: xml
   
Example DescribeProcess response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: urban-tep-wps-DescribeProcess-sample-response.xml
   :language: xml
   
Example Execute request
~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: urban-tep-wps-sample-request.xml
   :language: xml

Example Execute response
~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: urban-tep-wps-Execute-response.xml
   :language: xml

Example GetStatus response
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: urban-tep-wps-GetStatus-sample-response.xml
   :language: xml

Requirements
------------

.. req:: TS-FUN-640 WPS interface
  :show:

  The Processing Request Gateway/WPS provides an OGC WPS 1.0 interface with functions GetCapabilities, DescribeProcess, Execute, and GetStatus.

.. req:: TS-FUN-645 Processing mode
  :show:

  The Processing Request Gateway/WPS supports asynchronous requests and the retrieval of intermediate and final status with GetStatus.

.. req:: TS-FUN-650 Process offerings
  :show:

  The Processing Request Gateway/WPS provides the set of processor offerings with parameters and input datasets with the functions GetCapabilities and DescribeProcess. Spatial and temporal selection is among the parameters of the Execute request.

.. req:: TS-FUN-680 Deployment
  :show:

  Execute requests received are translated to YARN requests forwarded to Scheduling and Processing. This results into processing with the selected processor.

.. req:: TS-FUN-690 Processing result provision
  :show:

  The Processing Request Gateway/WPS stages the results to the Online Data Access storage and provides them via HTTP(S).

.. req:: TS-FUN-700 Catalogue entry
  :show:

  Either the Processing Request Gateway/WPS or the Ingestion and Processing Control component (detailed design decision) generates a metadata record and submits it to the catalogue.

.. req:: TS-FUN-720 Reference data upload
  :show:

  The Processing Request Gateway/WPS provides a HTTP interface for the upload of reference data and stores it in the user area of the HDFS EO Data and Processing Storage.

.. req:: TS-FUN-740 Software upload
  :show:

  The Processing Request Gateway/WPS provides a HTTP interface for the upload of (well-known) user-provided processor bundles and stores them in the user area of the HDFS EO Data and Processing Storage.

.. req:: TS-PER-610 Response time
  :show:

  The Processing Request Gateway/WPS returns an Execute response with the identifier and an intermediate status upon submission of the Execute request.

.. req:: TS-SEC-610 Authentication
  :show:

  A portal user belonging to the group *urbantep* is registered in the BC LDAP and authorized to use the WPS.

.. req:: TS-ICD-210 OGC Web Processing Service Interface

  The BC implementation of the WPS supports OGC WPS version 1.0 with functions GetCapabilities, DescribeProcess, Execute, and in addition GetStatus.

.. req:: TS-ICD-220 Result Access Interface

  The Processing Request Gateway/WPS provides the result datasets stored in the staging area of Online Data Access via its HTTP(S) interface.

.. req:: TS-ICD-230 Processor and Reference Data Upload Interface

  The Processing Request Gateway/WPS provides a HTTP interface for the upload of processor bundles by well-known users.

.. req:: TS-ICD-310 OGC Web Processing Service	

  The BC implementation of the WPS supports OGC WPS version 1.0 with functions GetCapabilities, DescribeProcess, Execute, and in addition GetStatus.

.. req:: TS-FUN-671 Temporal statistics/indices generator
  :show:

  The Urban TEP Config and Processor Repo contains an indexes generation processor (see beam-buildin~1.0~urban-tep-indices-meris-l1b in GetCapabilities example above) and several aggregators to build statistics with its generic L3 workflow.

