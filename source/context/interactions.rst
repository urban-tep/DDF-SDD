Interactions between roles
--------------------------

This section introduces the design contraints and the required interactions between roles.


Different services
^^^^^^^^^^^^^^^^^^

The users of the platform are provided with several interaction points:

- a website, with pages for the general public and some entry points for the registered users

- a geobrowser, with a Shop Window for the general public, and other features for registered users

- a catalogue along with a GUI editor to manage its own dataset collection fro registered users

- a convention with processing centers for processor integration (or catalogue provisioning) activities for "expert" users

- a social media handle for registered users, with different levels of usage (within the website or towards third party social media platforms)

- a Control Panel for the administrators of the Platform's resources (Data collections, Data Packages, Groups, Users, WPS providers, Web Processing Services, News, Banners)

User profiles are defined to specialize the interactions between roles, in order to map the underlying processes with community objectives.


.. uml::
  :caption: main user's interaction points
  :width: 10cm
  :align: center

  left to right direction
  skinparam packageStyle rect
  actor Users
  rectangle Platform {
    Users -- (interact with websitePages)
    Users -- (interact with thematicApps)
    Users -- (interact with catalogue)
    Users -- (interact with processingCenters)
    Users -- (interact with socialwebHandle)
  }


Constraints on Data providers | Administrators interactions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Existing catalogues of EO Data Collections can be registered through a Catalogue Description Url, compliant with the OGC standard "Earth Observation Profile". Collections are registered along with an identifier, a name and a description.

- Partner Data Admins are also provided with an organisational interface (handled through ESA RSS) which can setup a dedicated FTP resource (or access a provided one) and will migrate the uploaded data collections onto the Platforms storage, create the catalogue references, and make it registered on the Platform.

Constraints on Processor integrators | end-users interactions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deployment of processors and their orchestration is handled by the individual processing centres. There are calling conventions regarding the form and content of arguments for each processor, regardless if it is packaged in an image, container or software bundle. 
