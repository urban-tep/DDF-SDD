.. _group___tep_data:

Data
----



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___tep_data.iuml

This component is in charge of all the data management in the platform.

It implements the mechanism to search for Collection and Data Packages via an OpenSearchable interface.



Each user of the platform may define a DataPackage to save a set of dataset that he preselected. The 2 following state diagram shows the lifecycle of those data packages in creation and update.



.. uml::


	
	User -> WebPortal: Select data
	WebPortal -> WebServer: Stores in a temporary data package
	WebServer -> Database: Save a temporary data package
	User -> WebPortal: Save the data package \nwith name/identifier
	WebPortal -> WebServer: Request the storage \nof the current temporary data package \nwith given name/identifier
	WebServer -> Database: Save the data package \nwith associated opensearch urls
	WebServer -> WebPortal: Return new data package
	WebPortal -> User: Data package successfully created
	
	footer
	TEP Data Package creation state diagram
	(c) Terradue Srl
	endfooter
	
	



.. uml::


	
	User -> WebPortal: Load existing data package
	WebPortal -> WebServer: Stores the data package in the temporary data package
	WebPortal -> User: Displays the items from the data package
	User -> WebPortal: Remove items or add new ones in the temporary data package
	
	alt user is owner of the data package
	User -> WebPortal: Request the storage of the current temporary data package \nwith given name (update existing one)
	WebServer -> Database: Save the data package \nwith associated opensearch urls
	WebServer -> WebPortal: Return new data package
	WebPortal -> User: Data package successfully updated
	else user is not the owner of the data package
	WebPortal -> User: Displays an error message to the user
	end
	
	footer
	TEP Data Package update state diagram
	(c) Terradue Srl
	endfooter
	
	

Dependencies
^^^^^^^^^^^^
- uses :ref:`Authorisation <group___authorisation>` to manage the users in the groups with their roles and their access accordingly.

- uses :ref:`Series <group___series>` to delegates the dataset series persistence and search mechanism.



Classes
^^^^^^^
- :ref:`class_terradue_1_1_tep_1_1_controller_1_1_collection`
- :ref:`class_terradue_1_1_tep_1_1_controller_1_1_data_package`

