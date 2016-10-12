-- Show global workfiles size and count per segment

select
      case when segid = -1 then 'Master'
                           else 'Seg' || segid::text
      end as "Location",
      numfiles as "Number of Files",
      pg_size_pretty(size::bigint) "Total size of Workfiles"
    from gp_toolkit.gp_workfile_usage_per_segment
    order by segid;
    
--  Show workfiles size per actual query

select
      sum(numfiles) as "Number of Files",
      pg_size_pretty(sum(size)::bigint) "Total size of Workfiles",
      procpid as "Process ID",
      sess_id as "Session ID",
      usename as "User",
      state as "State of Query",
      current_query as "Query"
    from gp_toolkit.gp_workfile_usage_per_query
    where numfiles > 0
    group by procpid, sess_id, usename, state, current_query
    order by sum(size) desc;

-- Show workfiles size skew over segments

select
      case when segid = -1 then 'Master' 
           else 'Seg' || segid::text
      end as "Location",
      numfiles as "Number of Files",
      pg_size_pretty(size::bigint) "Total size of Workfiles over segment",
      procpid as "Process ID",
      sess_id as "Session ID",
      usename as "User",
      state as "State of Query",
      current_query as "Query"
    from gp_toolkit.gp_workfile_usage_per_query
    where numfiles > 0
    order by procpid, sess_id, 3 desc;    
        
-- Show workfiles location for queries

SELECT a.datname "Database Name",
    a.procpid "Process ID",
    a.sess_id "Session ID",
    a.segid "Segment number",
    a.optype "Operation type",
    a.workmem/1024 "Workmem MB",
    a.current_query,
    b.hostname "Host Name",
    c.fselocation||'/base/'||d.oid||'/'||directory "Workfile Directory"
FROM  gp_toolkit.gp_workfile_entries a , gp_segment_configuration b , pg_filespace_entry c , pg_database d
WHERE c.fsedbid=b.dbid 
AND a.segid=b.content
AND a.datname=d.datname
AND b.role='p'
ORDER BY 2,3,4;

--- Show workfile size and identify particular query and its slice spilling
 
select 
  pg_size_pretty((sum(size) over (partition by procpid,segid))::bigint) as size_pretty_qry_seg
, pg_size_pretty(size) as size_pretty
, (round(workmem/1024) || ' MB')::text as workmem_mb
, datname , procpid , sess_id , command_cnt , usename 
, substr(current_query,1,100) as current_query
, segid , slice ,  optype
, numfiles ,  state  , utility
from gp_toolkit.gp_workfile_entries
where procpid <> pg_backend_pid()
order by size desc;



        