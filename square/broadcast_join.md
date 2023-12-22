# Try to understand broadcasting data and cardinality

## Apache
Here's how a broadcast join works:
Data Broadcasting: The smaller table (or dataset) is broadcasted to all the worker nodes in the distributed system. Broadcasting means sending a copy of the smaller table to each node.
Data Shuffling: The larger table is divided into partitions based on a chosen join key (the column used to match rows from both tables). Each partition is sent to a specific worker node based on the value of the join key.
Local Join: Each worker node performs a local join between its partition of the larger table and the complete copy of the smaller table that it received during the broadcasting step. Since the smaller table is fully available on each node, there is no need for additional communication between nodes during the join operation.
Aggregation (if necessary): After the local join, the results from all the worker nodes are collected and combined to produce the final result of the join operation.


# Redshift
When you load data into a table, Amazon Redshift distributes the rows to each of the compute nodes according to the table’s DISTSTYLE. Within each compute node, the rows are assigned to a cluster slice. Depending on node type, each compute node contains 2, 16, or 32 slices. You can think of a slice like a virtual compute node. During query execution, all slices process the rows that they’ve had assigned in parallel. The primary goal in selecting a table’s DISTSTYLE is to evenly distribute the data throughout the cluster for parallel processing.

When you execute a query, the query optimizer might redistribute or broadcast the intermediate tuples throughout the cluster to facilitate any join or aggregation operations. The secondary goal in selecting a table’s DISTSTYLE is to minimize the cost of data movement necessary for query processing. To achieve minimization, data should be located where it needs to be before the query is executed.


## In favor of even distribution?

when selecting a DISTKEY ask yourself, Does the column data have a uniformly distributed data profile?

If the hashed column values don’t enable uniform distribution of data to the cluster slices, then you’ll end with both data skew at rest and data skew in flight (during query processing)—which results in a performance hit due to an unevenly parallelized workload. A nonuniformly distributed data profile occurs in scenarios such as these:

## When does skew happen
great reading: https://aws.amazon.com/blogs/big-data/amazon-redshift-engineerings-advanced-table-design-playbook-distribution-styles-and-distribution-keys/

Mostly from the article with my summary at the bottom.

Does the column data have a uniformly distributed data profile?
 

If the hashed column values don’t enable uniform distribution of data to the cluster slices, then you’ll end with both data skew at rest and data skew in flight (during query processing)—which results in a performance hit due to an unevenly parallelized workload. A nonuniformly distributed data profile occurs in scenarios such as these:

Distributing on a column containing a significant percentage of NULL values
Distributing on a column, customer_id, where a minority of your customers are responsible for the majority of your data
You can easily identify columns that contain “heavy hitters” or introduce “hot spots” by using some simple SQL code to review the dataset. In the example following, l_orderkey stands out as a poor option that you can eliminate as a potential DISTKEY column:

root@redshift/dev=# SELECT l_orderkey, COUNT(*) 
FROM lineitem 
GROUP BY 1 
ORDER BY 2 DESC 
LIMIT 100;
 l_orderkey |   count
------------+----------
     [NULL] | 124993010
  260642439 |        80
  240404513 |        80
   56095490 |        72
  348088964 |        72
  466727011 |        72
  438870661 |        72 

**In otherwords, if there's low cardinality or skewed data from nulls or heavy hitters or hot spots**

## Choosing a key as a distkey

Does the column data have high cardinality?
Cardinality is a relative measure of how many distinct values exist within the column. It’s important to consider cardinality alongside the uniformity of data distribution. In some scenarios, a uniform distribution of data can result in low relative cardinality. Low relative cardinality leads to wasted compute capacity from lack of parallelization. For example, consider a cluster with 576 slices (36x DS2.8XLARGE) and the following table:

CREATE TABLE orders (                                            
  o_orderkey int8 NOT NULL			,
  o_custkey int8 NOT NULL			,
  o_orderstatus char(1) NOT NULL		,
  o_totalprice numeric(12,2) NOT NULL	,
  o_orderdate date NOT NULL DISTKEY ,
  o_orderpriority char(15) NOT NULL	,
  o_clerk char(15) NOT NULL			,
  o_shippriority int4 NOT NULL		,
  o_comment varchar(79) NOT NULL                  
); 
Code
 

Within this table, I retain a billion records representing 12 months of orders. Day to day, I expect that the number of orders remains more or less consistent. This consistency creates a uniformly distributed dataset:

root@redshift/tpch=# SELECT o_orderdate, count(*) 
FROM orders GROUP BY 1 ORDER BY 2 DESC; 
 o_orderdate |  count
-------------+---------
 1993-01-18  | 2651712
 1993-08-29  | 2646252
 1993-12-05  | 2644488
 1993-12-04  | 2642598
...
...
 1993-09-28  | 2593332
 1993-12-12  | 2593164
 1993-11-14  | 2593164
 1993-12-07  | 2592324
(365 rows)
Code
However, the cardinality is relatively low when we compare the 365 distinct values of the o_orderdate DISTKEY column to the 576 cluster slices. If each day’s value were hashed and assigned to an empty slice, this data only populates 63% of the cluster at best. Over 37% of the cluster remains idle during scans against this table. In real-life scenarios, we’ll end up assigning multiple distinct values to already populated slices before we populate each empty slice with at least one value.

-- How many values are assigned to each slice
root@redshift/tpch=# SELECT rows/2592324 assigned_values, COUNT(*) number_of_slices FROM stv_tbl_perm WHERE name='orders' AND slice<6400 
GROUP BY 1 ORDER BY 1;
 assigned_values | number_of_slices
-----------------+------------------
               0 |              307
               1 |              192
               2 |               61
               3 |               13
               4 |                3
(5 rows)
Code
So in this scenario, on one end of the spectrum we have 307 of 576 slices not populated with any day’s worth of data, and on the other end we have 3 slices populated with 4 days’ worth of data. Query execution is limited by the rate at which those 3 slices can process their data. At the same time, over half of the cluster remains idle.

Note: The pct_slices_populated column from the table_inspector.sql query result identifies tables that aren’t fully populating the slices within a cluster.


On the other hand, suppose the o_orderdate DISTKEY column was defined with the timestamp data type and actually stores true order timestamp data (not dates stored as timestamps). In this case, the granularity of the time dimension causes the cardinality of the column to increase from the order of hundreds to the order of millions of distinct values. This approach results in all 576 slices being much more evenly populated.

Note: A timestamp column isn’t usually an appropriate DISTKEY column, because it’s often not joined or aggregated on. However, this case illustrates how relative cardinality can be influenced by data granularity, and the significance it has in resulting in a uniform and complete distribution of table data throughout a cluster.

**Pick a distkey that is joined or aggregated that also happens to have high cardinality or make the cardinality higher. When choosing your distkey , Choose the key based on how frequently it is joined and the size of the joining rows.Also check the distribution profile to ensure it is uniformly distributed. Ensure that the column does not have a significant amount of null values and also check the level of data skew after materializing a single column test table with a column as a distkey. Designate both the dimension table's primary key and the fact table's corresponding foreign key as the DISTKEY. The choice of your DIST key will be more important for what joins you will be doing with this table as this determines whether a distribution or broadcast will be needed**


## Choice of distkey with skew can be worse than without one
https://www.integrate.io/blog/amazon-redshift-distkey-and-sortkey/#mcetoc_1gparru4v1tr

- When such a skew occurs, the total query processing time takes much longer because the performance is capped by the slowest processing node; i.e., the query cannot be spread across multiple nodes. In this (extreme) case, almost all the rows were processed by a single node. That is why the query took longer than the query made against the table without a DISTKEY.

- The distribution key is used to distribute rows amongst servers. Preferably, when JOINing tables, they should have the same DISTKEY so that data is co-located on the same server and does not need to be sent between servers.

You will need to optimize for your most important table. It is not always possible to optimize for all tables and queries.
