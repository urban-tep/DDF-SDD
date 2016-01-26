.. _group___tep_data:

Data
----







.. req:: TS-FUN-010
	:show:

	The GeoNode and :ref:`GeoServer <namespace_geo_server>` export function allows user to upload their data to PUMA.

This component is in charge of all the data management in the platform.

It implements the mechanism to search for Collection and Data Packages via an OpenSearchable interface.

User Data Packages 
^^^^^^^^^^^^^^^^^^^

Each user of the platform may define a DataPackage to save a set of dataset that he preselected. The 2 following state diagram shows the lifecycle of those data packages in creation and update.



.. uml::
	:caption: Data package lifecycle #1 state diagram
	:align: center


	User -> WebPortal: Select data
	WebPortal -> WebServer: Stores in a temporary data package
	WebServer -> Database: Save a temporary data package
	User -> WebPortal: Save the data package \nwith name/identifier
	WebPortal -> WebServer: Request the storage \nof the current temporary data package \nwith given name/identifier
	WebServer -> Database: Save the data package \nwith associated opensearch urls
	WebServer -> WebPortal: Return new data package
	WebPortal -> User: Data package successfully created
	
	



.. uml::
	:caption: Data package lifecycle #2 state diagram
	:align: center


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
	
	
	

Persistence 
^^^^^^^^^^^^

When a dataset is processed with a remote processing (e.g. WPS), the results of this data may be located in a temporary storage. The user would want to keep that result and its metadata. The :ref:`Data <group___tep_data>` components integrates the function to "copy" the results and its metadata to a persistent storage on one for the files and on a catalogue index for the metadata.

Analysis and Visualization 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a dataset is processed with a remote processing (e.g. WPS), the results of this data may be located in a place where there is no other function than downloading the data directly on its local machine to visualize or analyze it. The :ref:`Data <group___tep_data>` components integrates functions to "export" the results and its metadata to an external tools or server that shall enhance the results for better visualization and analysis. The following export capabilities are implemented:



- :emphasis:`:ref:`GeoServer <namespace_geo_server>`` raster and vector export. If the results include standard vector files (e.g. shapefile, geojson, csv with WKT, ...) or raster files such as geolocated images (geotiff, png with world files...), the  components shall propose to the user to export them to geoserver that will resturn a new WMS layer that the web visualization widget shall display
- :emphasis:`GeoNode` from an existing WMS layer, the  components shall propose to the user to export them to geonode that will return a link to the geonode map for the visualisation.

It depends on other components as

- uses :ref:`Authorisation <group___authorisation>` to manage the users in the groups with their roles and their access accordingly.

- uses :ref:`Series <group___series>` to delegates the dataset series persistence and search mechanism.


It interacts with interfaces as it

- connects :ref:`GeoServer API <group___geo_server_a_p_i>` to export vector or raster data.

- connects :ref:`GeoNode API <group___geo_node_a_p_i>` to export WMS.



This component manages the following business objects: :ref:`class_terradue_1_1_tep_1_1_collection`, :ref:`class_terradue_1_1_tep_1_1_data_package`



