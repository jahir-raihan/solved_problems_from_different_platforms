select round(count(a1.player_id) / (select count( DISTINCT a3.player_id) from Activity a3), 2) as fraction
from Activity a1
where (a1.player_id, DATE_SUB(a1.event_date, INTERVAL 1 DAY)) in (
  select player_id, min(event_date)
  from Activity
  group by player_id
)