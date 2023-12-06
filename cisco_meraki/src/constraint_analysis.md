# High level of what to do in a constraint analysis interview

A few analysis to run when scoping a problem

1. traffic analysis
    - ask about DAU and average request per day
    - Say you have 100m DAU, and say each user 1 query per day. What's the query per second?
    - 100m = 100 * 10^6
    - 60 seconds in a minute, 60 minutes in an our, so 3600 seconds in an hour, 24 hours per day so 3600 * 24 seconds in a day. 
    so 100 * 10^6 / (3600 * 24) is about 100 * 10^6 / 10^5 approx is 100 * 10^1 = 1000 qps (query per second)

That's how you do traffic analysis

2. storage analysis. How much storage do we need?
    - Say 100m DAU, 1 post per day, and 100 characters in the post.
    - so that means 100m * 100 storage per day needed
    - 100m * 100 bytes = 10gb (use online calculator)
    - in 5 years: 100m * 100 * 365 * 5, space needed  approx is 100m * 100 * 2000 = 10gb * 2000 => 20TB
    - 20tb of data storage needed

3. latency analysis. 
    - say 99% of query finished within 200ms. include this in the constraints analysis. latency from different parts.
    - latency could be from network, disk query, memory. understand these 3. Getting data from disk is expensive than memory. That's why we have a cache layer when we do data query design.
    
4. availability
    - not a very hard limitation. try to understand how many 9s we needed lol. do we need 99.99% system is available. So only a couple hours of downtime a year if 99.99%. CAP theorum says network partitioning for distributed system. you should care for availability and consistency. Have one but not the other? 

# System design question 1: Design spotify
- say you have 1 billion users, 100 million songs, 5mb per song so...
- let's convert to bytes. 100m * 1000 = 100b and then * 1000 again to convert to bytes = 100b * 1000 = 100 trillion bytes.
- multipy that by 5 for the mb and you get 500 trillion bytes which is 0.5 petabytes or 500 terabytes.
- maybe you have multiple copies in a raw layer so you have 3x replication, so you get 1.5 petabytes of raw audio data
- metadata is just a bit more, song title and artist, metadata isn't very big so 100 bytes per song.
- say you have 100 bytes per song of metadata, and 100m songs so 100,000,000 * 10bytes = 10gb (online calculator...remember 100 megabytes in a gigabyte and 1m bytes in a megabyte)
- users data might be 1kb per user.

Now move onto components
- got your phone and spotify app, draw one rectangle
- phone is talking to an application server somewhere
- servers could be many with a load balancer in between. so teh phone is talking to the load balancer and then talking to the web servers
- databases can be 2 types, s3 for audio immutable data (just blob storage of 5mb audio files) and rds for metadata about users and songs and artists.f
- also a database which is talking to the web servers
- if a bunch of poeple request a new BTS song when it's released, we might want to use a CDN for highly popular resources, to reduce the load on the DB and the web server. use a content delivery network, close to users in terms of network connections. close to the main app. the CDn connects teh app and the db. first time it's requested, the web server reads and streams it like normal from the DB. web servers have a heat map of recently requested songs. if the song is highly popular, then it might update the cache.
- the webserver could also have a local cache. if you loaded songs into memory, the web server could have a cache to store commonly played songs.
- you can make the load balancer more intelligent than just round robin. if a server has too many requests outstanding or is IO bound by network requests and they are piling up, then load balancer to another server. there are dfifferenet metrics you can use to load balance.


# Design question 2, design twitter
 - read heavy, less so write heavy.
 - we care more about availability above consistency. eventual consistency is fine. we need a super fast read function, to access our timeline in less than a second. similar to facebook, we care about speed from consistency perspective (if we tweet, someone else has to see it), but we care more about availability. really bad if someone can't access the network.
 - twitter uses in memory fanout. takes your tweet and recomputes the person who follows you home timeline. twitter uses redis. stored in RAM in redis.
- in between updating the redis lists, we can reach out to a sql database to get the tweeter's followers. we get the follower's IDs and then use those IDs to update the appropriate redis lists. This occurrspecs after the load balancer step.
 - in redis, it's home timelines, lists of tweets for a user. every user has one list per redis machine. twitter has 3 redis machines. bob has his a list of tweets in redis, in every 3 redis machine (just for replication). this helps availability, eventually they will all have same state.
 - If the tweeter has 100 followers, 300 updates are made to the 3 redis instances. if followers are active, their redis list gets updated, 3 times.
 

# interview process
- ask questions and get key metric to help high level decision making
- bottleneck questions can be answered by caching, either by cdn or local caching or caching in the webserver.

# topics to study:
- load balancer
- CAP theorum
- eventual consistency

## Cap theorum

The CAP theorem applies a similar type of logic to distributed systems—namely, that a distributed system can deliver only two of three desired characteristics: consistency, availability, and partition tolerance (the ‘C,’ ‘A’ and ‘P’ in CAP).

A distributed system is a network that stores data on more than one node (physical or virtual machines) at the same time. Because all cloud applications are distributed systems, it’s essential to understand the CAP theorem when designing a cloud app so that you can choose a data management system that delivers the characteristics your application needs most.


What is the CAP theorem?
Have you ever seen an advertisement for a landscaper, house painter, or some other tradesperson that starts with the headline, “Cheap, Fast, and Good: Pick Two”?
The CAP theorem applies a similar type of logic to distributed systems—namely, that a distributed system can deliver only two of three desired characteristics: consistency, availability, and partition tolerance (the ‘C,’ ‘A’ and ‘P’ in CAP).

A distributed system is a network that stores data on more than one node (physical or virtual machines) at the same time. Because all cloud applications are distributed systems, it’s essential to understand the CAP theorem when designing a cloud app so that you can choose a data management system that delivers the characteristics your application needs most.

The CAP theorem is also called Brewer’s Theorem, because it was first advanced by Professor Eric A. Brewer during a talk he gave on distributed computing in 2000. Two years later, MIT professors Seth Gilbert and Nancy Lynch published a proof of “Brewer’s Conjecture.”

 
More on the ‘CAP’ in the CAP theorem
Let’s take a detailed look at the three distributed system characteristics to which the CAP theorem refers.

Consistency

Consistency means that all clients see the same data at the same time, no matter which node they connect to. For this to happen, whenever data is written to one node, it must be instantly forwarded or replicated to all the other nodes in the system before the write is deemed ‘successful.’

Consistency of CAP theorem means that regardless of the node they connect to, all clients see the same data at once. For the write to one node to succeed, it must also instantly be replicated or forwarded to all the other nodes in the system. CAP theorem eventual consistency.

In a consistent system, all nodes see the same data simultaneously. If we perform a read operation on a consistent system, it should return the value of the most recent write operation. The read should cause all nodes to return the same data. All users see the same data at the same time, regardless of the node they connect to. When data is written to a single node, it is then replicated across the other nodes in the system.

Availability

Availability means that any client making a request for data gets a response, even if one or more nodes are down. Another way to state this—all working nodes in the distributed system return a valid response for any request, without exception.

When availability is present in a distributed system, it means that the system remains operational all of the time. Every request will get a response regardless of the individual state of the nodes. This means that the system will operate even if there are multiple nodes down. Unlike a consistent system, there’s no guarantee that the response will be the most recent write operation.

Partition tolerance

A partition is a communications break within a distributed system—a lost or temporarily delayed connection between two nodes. Partition tolerance means that the cluster must continue to work despite any number of communication breakdowns between nodes in the system.

When a distributed system encounters a partition, it means that there’s a break in communication between nodes. If a system is partition-tolerant, the system does not fail, regardless of whether messages are dropped or delayed between nodes within the system. To have partition tolerance, the system must replicate records across combinations of nodes and networks.



CA databases
CA databases enable consistency and availability across all nodes. Unfortunately, CA databases can’t deliver fault tolerance. In any distributed system, partitions are bound to happen, which means this type of database isn’t a very practical choice. That being said, you still can find a CA database if you need one. Some relational databases, such as PostgreSQL, allow for consistency and availability. You can deploy them to nodes using replication.

CP databases
CP databases enable consistency and partition tolerance, but not availability. When a partition occurs, the system has to turn off inconsistent nodes until the partition can be fixed. MongoDB is an example of a CP database. It’s a NoSQL database management system (DBMS) that uses documents for data storage. It’s considered schema-less, which means that it doesn’t require a defined database schema. It’s commonly used in big data and applications running in different locations. The CP system is structured so that there’s only one primary node that receives all of the write requests in a given replica set. Secondary nodes replicate the data in the primary nodes, so if the primary node fails, a secondary node can stand-in.

AP databases
AP databases
AP databases enable availability and partition tolerance, but not consistency. In the event of a partition, all nodes are available, but they’re not all updated. For example, if a user tries to access data from a bad node, they won’t receive the most up-to-date version of the data. When the partition is eventually resolved, most AP databases will sync the nodes to ensure consistency across them. Apache Cassandra is an example of an AP database. It’s a NoSQL database with no primary node, meaning that all of the nodes remain available. Cassandra allows for eventual consistency because users can resync their data right after a partition is resolved.

## Use of CDNs

CDN
A CDN is a network of servers that distributes content from an “origin” server throughout the world by caching content close to where each end user is accessing the internet via a web-enabled device. The content they request is first stored on the origin server and is then replicated and stored elsewhere as needed. By caching content physically close to where a user is and reducing the distance it has to travel, latency is reduced. This process also decreases stress on origin servers by distributing the load geographically across multiple servers.



## Load balancers

When a website becomes extremely popular, the traffic on that website increases, and the load on a single server also increases. The concurrent traffic overwhelms the single server and the website becomes slower for the users. In order to meet the request of these high volumes of data and to return the correct response in a fast and reliable manner, we need to scale the server. This can be done by adding more servers to the network and distributing all the requests across these servers.  But….who is going to decide which request should be routed to which server…??? 

The answer is…Load Balancer.  Let’s understand the concept of a load balancer in detail… 

What is a Load Balancer?
A load balancer works as a “traffic cop” sitting in front of your server and routing client requests across all servers. It simply distributes the set of requested operations (database write requests, cache queries) effectively across multiple servers and ensures that no single server bears too many requests that lead to degrading the overall performance of the application. A load balancer can be a physical device or a virtualized instance running on specialized hardware or a software process. 
Consider a scenario where an application is running on a single server and the client connects to that server directly without load balancing. It will look something like the one below…

Without a load balancer:
We need to discuss the two main problems with this model…

- Single Point of Failure: If the server goes down or something happens to the server the whole application will be interrupted and it will become unavailable for the users for a certain period. It will create a bad experience for users which is unacceptable for service providers.
- Overloaded Servers: There will be a limitation on the number of requests that a web server can handle. If the business grows and the number of requests increases the server will be overloaded. To solve the increasing number of requests we need to add a few more servers and we need to distribute the requests to the cluster of servers. 
To solve the above issue and to distribute the number of requests we can add a load balancer in front of the web servers and allow our services to handle any number of requests by adding any number of web servers in the network. We can spread the request across multiple servers. For some reason, if one of the servers goes offline the service will be continued. Also, the latency on each request will go down because each server is not bottlenecked on RAM/Disk/CPU anymore.

