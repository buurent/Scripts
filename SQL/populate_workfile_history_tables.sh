#!/bin/bash

PGDATABASE=dwh
POPULATION_INTERVAL=60

declare -i series_number=0

while true
do
        psql -d $PGDATABASE -c "insert into gp_workfile_usage_per_segment_history (select now() , segid , numfiles , size from gp_toolkit.gp_workfile_usage_per_segment)"
        psql -d $PGDATABASE -c "insert into gp_workfile_usage_per_query_history  \
                              (select now(), datname, procpid, sess_id, usename, current_query, sum(size), sum(numfiles) \
                                from gp_toolkit.gp_workfile_usage_per_query \
                               where numfiles > 0 \
                                group by datname, procpid, sess_id, usename, current_query)"

date
echo "Workfile monitoring probes at series " $series_number " inserted. "
series_number=$(($series_number+1))

        sleep $POPULATION_INTERVAL
done