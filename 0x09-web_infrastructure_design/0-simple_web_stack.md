
![simple_server](https://user-images.githubusercontent.com/111706856/221423027-756c4050-04cf-4951-af70-c220bfadfdd1.JPG)


Assume that a user opens their web browser and types in '''www.foobar.com'''.
The DNS server that the user's computer is configured to use will receive the request to resolve the domain name www.foobar.com to an IP address. The DNS server will respond with the IP address '''8.8.8.8''', which is the IP address of the server hosting the website.

Now, let's design the infrastructure.

## Server:
A server is a computer system that provides services to other computers or devices connected to a network. In this case, the server will be used to host the website for www.foobar.com.

## Domain name:
A domain name is a human-readable label that is used to identify a website. It is easier for people to remember and use domain names than IP addresses. In this case, the domain name is foobar.com, which will be configured with a www record that points to the IP address of the server hosting the website.

## DNS record:
The www record in www.foobar.com is a type of DNS record called a CNAME record. It maps the www subdomain to the domain name foobar.com.

## Web server:
Nginx is a popular web server software that will be used to serve the website's static content, such as HTML, CSS, and JavaScript files. Nginx will also handle the HTTP requests and responses between the user's browser and the server.

## Application server:
An application server is software that runs application code and provides services to clients over a network. In this case, the application server will be used to run the server-side code that generates dynamic content for the website, such as user data or database queries.

## Application files:
The application files contain the code base for the website. This includes the server-side code that will run on the application server and generate dynamic content.

## Database:
MySQL is a popular relational database management system that will be used to store and retrieve data for the website.

## Communication with user's computer:
The server will use the HTTP protocol to communicate with the user's computer. When the user types in www.foobar.com, their browser will send an HTTP request to the server. The server will respond with an HTTP response, which will contain the website's content.

# To discuss the issues with this infrastructure.

## Single point of failure (SPOF):
Since there is only one server hosting the website, if the server fails or goes down for maintenance, the website will be unavailable.

## Downtime during maintenance:
When deploying new code to the web server or performing maintenance on the server, the website will be unavailable during that time.

## Scalability:
If the website receives a lot of incoming traffic, the server may not be able to handle the load. To handle more traffic, additional servers or resources would need to be added to the infrastructure.

Overall, this infrastructure is a good starting point for hosting a website, but additional measures should be taken to address the issues mentioned above, such as implementing load balancing, redundancy, and a more scalable infrastructure.
