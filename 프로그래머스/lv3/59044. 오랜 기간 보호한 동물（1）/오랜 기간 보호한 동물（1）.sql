SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME
from animal_ins left join animal_outs
on animal_ins.animal_id = animal_outs.animal_id
where animal_outs.datetime is null
order by animal_ins.datetime
limit 3;