from pprint import pprint
print str(5)
a=[[1,2,3,4],[1,2,3,4]]
try:
	a.remove(5)
except ValueError:
	pass

pprint(a)


a=[1,1,1,2]
for i,val in iter(a):
	print i,val
print a
b=list(a)
print b