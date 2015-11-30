.. _bcpc_part1 :

BC YARN scheduling and processing component
===========================================

Implementation software and configuration
-----------------------------------------

The YARN Scheduling and Processing component is based on Apache Hadoop 2.7.1 and Calvalus 2.7. It is deployed on the BC Calvalus infrastructure with 90 nodes, two redundant master nodes, and to I/O nodes in an internal protected network. It is accessible from the Processing Gateway/WPS virtual machine and the Ingestion and Processing Control virtual machine. YARN is a job scheduler supporting distributed map-reduce. Calvalus defines certain job types and task implementations for EO data processing.

The configuration specific for Urban TEP comprises:

 * an *urbantep* project request queue configured for the equivalent of 4 hosts (4.4%), either with limitation to this rate or with elastic extension if more resources are idle

State representation and persistent data
----------------------------------------

The persistent data of this component is the Hadoop configuration and the a list of jobs. The configuration of Hadoop except for the queue configuration is not Urban TEP-specific. The YARN scheduler while it is running maintains a list of active jobs and their distributed tasks and a history of jobs stored for a certain time period. 

Computational service and functions
-----------------------------------

The computational service of this component is job scheduling and processing:

 * Jobs are received from Processing Gateway/WPS and from Ingestion and Processing Control with specifications of the workflow type, the processor to be used, the input dataset, and parameters.
 * The job is split into tasks according to the input dataset
 * Processor software is automatically deployed (and cached) on the nodes used for processing
 * Tasks are executed and processors are called concurrently on the nodes
 * Results of processing are stored in HDFS
 * Partial/temporal processing failure or hardware failure is handled by automated failover/retry
 * Job status is returned to the calling service.

The computational service is provided by:

 * a resourcemanager Unix process on the master node accepting jobs
 * the nodemanger Unix processes on all cluster nodes as daemons for task execution
 * the Unix processes running EO data processors started by the nodemanger daemons on the nodes
 * additional map-reduce Unix processes for the aggregation of processing results

Interfaces and interface items
------------------------------

The interface of YARN is that for job submission and job status monitoring. Calvalus provides a higher level interface on top of this used by the WPS as well as by Ingestion and Processing Control:

 * Job interface of YARN, jobs represented as key-value lists, provided as a Java API
 * Request interface of Calvalus, represented as WPS-structured XML requests

In addition there is an operator interface:

 * Web GUI of Hadoop for monitoring
 * command line interface of Hadoop for monitoring and control

Example Calvalus Request
~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: seasonality-test.xml
   :language: xml
   
Requirements for the design of BC YARN scheduling and processing component
--------------------------------------------------------------------------

.. req:: TS-FUN-670
  :show:

  (Processing) The Scheduling and Processing processes submitted jobs by applying the requested workflow (e.g. Level 2 processing, aggregation) and processing with the requested EO data processors.

.. req:: TS-FUN-680
  :show:

  (Deployment) Scheduling and Processing automatically deploys Urban TEP processors provided in HDFS on the Calvalus-specific locations on processing job submission that require these processors.

.. req:: TS-FUN-710
  :show:

  (Processing statistics) The Scheduling and Processing maintains a history of jobs accessible for Urban TEP Processing and Ingestion Control for the purpose of reporting.
