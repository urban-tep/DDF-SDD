.. _design_portal :

Portal
======

The portal is mainly composed of 

- a Web Server running a web application including the components :ref:`group___core`, :ref:`group___security`, :ref:`group___tep`, :ref:`group___web_services`, 
- a web site of html and javascript in the component :ref:`group___urban_site`

The backend relies on a relational databse to store persistently the portal and user data.

The following diagram describes the components interactions.


.. include:: component_diagram.rst

.. toctree::
   :maxdepth: 1
   
   Core <../../groups/group___core>
   Security <../../groups/group___security>
   TEP modules <../../groups/group___tep>
   Urban site <../../groups/group___urban_site>
   Web-services <../../groups/group___web_services>
   
