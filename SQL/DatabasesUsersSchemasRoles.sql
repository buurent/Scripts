--- list databases
select datname,datacl from pg_database;
 
-- List Schemas
select nspname from pg_catalog.pg_namespace;
 
-- List User Roles
select usename as username from pg_user;
 
 -- List Group Roles
select distinct rolname as group_role from pg_roles join pg_auth_members on (pg_roles.oid=pg_auth_members.roleid);
