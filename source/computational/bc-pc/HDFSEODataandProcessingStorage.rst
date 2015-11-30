.. _bcpc_part1 :

BC HDFS EO data and processing storage
======================================

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

.. req:: TS-FUN-610 Data ingestion
  :show:

  The Urban TEP Processing and Ingestion Control shall systematically harvest data from ESA Sentinel data hub, Landsat archives (ESA, Google, USGS) and MERIS archive (BC).

.. req:: TS-FUN-611 Settlement mask processing input
  :show:

  The EO Data and Processing Storage shall make settlement mask data (GUF) available for processing.

.. req:: TS-FUN-612 GSI input processing input
  :show:

  The EO Data and Processing Storage shall make GSI data available for processing.

.. req:: TS-FUN-613 Population distribution processing input
  :show:

  The EO Data and Processing Storage shall make population distribution data (WorldPop) available for processing.

.. req:: TS-FUN-614 Administrative units processing input
  :show:

  The EO Data and Processing Storage shall make administrative units data (GADM) available for processing.

.. req:: TS-FUN-615 Socio-economic statistics processing input
  :show:

  The EO Data and Processing Storage shall make socio-economic statistics data (WBG) available for processing.

.. req:: TS-FUN-660 Subsetting processor
  :show:

  The Urban TEP Config and Processor Repo shall provide a processor for subsetting the GUF and GSI input dataset.

.. req:: TS-FUN-710 Processing statistics
  :show:

  The Urban TEP Processing and Ingestion Control shall maintain a list of processing jobs performed with information on users and used resources, such as CPU hours, input data size, and storage capacity. This component shall report this information to the Reporting Interface of the portal.

.. req:: TS-RES-610 Data storage for EO data
  :show:

  The EO Data and Processing Storage shall store EO data.

.. req:: TS-RES-620 Data storage for non-EO data
  :show:

  The EO Data and Processing Storage shall store non-EO data like:
  •	Temporal statistics data
  •	Global Human Settlements Data
  •	Urban extents
  •	Imperviousness/urban greenness layer
  •	Settlements properties and pattern
  •	Urban areas definition in multiple options

