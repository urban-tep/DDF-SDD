.. _group___authentication:

Authentication
--------------





It provides with the functions to identify a user through a generic interface for implementing multiple authentication mechanism.



.. uml::
	:caption: Authentication mechanism Activity Diagram
	:align: center


	start
	:read session information;
	if (valid session) then (yes)
	    :Load user info from session;
	else (No) 
	    while (user not authenticated & next authentication method ?) is (yes)
	        if (Authentication successful) then (yes)
	            if (user exists) then (no)
	                if (authentication method allows user creation) then (yes)
	                    :create user account;
	                endif
	            endif
	         endif
	    endwhile (no)
	    if (user authenticated) then (yes)
	        if (user is enabled) then (no)
	            if ( configuration needs user activation ) then (yes)
	                :Throw User Activation Exception;
	                stop
	            endif
	        endif
	        :Load user info and create session;
	    endif
	endif
	stop
	
	
	

It depends on other components as

- :ref:`Persistence of Data <group___persistence>` reads/writes the user information


