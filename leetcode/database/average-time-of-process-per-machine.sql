select m1.machine_id as machine_id, round(avg(m2.timestamp - m1.timestamp), 3) as processing_time
from activity as m1 join activity as m2 on m1.machine_id = m2.machine_id and
    m1.activity_type = 'start' and m2.activity_type = 'end'
group by machine_id