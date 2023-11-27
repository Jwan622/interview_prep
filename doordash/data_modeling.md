"""
Data Modeling at Doordash
 Let’s say you work for doordash. A customer can go to the doordash app and place an order at their favorite restaurant for either pickup or delivery. Once that restaurant receives the order, they can choose to accept or deny the order. If accepted, then doordash connects the restaurant with a nearby delivery man who picks up the order, and delivers to food to the customer. Design a schema that takes this entire process into account.
"""

Designing a schema for a DoorDash-like application involves creating tables to capture various aspects of the ordering and delivery process. The schema should reflect the relationships between customers, restaurants, orders, delivery personnel, and the status of each order. Here's a high-level design:


# Schema
Users Table: This table stores information about all users, including both customers and delivery personnel.
user_id (Primary Key)
name
email
phone_number
user_type (e.g., customer, delivery personnel)  # key part is that Users can be customers or delivery personnel
address (for customers)
vehicle_type (for delivery personnel)


Restaurants Table: Stores details about each restaurant.
restaurant_id (Primary Key)
name
address
phone_number
cuisine_type


MenuItems Table: Each restaurant has a list of items that can be ordered.
item_id (Primary Key)
restaurant_id (Foreign Key)
name
description
price


Orders Table: This table tracks each order placed by a customer. Key part is that it has 2 foreign keys to the Users table.
order_id (Primary Key)
user_id (Foreign Key, references Users)
restaurant_id (Foreign Key, references Restaurants)
order_time
delivery_address
order_status (e.g., pending, accepted, denied, delivered)
delivery_type (pickup or delivery)
delivery_person_id (Foreign Key, references Users, null until assigned)


OrderItems Table: This table links orders to menu items (many-to-many relationship). An order can have many MenuItems and MenuItems can be in many orders.
order_item_id (Primary Key)
order_id (Foreign Key, references Orders)
item_id (Foreign Key, references Menu Items)
quantity


Order Status Table: Tracks the status of each order through its lifecycle.
order_status_id (Primary Key)
order_id (Foreign Key, references Orders)
status (e.g., accepted by restaurant, picked up, in transit, delivered)   # an order might have 3 of these, one for each status. different timestamp for each
timestamp


Payments Table: To manage payments for each order.
payment_id (Primary Key)
order_id (Foreign Key, references Orders)
amount
payment_method (e.g., credit card, PayPal)
status (e.g., pending, completed, failed)


Ratings and Reviews Table: Optional, for customer feedback.
review_id (Primary Key)
order_id (Foreign Key, references Orders)
rating
comment
created_at

Payments could also use a status table to keep track of payment status transitions through time. Both order status and payment status table would have timestamps to show the times in which the statuses changed


# Notes:
Normalization: The schema is designed to normalize data, reducing redundancy and improving data integrity.
Indexes: Consider creating indexes on frequently queried columns for better performance.
Foreign Keys: They enforce referential integrity between tables.
Optional Tables: Depending on the requirements, additional tables like Ratings and Reviews can be added or removed.
This schema provides a robust foundation for a DoorDash-like application, covering the essential aspects of the food ordering and delivery process. Fine-tuning and additional attributes can be added based on specific business requirements and application features.
