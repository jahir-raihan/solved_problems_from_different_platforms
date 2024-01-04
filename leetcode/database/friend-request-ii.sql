select a.id, count(a.id) num from
(select requester_id as id from requestaccepted
union all
select accepter_id from requestaccepted) as a
group by a.id
order by num desc limit 1
