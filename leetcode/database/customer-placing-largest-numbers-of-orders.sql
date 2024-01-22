select customer_number
from
(select customer_number, count(*) as cnt
from orders
group by customer_number
order by cnt desc
limit 1) as a