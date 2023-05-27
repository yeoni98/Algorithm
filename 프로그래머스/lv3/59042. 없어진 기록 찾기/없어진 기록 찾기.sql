
SELECT animal_outs.animal_id, animal_outs.name
from
animal_ins right join animal_outs
on animal_outs.animal_id = animal_ins.animal_id
where animal_ins.datetime is null
order by animal_outs.animal_id;