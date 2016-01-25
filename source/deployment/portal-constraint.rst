Portal Constraints
------------------
  
The computing constraints are calculated on the basis of a number of 1000 registerd users
visiting the platform daily and their insfrastructure needs.

General Operating System Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All system described hereafter are deployed on a similar baseline for the operating system
and the initial configuration:

- Centos 6 x86_64 arch


Computing Constraints
^^^^^^^^^^^^^^^^^^^^^

The minimum computing requirements of the system on which the Web Portal are:

- 8 core or thread CPUs at 2Ghz
- 16Gb RAM
- 250Gb HD
- Gigabit Network interface


Sizing Options
^^^^^^^^^^^^^^

The portal may be scaled up horizontally by running multiples instances of the Web Server via
a load balancing mechanism.
The data base mayalso be decoupled from the Web Server on several nodes with a replication mechanism


Security Constraints
^^^^^^^^^^^^^^^^^^^^

By default all ports of any protocol on every external network interface is closed for any inbound connection.
According to the type of deployment, The following exceptions must be defined in the firewall system:

**Frontline Web Server**

- port 443 for HTTPS traffic on protocol TCP


