-- Returns: product, revenue, sale_date.
select product,revenue,sale_date from sales
order by revenue DESC NULLS LAST,sale_date asc NULLS last   LIMIT 3 OFFSET 1;