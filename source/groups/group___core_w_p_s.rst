.. _group___core_w_p_s:

WPS
---



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___core_w_p_s.iuml

This component is an helper for

- providing with WPS Server as a processing resource;
- providing with WPS process as processing offerings.

It has two main functions:

- analyses the GetCapabilities() of the WPS server of a WpsProvider to retrieve all the process offered;
- retrieves the DescribeProcess() of the previously discovered process to describe the process with input and ouput parameters and create a WpsProcessOffering;
- submits, controls and monitors processing via the Execute() of the WPS server of a WpsProvider

Below, the sequence diagram describes the the previously listed functions.



.. uml::


	!define DIAG_NAME WPS Service Analysis Sequence Diagram
	
	participant "WebClient" as WC
	participant "WebServer" as WS
	participant "Provider" as P
	participant "Cloud Provider" as C
	participant "DataBase" as DB
	
	autonumber
	
	== Get Capabilities ==
	
	WC -> WS: GetCapabilities request
	activate WS
	WS -> DB: Load all Providers (Proxy=true)
	loop on each provider
	    WS -> DB: load services
	    loop on each service
	        WS -> WS: get service info (identifier, title, abstract)
	    end
	end
	WS -> C: Load all Providers
	loop on each provider
	    WS -> P: GetCapabilities
	    WS -> WS: extract services from GetCapabilities using request identifier
	    loop on each service
	        WS -> WS: get service info (identifier, title, abstract)
	    end
	end
	WS -> WS: aggregate all services info into response offering
	WS -> WC: return aggregated GetCapabilities
	deactivate WS
	
	== Describe Process ==
	
	WC -> WS: DescribeProcess request
	activate WS
	alt case process from db
	    WS -> DB: load service from request identifier
	    WS -> DB: get provider url + service identifier on the provider
	else case process from cloud provider
	    WS -> C: get service provider
	    WS -> P: GetCapabilities
	    WS -> WS: extract describeProcess url from GetCapabilities using request identifier
	end
	WS -> WS: build "real" describeProcess request
	WS -> P: DescribeProcess
	WS -> WC: return result from describeProcess
	deactivate WS
	
	== Execute ==
	
	WC -> WS: Execute request
	activate WS
	alt case process from db
	    WS -> DB: load service from request identifier
	    WS -> DB: get provider url + service identifier on the provider
	else case process 'from cloud provider'
	    WS -> C: get service provider
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
	
	== Retrieve Result Servlet ==
	
	WC -> WS: RetrieveResultServlet request
	activate WS
	WS -> DB: load job info from request identifier
	WS -> P: call "real" statusLocation url
	WS -> WS: update href in response to put local server url instead of real provider
	WS -> WC: return updated statusLocation response
	deactivate WS
	
	== Search WPS process ==
	
	WC -> WS: WPS search request
	activate WS
	WS -> DB: Load all Providers
	WS -> C: Load all Providers
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
	
	
	footer
	DIAG_NAME
	(c) Terradue Srl
	endfooter
	

Model and Representation 
^^^^^^^^^^^^^^^^^^^^^^^^^

This components has also a function to represent a WpsProcessOffering object as a OwcOffering in the :ref:`OWS Context <group___o_w_s_context>` model. It implements the mechanism to search for  and the WpsProcessOffering via an OpenSearchable interface.

""

.. req:: TS-FUN-250
	:show:

	This section describes with sequence diagrams the internal WPS service discovery



Dependencies
^^^^^^^^^^^^
- :ref:`Persistence of Data <group___persistence>` stores the  and WpsProcessOffering references in the database

- :ref:`Authorisation <group___authorisation>` controls the access on the WPS services


Interfaces
^^^^^^^^^^
- connects :ref:`Remote Web Processing Services Interface <group___r_w_p_s>` interface to retrieve process offerings from WPS Server and to submit, control and monitor prcoessing.


