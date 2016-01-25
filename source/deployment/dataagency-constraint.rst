Data Agency Constraints
-----------------------
  
The computing constraints are calculated on the basis of a number of 10000 indexes
in the :ref:`design_catalogue` and with a number of entries from 1000 to 100.000.000 entries each.
The :ref:`design_data_gateway` must be able to server 1000 users daily with an average of 1TB each.

General Operating System Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All system described hereafter are deployed on a similar baseline for the operating system
and the initial configuration:

- Centos 6 x86_64 arch


Catalogue Computing Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Catalogue computing requirements is based on a cluster of 3 nodes to run :ref:`design_elasticsearch` is cluster mode
with 3 web server to run :ref:`group___geosquare` that are server on a capacity basis via a load balancer that also ensures
a failover mechanism.

Each node has the following resources requirements:

- 8 core or thread CPUs at 3Ghz
- 32Gb RAM
- 500Gb SSD HD
- double Gigabit Network interface (internal for clustering, external for load balancing)


Sizing Options
^^^^^^^^^^^^^^

The catalogue may be upgraded in a very short term provisioning new nodes and installing them using the configuration server as described in :ref:`deploy_configmgmt` section.


Network Security Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default all ports of any protocol on every external network interface is closed for any inbound connection.
According to the type of deployment, The following exceptions must be defined in the firewall system:

**Frontline Catalogue API**

- port 443 for HTTPS traffic on protocol TCP


