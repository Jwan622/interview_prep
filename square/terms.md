[SCD - type 2](https://en.wikipedia.org/wiki/Slowly_changing_dimension)
[cardinality](https://www.actian.com/what-is-cardinality/)
    - When selecting a column to index or use as a basis for a partitioning key, you are looking for high cardinality candidates.
    - When partitioning a table based on ranges of data values, low cardinality can lead to data skew, resulting in uneven data distribution across partitions.  This isn’t good because you want to balance resource usage across all the available processors, not just a subset.

Why is skew bad?
    - When data is unevenly distributed across nodes, some nodes may be overloaded with excessive data, while others remain underutilized. The overall performance is limited by the slowest node. Skewed data can create bottlenecks on certain nodes, slowing down the entire data processing pipeline.
- [more on data skew](https://www.linkedin.com/pulse/challenges-skewed-data-join-hadoop-spark-benefits-broadcast-dip/)

- [broadcast join](./broadcast_join.md)
