select e.reports_to as employee_id, a1.name, count(*) as reports_count, round(sum(e.age) / count(*)) as average_age
from Employees as e join Employees as a1 on e.reports_to = a1.employee_id
where e.reports_to is not null
group by e.reports_to
order by employee_id