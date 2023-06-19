select q.query_name, round(sum(q.rating / q.position) / count(*),2) as quality,
  round(sum(if(q.rating<3, 1, 0)) / count(*) * 100, 2) as poor_query_percentage
from Queries as q
group by query_name