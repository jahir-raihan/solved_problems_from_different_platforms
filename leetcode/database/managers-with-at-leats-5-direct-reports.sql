select distinct e.name from (
select managerId, count(*) as count from (
select * from employee where managerId is not null) as data
group by managerId) as sub_data join employee as e on e.id = sub_data.managerId
where count >= 5