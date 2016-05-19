
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