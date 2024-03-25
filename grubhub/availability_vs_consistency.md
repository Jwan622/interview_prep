# Availability
Availability in a distributed system refers to the system's ability to remain accessible and operational, even during failures or network partitions. High availability means the system can serve requests and perform operations despite some components being down.


# Consistency
Consistency means that all nodes (or clients) see the same data at the same time. In a consistent system, any read operation will return the most recent write.

# What gets in the way of having both?

These two concepts are often balanced against each other, as highlighted in the CAP theorem (Consistency, Availability, Partition tolerance). The theorem posits that in the presence of a network partition (P), a distributed system can offer either Consistency (C) or Availability (A) but not both simultaneously.


- availibility: replication of data across nodes means you have to update them. That's hard to do and would lead to weak consistency or eventualy consistency.


## Example

Consider an e-commerce application that uses Redis for caching product information to speed up read operations.

Availability Focus:

If the application prioritizes availability, it will ensure that product information is always accessible, **even if it's not the latest**. For example, during a network partition, the application might continue serving product data from the Redis cache, even if it cannot connect to the main database to get updated data. This approach maximizes uptime but might show outdated information to users.

Consistency Focus:

If consistency is the priority, the application will only show product information that is guaranteed to be up-to-date. If the application cannot confirm that the cached data in Redis is current (perhaps due to a network partition preventing updates), it might refuse to serve the cached data, ensuring users only see consistent and accurate data, but possibly at the expense of availability.

### Other considerations when deciding on caching
CAP Theorem Consideration:

For an e-commerce system, certain parts, like product listings, might prioritize availability (allowing users to see product pages even if some backend systems are down), while the checkout process might prioritize consistency to ensure accurate pricing and inventory data.

Read vs. Write Ratio:

An e-commerce system is typically read-heavy; users browse many products for every purchase made. Caching systems like Redis are particularly beneficial here to quickly serve these frequent read requests and reduce load on the primary database.

Query Access Pattern:

Access patterns might have regular bursts during specific periods, like holiday sales or flash sales events. This requires the system to scale dynamically to handle sudden increases in load, possibly by leveraging additional caching or temporarily provisioning more resources.
