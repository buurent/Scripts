import os
import glob
import sys
import csv
sys.stdout = open('create_table.sql', 'w')
set1=()
set2=()

listing = glob.glob('*.csv')
#csvfile_init = open( listing[0] , "rb")
#headers  = csvfile_init.next()
#set2 = set(headers.split(';'))
#print set2
n=0

for filename in listing:
    n=n+1
    m=1
    csvfile = open(filename , "r")
    headers = csvfile.next()
    set1 = set(headers.rsplit(';'))
    if n == 1:
        set2 = set1
        print '/*CREATE EXTERNAL TABLE FOR EXCEL '+ filename+'*/'
        print ' ' 
        print 'CREATE EXTERNAL TABLE DIODOR_EXT'+str(n)+'('
        kolom = headers.replace("[Double];"," varchar, ")
        kolom = kolom.replace("DateValue[Date];"," Datevalue Date, ")
        kolom = kolom.replace("[String];"," varchar, ")
#       kolom = kolom.replace("[Date];"," varchar, ")
        kolom = kolom.replace("DateValue[Date]","Datevalue Date ")
        kolom = kolom.replace("[String]"," varchar)")
#       kolom = kolom.replace("[Date]"," varchar) ")
        kolom = kolom.replace("[Double]"," varchar) ")
        print kolom
        print   "LOCATION ('gpfdist://10.2.9.18:8081/data/source/Stammdaten/*.csv') format 'csv' (header delimiter ';') log errors into ext_test_err segment reject limit 2 rows;"
        print ' '
        print '/* Insert statement for diodor_extn '+filename+'*/'
        print ''
        print 'INSERT INTO DIODOR('
        kolom = headers.replace("[Double];",", ")
        kolom = kolom.replace("[String];"," , ")
        kolom = kolom.replace("[Date];"," , ")
        kolom = kolom.replace("[String]"," ) ")
        kolom = kolom.replace("[Date]"," ) ")
        kolom = kolom.replace("[Double]"," ) ")
        print kolom
#       print ''
        print 'SELECT '
        kolom = headers.replace("[Double];","::float, ")
        kolom = kolom.replace("[String];"," , ")
#       kolom = kolom.replace("[Date];"," , ")
        kolom = kolom.replace("DateValue[Date];" , "to_date(datevalue,'YYYY-MM-DD:HH24:MI:SS'),")
        kolom = kolom.replace("[String]"," ) ")
#       kolom = kolom.replace("[Date]"," ) ")
        kolom = kolom.replace("[Double]","::float ")
        kolom = kolom.replace("DateValue[Date]" , "to_date(datevalue,'YYYY-MM-DD:HH24:MI:SS')")
        print kolom
        print 'FROM DIODOR_EXT'+str(n)+';'
    elif set1 <= set2:
        print "bestaat al"
    else:
        set2=set1|set2
        print '/*CREATE EXTERNAL TABLE FOR EXCEL '+ filename+'*/'
        print ' ' 
        print 'CREATE EXTERNAL TABLE DIODOR_EXT'+str(n)+'('
        kolom = headers.replace("[Double];"," varchar, ")
        kolom = kolom.replace("DateValue[Date];"," Datevalue Date, ")
        kolom = kolom.replace("[String];"," varchar, ")
#       kolom = kolom.replace("[Date];"," varchar, ")
        kolom = kolom.replace("DateValue[Date]","Datevalue Date ")
        kolom = kolom.replace("[String]"," varchar)")
#       kolom = kolom.replace("[Date]"," varchar) ")
        kolom = kolom.replace("[Double]"," varchar) ")
        print kolom
        print   "LOCATION ('gpfdist://10.2.9.18:8081/data/source/Stammdaten/*.csv') format 'csv' (header delimiter ';') log errors into ext_test_err segment reject limit 2 rows;"
        print ' '
        print '/* Insert statement for diodor_extn '+filename+'*/'
        print ''
        print 'INSERT INTO DIODOR('
        kolom = headers.replace("[Double];",", ")
        kolom = kolom.replace("[String];"," , ")
        kolom = kolom.replace("[Date];"," , ")
        kolom = kolom.replace("[String]"," ) ")
        kolom = kolom.replace("[Date]"," ) ")
        kolom = kolom.replace("[Double]"," ) ")
        print kolom
#       print ''
        print 'SELECT '
        kolom = headers.replace("[Double];","::float, ")
        kolom = kolom.replace("[String];"," , ")
#       kolom = kolom.replace("[Date];"," , ")
        kolom = kolom.replace("DateValue[Date];" , "to_date(datevalue,'YYYY-MM-DD:HH24:MI:SS'),")
        kolom = kolom.replace("[String]"," ) ")
#       kolom = kolom.replace("[Date]"," ) ")
        kolom = kolom.replace("[Double]","::float ")
        kolom = kolom.replace("DateValue[Date]" , "to_date(datevalue,'YYYY-MM-DD:HH24:MI:SS')")
        print kolom
        print 'FROM DIODOR_EXT'+str(n)+';'

print ''
print'/*CREATE OVERALL TABLE DIODOR*/'
print '' 
print 'CREATE TABLE DIODOR('
kolom = headers.replace("[Double];"," float, ")
kolom = kolom.replace("[String];"," varchar, ")
kolom = kolom.replace("[Date];"," date, ")
kolom = kolom.replace("[String]"," varchar) ")
kolom = kolom.replace("[Date]"," date) ")
kolom = kolom.replace("[Double]"," float) ")
print kolom
print 'WITH (appendonly=true, orientation=column,compresstype=QUICKLZ)'
print 'distributed randomly'
print 'PARTITION BY RANGE (DateValue)'
print "( START (Date '2014-01-01') INCLUSIVE"
print "    END (Date '2016-12-01') EXCLUSIVE"
print "   EVERY (INTERVAL '1 month') );"

    
 #   else:
 #       os.rename(filename,'./fout/'+filename)
        
    
   