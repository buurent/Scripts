-- Create two history tables to collect workfile activity data over time

drop table gp_workfile_usage_per_segment_history;

create table gp_workfile_usage_per_segment_history
(
   probe_timestamp timestamp not null default now(),
   segid smallint,
   numfiles bigint,
   size numeric
)
distributed by (segid);

drop table gp_workfile_usage_per_query_history;

create table gp_workfile_usage_per_query_history
(
   probe_timestamp timestamp not null default now(),
   datname name,
   procpid int,
   sess_id int,
   usename name,
   current_query text,   
   size numeric,
   numfiles bigint
)
distributed by (procpid, sess_id);




