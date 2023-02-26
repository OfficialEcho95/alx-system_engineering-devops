
![2_servers_1_LB](https://user-images.githubusercontent.com/111706856/221423363-d2888e23-2b9f-4a7c-9c43-f0e93e436656.JPG)

### To design a three server web infrastructure that hosts the website www.foobar.com, we can add two additional servers to the original infrastructure, and use HAproxy as a load-balancer to distribute incoming traffic across the servers. The following is a design on the whiteboard:

User's computer --> HTTP request--> DNS server --> DNS response--> Load balancer

Load balancer:
- HAproxy (Load balancer)

Server 1:
- Nginx (Web server)
- Application server
- MySQL Primary (Master) node
- Application files

Server 2:
- Nginx (Web server)
- Application server
- MySQL Replica (Slave) node
- Application files

Server 3:
- MySQL Replica (Slave) node

## Domain name:
foobar.com

DNS record: www CNAME foobar.com

The additional components are:

## Two servers:
we add two more servers to the original infrastructure to create a more robust and scalable system.
## Load-balancer:
we add a load-balancer to distribute incoming traffic across the servers, to ensure high availability and reliability of the service.
## MySQL Replica node:
we add a third server to act as a MySQL Replica node, which will replicate the Primary node's data for data redundancy and failover protection.
HAproxy is configured with a round-robin distribution algorithm that works by evenly distributing incoming traffic to each server in turn.

## The load-balancer:
is enabling an Active-Active setup, where all servers are active and receive traffic, unlike an Active-Passive setup where only one server is active at a time and the other server(s) are passive and standby.

**A database Primary-Replica (Master-Slave) cluster** works by having the Primary node receive all write requests and then replicate the data to the Replica nodes, which receive read requests. This provides data redundancy and failover protection, as if the Primary node fails, one of the Replica nodes can take over as the Primary node.

**The Primary node** is the main node that receives all write requests, while the Replica nodes are backup nodes that receive read requests. In regards to the application, the Primary node is responsible for all database writes, while the Replica nodes are responsible for database reads.

## The issues with this infrastructure:

**Single Point of Failure (SPOF):** Although the infrastructure is more robust than the previous one, there is still a SPOF with the load-balancer. If the load-balancer fails, the service will be unavailable until the issue is resolved.

**Security issues:** There is no firewall and HTTPS enabled, leaving the infrastructure vulnerable to cyber-attacks and data breaches.

**No monitoring:** There is no monitoring in place to track the performance and availability of the infrastructure, making it difficult to detect and resolve issues.
