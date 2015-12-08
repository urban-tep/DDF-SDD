.. _group___auth___umsso:

UM-SSO plugin
-------------





This module enables external authentication using UM-SSO mechanism. In the core, the :ref:`Context <group___context>` component provides with an interface that allows using HTTP headers present in the HHTP context to authenticate the user. Associated with a set of rules, the :ref:`Authentication <group___authentication>` is able to establish a protocol to authenticate user.

Typical code ruleset is declared with the method UM-SSO. accountType maps the rule to an account. The rule is applied only if the condition that specified that the header  is present and not empty. Then the value present in  is used as login username and user is registered automatically if not yet present in the database with register="true" and the user receives a account creation mail with the mail information found in header Umsso-Person-Email.

Following diagram depicts the User status when logging with UM-SSO.



.. uml::
	:caption: User login with UM-SSO activity diagram


	start
	    if (secured service?) then (yes)
	      if (UM-SSO logged?) then (yes)
	        if (user in DB?) then (yes)
	          if (user pending activation?) then (yes)
	            :reinvite user to confirm email;
	            stop
	          endif 
	        else (no)
	          :create user account in db;
	          :set account status to **Pending Activation**;
	          :send confirmation email to user;
	          :invite user to confirm email;
	          stop
	        endif
	      else (no)
	        :redirect user to UM-SSO IDP;
	        stop
	      endif
	    endif
	    :process service;
	stop
	
	

Next diagram depicts the scenarios that applies when a user perform an HTTP request to a web service protected by UM-SSO. This scenario is the “normal” case where user credentials are correct.



.. uml::
	:caption: UM-SSO protected HTTP request sequence diagram


	actor "User\n(Web Browser)" as U
	participant "Web Server\n(ngEO SP checkpoint)" as W
	participant "Web Service\nusing :Context" as C
	participant "Authentication\nConfiguration\nAuth.xml" as A
	entity "UM-SSO Identity Provider" as I
	
	autonumber
	
	== UM-SSO authentication ==
	
	U ->> W: HTTP request
	activate W
	
	alt "user not authenticated on UM-SSO"
	
	W -->> U: HTTP redirect\nto IdP
	deactivate W
	activate U
	U ->> I: login form URL
	deactivate U
	activate I
	I -->> U: login form
	deactivate I
	
	U ->> I: username & password
	activate I
	I -> I:Authenticate user
	I -->> U: user credentials (cookie, SAML token, validity period, redirection)
	deactivate I
	
	U -> U: Write cookie
	U ->> W: HTTP redirect
	
	end
	
	activate W
	W ->> I: check User attribute
	activate I
	I -->> W: Identity attributes in SAML
	deactivate I
	W -> W: Create a security context
	W -->> U: HTTP redirection\nto original resources
	deactivate W
	activate U
	
	== Web Server authentication ==
	
	U ->> W: original HTTP request
	deactivate U
	activate W
	W -> C: original HTTP request\n+ additional HTTP headers
	deactivate W
	
	activate C
	
	C -> A: Read configuration
	A --> C: Authentication RuleSet
	C -> C: Apply ruleset\nto HTTP Headers
	
	alt "User not present in DB"
	
	C -> C: Register new User\n(username, email)
	
	end
	
	C -> C: Initialize Local Context\nwith user space
	C -> C: Perform request 
	
	C --> W: HTTP response
	deactivate C
	W -->> U: HTTP response
	
	

.. req:: TS-SEC-040
	:show:

	UM-SSO plugin described 



It interacts with interfaces as it

- implements :ref:`Authentication <group___authentication>` to enable UM-SSO Authentication.


The following normative references are applied to this component:

- EO op UM-SSO Interface Control Document [SIE-EO-OP-UM-SSO-ICD-002]


