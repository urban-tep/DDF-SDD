.. _dlrpc_Mesos :

DLR  Mesos scheduling and processing component
==============================================


.. req:: TS-FUN-670
  :show:

  (Processing) The Scheduling and Processing processes submitted jobs by applying the requested workflow with the requested thematic processors.

.. req:: TS-FUN-680
  :show:

  (Deployment) Scheduling and Processing automatically deploys Urban TEP processors when requested by the Portal via the Processing Gateway

.. req:: TS-FUN-710
  :show:

  (Processing statistics) The Scheduling and Processing maintains a history of jobs accessible for Urban TEP Processing and Ingestion Control for the purpose of reporting and accounting. 

  


Implementation software and configuration
-----------------------------------------

Apache Mesos Sheduler abstracts CPU, memory, storage, and other compute resources away from machines (physical or virtual), enabling fault-tolerant and elastic distributed systems to easily be built and run effectively.
It can deploy processing jobs to the DLR Calvalus Cluster with 28 nodes one master and one IO node and the private virtualized cloud (Geofarm) which currently consists of 16 Blades (672 Cores) with a planned extension to 4300 Cores in the next year. 
The Mesos master knows the state and controls all available computing resources, in case of DLR the Geofarm and Calvalus clusters. The mesos master checks availability of suitable processing resources (Mesos slaves) and triggers the calculations.
In case of the Geofarm cluster each virtual machine is managed as one Mesos slave, whereas the Calvalus cluster is treated as one giant resource that is scheduled via the Mesos-YARN interface. 
Once the job is finished and the results are transferred to the distribution nodes, the master is informed by the corresponding slave that processing is finished and resources are ready for new tasks. 
This system ensures flexible and transparent management of a heterogeneous processing infrastructure. It also allows the flexible integration of additional processing nodes.

State representation and persistent data
----------------------------------------

The persistent data of this component is a list of current and processed jobs. It also accounts for the ressources spent on each job. 

Computational service and functions
-----------------------------------

The computational service of this component is job scheduling and processing:

 * Jobs are received by the mesos master from the Processing Gateway/WPS (polling) with specifications of the workflow type, thethematic  processor to be used, the input dataset, and parameters.
 * The WPS OGC standard allows submission of requests as XML and REST calls. The WPS requests are then serialized and ingested by a Mesos master. 
 * The job is split into tasks according to the input dataset and parameters
 * The thematic Processors are automatically deployed (and cached) to the processing nodes
 * Tasks are executed concurrently on available nodes via mesos slave or the mesos-YARN interface subject to where the required input data is is situated
 * Results of processing are stored on HDFS (jobs running on Calvalus) of XFS (jobs running on Geofarm)
 * Partial/temporal processing failure or hardware failure is handled by automated failover/retry
 * Job status is returned to the Processing Gateway on request via polling interface(XMPP) .

The computational service is provided by:

 * a mesos master process on the master node accepting jobs
 * the mesos slave process on all cluster nodes as daemon for task execution direct or via mesos-YARN interface
 * processing processes are spun up on request
 * the metadata and information about accessing the products will the sent to the catalgue entry interface of the portal

Interfaces and interface items
------------------------------

The interface of Mesos is that for job submission and job status monitoring. 

 * Job interface of mesos is via WPS-structured XML or REST calls
 

In addition there is an operator interface:

 * Web GUI of Mesos for monitoring (accessible only on internal secure network)
 * REST interface of mesos for monitoring and control

  