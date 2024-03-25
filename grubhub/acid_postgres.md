# Postgres and ACID transactions

# What is ACID

ACID is an acronym representing four key properties of transactions in a database management system: Atomicity, Consistency, Isolation, and Durability. These properties ensure that database transactions are processed reliably. PostgreSQL, being a robust and widely-used relational database, fully supports these ACID properties. Here's how each of these properties is implemented in PostgreSQL:

## Atomicity
Atomicity guarantees that all operations within a transaction are treated as a single unit. This means that either all operations succeed, or none of them are applied.
In PostgreSQL, atomicity is achieved through the use of transaction logs. If a transaction is successfully completed, it is committed and all its changes are made permanent. If the transaction fails at any point, it is rolled back, and all changes are undone to bring the database back to its original state before the transaction started.

## Consistency
Consistency ensures that a transaction brings the database from one valid state to another, maintaining all predefined rules, including integrity constraints, cascades, triggers, and any combination thereof.
PostgreSQL enforces consistency by implementing constraint checks, such as foreign key constraints, check constraints, unique constraints, and not-null constraints. Before a transaction is committed, all these constraints are checked to ensure that the changes are valid.
