select *
from (select year, month, day, measid, vid, start_criteria, lead(end_criteria) over (order by reltime)
, lead(end_criteria) over (order by reltime) - start_criteria duration
from
(
select
*
, case when criteria =1 and prev_criteria=0 then reltime else 0 end start_criteria
, case when criteria =0 and prev_criteria=1 then reltime else 0 end end_criteria
from
( select q.*
  , lag(criteria) over (order by reltime) prev_criteria
  from
  ( select measid,day,month,year,vid,reltime, nkw
    , case when nkw >= 900 then 1 else 0 end criteria
    from diodor order by measid,day,month,year,vid,reltime
  )q
)qq
)qqq
where start_criteria <> 0 or end_criteria <> 0 
)qqqq
where duration > 1;