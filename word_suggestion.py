import difflib
import sys
import csv 

l=[]
res=[]
s=""
count=0
with open('dictionary.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    csv_reader=list(csv_reader)
    for lines in csv_reader:
        l.append(lines[0])
        
    
    ans=difflib.get_close_matches(sys.argv[1], l)
    ans.sort()
    for i in range(len(ans)):
        res.append(ans[i])
        count=count+1
        if count>5:
            break
    s=",".join(res)
    print(s)