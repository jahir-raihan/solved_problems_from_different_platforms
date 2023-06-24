select customer_id from (

  select customer_id, count(distinct product_key) as count_n
  from Customer
  group by customer_id
  ) as d

where count_n = (select count(*) from Product)