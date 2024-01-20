# Write your MySQL query statement below
select request_at as Day, round((
    select count(*) from Trips where request_at = '2013-10-01' and status != 'completed' and
    (
        client_id not in (select users_id from Users where banned = 'Yes')
        and driver_id not in (select users_id from Users where banned = 'Yes')
    )
) / count(*), 2) as 'Cancellation Rate'

from Trips
where request_at = '2013-10-01' and (
    client_id not in (select users_id from Users where banned = 'Yes')
    and driver_id not in (select users_id from Users where banned = 'Yes'))

group by request_at

union all

select request_at as Day, round((
    select count(*) from Trips where request_at = '2013-10-02' and status != 'completed' and
    (
        client_id not in (select users_id from Users where banned = 'Yes')
        and driver_id not in (select users_id from Users where banned = 'Yes')
    )
) / count(*), 2) as 'Cancellation Rate'

from Trips
where request_at = '2013-10-02' and (
    client_id not in (select users_id from Users where banned = 'Yes')
    and driver_id not in (select users_id from Users where banned = 'Yes'))

group by request_at

union all

select request_at as Day, round((
    select count(*) from Trips where request_at = '2013-10-03' and status != 'completed' and
    (
        client_id not in (select users_id from Users where banned = 'Yes')
        and driver_id not in (select users_id from Users where banned = 'Yes')
    )
) / count(*), 2) as 'Cancellation Rate'

from Trips
where request_at = '2013-10-03' and (
    client_id not in (select users_id from Users where banned = 'Yes')
    and driver_id not in (select users_id from Users where banned = 'Yes'))

group by request_at

--
--# Shorter version

select request_at as Day,
    round(sum(status != 'completed') / count(*), 2) as 'Cancellation Rate'
from Trips
    left join users as clients on trips.client_id = clients.users_id
    left join users as drivers on trips.driver_id = drivers.users_id

where clients.banned = 'No'
    and drivers.banned = 'No'
    and request_at between '2013-10-01' and '2013-10-03'
group by Day