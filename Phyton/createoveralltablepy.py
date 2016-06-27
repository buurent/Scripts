import os
import glob
import sys
import csv
sys.stdout = open('create_table.sql', 'w')
set1=()
set2=()

listing = glob.glob('*.csv')
#csvfile = open( listing[0] , "rb")
#headers = csvfile.next()
#set2 = set(headers.split(';'))
#print set2
n=0

for filename in listing:
    n=n+1
    m=1
    csvfile = open(filename , "r")
    headers = csvfile.next()
    set1 = set(headers.split(';'))
    if n == 1:
        set2 = set1
        print '/*CREATE EXTERNAL TABLE FOR EXCEL '+ filename+'*/'
        print ' ' 
        print 'CREATE EXTERNAL TABLE DIODOR_EXT'+str(n)+'('
        for kolom in set1:
            if m >= int(len(set1)):
                kolom = kolom.replace("Double","float")
                kolom = kolom.replace("String","varchar")
                kolom = kolom.replace("]",") ")
                kolom = kolom.replace("["," ")
            else:
                kolom = kolom.replace("Double","float")
                kolom = kolom.replace("String","varchar")
                kolom = kolom.replace("]",",")
                kolom = kolom.replace("["," ")
            print kolom
            m=m+1
        m=1
        print   "LOCATION ('gpfdist://10.2.9.18:8081/data/source/Stammdaten/*.csv') format 'text' (delimiter ';') log errors into ext_test_err segment reject limit 2 rows;"
        print ' '
        print '/* Insert statement for diodor_extn '+filename+'*/'
        print ''
        print 'INSERT INTO TABLE DIODDOR('
        for kolom in set1:
            if m >= int(len(set1)):
                kolom = kolom.replace("Double","")
                kolom = kolom.replace("String","")
                kolom = kolom.replace("\sDate","")
                kolom = kolom.replace("]",") ")
                kolom = kolom.replace("["," ")
            else:
                kolom = kolom.replace("Double","")
                kolom = kolom.replace("String","")
                kolom = kolom.replace("\sDate","")
                kolom = kolom.replace("]",",")
                kolom = kolom.replace("["," ")
            print kolom
            m=m+1
        m=1
        print 'SELECT '
        for kolom in set1:
            if m >= int(len(set1)):
                kolom = kolom.replace("Double","")
                kolom = kolom.replace("String","")
                kolom = kolom.replace("\sDate","")
                kolom = kolom.replace("]"," )")
                kolom = kolom.replace("["," ")
            else:
                kolom = kolom.replace("Double","")
                kolom = kolom.replace("String","")
                kolom = kolom.replace("\sDate","")
                kolom = kolom.replace("]",",")
                kolom = kolom.replace("["," ")
            print kolom
            m=m+1
        print 'FROM DIODOR_EXT'+str(n)+';'
    elif set1 <= set2:
        print ""
    else:
        set2=set1|set2
        print '/*CREATE EXTERNAL TABLE FOR EXCEL '+filename+'*/'
        print ' ' 
        print 'CREATE EXTERBAL TABLE DIODOR_EXT'+str(n)+'('
        for kolom in set1:
            if m >= int(len(set1)):
                kolom = kolom.replace("Double","float")
                kolom = kolom.replace("]",") ")
                kolom = kolom.replace("["," ")
            else:
                kolom = kolom.replace("Double","float")
                kolom = kolom.replace("]",",")
                kolom = kolom.replace("["," ")
            print kolom
            m=m+1
        m=1
        print   "LOCATION ('gpfdist://10.2.9.18:8081/data/source/Stammdaten/*.csv') format 'text' (delimiter ';') log errors into ext_test_err segment reject limit 2 rows;"
        print ' '
        print '/* Insert statement for diodor_extn'+filename+'*/'
        print ''
        print 'INSERT INTO TABLE DIODDOR('
        for kolom in set1:
            if m >= int(len(set1)):
                kolom = kolom.replace("Double","float")
                kolom = kolom.replace("]"," )")
                kolom = kolom.replace("["," ")
            else:
                kolom = kolom.replace("Double","float")
                kolom = kolom.replace("]",",")
                kolom = kolom.replace("["," ")
            print kolom
            m=m+1
        m=1
        print 'SELECT '
        for kolom in set1:
            if m >= int(len(set1)):
                kolom = kolom.replace("Double","float")
                kolom = kolom.replace("]"," )")
                kolom = kolom.replace("["," ")
            else:
                kolom = kolom.replace("Double","float")
                kolom = kolom.replace("]",",")
                kolom = kolom.replace("["," ")
            print kolom
            m=m+1
        print 'FROM DIODOR_EXT'+str(n)+';' 


print ''
print'/*CREATE OVERALL TABLE DIODOR*/'
print '' 
print 'CREATE TABLE DIODOR('
m=1 
for kolom in set2:
    if m >= int(len(set2)):
        kolom = kolom.replace("Double","float")
        kolom = kolom.replace("String","varchar")
        kolom = kolom.replace("]"," )")
        kolom = kolom.replace("["," ")
    else:
        kolom = kolom.replace("Double","float")
        kolom = kolom.replace("String","varchar")
        kolom = kolom.replace("]",",")
        kolom = kolom.replace("["," ")
    print kolom
    m=m+1
print 'WITH (appendonly=true, orientation=column,compresstype=QUICKLZ)'
print 'distributed randomly'
print 'PARTITION BY RANGE (DateValue)'
print "( START (Date '2014-01-01') INCLUSIVE"
print "    END (Date '2016-12-01') EXCLUSIVE"
print "   EVERY (INTERVAL '1 month') );"

    
 #   else:
 #       os.rename(filename,'./fout/'+filename)
        
    
   