
# Data Contract


## Background
A data contract acts as an agreement between multiple parties; specifically, a data producer and its consumer(s). Data contracts reduce surprise; this contract explicitly lays out how the data will be stored in warehouses and brokers as expected by their consumers. 

A contract is an agreement between data producers, who produce the data (like software engineers and platforms), and data consumers, who use the data (like data engineers and data scientists). It dictates how data should be organized so that it can be used effectively by downstream processes, like data pipelines. Often, the software engineers working for data producers do not understand the specific data consumer requirements of each data team or organization using their product. To bridge this gap, you can implement a data contract.

This example contract serves as a statement of data expectation between backend, data engineering, and data scientists. This contract documents the data to be landed in Kafka which is an intermediary broker between backend and data engineering. This contract also documents how the data will be stored/sorted/distributed in the data warehouse by data engineering and the expected usage of the data by data scientists. This will facilitate development and reduce surprise among the involved teams.


## Data Science Contract
The expected query and usage the table outline here is done early on in the sprint planning so that data engineering knows how to sort/dist the data.

**Data Requested**: We want to know the messages sent between the user and the subject on the dating app. The messages will be used for the Bad Actor service and to track phone number and social media exchanges which will aid our recommender.

Expected Query:
```sql
Select * from interactions.messages 
WHERE created_at BETWEEN 2023-06-01 AND 2024-01-30
```

**SLA**: Hourly data so that our Bad Actor service and Recommendations services can be accurate and up-to-date.

**Slowly Changing Dimensions**: Type 1 (update only is fine) or Type 2 (historical or audit) data?

## Backend Contract
This section details the message stored in the kafka topic for data engineering ELT pipelines to consume and ultimately move to the data warehouse. The data fields describe the data and the type of its fields. An example is also provided to show how it’s stored in Kafka.

**Kafka Topic**: <some topic name here>, 4 partitions.  
**Traffic Expectation**: 30,000 messages per day  
**Data Format**: JSON or Protobuf  
**PII present?**: False  
**Data Fields**:  
```text
user_id   Varchar(128)   The user who sent the message
subject_id   Varchar(128)  The user who received the message
message_text varchar(2056)  The content of the message sent
status  varchar(16)  opened/unread/archived
cloudinary_url   varchar(64)   If a voice message, the url for the CDN content
length_seconds   int     If a voice message, length of the voice message, stored in seconds. Can be from 0-60 seconds.
created_at   timestamp    Time that the message was created
updated_at   timestamp    Time that the message was last updated
```



Example:
```json
{
	“user_id”: 1234,
	“subject_id”: 5678,
	“message_text”: “Please date me”,
	“status”: “opened”,
	“cloudinary_url”: “https://someCdnUrlGoesHereWhereTheVoiceTextIsStored.com”,
	“length_seconds”: 30
	“created_at”: 2023-10-31T03:58:22Z,
	“updated_at”: 2024-01-01T04:21:08Z,
}
```

## Data Engineering Contract
This section describes the data warehouse table, including the sort/dist keys of the table and meta information about the data. Metafields are useful in case of a bug (can more easily track down the bug) or a necessary rerun of data.

**Schema**: interactions  
**Table Name**: messages  
**Backfillable?**: No  
**Distribution Key**: user_id  
**Sort Key**: created_at  
**Data Fields**:  

```text
user_id  Varchar(128)  The user who sent the message
subject_id   Varchar(128)  The user who received the message
message_text   varchar(2056)  The content of the message sent
status   varchar(16)   opened/unread/archived
cloudinary_url    varchar(64)    If a voice message, the url for the CDN content
length_seconds   int    If a voice message, length of the voice message
created_at   timestamp    Time that the message was created
updated_at    timestamp    Time that the message was last updated
metafield_insert_time   timestamp     Time that the message was inserted into the redshift table
metafield_process_id    varchar(32)    The ELT process that inserted the row
metafield_source_id    varchar(32)    The name of the source of the data (perhaps a kafka topic or s3 bucket or api endpoint)
```



