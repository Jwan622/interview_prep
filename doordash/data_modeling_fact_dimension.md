# Prompt

Let’s say you work for a delivery food company, XYZ. A customer can go to the XYZ app and place an order at their favorite restaurant for either pickup or delivery. Once that restaurant receives the order, they can choose to accept or deny the order. If accepted, then the XYZ app connects the restaurant with a nearby delivery man who comes, picks up the order, and delivers to food to the customer. Design a schema that takes this entire process into account. 

# Solution: 

Food Delivery Company Data Modeling

Schema Outline
1) Let’s start with the dim tables. What are the distinct objects? Those are your entities and should be your dimension tables? This includes:

o Dim_deliverer
 Deliverer_id
 Full Name
 Region_Id
 (Other Relevant Demographic_info_cols)
 Account_creation_date – life of the Deliverer
 Last_login_date
 Number_of_trips
 L7_Number_of_trips (last 7 days)
 L28_Number_of_trips (last 28 days)

o Dim_customer
 Customer_id
 Full_Name
 Region_Id
 (Other Relevant Demographic_info_cols, like address)
 Accont_creation_date – life of the customer
 Last_login_date
 Number_of_orders
 L7_Number of_ orders (last 7 days)
 L28_Number of_ orders (last 28 days)
 Premium_user (Y or N)
 Premium_user_start_date (Y or N)

o Dim_restaurant
 Restaurant_id
 Restaurant_Name
 Region_Id
 (Other Relevant Demographic_info_cols)
 Account_creation_date – life of the resturant
 Number_of_orders
 L7_ Number of_ orders (last 7 days)
 L28_ Number of_ orders (last 28 days)
 Menu_items (a json)
 Opening_Hour
 Closing_Hour
 Food_Category (fast_food, healthy, etc)


2) Next, what are the fact tables? Recall that there could be multiple fact tables, and this
problem is the perfect place for that. Activity based tables deserve their own fact tables,
such as the following. One row per different activity. so there can be multiple rows per deliverer_id and customer_id

o Fact_deliverer_activity
 Session_id
 Deliverer_id
 Region_id
 Timestamp
 Activity_type –
login/update_account_info/available_to_pickup/accept_order/Cancel_order/arrive_to_restaurant/picks_up_order/drops_off_order

o Fact_customer_activity
 Session_id
 Customer_id
 Region_id
 Timestamp
 Activity_type – login/update_account_info/available_to_order/places_order/Cancels_order/receives_order/rates_driver/tips_driver


3) Are there any entities that interact often that you can then create a fact table from? We  know that the two fact tables above interest, so let’s create one more fact table:

o Fact_order_activity
 Order_id
 Deliverer_id
 Customer_id
 Region_id
 Timestamp
 Activity_type – (places_order/driver_picks_up_order/driver_drops_off_order)


4) Finally, is there any Dimension table needed for the fact table above? Yes. This concept
is called “creating a wide table” or “flattening out” the fact_order_activity table we see in
part 3.

o Dim_orders – have ONE RECORD per interaction (one record per order id). so all the orders in the activity table are collapsed into this dimension table. All the activity type times are recorded in columns for each order id row)
 Order_id
 Deliverer_id
 Customer_id
 Region_id
 places_order_time
 deliverer_accepted_time
 deliverer_picks_up_order_time
 deliverer_drops_off_order_time



# Explanation
1) This section is related to dim tables. The way we go about deciding which dim tables to
create is by first thinking which “objects” exist. An object here is a part of the business flow that
will exist regardless of changes to the business. For example, if this food delivery company
decides to charge more, it won’t change the objects needed to run the business. You can see
that the fields are similar.
One field that stands out in the Dim_customer table is Premium_user This is just a
Boolean field which will indicate whether the user is a premium user (Y) or not (N). Another field
to point out is the Menu_items in the Dim_ restaurant table. Note that I wrote that this field is
JSON value. For example, resturant A may have 4 menu items. Therefore, the value of this row
might like something like {menu_item_ids: 242,256,2457,823}. Can you think of another dim
table that can be created knowing this fact?

2) Each object can have can theoretically have a fact table. I did include one for the restaurant
object, but the concepts remain the same as for the Fact_deliverer_activity and
Fact_customer_acivity tables. The one important thing to point out is that this table is at a
Session_id, Customer_id , Region_id granularity. Note that each value in the activity_type
column has its own timestamp. This will be important for the fourth part.

3) You might be wondering why a table like Fact_order_activity is necessary if in section two
we already have Fact_deliverer_activity and Fact_customer_acivity. The concept is simply:
Storage is cheaper than compute! Duplicating data is better than doing JOINs and there is less
room for error if analysts and scientists incorrectly join columns that cause expensive queries.

4) As mentioned, Dim_orders is simply a “flattened out” version of Fact_order_activity. If you
look closely, you can see that timestamp column is not in Dim_orders... it's split out into separate columns per activity type. The reason for this is vital difference is simply because a lot of times in businesses like these (food delivery, car sharing, etc), optimizing for
time is very essential. A table like Dim_orders let the data scientists write very simple Queries
for each order id (since there is only 1 row per order_id) and optimize the routes that their
algorithms are creating to minimize ETA times.
