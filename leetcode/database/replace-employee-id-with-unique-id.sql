select unq.unique_id as unique_id, e.name as name
from employees as e left join EmployeeUNI as unq
    on e.id = unq.id