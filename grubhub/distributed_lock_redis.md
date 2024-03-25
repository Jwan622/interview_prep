# Dsitributed lock with redis

It's much better. You don't overload the database with long-running locks.

It's actually at the redis level, the lock. Not at the database level.

The benefit of implementing the distributed lock at the Redis level, rather than in a traditional relational database like PostgreSQL, primarily relates to the nature of distributed systems and the specific strengths of Redis. 

## How it works

Redis can manage distributed locks, often using a feature called RedLock or simple key expiration mechanisms. Here's how it typically works:

Acquiring the Lock:
A process attempts to acquire a lock by setting a key in Redis with a value representing the lock (e.g., a unique identifier for the session or transaction) and a TTL (Time to Live).
- The SET command in Redis can be used with NX (set if not exists) and EX (expiration time) options to ensure that the key is set only if it doesn’t already exist and to specify a TTL for the lock.

Checking the Lock:
- If the SET operation is successful, the process acquires the lock and proceeds with its operation (like booking a ticket).
- If the operation fails (the key already exists), it means another process has the lock, and the current process must wait or retry later.

Releasing the Lock:
- Once the operation is complete, the process releases the lock by deleting the key in Redis.
- It's crucial to ensure that a lock is released after the operation to prevent deadlocks or blocking other processes indefinitely.
- In a ticket booking system, the Redis lock prevents multiple services from attempting to book the same ticket simultaneously. Once a service acquires the lock and proceeds, it might then interact with PostgreSQL to update the ticket status, during which PostgreSQL handles transactional locks to maintain database consistency.

## Example

Imagine a scenario on Ticketmaster where two users attempt to book the last ticket for a concert at the same time:

- User A and User B send requests to book the ticket.
- Both services handling these requests attempt to acquire a distributed lock in Redis.
  - Let’s say User A’s request gets the lock first.
- User B’s service fails to acquire the lock and receives a message to retry or that the ticket is being booked.
- User A’s service, having acquired the lock, proceeds to book the ticket, interacting with PostgreSQL to update the ticket status.
- After booking the ticket, User A’s service releases the Redis lock. 

This mechanism ensures that even in a distributed system with many concurrent operations, only one process can perform a critical transaction at a time, preventing double bookings or order overlaps.

In summary, distributed locks in systems like Redis provide a mechanism to ensure mutual exclusion across distributed processes, crucial for maintaining consistency and preventing race conditions in systems where concurrent operations on the same resource occur.
