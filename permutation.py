import sys
import csv
def toString(List):
	return ''.join(List)


def permute(a, l, r):
	if l==r:
		print (toString(a))
	else:
		for i in range(l,r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l]

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
