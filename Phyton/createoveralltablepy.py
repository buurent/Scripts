import os
import glob
import sys
import csv
sys.stdout = open('create_table.sql', 'w')

listing = glob.glob('*.csv')
#csvfile = open( listing[0] , "rb")
#headers = csvfile.next()
#set2 = set(headers.split(';'))
#print set2
n=0

for filename in listing:
    n=n+1
    csvfile = open(filename , "rb")
    headers = csvfile.next()
    set1 = set(headers.split(';'))
    if n == 1:
        set2 = set1
        print 'CREATE EXTERBAL TABLE DIODOR_EXT'+str(n)+'('
        for kolom in sorted(set1):
            if len(set1) == len(set1)-1:
                kolom = kolom.replace("Double","float")
                kolom = kolom.replace("]"," ")
                kolom = kolom.replace("["," ")
            else:
                kolom = kolom.replace("Double","float")
                kolom = kolom.replace("]",",")
                kolom = kolom.replace("["," ")   
            print kolom
        print   "LOCATION ('gpfdist://10.2.9.18:8081/data/source/Stammdaten/*.csv') format 'text' (delimiter ';') log errors into ext_test_err segment reject limit 2 rows;'"   
    elif set1 <= set2:
        print "ongewijzigd"
    else:
        set2=set1|set2
        print 'CREATE EXTERBAL TABLE DIODOR_EXT'+str(n)+'('
        for kolom in sorted(set1):
            kolom = kolom.replace("Double","float")
            kolom = kolom.replace("]"," ,")
            kolom = kolom.replace("["," ")
            print kolom
        print   "LOCATION ('gpfdist://10.2.9.18:8081/data/source/Stammdaten/*.csv') format 'text' (delimiter ';') log errors into ext_test_err segment reject limit 2 rows;'"   



print 'CREATE TABLE DIODOR('
for kolom in sorted(set2):
    kolom = kolom.replace("Double","float")
    kolom = kolom.replace("]"," ,")
    kolom = kolom.replace("["," ")
    print kolom
print 'WITH (appendonly=true, orientation=column,compresstype=QUICKLZ)'
print 'DISTRIBUTED BY VIN;'
    
 #   else:
 #       os.rename(filename,'./fout/'+filename)
        
    
   