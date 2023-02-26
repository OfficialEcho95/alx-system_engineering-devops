# Design of Three Server Web Infrastructure for www.foobar.com
## Description of Infrastructure:

## The proposed infrastructure includes the following components:

**Three servers (web server, application server, and database server)** to distribute the workload and improve scalability and redundancy.
**A Load Balancer** to manage the incoming traffic and distribute it to the appropriate servers.
**Three firewalls** to protect the servers from unauthorized access and provide an additional layer of security.
**An SSL certificate** to serve www.foobar.com over HTTPS, which is encrypted traffic and prevents data theft and man-in-the-middle attacks.
**Three monitoring clients** to collect data and monitor the performance and health of the servers.
Explanation for Each Component:

## Three Servers
The use of three servers, each dedicated to a specific task, allows for better scalability and fault tolerance. In case of failure, the other two servers can continue to serve traffic without any disruption.
## Load Balancer
A load balancer is a device or software that distributes incoming traffic among multiple servers to improve performance, reduce downtime, and provide scalability.
## Firewalls
Firewalls are devices or software that monitor and control incoming and outgoing traffic to and from a network. They help to prevent unauthorized access, block unwanted traffic, and detect and alert on suspicious activity.
## SSL Certificate
SSL (Secure Sockets Layer) certificates provide encryption for data transmitted between servers and web browsers, preventing hackers from intercepting and reading sensitive information. It also helps to build trust with visitors to the website.
## Monitoring Clients
Monitoring clients collect data on the performance and health of the servers, applications, and network. This data is then used to identify and resolve issues proactively and improve the overall performance of the system.

# Issues with Infrastructure:

- Terminating SSL at the load balancer level is an issue because it can lead to security vulnerabilities. If the SSL certificate is not installed correctly, or if the load balancer is compromised, sensitive information can be leaked.
- Having only one MySQL server capable of accepting writes can be an issue because it can create a single point of failure. If the server fails, the website will be inaccessible until it is restored, leading to downtime and lost revenue.
- Having servers with all the same components (database, web server, and application server) might be a problem because it creates a single point of failure. If one server goes down, it can affect the performance of the entire system. It is better to have different types of servers with different roles to improve redundancy and scalability.

## How to Monitor QPS:

- To monitor QPS (Queries Per Second), we can use the monitoring tool to collect data on the number of queries processed by the database server per second. We can set up alerts to notify us if the QPS exceeds a certain threshold or if there is a sudden drop in the number of queries. We can also use the monitoring data to identify the cause of any performance issues and optimize the database server accordingly.
