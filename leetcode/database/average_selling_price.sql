select u.product_id ,round(sum( u.units * p.price) / sum(u.units),2 ) as average_price
from UnitsSold as u join Prices as p on u.product_id = p.product_id and u.purchase_date between p.start_date and p.end_date
group by product_id