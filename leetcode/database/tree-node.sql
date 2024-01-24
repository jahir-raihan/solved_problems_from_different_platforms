select id,
    case
        when p_id and id in (select p_id from tree) then 'Inner'
        when p_id is null then 'Root'
        else 'Leaf'
    end as type
from Tree