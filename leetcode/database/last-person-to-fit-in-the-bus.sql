select person_name from Queue
where
  turn = (select turn from (
    select t1.turn, t1.weight, SUM(t2.weight) as sum
    from Queue as t1
    inner join Queue as  t2 on t1.turn >= t2.turn
    group by t1.turn, t1.weight
    order by t1.turn
  ) as x
  where sum <= 1000
  order by turn desc
  limit 1)
