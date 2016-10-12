-- Once you created tables:
--  gp_workfile_usage_per_segment_history
--  gp_workfile_usage_per_query_history
-- and collected data using populate_workfile_history_tables.sh
-- you are ready to report spilling activity now.
-- Example queries below.

-- Check spilling activity history over time

select 
  to_char(probe_timestamp,'YYYY-MM-DD HH24:MM:SS') as "Probe time", 
  sum(numfiles) as "Number of files", 
 -- pg_size_pretty(sum(size)::bigint) as "Workfiles Size",
 round(sum(size)/1024/1024/1024) as "Workfiles GB"
 from gp_workfile_usage_per_segment_history 
  group by probe_timestamp 
 order by 1;

-- Check spilling queries collected 

select 
  to_char(probe_timestamp,'YYYY-MM-DD HH24:MM:SS') as "Probe time", 
  datname as "Database",
  procpid as "PID",
  sess_id as "Session ID",
  usename as "User",
  substr(current_query,1,50) as "Query",
  round(size/1024/1024/1024) as "Workfiles GB",
  numfiles as "Number of files"
 from gp_workfile_usage_per_query_history
 order by 7 desc;
 
 
 