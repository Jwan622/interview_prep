# hihi. Jeff Wan here

# - send events to kafka in code
# - there are issues with this. say the event is fired before the actual pdatabase write is written, then the event could be sent but the database write could not happen. same thing if the evnet was fired after the database write. we could be missing events if the code crashes or the dtabase write doens't succeed.
# - however, that could be inaccurate so maybe using a tool like debezium is best becasue thats' closer to the truth
# - debeium reads from the wal logs so is a better source of truth. those events are also sent to a message bus like kafka or kinesis for us to consume using our elt pipelines
# - debezium takes more time to setup so I would prefer to go the easier write first, of least resistance (send events to a bus or queue) and then argue for why dbezium is best with our tech lead to address at a later time.

# - elt pipeline generally go lik ethis. kafka -> s3 raw -> some kind of staging for deduping either in s3 or the DW (redshift?) -> dbt can move data from staging to redshift -> using something like dbt we can denormalize to presentatino tables within redshift. 
# - this architecture is generally ELT because we load to redshift first before joining/trasnformining. several benefits to this but speed and data lineaage are best. 
# - tag with metadata in s3 raw so we can replay and tarck down inevitable data bugs or when the intern deletes data.
# - orchestrate hourly with somehintg. cron or airflow or whatever tool. incremental model.

# - how to handle dupes?


# tables

1. User table <this is the cusotmer using engage)
- userid (primary key)
- username
- department at comapny
- contact if you want to know they are`



2. template
- template id
- template name
- template type (like minimalist, business jargon, lots of flowers)



---- we populate users in a campaing using the audience_mbmers table which might have 10000000 users but for our example, we pull 100, deduped on email for this email. those users are in the campaign_audience_table
3. campaign
- primary key
- template_id (FK)
- user_id (which colleague sent it) (FK)
- campaign_audience_id (this links to emails and converted data) (FK) (this is how to tell size)
- datetime (send time, when we actually send to audience)
- in reality  Ijsut see datetime in the table. however, some textbooks actualyl breakout time into a dimension table as well. but... I'm not going to do that here.
- (the reason why well have timestamp is becase we're ELT, we're loading the data as is and backend sends the timestamps for the data)
- clickrates (calculate every perid of time?)
- conversion rates
- sent emails yet? booelan field.
- datetime (creation time)
- maybe expiration date?
- type (mobile, ad)

-- these represents the members in teh actual campaign.
4.5 campaign_audience_id (this will have 100 rows)
- member_id (FK)
- clicked? boolean false by default
- converted? boolean false by default
- open?
- clicked_timestamp? updated in time
- converted_timestamp updatime
- open_timestamp? updated in time
 


4. audience
- audience id
- segment type (young, old, men, women, college, active, etc) (array type)
- location_type (northeast, cities, country)
- size?


5. audience_members   (a member can be duplicated here since a member can be in many audiences, so someone needs to dedupe on email, this could have liek 10000000 members).
- member_id (might appear mutliple times because a member can be in many audiences)
- audience_id
- email (this shosuld be unique right?)
- contact



6. membmers
- user name
- email
-contact
- john from nyc. just a member

--- example that tal gave, someone john sends out a campgin to a 100 people. what does it look like?
<campaign>
template_id (flowers)
- john's user id 1233456
- audience_id (5 for finance bros in nyc, say governor's ball)
- datetime (when it'll be sent)


auidnec table
- 5
- finance bros
- nyc
- 100 (even though you don't neeod this) since the join tabe will have this


<audience_members>
- audience-id = 5
- user_id 1
<this has 100 rows>
- <100 different emails>



