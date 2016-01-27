.. _group___tep_accounting:

Accounting
----------







.. req:: TS-FUN-420
	:show:

	Quota mechanism based on the account balance of the user or groups is described in this section.



.. req:: TS-FUN-410
	:show:

	Business objects used to represent user or group account are referenced in this section.



.. req:: TS-FUN-400
	:show:

	The mechanism of debit and credit of user or group accounts is described in this section.

This component makes the integrated accounting of the TEP.

Accounting to user/group accounts 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Periodically, it collects the usage records from the :ref:`Apel Server <group___apel_server>` and use them to balance the user accounts with credits. The following figure describes this process.



.. uml::
	:caption: Accounting to user/group accounts sequence diagram
	:align: center


	  control "Portal Agent" as PA
	  participant "Portal" as P
	  database "Portal database" as PDB
	  database "APEL reporting" as AR
	  
	  autonumber
	
	  loop every n sec
	
	      PA -> P : Start accounting adjustment
	      activate P
	      P <-> PDB : load last sync time
	      P <-> PDB : load users and groups accounts
	      P -> AR : request integrated accounting for users and groups
	      activate AR
	      AR -> AR : aggregate accounts
	      AR -> P : accounts
	      deactivate AR
	      loop for every user and groups in accounts
	        P <-> PDB : load rates for items in accounts
	        P -> P : control eventual deposit
	        P -> P : debit user or group with cost
	        P -> P : credit user or group provider with cost
	        P <-> PDB : save account
	      end
	      deactivate P
	
	  end
	
	

Credit Authorization and Quota restrictions 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The quota restriction is implemented using the balance of the user or group account used to query the resource.

The following figure describes the example of the portal controlling the cost of a processing service and then check that the balance on the user account requesting it is sufficient.



.. uml::
	:caption: Quota control using credits example on WPS sequence diagram
	:align: center


	  actor "User" as U
	  participant "Portal" as P
	  database "Portal database" as PDB
	  participant "WPS Service" as WPS
	  
	  autonumber
	
	  U -> P : Request processing
	  activate P
	  P <-> PDB : load user account
	  P -> WPS : execute request (quotation mode)
	  activate WPS
	  WPS -> WPS : quote processing based on params
	  WPS -> P : WPS result (quotation)
	  deactivate WPS
	  P -> P : check user balance
	  alt enough credit
	    P -> WPS : execute request (normal mode)
	    P <-> PDB : update account with deposit charged
	    P -> U : request confirmation (id)
	  else not enough credit
	    P -> U : request refused
	  end
	  deactivate P
	
	

It depends on other components as

- :ref:`Persistence of Data <group___persistence>` stores the user accounts in the database


It interacts with interfaces as it

- connects :ref:`Apel Reporting <group___apel_reporting>` to retrieve the aggregated usage records.



This component manages the following business objects: :ref:`class_terradue_1_1_tep_1_1_account`, :ref:`class_terradue_1_1_tep_1_1_rates`



