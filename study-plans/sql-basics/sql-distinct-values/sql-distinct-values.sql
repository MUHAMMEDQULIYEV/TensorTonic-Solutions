-- Returns: customer_name, unique_products.
 select customer_name,COUNT(DISTINCT product) AS unique_products  from orders
GROUP BY customer_name
Order by unique_products desc,customer_name asc;