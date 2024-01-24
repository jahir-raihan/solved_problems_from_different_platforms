select c.name
from Salesperson c
where c.name not in (

    select s.name
    from Salesperson s join orders o join company c
    on s.sales_id = o.sales_id and c.com_id = o.com_id
    and c.name = 'RED'
)