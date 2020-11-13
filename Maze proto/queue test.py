from queue import *

q = Queue()
s = LifoQueue()


s.put([1,2])
s.put([2,3])
s.put(3)

print(s.qsize())

for i in range(s.qsize()):
	print(s.get())