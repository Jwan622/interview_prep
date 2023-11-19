# High level of what to do in a constraint analysis interview

A few analysis to run when scoping a problem

1. traffic analysis
    - ask about DAU and average request per day
    - Say you have 100m DAU, and say each user 1 query per day. What's the query per second?
    - 100m = 100 * 10^6
    - 3600 seconds in an hour, 24 hours per day so 3600 * 24 seconds in a day. 
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

# System design question: Design spotify
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


# interview process
- ask questions and get key metric to help high level decision making
- bottleneck questions can be answered by caching, either by cdn or local caching or caching in the webserver.

# topics to study:
- load balancer
- CAP theorum

