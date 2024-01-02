
(select u.name as results

 from MovieRating m inner join Users u on m.user_id = u.user_id
 group by m.user_id
 order by count(m.movie_id) desc, u.name limit 1
)

union all

(
select title as results
from MovieRating r inner Join Movies m on r.movie_id = m.movie_id
where r.created_at like '2020-02-%'
group by r.movie_id
order by avg(r.rating) desc, m.title limit 1
)