select product_id, 10 as price
from Products
group by product_id
having min(change_date) > '2019-08-16'

union all

select x.product_id, x.new_price
from Products as x join (select product_id, max(change_date) as date
from Products
where change_date <= '2019-08-16'
group by product_id) as y on x.product_id = y.product_id and x.change_date = y.date
