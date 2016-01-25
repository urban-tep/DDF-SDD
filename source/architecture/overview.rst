.. _static_overview :

Overview
========

The following schema provide a static overview of the main components that comes into play in Urban TEP.


.. include:: component_diagram.rst

    
The figure above describes all the internal or external interfaces of the TEP Urban system. In Blue and green are colored the external interfaces. The green ones are general user interface, typically web page. In red are colored the internal interfaces and in yellow the one for which the visibility is not yet defined.

This section describes them by subsystem:

- The :ref:`design_portal` is the front-end subsystem to the end-user interfaces via the :ref:`group___urban_site`. It is supported by the rest of the portal modules via many :ref:`group___web_services` to discover the collections, services and other :ref:`business objects <objects>` representing the real world entities registered and searchable in the TEP Urban portal. It also uses directly :ref:`group___r_w_p_s` interface as the processing request endpoint for all the completed, ongoing or new processing tasks to request. :ref:`design_portal` manages all :ref:`business objects <objects>` internally and store them peristently in the TEP database. For dataset query in the collection, it dispatches request to the :ref:`design_dataagency`.

- The :ref:`design_dataagency` hosts the services for dataset metadata ingestion and query using the catalogue as a service. The :ref:`design_data_gateway` is intended to be the main data access endpoint. It handles the data requests according to the partnership policies either by proxying the data to the most suitable cache or mirror site or redirecting to its location.

- The :ref:`design_apel` is a subsystem that collects accounting records via the accounting interface. It provides then with an reporting interface to provide with aggregated accounting.
   
- **PUMA** supports the portal for specific data visualization and analysis functionnalities.

- All **Processing Center** subsystems are in charge of the processing services from integration to production. For integration and processor deployment, they all have a specific integration point for new services in the processing center. They also exposes all a WPS endpoint for processing tasks management at the processing center level. Finally, process results of the completed processing tasks are accessible in a data result pool.


   
   
