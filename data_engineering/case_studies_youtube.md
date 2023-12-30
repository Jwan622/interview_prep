# Case studies
Going over through some case studies found on youtube

## Spotify

https://www.youtube.com/watch?v=0WJZ5wtQRWI

[learnings](https://youtu.be/0WJZ5wtQRWI?t=1139)
- each event has its own topic in kafka
- pushing more of the work onto producer means less time spent in converting the format in ETL later in the process. Avro format earlier.
- they do hourly partitions in HDFS
- if HDFS goes down, they need a persistent queue to retain data for several days. Maybe kafka 0.8 was a good decision for them. improved kafka brokers provide reliable persistent storage.
- if distributed around hte world, can use something like kafka mirror maker to move data from one kafka broker to another kafka broker.
- google pub/sub also is a persistent message queue. can store messages for 7 days and has at-least-once delivery semantics for messages.
- would pub/sub be better than kafka? Let's find out...


## producer load test

- could google pub/sub handle the anticipated load?
- Say spotify peak load is 700k events per second. So they chose 2m events per second as a disaster case.
- they stress tested by publishing to a single data center so that all requests were hitting the pub/sub machines in the same zone.
- they mocked traffic through the event service to pub/sub. To push 2m messages per second, they ran the event services on 29 machines
