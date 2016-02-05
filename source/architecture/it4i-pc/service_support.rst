.. _it4ipc_service_support :

IT4I Service Support
====================
The *IT4I Service Support* will provide support for all things related to the IT4I processing centre and will administrate all parts of the IT4I processing centre infrastructure. This requires mostly manual human-based processes that will be performed by *IT4I Service Support Operators*. Several software components described in the following subsections will be used to increase the effectiveness of these support and administration processes.


IT4I Helpdesk
-------------
The *IT4I Helpdesk* is a helpdesk solution that manages the issues and support requests related to the IT4I processing centre. This helpdesk will serve as a processing center specific third escalation level for *Urban TEP Service Desk* incident and problem management.

The *IT4I Helpdesk* is a web-based solution deployed on a virtual server in IT4I virtualisation infrastructure and hosted on the Apache Web Server. It will provide HTTPS interface to the *Urban TEP Service Desk* to escalate selected issues. The *IT4I Helpdesk* will also send status updates for escalated issues via an HTTP(S) interface of the *Urban TEP Service Desk*.

The issues tracked by the *IT4I Helpdesk* are solved by *IT4I Service Support Operators* that have access to all parts of the IT4I processing centre infrastructure.

.. req:: TS-FUN-760
  :show:

  The *IT4I Helpdesk* will handle issues addressed to the IT4I Processing Centre.

.. req:: TS-ICD-240
  :show:

  The *IT4I Helpdesk* will track issues and requests addressed to the IT4I Processing Centre.
