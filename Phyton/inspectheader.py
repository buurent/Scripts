import os
import glob

listing = glob.glob('*.csv')
csvfile = open( listing[0] , "rb")
headers = csvfile.next()
print listing[0]
oldheaders = headers
set2 = set(oldheaders.split(';'))

for filename in listing:
    csvfile = open( filename , "rb")
    headers = csvfile.next()
    set1 = set(headers.split(';'))
    if set1 <= set2:
        print filename
    else:
        print set2
 #   else:
 #       os.rename(filename,'./fout/'+filename)
        
    
   