.. _bcpc_part1 :

BC YARN scheduling and processing component
===========================================

Implementation software and configuration
-----------------------------------------

State representation and persistent data
----------------------------------------

Computational service and functions
-----------------------------------

Interfaces and interface items
------------------------------

...

Requirements
------------

.. req:: TS-FUN-670 Processing
  :show:

  The Scheduling and Processing shall perform the requested operation based on the specified configurations.

.. req:: TS-FUN-680 Deployment
  :show:

  Scheduling and Processing shall run Urban TEP processors provided in the Urban TEP Config & Processor Repo triggered by a request from the Processing Request Gateway/WPS. 

.. req:: TS-FUN-710 Processing statistics
  :show:

  The Urban TEP Processing and Ingestion Control shall maintain a list of processing jobs performed with information on users and used resources, such as CPU hours, input data size, and storage capacity. This component shall report this information to the Reporting Interface of the portal.

