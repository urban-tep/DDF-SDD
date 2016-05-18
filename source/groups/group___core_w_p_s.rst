.. _group___core_w_p_s:

WPS
---







.. req:: TS-FUN-250
	:show:

	This section describes with sequence diagrams the internal WPS service discovery

This component is an helper for

- providing with WPS Server as a processing resource;
- providing with WPS process as processing offerings.

Main Functions 
---------------



- analyses the GetCapabilities() of the WPS server of a WpsProvider to retrieve all the process offered;
- retrieves the DescribeProcess() of the previously discovered process to describe the process with input and ouput parameters and create a WpsProcessOffering;
- submits, controls and monitors processing via the Execute() of the WPS server of a WpsProvider

Below, the sequence diagrams describe the previously listed functions.



.. uml::
	:caption: WPS Service Analysis Sequence Diagram - Get Capabilities
	:align: center


	actor "User or System" as WC
	participant "Portal" as WS
	participant "WPS Provider" as P
	participant "Cloud Controller" as C
	participant "Portal DataBase" as DB
	
	autonumber
	
	== Get Capabilities ==
	
	WC -> WS: GetCapabilities request
	activate WS
	WS -> DB: Load all Providers (Proxy=true)
	loop on each provider
	    WS <-> DB: load services
	    loop on each service
	        WS <-> WS: get service info (identifier, title, abstract)
	    end
	end
	WS -> C: discover Providers
	loop on each provider
	    WS <-> P: GetCapabilities
	    WS <-> WS: extract services from GetCapabilities using request identifier
	    loop on each service
	        WS <-> WS: get service info (identifier, title, abstract)
	    end
	end
	WS -> WS: aggregate all services info into response offering
	WS -> WC: return aggregated GetCapabilities
	deactivate WS
	
	



.. uml::
	:caption: WPS Service Analysis Sequence Diagram - Describe Process
	:align: center


	participant "User or System" as WC
	participant "Portal" as WS
	participant "WPS Provider" as P
	participant "Portal DataBase" as DB
	
	autonumber
	
	== Describe Process ==
	
	WC -> WS: DescribeProcess request
	activate WS
	alt case process from db
	    WS <-> DB: load service from request identifier
	    WS <-> DB: get provider url + service identifier on the provider
	else case process from cloud provider
	    WS <-> P: GetCapabilities
	    WS <-> WS: extract describeProcess url from GetCapabilities using request identifier
	end
	WS -> WS: build "real" describeProcess request
	WS <-> P: DescribeProcess
	WS -> WC: return result from describeProcess
	deactivate WS
	
	



.. uml::
	:caption: WPS Service Analysis Sequence Diagram - Execute
	:align: center


	participant "User or System" as WC
	participant "Portal" as WS
	participant "WPS Provider" as P
	participant "Portal DataBase" as DB
	
	autonumber
	
	== Execute ==
	
	WC -> WS: Execute request
	activate WS
	alt case process from db
	    WS -> DB: load service from request identifier
	    WS -> DB: get provider url + service identifier on the provider
	else case process 'from cloud provider'
	    WS -> P: GetCapabilities
	    WS -> WS: extract execute url from GetCapabilities using request identifier
	end
	WS -> WS: build "real" execute request
	WS -> P: Execute
	alt case error
	    WS -> WC: return error
	else case success
	    WS -> DB: store job
	    WS -> WS: update job RetrieveResultServlet url
	    WS -> WC: return created job
	end
	deactivate WS
	
	



.. uml::
	:caption: WPS Service Analysis Sequence Diagram - Retrieve Result
	:align: center


	participant "User or System" as WC
	participant "Portal" as WS
	participant "WPS Provider" as P
	participant "Portal DataBase" as DB
	
	autonumber
	
	== Retrieve Result Servlet ==
	
	WC -> WS: RetrieveResultServlet request
	activate WS
	WS -> DB: load job info from request identifier
	WS -> P: call "real" statusLocation url
	WS -> WS: update href in response to put local server url instead of real provider
	WS -> WC: return updated statusLocation response
	deactivate WS
	
	



.. uml::
	:caption: WPS Service Analysis Sequence Diagram - Search WPS process
	:align: center


	participant "User or System" as WC
	participant "Portal" as WS
	participant "WPS Provider" as P
	participant "Cloud Controller" as C
	participant "Portal DataBase" as DB
	
	autonumber
	
	== Search WPS process ==
	
	WC -> WS: WPS search request
	activate WS
	WS -> DB: Load all Providers
	WS -> C: discover Providers
	loop on each provider
	    WS -> P: GetCapabilities
	    WS -> WS: get services info
	    loop on each service
	        alt provider is Proxied
	            WS -> WS: create local identifier and save remote identifier
	            WS -> WS: use local server url as baseurl
	        end
	        WS -> WS: add service info to the response
	    end
	end
	deactivate WS
	
	



.. uml::
	:caption: WPS Service Analysis Sequence Diagram - Integrate WPS provider
	:align: center


	participant "User or System" as WC
	participant "Portal" as WS
	participant "WPS Provider" as P
	participant "Portal DataBase" as DB
	
	autonumber
	
	== Integrate WPS provider ==
	
	WC -> WS: POST provider
	activate WS
	WS -> DB: store provider
	WS -> P: GetCapabilities
	WS -> WS: get services info
	loop on each service
	    alt provider is Proxied
	        WS -> WS: create local identifier and save remote identifier
	        WS -> WS: use local server url as baseurl
	    end
	    WS -> DB: store service
	end
	
	

Model and Representation 
-------------------------

This components has also a function to represent a :ref:`Terradue.Portal.WpsProcessOffering <class_terradue_1_1_portal_1_1_wps_process_offering>` object as a :ref:`Terradue.ServiceModel.Ogc.OwsModel.OwcOffering <class_terradue_1_1_service_model_1_1_ogc_1_1_ows_model_1_1_owc_offering>` in the :ref:`OWS Context <group___o_w_s_context>` model. It implements the mechanism to search for :ref:`Terradue.Portal.WpsProvider <class_terradue_1_1_portal_1_1_wps_provider>` and the :ref:`Terradue.Portal.WpsProcessOffering <class_terradue_1_1_portal_1_1_wps_process_offering>` via an OpenSearchable interface.

It depends on other components as

- :ref:`Persistence of Data <group___persistence>` stores the :ref:`Terradue.Portal.WpsProvider <class_terradue_1_1_portal_1_1_wps_provider>` and :ref:`Terradue.Portal.WpsProcessOffering <class_terradue_1_1_portal_1_1_wps_process_offering>` references in the database

- :ref:`Authorisation <group___authorisation>` controls the access on the WPS services


It interacts with interfaces as it

- connects :ref:`Remote Web Processing Services Interface <group___r_w_p_s>` interface to retrieve process offerings from WPS Server and to submit, control and monitor prcoessing.


