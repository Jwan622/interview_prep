# Analysis


# Questions to ask before starting the case study

## Stage 1
- who is using the data and how will they use it. once a day, once a week. this will determine my orchestration of the data
- shape of the data
- where is the data, what's the data type.
- who needs the data and why?
- What's the flow and sequence of data? Are we collecting that data?

## Stage 2
- Develop data dictionary for core KPIs and metrics needed
- define kpi definitions

## Stage 3
- how can we QA the data
- share with internal users first to get feedback


## Example

Say we have a food delivery service, we implement a new feature, and we want to see its impact on KPIs.

![delivery_service](../images/square/metrics_to_keep_track_of.png)

- maybe 2 metrics to keep track of:
1. time from order to delivery
2. customer satisfaction


## Here's a dashboard of metrics
![dashboard](../images/square/dashboard.png)

## Here are metrics to know

![metrics](../images/square/metrics_to_know.png)




# Here's another example

![case_study_prompt.png](../images/square/case_study_prompt.png)

and the data

![csv_data](../images/square/csv_data.png)

some questions to ask:
- lots of timestamp components. customer placing order, restaurant receiving order, driving arriving at restaurant, driver delivering the food to customer. So look into time duration. Is the marketplace running smoothly? Draw insights from the timestamps to see if delivery is smooth.
- we have restaurant IDs. The restaurant's business. Where are people ordering the food from? Where are they ordering from? Which are most popular restaurants? How many orders? But also most revenue restaurants? Wtihin each city, what are most popular restaurants. Highest orders? Highest revenue.
- customer perspective, what are customers ordering, what's the tip amount/value. correlation between customer tip and order amount.


### Some insights
![insights](../images/square/insights.png)

- palo alto has the most customer spend and volume. those customers order the most.
- also palo alto and mountain view, avg customer order is higher.
- so... perhaps the food delivery company should build corporate seamless plans. entice companies to do that for employee happiness because their employees want it and order a lot.

![insights2](../images/square/insights2.png)
- some merchants get more than others
- suggest to some merchants to expand or promote those merchants as a recommendation engine.

and then recommendations on what to do:
![recs](../images/square/recs.png)


## case study on conversions (business requirements gathering, identifying right analysis to generate insights, draw conclusions and make recommendations)
(from alessandro, mentorcruise person)

### Topics to learn:
- How people design A/B testing and how to deal with confounding variables.
- network effects: confunding variable. excitements. 
- metrics vs kpi. say metric. that's what we're measuring.
- data analysis. How to analyze data.

### Some notes about setting up an experiment.
- A/B testing. Let's understand this and read up on it.
- how do we collect the data. How will we redirect the traffic in case we want to setup this experiment. control vs variant.
- redirect the traffic with a proxy and randomized groups created on the fly and send the traffic to a different group of users. build an experiment and collect data from these 2 groups. Is what we're testing actually increasing the conversion rate. This is a basic scenario. 
- They may have a constraint, how do we handle this situation?
- A curveball study about taxi drivers: when we have to design an experiment. users and taxis in london. The problem was that basically we wanted to test 2 different pricing models. Two groups of users, one price from one model for one group, one price to another group from another model and after 1 month, we collect results and see which performs better... maybe model A is increasing the conversion rate....or so it seems. The problem is that this experiment can fail but there is something wrong... in 1 area maybe we have prices increasing by 5%. But the taxi drivers can be aware of the change of prices and add **bias**. This form of bias is called network effects. A confounding variable of some sort. So the results that we see are not coming from the actions from our system (the pricing model) but an external confounding variable or network effects. 
- environmental constraints, technical constraint. in this case we were using a framework from Uber and it was allowing us to split the city into small hexagons. Area in London was split into several hexagons. Taxi drivers were aware and they all go to a certain part of the city because the prices were higher for them. But the experimenters realized this and so they switched pricing model A and B every hour instead to keep the taxi drivers from realizing. This was to destroy the confounding variable.
- so either the pricing model is responsible for the increasing taxi bookings, or the network effect. There's a confounding variable. The point is the destroy the connection between the confounding variable and the experiment.
- Another example is ice cream and sunburn...say you see a correlation. Say you see ice cream, you see an increase in sunburn. The key is to destroy the summer and -> sunburn and -> ice creams. randomize the groups destroys the bias in the data. But sometimes this is not enough. A/B testing is not that easy.
- but sometimes randomization can get rid of gender bias but not all bias like network effects in taxi drivers. A lot of users and so gender in both groups. But confounding variables sometimes can't be destroyed by randomization like network effects. Taxi drivers now talk and so maybe it's the network effect (talking and feelings and it's too complicated) and so maybe that's driving bookings.
- adding dimension: this is about B/I. Dimension can be revenue over time.
