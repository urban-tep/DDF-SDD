.. _group___context:

Context
-------





This component manages the general context for the entire system for a given session. It manages the identification of the user with a pluggable authentication interface to extend the generic username/password scheme with an external authentication mechanism. It interacts with the database to store and read the persistent configuration data. This component also manages the configuration data for the system. Basically, it saves and loads key/value pairs in the database on the behalf of all other components of the system.

It depends on other components as

- :ref:`Persistence of Data <group___persistence>` loads/stores data from/to the database

- :ref:`Authentication <group___authentication>` authenticates a user


