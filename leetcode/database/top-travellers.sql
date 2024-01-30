select u.name, IFNULL(SUM(r.distance), 0) as travelled_distance
from rides r right join users u on u.id = r.user_id
group by u.id
order by travelled_distance desc, u.name asc