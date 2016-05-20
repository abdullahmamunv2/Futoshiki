from pprint import pprint
print str(5)
a=[[1,2,3,4],[1,2,3,4]]
try:
	a.remove(5)
except ValueError:
	pass

pprint(a)


try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

q = Q.PriorityQueue()
q.put((3,(3,3)))
q.put((1,(3,3)))
q.put((2,(3,3)))
while not q.empty():
	print q.get(),