.. _bcpc_part1 :

BC Urban TEP configuration and processor repository
===================================================

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

.. req:: TS-FUN-650 Process offerings
  :show:

  The Processing Request Gateway/WPS shall provide a set of processor offerings with parameters and input datasets of the Processing Centre. It shall accept requests with spatial and temporal selection. 

.. req:: TS-FUN-660 Subsetting processor
  :show:

  The Urban TEP Config and Processor Repo shall provide a processor for subsetting the GUF and GSI input dataset.

.. req:: TS-FUN-670 Processing
  :show:

  The Scheduling and Processing shall perform the requested operation based on the specified configurations.

.. req:: TS-FUN-671 Temporal statistics/indices generator
  :show:

  The Urban TEP Config and Processor Repo shall provide a processor for generating the statistics (MIN, MAX, MEAN, etc.) and indices (NDBI, NDVI, ARVI, etc.).

.. req:: TS-FUN-680 Deployment
  :show:

  Scheduling and Processing shall run Urban TEP processors provided in the Urban TEP Config & Processor Repo triggered by a request from the Processing Request Gateway/WPS. 

.. req:: TS-RES-630 Subsystem configuration
  :show:

  The Urban TEP Config and Processor Repo shall store all processors and processor versions used for Urban TEP in this Processing Centre as well as all system configurations, like user, queue resources, online data access quotas, and systematic workflows.

