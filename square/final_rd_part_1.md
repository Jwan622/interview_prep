# Data Modeling, ETL & Data Architecture

## Efficient data modeling design (from requirement gathering, determining the right questions to ask, data onboarding case study)
What Data Sources Are Available?
Identify the various data sources, such as transaction databases, website clickstreams, customer surveys, and social media interactions.

What Are the Business Goals?
Understand the specific objectives, such as increasing customer retention, optimizing marketing spend, or personalizing product recommendations.

What Are the Key Metrics and KPIs?
Determine the critical performance indicators that the analytics platform needs to track, such as customer lifetime value, conversion rates, and customer churn.

Data Volume and Velocity:
Assess the volume and velocity of data. How much data is generated daily, and how frequently does it need to be updated? This will guide your choices for data storage and processing technologies.

Data Quality and Cleansing:
Investigate the quality of the data sources. Are there issues with missing or inconsistent data? Plan for data cleansing and transformation.

Data Security and Compliance:
Are there any data privacy regulations (e.g., GDPR or CCPA) that need to be adhered to? Ensure that the data modeling and storage comply with these regulations.

User Access and Permissions:
Define who in the organization will have access to the analytics platform and what level of permissions they require. This is crucial for data security.

Scalability and Performance:
Consider future scalability requirements. How will the platform handle increased data volume and user load over time?

Technology Stack:
Based on the data sources and requirements, select the appropriate technology stack. This might include databases, data warehousing solutions, ETL tools, and analytics platforms.

Data Governance and Documentation:
Establish data governance practices, including data naming conventions, data dictionaries, and documentation of data transformations and models.

## Case Study

Case Study: Building a Healthcare Analytics System

1. Requirement Gathering:

You've been tasked with developing a Healthcare Analytics System for a hospital. The objective is to improve patient care, optimize resource allocation, and enhance overall hospital operations.
2. Ultimate Questions to Ask Before Data Modeling:

Data Sources:

What are the primary data sources in the healthcare domain, such as electronic health records (EHRs), laboratory results, billing data, and patient demographics?
Do we have access to external sources like public health databases or research studies for broader insights?
Business Objectives:
What are the primary goals of the analytics system? Are we focusing on reducing readmission rates, optimizing staffing levels, or identifying high-risk patients?

Key Metrics and KPIs:
Which healthcare metrics are crucial, such as patient outcomes, length of stay, and cost per case?
What are the key performance indicators (KPIs) that hospital administrators and clinicians need to track?

Data Volume and Real-time Needs:
How much data is generated daily, and do we require real-time access to certain data, such as vital signs or patient admissions?
Will we need to implement data streaming technologies?

Data Quality and Compliance:
How do we ensure the accuracy and completeness of medical records?
What privacy and compliance standards (e.g., HIPAA) must we adhere to, and how will we secure patient data?

User Access and Roles:
Who will be using the system? Define roles and permissions for healthcare providers, administrators, and analysts.
What level of data access is appropriate for each role?

Scalability and Disaster Recovery:
How do we plan for scalability as the hospital expands or acquires new facilities?
What disaster recovery measures are in place to ensure data availability in case of emergencies?

Technology Stack:
What database systems, ETL tools, and analytics platforms are suitable for handling healthcare data and analytics?
Consider factors like interoperability with EHR systems.

Data Governance and Ethics:
Establish data governance practices, including data stewardship, data lineage tracking, and ethical considerations for data usage.

3. Data Onboarding and Modeling:
Data onboarding involves extracting data from various sources (EHRs, billing systems, etc.), transforming it into a usable format, and loading it into the chosen data storage system.
Data modeling design may include creating a healthcare data warehouse with tables for patients, diagnoses, treatments, and medical staff.
Implement measures for data anonymization and de-identification to protect patient privacy.
Consider designing dashboards and reports that provide actionable insights for healthcare professionals.
This case study highlights the critical questions and considerations before embarking on data onboarding and modeling for a healthcare analytics system. If you'd like to explore any specific aspect in more detail or have questions about the technical implementation, feel free to ask for additional information or code examples.



## ETL Development Lifecycle:

Requirement Gathering: Start by understanding the business needs and data requirements. Work closely with stakeholders to define what data needs to be extracted, transformed, and loaded.

Data Extraction:

Identify the source systems where data resides, such as databases, APIs, flat files, or streaming platforms.
Design data extraction processes to retrieve relevant data efficiently.
Consider scheduling and data change detection mechanisms.
Data Transformation:

Cleanse and validate the extracted data to ensure data quality.
Apply transformations like aggregations, joins, filtering, and enrichment to prepare the data for its destination.
Implement business logic and data mapping as required.
Data Loading:

Determine the destination, which can be a data warehouse, database, or data lake.
Load the transformed data into the destination using appropriate methods like batch or real-time loading.
Handle data integrity and error handling during loading.
Testing and Quality Assurance:

Perform thorough testing, including unit testing for individual ETL components and integration testing for the entire ETL pipeline.
Validate data accuracy and consistency throughout the process.
Implement logging and monitoring for error detection.
Deployment:
Deploy ETL processes to the production environment, considering scalability and performance requirements.
Set up scheduling and orchestration to automate ETL job execution.

Maintenance and Monitoring:
Continuously monitor ETL pipelines for data issues, errors, and performance bottlenecks.
Handle updates to source systems and data schema changes gracefully.
Maintain documentation and version control.

ETL Optimization:

Performance Tuning:
Profile your ETL processes to identify performance bottlenecks. Tools like query optimizers and monitoring dashboards can help.
Optimize SQL queries, indexing, and data loading strategies to reduce processing time.

Parallel Processing:
Implement parallel processing to distribute the workload across multiple processors or nodes.
Use distributed computing frameworks like Apache Spark for large-scale data processing.

Data Partitioning:
Partition large datasets to improve query performance. Partitioning can be based on time, region, or other relevant criteria.

Caching and Materialized Views:
Use caching mechanisms or materialized views to store intermediate results, reducing redundant computations.
ETL Code Refactoring:
Regularly review and refactor ETL code to enhance maintainability and reduce complexity.
Eliminate redundant transformations and optimize data flow.

Debugging ETL Processes:

Logging and Monitoring:
Implement comprehensive logging to capture errors, warnings, and processing steps.
Set up monitoring tools to alert you when issues occur.

Data Profiling:
Profile data at various stages of the ETL process to identify data quality problems or anomalies.
Use data profiling tools to automate this process.


## ETL vs ELT

- ETL transforms data on a separate processing server, while ELT transforms data within the data warehouse itself.
- ETL does not transfer raw data into the data warehouse, while ELT sends raw data directly to the data warehouse.

### What is ELT

Data is extracted from a source system, loaded into a destination system, and transformed inside the destination system. 

### What is ETL
Data is extracted from a source system, transformed on a secondary processing server, and loaded into a destination system. 

### Benefits of ETL
On the other hand, ETL is ideal for compute-intensive transformations, systems with legacy architectures, or data workflows that require manipulation before entering a target system, such as erasing personal identifying information (PII). Sometimes this happens unintentionally. But with ETL, you will reduce the risk of transferring non-compliant data. Why? Because of the data pipeline, meaning the data is cleaned and filtered before it leaves its initial destination.
- The reasons we had ETL before was because storage particularly cloud storage was expensive so you had to limit the data you were writing in your warehouse to keep costs down. There was loads of benefits for this, the data models were usually well defined, things were built properly by necessity.

### Downsides of ELT
- Enter cheaper storage in recent times and suddenly you got ELT. You extract the raw data from source and dump it into your datalake/dwh. 
- Upside you can chop and change schemas at will since the source data always exists. Downsides less focus on data modelling since everyone is just dumping data into the warehouse and its a free for all.
- **practical example of ELT downsides, i've recently had to process 3.3Tb worth of data on snowflake in one table in one variant column. When it was made two years ago the original creator found it easier to just extract and dump the one stream into the table then create downstream tables later. This is all well and good initially but 2 years later the data grew and their query time grew with it. So it cost me 8 hours to deconstruct the variant type into a better model that can better server its downstream assets.

Most pipelines are EtLT. The t being "tweak" for some data cleaning, PII removals, etc. YMMV depending on use case.

## Some tips:
https://towardsdatascience.com/5-helpful-extract-load-practices-for-high-quality-raw-data-65b9a59a8721

But here are a few that stood out:

1. Make each EL run uniquely identifiable — timestamp everything
We start with arguably the most important best practice: Make every bit of data you load into your data system identifiable and traceable back to the process that got it there.

Typical ways of doing this are to include metadata values that capture:

- Ingestion time: the timestamp indicating when the load process started.
- Ingestion process: a unique identifier representing the load process and its instance.
- Source system: Metadata about where the data was extracted from.

2. Deduplicate data at a level beyond the raw level
There are usually three cases of duplicate data hitting your data systems you will want to “deduplicate.” But no matter the case, don’t do it at the raw/landing level!

The first case is intentional duplicate data, where a source system contains something your end-users or you consider duplicated. For instance, your CRM system might have two entries for a certain customer that canceled and signed up again. If you deduplicate at the raw level, this means either merging the two or deleting one. Both of which will delete data that is present in the source system.

The second case is unintentional duplicate data, where the source system either deletes a record you still have in your data warehouse or the source system unintentionally produces duplicate data it will likely delete in the future. Even though this is an “error,” I don’t recommend deleting this data in your raw ingestion area but rather filter it further down the line, for instance, in the next stage of your modeling. Otherwise, you add logic to your ingestion that is hard to follow up on later.

The third case is duplication happening due to technical restrictions. It might be the case that your ingestion tooling prefers an “at least once delivery” strategy, or it might even be a bug in an ingestion process. With “at least once delivery” incremental load strategies, you’re ensuring to get all data rows but might duplicate some. Again we recommend keeping the duplicate data at the raw level and filtering it down at a later level.

3. Don’t flatten during EL, do it one stage later
Many source systems you ingest will return arrays, JSONs, or other nested objects with some hierarchy you want to break down for further processing. But not at the ingestion level. Take the raw data and dump it as it is in your data system, then have a process do your “flattening.”

A very typical example is JSON objects. Your source might contain a large JSON object, and you would like to have it processed into individual columns inside your Snowflake database. This practice suggests first having a raw table with just your metadata columns and one “JSON_blob” column containing the JSON object. In a second step, you can then process this data into columns.

The reason for this is that flattening involves business logic. It involves you knowing what properties are “always there.” If you flatten on ingestion, your ingestion process might break because one JSON object is NULL, or one JSON object doesn’t come with one expected value. It is always easier to take the already ingested data and rerun your flattener than to run your ingestion + flattening process together.

## Some other topics

### Schema on read vs schema on write
Schema-on-Write is associated with Relational Database Schema
Databases have employed a Schema-on-Write paradigm for decades, that is, the schema/table structure is first defined up front and then the data is written to the said schema as a part of the write process. Once the data has been written to the schema it is then available for reading, as such it’s named Schema-on-Write.

ETL from relational databases needs Schema-on-Write. The Schema-on-Write approach means the tables must be created first and schemas configured before data can be ingested. Relational databases have structured data whose structure is known in advance, so you can create tables accordingly, defining columns, data formats, column relationships at destination before the data is uploaded and available for analytical queries.

Schema-on-Read is associated with the rise of Data Lakes
Schema-on-Read has come about in conjunction with the rise of data lakes primarily for data science use cases and Machine Learning models. Here the raw data is first landed in its native form (structured and/or unstructured) with no imposed schema. Only once the data is read is the schema is applied, hence Schema-on-Read. Schema-on-Read is the opposite of Schema-in-Write. With the Schema-on-Read approach, the schema is created only when the data is read and not before data ingestion. Data schema are created while the ETL process is carried out. This enables raw, unstructured data to be stored in the database

DBT, by virtue of its models and file names, does Schema-On-Read

### Schema on read
The schema-on-read concept counterbalances the schema-on-write construct. The database schema is created when the data is read. The data structures are not applied or initiated before the data is ingested into the database; they are created during the ETL process. This enables unstructured data to be stored in the database (much like our jsonb columns during into DBT models and tables at Hinge).

The primary reason for developing the schema-on-read principle is the exploding growth of unstructured data volumes and the high overhead involved during the schema-on-write process. 

One example of a schema-on-read data loading process: Using Upsolver SQLake and  Amazon Athena to ingest and analyze raw data stored in an Amazon S3 data lake. Amazon Athena is a SQL engine that runs on top of the S3 data lake; you write SQL statements to query the data in the database:


### How does schema on read even work?

- The schema is inferred from the raw data, using SQlake to parse and stream the data and Amazon Glue Data Catalog to connect the metadata, schema, and data. 
- Athena then runs a SQL query to analyze the data in the data lake.
- As the query runs, SQLake ingests the data based on the schema-on-read principle. The ETL layer creates the database schema based on the schema-on-read.  The result: if your data lake contains live data, by using the schema-on-read construct new fields are added to the database schema as the data is loaded.

In this context let’s revisit the example of the taxi:

- The transactional data with details about each trip a taxi driver makes is loaded into an S3 data lake in near real-time. Most of the data is the same.
- At some point new data is added to this feed – for example, weather details for each trip. Until this point, the software application that records trip data only recorded general weather information such as snow, rain, or sunshine. The new data includes the precipitation amount, the time of day it fell, and how long it lasted.
- The schema-on-read process automatically creates new fields in the trip database table and ingests the data.

### Benefit of schema on read

Schema-on-Read is much faster than Schema-on-Write since the schema does not need to be defined prior to loading. This is a huge advantage in a big data environment with lots of unstructured data. The Schema-on-Read process can scale up rapidly as per requirement and can consume vast volumes of data in quick time, since it is not constrained by data modelers required in the case of a rigid database. 

When schema is generated on write, the schema comes before the data. A very common schema on write scenario is that a data engineer creates several tables in a relational database that are connected by primary keys with a rigid schema. Then, the data engineer populates the table with data. In a schema on read scenario, different types of data, potentially both structured and unstructured, are loaded into the destination, and the schema is generated when queries against the data are executed. This means the data engineer can spend more time crafting queries to gain better insights rather than spending all of their time carefully defining fields.

Based on the information described above, it is reasonable to assume that the schema-on-read principle is superior to the schema-on-write principle, especially in an environment where there are large amounts of unstructured data, such as the data that falls within the Big Data ambit.

Not only is the schema-on-read process **faster** than the schema-on-write process, but it also has the capacity to scale up rapidly. The reason being is that the schema-on-read construct does not utilize data modelers to model a rigid database. It consumes the data as it is being read and is suitable for massive volumes of unstructured data.  

Handles schema drift naturally.

## What is data management
Succinctly stated, “data management is the process of ingesting, storing, organizing, and maintaining the data created and collected by an organization.” Juxtapositionally, the lack of data management leads to incompatible data silos, inconsistent data sets, data swamps instead of data lakes, and data quality problems, resulting in the limited ability of BI (Business Intelligence) and analytics applications to produce correct and viable information. 

## What is data partitioning
Data Partitioning in Data Lakes is the practice of dividing data sets into smaller, more manageable parts based on specific criteria, such as time, location, or any other relevant attribute. This technique creates a logical structure within a data lake, enabling efficient data retrieval and analysis.

Data Warehouse Partitioning is a technique used in data warehousing to improve query performance and optimize resource utilization. By dividing large tables into smaller, more manageable units called partitions, businesses can significantly reduce processing time and achieve better query response.

### How partitioning works
folders where data is stored on S3, which are physical entities, are mapped to partitions, which are logical entities, in a metadata store such as Glue Data Catalog or Hive Metastore. As covered in AWS documentation, Athena leverages these partitions in order to retrieve the list of folders that contain relevant data for a query.

Data is commonly partitioned by time, so that folders on S3 and Hive partitions are based on hourly / daily / weekly / etc. values found in a timestamp field in an event stream. Here’s an example of how Athena partitioning would look for data that is partitioned by day:

Athena matches the predicates in a SQL WHERE clause with the table partition key. The best partitioning strategy enables Athena to answer the queries you are likely to ask while scanning as little data as possible, which means you’re aiming to filter out as many partitions as you can.

For example – if we’re typically querying data from the last 24 hours, it makes sense to use daily or hourly partitions. Monthly partitions will cause Athena to scan a month’s worth of data to answer that single day query, which means we are scanning ~30x the amount of data we actually need, with all the performance and cost implication.

Suppose you want to run the following query: select count(*) from the_table where country = 'Angola'. This query will run faster if the data lake is partitioned by the country column. The query engine only needs to list and read the data files in the country='Angola' directory. It can skip the data files in the other directories.

Engines need to run file listing operations to determine the files that must be read for different queries. Hive-style partitioning allows the query engine to read less files for certain queries.

For a query like select count(*) from the_table, the Hive-style partitioning doesn’t allow for any data skipping, so the query won’t run any faster. The Hive-style partitioning can actually make queries that can’t leverage data skipping run far slower.

### How to partition
 Partition columns are usually designed by a common query pattern in your use case. For example, a common practice is to partition the data based on year/month/day because many queries tend to run time series analyses in typical use cases. This often leads to a multi-level partitioning scheme. Data is organized in a hierarchical directory structure based on the distinct values of one or more columns.

Let’s look at an example of how partitioning works.

Files corresponding to a single day’s worth of data are placed under a prefix such as s3://my_bucket/logs/year=2023/month=06/day=01/.

If your data is partitioned per day, every day you have a single file, such as the following:

s3://my_bucket/logs/year=2023/month=06/day=01/file1_example.json
s3://my_bucket/logs/year=2023/month=06/day=02/file2_example.json
s3://my_bucket/logs/year=2023/month=06/day=03/file3_example.json
We can use a WHERE clause to query the data as follows:

SELECT * FROM table WHERE year=2023 AND month=06 AND day=01
The preceding query reads only the data inside the partition folder year=2023/month=06/day=01 instead of scanning through the files under all partitions. Therefore, it only scans the file file1_example.json.

Systems such as Athena, Amazon Redshift Spectrum, and now AWS Glue can use these partitions to filter data by value, eliminating unnecessary (partition) requests to Amazon S3. This capability can improve the performance of applications that specifically need to read a limited number of partitions. 


**it's also est to use system or server time instead of client time because clients might be down or send data late. So in order to not have to handle late arriving data (maybe months later), we should use the server's received time as the partitiong time so we don't have to handle late arriving data. The late arriving client data would still be in a current partition in the data lake but still retain its client time column.**

## Benefits of partitioning
Reducing query execution time and improving performance
Optimizing resources and minimizing operational costs
Data Warehouse Partitioning can substantially improve query performance by reducing data scanning, pruning irrelevant partitions, and facilitating parallel processing. However, the performance benefits depend on the proper design and implementation of partitioning strategies.


## Partitioning on s3

Large organizations processing huge volumes of data usually store it in Amazon Simple Storage Service (Amazon S3) and query the data to make data-driven business decisions using distributed analytics engines such as Amazon Athena. If you simply run queries without considering the optimal data layout on Amazon S3, it results in a high volume of data scanned, long-running queries, and increased cost.

## Hive style

If you look at the Athena documentation you often see data organized with paths that contain key value pairs, like country=fr/… or year=2020/month=06/day=26/…. This is Hive style (or format) partitioning. The paths include both the names of the partition keys and the values that each path represents. It can be convenient and self documenting, but it’s also uncommon to see it outside outside the Hadoop and Hive ecosystem, where it originated.

A self-documenting scheme
Consider a file listing like this one:

```
data/day=2020-04-20/country=fr/7fc6742c.json
data/day=2020-04-20/country=ir/80af7e0c.json
data/day=2020-04-20/country=se/f76c0d8f.json
data/day=2020-04-20/country=us/cf7e76b9.json
data/day=2020-04-21/country=af/cb81aacf.json
data/day=2020-04-21/country=ch/6b8ea57f.json
data/day=2020-04-21/country=fr/0c8e74a2.json
data/day=2020-04-21/country=us/68af2b83.json
```

You can probably guess that the data is partitioned by day and country just by looking at the file paths. The benefit of this style is that it is more or less self-documenting. Both humans and computers can see how the data is partitioned, and select only the files relevant for a query that includes conditions on day and country.

If you are starting from scrach and have full control over how the data in your data lake is organized, this is a good convention to follow, and it is understood by many tools in the Hadoop ecosystem.

Often, though, you don’t fully control the way data is produced and organized, and most tools outside of the Hadoop world don’t organize data using the Hive style. Instead, you probably get files organized like this:

```
data/2020-04-20/fr/7fc6742c.json
data/2020-04-20/ir/80af7e0c.json
data/2020-04-20/se/f76c0d8f.json
data/2020-04-20/us/cf7e76b9.json
data/2020-04-21/af/cb81aacf.json
data/2020-04-21/ch/6b8ea57f.json
data/2020-04-21/fr/0c8e74a2.json
data/2020-04-21/us/68af2b83.json
```

This listing has the same files, and if you were presented with this listing you would still figure out how it was organized. This is probably also how most people would organize this data set if given no specific instructions. As long as there is some documentation on what the path components mean it’s also not really any worse than the Hive style, except that Hive-aware tools can’t use it directly.

Another variant that is fairly common, and used by, for example, CloudTrail and Kinesis Firehose is using separate path components for the date parts, e.g. data/2020/04/20/fr/7fc6742c.json.


## Partitioning data in Athena
https://docs.aws.amazon.com/athena/latest/ug/partitions.html

By partitioning your data, you can restrict the amount of data scanned by each query, thus improving performance and reducing cost. You can partition your data by any key. A common practice is to partition the data based on time, often leading to a multi-level partitioning scheme. For example, a customer who has data coming in every hour might decide to partition by year, month, date, and hour. Another customer, who has data coming from many different sources but that is loaded only once per day, might partition by a data source identifier and date.

Athena can use Apache Hive style partitions, whose data paths contain key value pairs connected by equal signs (for example, country=us/... or year=2021/month=01/day=26/...). Thus, the paths include both the names of the partition keys and the values that each path represents. To load new Hive partitions into a partitioned table, you can use the MSCK REPAIR TABLE command, which works only with Hive-style partitions.

Athena can also use non-Hive style partitioning schemes. For example, CloudTrail logs and Kinesis Data Firehose delivery streams use separate path components for date parts such as data/2021/01/26/us/6fc7845e.json. For such non-Hive style partitions, you use ALTER TABLE ADD PARTITION to add the partitions manually.



# NoSQL vs SQL

In contrast, NoSQL databases were designed for unstructured data. As explained previously, these can be column-oriented databases, graph databases, document stores, or key-value stores.
In NoSQL databases, data is stored together (not separately, as with SQL). This means that it’s faster to perform read or write operations on one data entity compared with SQL databases.
Essentially, SQL is great for protecting data validity, whereas NoSQL is ideal for when you need fast availability of big data.

NoSQL is great for just fast lookups of non-relational data, it stores all the data together in a document.

NoSQL is a type of database that does not use the traditional table-based structure of relational databases. Instead, it uses a more flexible schema-less design. This means that data can be stored in any format and there is no need to predefine the structure of the data beforehand. NoSQL databases are often used for big data applications where scalability is important. They can also be used for real-time web applications where data needs to be accessed quickly.

## NoSQL benefits:
1. Fast queries
With NoSQL, it’s faster to run queries on large data sets. SQL can also be fast, but its speed becomes hampered as the database grows. This does not happen with NoSQL databases since they don’t require joins.

2. Resilient and stable
Because NoSQL data is spread over many regions and servers, there is no single point of failure. This means they provide zero downtime and continuous availability.

3. Cheaper in comparison
Since you can scale NoSQL databases horizontally by adding servers, you can expand them relatively cheaply. You should be able to find affordable options regardless of your organization’s needs.

4. Agile 
Rows and columns don’t stifle NoSQL databases, so they can handle all kinds of data, such as unstructured, structured, and polymorphic data.


