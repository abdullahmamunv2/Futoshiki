from pprint import pprint
print str(5)
a=[[1,2,3,4],[1,2,3,4]]
try:
	a.remove(5)
except ValueError:
	pass

pprint(a)


def createGenerator():
	mylist = range(3)
	for i in mylist:
		yield i*i
mygenerator = createGenerator()
for i in mygenerator:
	print(i)
for i in mygenerator:
	print(i)
a=['1']
print map(int,a)