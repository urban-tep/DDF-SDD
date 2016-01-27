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

Each user of the platform may define a DataPackage to save a set of dataset that he preselected.

This selection can be done by

- selecting single datasets in the basket;
- or saving a set of filters from a search.

This latter selection way is an important feature especially to define a dynamic subset of data Collection allowing data driven processing.

Persistence 
^^^^^^^^^^^^

When a dataset is processed with a remote processing (e.g. WPS), the results of this data may be located in a temporary storage. The user would want to keep that result and its metadata. The :ref:`Data <group___tep_data>` components integrates the function to "copy" the results and its metadata to a persistent storage on one for the files and on a catalogue index for the metadata.

Analysis and Visualization 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

*[]*

It depends on other components as

- uses :ref:`Authorisation <group___authorisation>` to manage the users in the groups with their roles and their access accordingly.

- uses :ref:`Series <group___series>` to delegates the dataset series persistence and search mechanism.


It interacts with interfaces as it

- connects :ref:`GeoServer API <group___geo_server_a_p_i>` to export vector or raster data.



This component manages the following business objects: :ref:`class_terradue_1_1_tep_1_1_collection`, :ref:`class_terradue_1_1_tep_1_1_data_package`



