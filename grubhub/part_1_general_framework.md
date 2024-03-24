# Overview

## Delivery framework

Here's what to ask before you get started

### Functional requirements

Functional requirements are your "Users should be able to..." statements. These are the core features of your system and should be the first thing you discuss with your interviewer. Oftentimes this is a back and fourth with your interviewer. Ask targeted questions as if you were talking to a customer or product manager ("does the system need to do X?", "what would happen if Y?") to arrive at a prioritized list of core features.

For example, if you were designing a system like Twitter, you might have the following functional requirements:

- Users should be able to post tweets
- Users should be able to follow other users
- Users should be able to see tweets from users they follow

### non functional requirements

Non-functional requirements are statements about the system qualities that are important to your users. These can be phrased as "The system should be able to..." or "The system should be..." statements.

For example, if you were designing a system like Twitter, you might have the following non-functional requirements:

The system should be highly availability, prioritizing availability over consistency
The system should be able to scale to support 100M+ DAUs
The system should be low latency, rendering feeds in under 200ms

**tip:**
When you consider non-functional requirements, it's not enough to just consider the long list of -ilities you are probabily familiar with e.g. scalability, availability, durability, reliability, consistincy, etc. The most important aspect of your non-functional requirements is your ability to identify what makes this system uniquely challenging. So if you were designing Ticketmaster, for example, you would note that consistency is important to ensure no double-booking (one user per ticket) and that you need to be able to scale quickly to accommodate bursty traffic from popular events (like a Taylor Swift concert).

### Capacity estimation

Many guides you've read will suggest doing back-of-the-envelope calculations at this stage. We believe this is often unnecessary. Instead, perform calculations only if they will directly influence your design. In most scenarios, you're dealing with a large, distributed system – and it's reasonable to assume as much. Many candidates will calculate storage, DAU, and QPS, only to conclude, "ok, so it's a lot. Got it." As interviewers, we gain nothing from this except that you can perform basic arithmetic.

Our suggestion is to explain to the interviewer that you would like to skip on estimations upfront and that you will do math while designing when/if necessary. When would it be necessary? Imagine you are designing a TopK system for trending topics in FB posts. You would want to estimate the number of topics you would expect to see, as this will influence whether you can use a single instance of a data structure like a min-heap or if you need to shard it across multiple instances, which will have a big impact on your design.


### Core entities

Next you should take a moment to identify and list the core entities of you system. This helps you to understand the data central to your design and gives you a foundation to build on. These are the core entities that your API will exchange and that your system will persist in a Data Model. In the actual interview, this is as simple as jotting down a bulleted list and explaining this is your first draft to the interviewer.

Why not list the entire data model at this point? Because you don't know what you don't know. As you design your system, you'll discover new entities and relationships that you didn't anticipate. By starting with a small list, you can quickly iterate and add to it as you go. Once you get into the high level design and have a clearer sense of exactly what state needs to update upon each request you can start to build out the list of relevant columns/fields for each entity.

For our Twitter example, our core entities are rather simple:

User
Tweet
Follow

### API Design

Before you get into the high-level design, you'll want to define the contract between your system and its users. Oftentimes, especially for Product Design style interviews, this maps directly to the functional requirements you've already identified (but not always!). You will use this contract to guide your high-level design and to ensure that you're meeting the requirements you've identified.

You have a quick decision to make here -- do you want to design a RESTful API or a GraphQL API?

RESTful API: The standard communication constraints of the internet. Uses HTTP verbs (GET, POST, PUT, DELETE) to perform CRUD operations on resources.

GraphQL API: A newer communication protocol that allows clients to specify exactly what data they want to receive from the server.

Don't overthink this. Use GraphQL only if you really need clients to fetch only the requested data (no over- or under- fetching). Otherwise, stick with REST.

For Twitter, we would choose REST and would have the following endpoints. Notice how we can use our core entities as the objects that are exchanged via the API.

POST /v1/tweet/create
body: {
  "text": string
}

GET /v1/tweet/:tweetId -> Tweet

POST /v1/follow/:userId

GET /v1/feed -> Tweet[]
Notice how there is no userId in the POST /v1/tweet/create endpoint? This is because we will get the id of the user initiating the request from the authentication token in the request header. Putting sensitive information like authentication tokens in the request body is a security risk and a mistake that many candidates make. Don't be one of them!

### High level Design

Now that you have a clear understanding of the requirements, entities, and API of your system, you can start to design the high-level architecture. This consists of drawing boxes and arrows to represent the different components of your system and how they interact. Components are basic building blocks like servers, databases, caches, etc. This can be done either in person on a whiteboard or virtually using whiteboarding software like Excalidraw. The Key Technologies section below will give you a good sense of the most common components you'll need to know.

Ask your recruiter what software you'll be using for your interview and practice with it ahead of time. You don't want to be fumbling with the software during your interview.

Don't over think this! Your primary goal is to design an architecture that satisfies the API you've designed and, thus, the requirements you've identified. In most cases, you can even go one-by-one through your API endpoints and build up your design sequentially to satisfy each one.

Stay focused! It's incredibly common for candidates to start layering on complexity too early, resulting in them never arriving at a complete solution. Focus on a relatively simple design that meets the core functional requirements, and then layer on complexity to satisfy the non-functional requirements in your deep dives section. It's natural to identify areas where you can add complexity, like caches or message queues, while in the high-level design. We encourage you to note these areas with a simple verbal callout and written note, and then move on.

As you're drawing your design, you should be talking through your thought process with your interviewer. Be explicit about how data flows through the system and what state (either in databases, caches, message queues, etc.) changes with each request, starting from API requests and ending with the response. When your request reaches your database or persistence layer, it's a great time to start documenting the relevant columns/fields for each entity. You can do this directly next to your database visually. This helps keep it close to the relevant components and makes it easy to evolve as you iterate on your design. No need to worry too much about types here, your interviewer can infer and they'll only slow you down.

**TIP**: Don't waste your time documenting every column/field in your schema. For example, your interviewer knows that a User table has a name, email, and password hash so you don't need to write these down. Instead, focus on the columns/fields that are particularly relevant to your design.


### Deep dives

Astute readers probably noticed that our simple, high-level design of Twitter is going to be woefully inefficient when it comes to fetching user's feeds. No problem! That's exactly the sort of thing you'll iterate on in the deep dives section. Now that you have a high-level design in place you're going to use the remaining 10 or so minutes of the interview to harden your design by (a) ensuring it meets all of your non-functional requirements (b) identifying and adressing issues and bottlenecks and (c) improving the design based on probes from your interviewer.

The degree in which you're proactive in leading deep dives is a function of your seniority. More junior candidates can expect the interviewer to jump in here and point out places where the design could be improved. More senior candidates should be able to identify these places themselves and lead the discussion.

So for example, one of our non-functional requirements for Twitter was that our system needs to scale to >100M DAU. We could then lead a discussion oriented around horizontal scaling, the introduction of caches, and database sharding -- updating our design as we go. 

Another was that feeds need to be fetched with low latency. In the case of Twitter, this is actually the most interesting problem. We'd lead a discussion about fanout-on-read vs fanout-on-write and the use of caches.
