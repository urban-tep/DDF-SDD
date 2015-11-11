.. _group___tep_user:

Urban TEP User
--------------



.. uml::

  !include includes/skins.iuml
  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2
  !include source/groups/group___tep_user.iuml

This represents a user in TEP Urban platform.



.. uml::


	
	[*] --> PendingActivation : first time login
	PendingActivation : User must confirm its UM-SSO email
	PendingActivation : User cannot access secured services
	
	PendingActivation --> Enabled : email confirmation
	Enabled : User can access secured services
	
	footer
	Urban TEP User state diagram
	(c) Terradue Srl
	endfooter
	



.. uml::


	
	start
	if (secured service?) then (yes)
	  if (UM-SSO logged?) then (yes)
	    if (user in DB?) then (yes)
	      if (user pending activation?) then (yes)
	        :reinvite user to confirm email
	        stop
	      endif
	    else (no)
	      :create user account in db
	      :set account status to **Pending Activation**
	      :send confirmation email to user
	      :invite user to confirm email
	      stop
	    endif
	  else (no)
	    :redirect user to UM-SSO IDP
	    stop
	  endif
	endif
	:process service
	stop
	
	footer
	Urban TEP User account activity diagram
	(c) Terradue Srl
	endfooter
	

Dependencies
^^^^^^^^^^^^
- :ref:`Authentication <group___authentication>` authenticates the user


