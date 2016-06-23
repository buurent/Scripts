-- Read external files headers (CSV) and translate to columns


drop external table ext_read_header;
CREATE EXTERNAL WEB TABLE ext_read_header (header text)
EXECUTE 'grep -m 1 ''.'' /home/gpadmin/file/*.csv' ON MASTER
 FORMAT 'text' (delimiter 'OFF')
 ENCODING 'UTF8';
 
drop table header_type; 
create table header_type
(id_type text
, file_columns text
, gpload_script text
,target_table text)
distributed randomly;

truncate header_type;
insert into header_type
select 'type ' || row_number() over()
,file_columns
,'gpload_Type' || row_number() over()
,'target_type' || row_number() over()
from (select
distinct split_part(header,':',2) as file_columns from ext_read_header ) T;

-- Identifiy the header type
select split_part(header,':',1) as filename
,split_part(header,':',2) as file_columns_in
,T2.*
 from ext_read_header T1
 left outer join header_type T2
 on trim(split_part(T1.header,':',2)) = trim(T2.file_columns);
 
 
 --Idenitify the columns
select id_type
,num_field
,arr_fields
,split_part(arr_fields[num_field],'[',1) as field_name
,replace(split_part(arr_fields[num_field],'[',2),']','') as field_data_type
from (
 select 
id_type
 ,string_to_array(file_columns,';') as arr_fields
 ,generate_series(1,length(file_columns) - length(replace(file_columns,';',''))) as num_field
 from header_type) T
 order by id_type,num_field;
 
 
 select
        split_part(arr_fields[num_field],'[',1) ||' '|| replace(split_part(arr_fields[num_field],'[',2),']','')||',' 
        from (
        select 
         id_type
        ,string_to_array(file_columns,';') as arr_fields
        ,generate_series(1,length(file_columns) - length(replace(file_columns,';',''))) as num_field
        from header_type) T
        order by id_type,num_field;
 
 
 
        select
        distinct split_part(arr_fields[num_field],'[',1) ||' '|| replace(split_part(arr_fields[num_field],'[',2),']','')||',' kolom
        from (
        select 
         id_type
        ,string_to_array(file_columns,';') as arr_fields
        ,generate_series(1,length(file_columns) - length(replace(file_columns,';',''))) as num_field
        from header_type) T
        group by kolom, id_type,num_field;
 
 
