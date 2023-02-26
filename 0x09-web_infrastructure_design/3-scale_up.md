![scale_up](https://user-images.githubusercontent.com/111706856/221423782-3bb8a7c4-c047-40c1-b6d2-e29cc8513aa7.JPG)


# Scaled Up Web Infrastructure

## Description

This web infrastructure is a scaled up version of the previous infrastructure described [here](2-secured_and_monitored_web_infrastructure.md). In this version, all SPOFs have been removed and each of the major components (web server, application server, and database servers) have been moved to separate GNU/Linux servers. The SSL protection isn't terminated at the load-balancer and each server's network is protected with a firewall and they're also monitored.

## Specifics About This Infrastructure

+ Firewall: A firewall is added to provide an additional layer of security to the infrastructure. This helps to protect the servers from unauthorized access, block unwanted traffic, and detect and alert on suspicious activity.
+ By splitting components onto their own servers, we ensure that each server is dedicated to its own task, which improves performance and scalability. The use of two load balancers configured as a cluster provides high availability and ensures that if one load balancer fails, the other one will take over, preventing any disruption in the service. The use of a firewall provides an additional layer of security and helps to protect the servers from unauthorized access, block unwanted traffic, and detect and alert on suspicious activity. 


## Issues With This Infrastructure

+ High maintenance costs.<br/>Moving each of the major components to its own server, means that more servers would have to be bought and the company's electricity bill would rise along with the introduction of new servers.
