.. _rolesactionsandinteractions :

Roles Actions and Interactions
-------------

Roles on the Platform are complying to a community policy (e.g. the data access quota allocated to a Principal Investigator on-boarded on the Platform), and are defined as a set of actions and interactions (Behaviours), observable in the system through process steps involving two types of business objects: Actors (e.g. a user) and Resources (e.g. :term:`datasets <dataset>`, processing service).

**Community Roles:**

* Data discovery and access
* Processor integration and Service offering
* Data processing over managed ICT
* Data visualization and analysis
* Reproducible Science collaborations
* Capacity Building through Data Sharing

**Community Policy:**

* Data provider partnership policy
* Data access policy
* Processor terms of use
* ICT Provider terms of use
* ICT provisioning policy

**Community Processes:**

* On-demand provisioning of EO processor integration resource
* On-demand provisioning of compute cluster

Data access
^^^^^^^^^^^

Users dicovers the available dataset collection and their related

* Policy: applicable EO data access and sharing policies
* Process: collection discovery, catalogue query, data package creation, EO product download
* Resource: :ref:`design_dataagency`, :ref:`design_portal`

Processor integration and service offering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Policy: Processor terms of use, ICT Provider terms of use
* Process: processor code wrapping, processor integration testing and validation, processor deployment as a service to user Portal
* Resource: Processing centers, :ref:`design_portal`

Data processing over managed ICT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Platform can instantiate processing resource, provision the infrastructure on a pre-configured ICT Provider and invoke the processing via the OGC Web Processing Service interface.
Users define input data and select a results location 

* Policy: applicable Public Cloud Provider terms of use
* Process: runJob - On-demand cloud appliance
* Resource: :ref:`design_dataagency`, :ref:`design_portal`, Processing centers

      
Users can run existing processing services (e.g. G-POD services) and and invoke the processing via the OGC Web Processing Service interface.
Users define input data and select a results location (e.g. portal, cloud block storage, dropbox, google drive, ...)

* Policy: applicable Public Cloud Provider terms of use
* Process: runJob - On-demand computing element
* Resource: Processing centers, :ref:`design_portal`

Data visualization and analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Policy: applicable EO data access and sharing policies, applicable Processor terms of use
* Process: data catalogue query, query results retrieval, results upload to shared storage
* Resource: , :ref:`design_puma`, :ref:`design_portal`

The platform is meant to allow users to perform data visualisation tasks:

* from processing software toolboxes hosted on their dedicated virtual machine: visualize and analyse EO-based products, e.g. to further apply data manipulation tools to them.
* from Web Portal Geobrowser: overlay EO data collections density maps, geohazards events layers (e.g. Disasters Charter activations)
* still from the Web Portal Geobrowser: combine EO data footprints and EO-based products to support data processing decision making (selection of processing input data, discovery and analysis of data processing results)
* from PUMA, apply advance WebGIS analysis

Reproducible science collaboration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Policy: applicable EO data access and sharing policies
* Process: Job run sharing, code sharing via social coding platforms, Cloud bursting
* Resource: :ref:`design_dataagency`, :ref:`design_portal`, Processing centers

The Urban TEP Platform is investigating on different collaborative eScience scenarios made available to users:

* Job run sharing, allowing users to see a job processing parameters and results, and reuse a job definition as a baseline for further runs. 
* Collaborative work on algorithm integration, Virtual Machines accessing Git repositories, like offered by social coding platforms such as GitHub).
* Cloud bursting of Processing services to Commercial Clouds, in order to absorbe peaks in the processing and increase scalability for massive data processing campaigns.

Capacity building through data sharing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Urban TEP Web Portal is investigating on different work areas (or 'contexts') made available to users:

EO data exploitation
""""""""""""""""""""

* Policy: applicable EO data access and sharing policies
* Process: EO data catalogue access, Job run sharing, shared Search result referencing, :ref:`class_terradue_1_1_tep_1_1_thematic_application` interactions
* Resource: :ref:`design_dataagency`, :ref:`design_portal`, Processing centers

* dedicated to EO data collections available as input data for processing tasks
* provides Portal links to automate the discovery allowing users to easily feed processing tasks

EO-based products exploitation
""""""""""""""""""""""""""""""

* Policy: applicable EO data access and sharing policies
* Process: EO data catalogue access, Job run sharing, Job intermediate results detailed analysis, :ref:`class_terradue_1_1_tep_1_1_thematic_application` interactions
* Resource: :ref:`design_dataagency`, :ref:`design_portal`, Processing centers

* dedicated to U-TEP processors results (final and intermediate processing outputs) 
* provides Portal links to processing jobs runs, to allow users understand a processor, and its possible improvements 

Publication referencing
"""""""""""""""""""""""

* Policy: applicable EO data access and sharing policies
* Process: Web link referencing, shared Search result referencing, :ref:`class_terradue_1_1_tep_1_1_thematic_application` interactions
* Resource: :ref:`design_dataagency`, :ref:`design_portal`

* related to the scientific community curated results (scientific papers)
* provides Portal links to collateral resources that allow researchers to understand and reproduce an experiment or a production

Community sharing
"""""""""""""""""

* Policy: applicable EO data access and sharing policies, 
* Process: Offering description, Offering cataloguing, shared Search result referencing, Geobrowser interactions
* Resource: :ref:`design_dataagency`, :ref:`design_portal`

* dedicated to geotag and reference web accessible content that labs, institutes, agencies, ... are openly sharing on the web (articles and blog posts, products images delivered in web-browser compatible formats, ...)
* provides a Portal integration mechanism based on the OGC standard "OWS Context" (http://www.opengeospatial.org/standards/owc)

