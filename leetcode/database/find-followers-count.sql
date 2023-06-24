select user_id, count(*) as followers_count
from Followers
where user_id != follower_id
group by user_id
order by user_id