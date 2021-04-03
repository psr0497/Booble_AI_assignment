import sys
import csv
def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.

def permute(a, l, r):
	if l==r:
		print (toString(a))
	else:
		for i in range(l,r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l] # backtrack

if __name__=='__main__':
    with open(sys.argv[1],'r') as csv_file:
        csv_reader=csv.reader(csv_file)
        csv_reader=list(csv_reader)
        for line in csv_reader:
            for i in line:
                string = i
                n = len(string)
                a = list(string)
                permute(a, 0, n-1)