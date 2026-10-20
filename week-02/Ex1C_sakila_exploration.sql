/*
a) In the actor table, we have information for 'actor_id', 'first_name', 'last_name', & 'last_update'
b) In the film table, we have information for 'film_id', 'title', 'description', 'release_year', 'language_id', 'original_language_id', 'rental_duration', 'rental_rate', 'length', 'replacement_cost', 'rating', 'special_features', & 'last_update'
c) 'film_actor' contains columns for both 'actor_id' & 'film_id'
d) In this rental table, I can find information on when items were rented and when they were returned. It includes rental_id to indicate different rentals, along with rental_date & return_date to let you calculate how long each item was rented for. It is fairly easy to read, as each column name gives you a clear understanding of what you're looking at within this context
e) This table includes information about each item in their inventory. I can kind of deduce that inventory_id identifies each item, film_id identifies the film, and store_id shows which store it belongs to. However, it is not clear at all as some use numbers that repeat. So now I'm looking at 1:1:1 & 2:1:1 to try and locate different items, which can get confusing when trying to pull out quick information
f) The rental, inventory, and film tables are all needed to understand the names of films that were rented on a specific date. These tables are related to each other through IDs, which help us know where to pull the data from next. For example, we can use inventory_id from the rental table to find the item in the inventory table. From there, we can use film_id to find the name of the movie in the film table.
*/

SELECT inventory_id, rental_date FROM rental;
SELECT film_id, inventory_id FROM inventory;
SELECT film_id, title FROM film;
