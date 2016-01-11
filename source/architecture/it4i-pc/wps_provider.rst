.. _it4ipc_wps_provider :

IT4I WPS Provider
=================
The WPS Provider package contains components that publish the processing functionality of the platform as WPS services to the Urban TEP Portal and execute workflows connected with these services. As the package contains several related web-based J2EE applications and tools, it will be deployed on one Linux-based virtual server in the IT4I virtualisation infrastructure and hosted in the Apache Tomcat webserver and servlet container. Individual components of the IT4I processing centre WPS Provider are described in the following subsections.


GeoServer
---------
As OGC WPS is the main interface for executing processing services in the Urban TEP platform, IT4I will build all WPS related functionality on *GeoServer*, which is an open source server for sharing geospatial data. *GeoServer* is an OGC compliant implementation of a number of open standards such as Web Feature Service (WFS), Web Map Service (WMS), and Web Coverage Service (WCS). Additional formats and publication options are available including Web Map Tile Service (WMTS) and extensions for Catalogue Service (CSW) and finally Web Processing Service (WPS). (http://geoserver.org/)

Whenever the *Urban TEP Portal* wants to discover, which services are available in the IT4I processing centre, or wants to execute any of these services, it sends WPS reguests to the *GeoServer*. *GeoServer* then either provides the information about supported services in its service catalogue or starts the configured execution workflow related to the requested service. All processing workflow requests are then forwarded to the *HPC as a Service* solution that manages all processing jobs and information about available HPC clusters and their resources.

.. req:: TS-FUN-640
  :show:

  The *GeoServer* will provide the WPS interface for the IT4I processing centre.

.. req:: TS-FUN-645
  :show:

  The *GeoServer* will provide asynchronous processing of the WPS requests at the IT4I processing centre.

.. req:: TS-FUN-650
  :show:

  The *GeoServer* will provide the supported processors and information about parameters and available datasets at the IT4I processing centre.

.. req:: TS-FUN-680
  :show:

  The *GeoServer* will receive WPS requests to execute all supported service processors at the IT4I processing centre.

.. req:: TS-PER-610
  :show:

  The *GeoServer* will produce regular close-to-instant responses for the processing at the IT4I processing centre.

.. req:: TS-ICD-310
  :show:

  The *GeoServer* will provide the WPS interface for the IT4I processing centre.




Service Configuration Tool
--------------------------
The *Service Configuration Tool* is an IT4I in-house J2EE solution that serves as an auxiliary tool for managing and updating configuration of supported services in the *GeoServer*. It is actually a web service-based adapter that synchronises the *HPC as a Service Middleware* and *GeoServer* service configurations to simplify the administration of both solutions. Whenever any change in the service configuration appears in *HPC as a Service* (either by a processing workflow or by administration intervention), the *Service Management Module* of the *HPC as a Service Middleware* synchronises the configuration changes with the *GeoServer* using the *Service Configuration Tool*.

This solution will also generate a metadata record and submit it to the Urban TEP catalogue for any changes in service definition at the IT4I processing centre.

.. req:: TS-FUN-700
  :show:

  The *Service Configuration Tool* will receive the metadata record from the *HPCaaS Service Management Module* and will submit it to the catalogue at the IT4I processing centre and subsequently generates a metadata record and submits it to the Urban TEP catalogue.