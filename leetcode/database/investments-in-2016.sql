
select round(sum(a.tiv_2016), 2) as tiv_2016
from insurance a
where (select count(*) from insurance b where a.lat = b.lat and b.lon = a.lon) = 1
    and (select count(*) from insurance c where a.tiv_2015 = c.tiv_2015) > 1
