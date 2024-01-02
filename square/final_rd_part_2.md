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


## A/B testing

A/B testing, also known as split testing, is a marketing experiment wherein you split your audience to test variations on a campaign and determine which performs better. In other words, you can show version A of a piece of marketing content to one half of your audience and version B to another.

A/B testing can be valuable because different audiences behave, well, differently. Something that works for one company may not necessarily work for another.

In fact, conversion rate optimization (CRO) experts hate the term "best practices" because it may not actually be the best practice for you. However, this kind of testing can be complex if you’re not careful.

To run an A/B test, you need to create two different versions of one piece of content, with changes to a single variable.

Then, you'll show these two versions to two similarly sized audiences and analyze which one performed better over a specific period (long enough to make accurate conclusions about your results).

![ab_testing](../images/square/ab_testing.png)

### Some A/B Testing tips
1. Test only one element.
Each variable of your website or ad campaign can significantly impact your intended audience’s behavior. That’s why looking at just one element at a time is important when conducting A/B tests.
Attempting to test multiple elements in the same A/B test will yield unreliable results. With unreliable results, you won't know which element had the biggest impact on consumer behavior.
Be sure to design your split test for just one element of your ad campaign or website.
Pro tip: Don’t try to test multiple elements at once. A good A/B test will be designed to test only one element at a time.

3. Create a 'control' and a 'challenger.'
You now have your independent variable, your dependent variable, and your desired outcome. Use this information to set up the unaltered version of whatever you're testing as your control scenario.
If you're testing a web page, this is the unaltered page as it exists already. If you're testing a landing page, this would be the landing page design and copy you would normally use.
From there, build a challenger — the altered website, landing page, or email that you’ll test against your control.
For example, if you're wondering whether adding a testimonial to a landing page would make a difference in conversions, set up your control page with no testimonials. Then, create your challenger with a testimonial.

9. Test both variations simultaneously.
Timing plays a significant role in your marketing campaign’s results, whether it's the time of day, day of the week, or month of the year.
If you were to run version A during one month and version B a month later, how would you know whether the performance change was caused by the different design or the different month?
When running A/B tests, you must run the two variations simultaneously. Otherwise, you may be left second-guessing your results.
The only exception is if you're testing timing, like finding the optimal times for sending emails.

1. Check your goal metric.
The first step in reading your A/B test results is looking at your goal metric, which is usually conversion rate.
After you’ve plugged your results into your A/B testing calculator, you’ll get two results for each version you’re testing. You’ll also get a significant result for each of your variations.

2. Compare your conversion rates.
By looking at your results, you’ll likely be able to tell if one of your variations performed better than the other. However, the true test of success is whether your results are statistically significant.
For example, variation A had a 16.04% conversion rate. Variation B had a 16.02% conversion rate, and your confidence interval of statistical significance is 95%. Variation A has a higher conversion rate, but the results are not statistically significant, meaning that variation A won’t significantly improve your overall conversion rate.
How to Read A/B Testing Results
As a marketer, you know the value of automation. Given this, you likely use software that handles the A/B test calculations for you — a huge help. But, after the calculations are done, you need to know how to read your results. Let’s go over how.

1. Check your goal metric.
The first step in reading your A/B test results is looking at your goal metric, which is usually conversion rate.
After you’ve plugged your results into your A/B testing calculator, you’ll get two results for each version you’re testing. You’ll also get a significant result for each of your variations.

2. Compare your conversion rates.
By looking at your results, you’ll likely be able to tell if one of your variations performed better than the other. However, the true test of success is whether your results are statistically significant.
For example, variation A had a 16.04% conversion rate. Variation B had a 16.02% conversion rate, and your confidence interval of statistical significance is 95%. Variation A has a higher conversion rate, but the results are not statistically significant, meaning that variation A won’t significantly improve your overall conversion rate.

### A/B test example

1. Site Search
Site search bars help users quickly find what they’re after on a particular website. HubSpot found from previous analysis that visitors who interacted with its site search bar were more likely to convert on a blog post. So, we ran an A/B test to increase engagement with the search bar.
In this test, search bar functionality was the independent variable, and views on the content offer thank you page was the dependent variable. We used one control condition and three challenger conditions in the experiment
The search bar remained unchanged in the control condition (variant A).

In variant B, the search bar was larger and more visually prominent, and the placeholder text was set to “search by topic.”

Variant C appeared identical to variant B but only searched the HubSpot Blog rather than the entire website.

![search_bar](../images/square/search_bar.png)

In variant D, the search bar was larger, but the placeholder text was set to “search the blog.” This variant also searched only the HubSpot Blog.
We found variant D to be the most effective: It increased conversions by 3.4% over the control and increased the percentage of users who used the search bar by 6.5%.

## How Does A/B Testing Work?
You start an A/B test by deciding what it is you want to test. Fung gives a simple example: the size of the subscribe button on your website. Then you need to know how you want to evaluate its performance. In this case, let’s say your metric is the number of visitors who click on the button. To run the test, you show two sets of users (assigned at random when they visit the site) the different versions (where the only thing different is the size of the button) and determine which influenced your success metric the most. In this case, which button size caused more visitors to click?

In real life there are lots of things that influence whether someone clicks. For example, it may be that those on a mobile device are more likely to click on a certain size button, while those on desktop are drawn to a different size. This is where randomization can help — and is critical. By randomizing which users are in which group, you minimize the chances that other factors, like mobile versus desktop, will drive your results on average.

“The A/B test can be considered the most basic kind of randomized controlled experiment,” Fung says. “In its simplest form, there are two treatments and one acts as the control for the other.” As with all randomized controlled experiments, you must estimate the sample size you need to achieve a statistical significance, which will help you make sure the result you’re seeing “isn’t just because of background noise,” Fung says.

Sometimes, you know that certain variables, usually those that are not easily manipulated, have a strong effect on the success metric. For example, maybe mobile users of your website tend to click less on anything, compared with desktop users. Randomization may result in set A containing slightly more mobile users than set B, which may cause set A to have a lower click rate regardless of the button size they’re seeing. To level the playing field, the test analyst should first divide the users by mobile and desktop and then randomly assign them to each version. This is called blocking.

The size of the subscribe button is a very basic example, Fung says. In actuality, you might not be testing just the size but also the color, and the text, and the typeface, and the font size. Lots of managers run sequential tests — e.g., testing size first (large versus small), then testing color (blue versus red), then testing typeface (Times versus Arial) — because they believe they shouldn’t vary two or more factors at the same time. But according to Fung, that view has been debunked by statisticians. And sequential tests are suboptimal because you’re not measuring what happens when factors interact. For example, it may be that users prefer blue on average but prefer red when it’s combined with Arial. This kind of result is regularly missed in sequential A/B testing because the typeface test is run on blue buttons that have “won” the prior test.

Instead, Fung says, you should run more-complex tests. This can be hard for some managers, since the appeal of A/B tests are how straightforward and simple they are to run (and many people designing these experiments, Fung points out, don’t have a statistics background). “With A/B testing, we tend to want to run a large number of simultaneous, independent tests,” he says, in large part because the mind reels at the number of possible combinations you can test. But using mathematics you can “smartly pick and run only certain subsets of those treatments; then you can infer the rest from the data.” This is called “multivariate” testing in the A/B testing world and often means you end up doing an A/B/C test or even an A/B/C/D test. In the example above with colors and size, it might mean showing different groups: a large red button, a small red button, a large blue button, and a small blue button. If you wanted to test fonts, too, the number of test groups would grow even more.
