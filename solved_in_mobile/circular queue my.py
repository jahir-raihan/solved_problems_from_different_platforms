class cq:
	def __init__(self,n):
		self.n = n
		self.queue = [None]*n
		self.head= self.tail = -1
		
	def enqueue(self,data):
		if self.head == -1 and self.tail == -1:
			self.head = self.tail = 0
			self.queue[self.tail] = data
			
		elif ( self.tail+1)%self.n==self.head:
			print('queue is full')
		else:
			self.tail = (self.tail+1)%self.n
			self.queue[self.tail] = data
			
	def dequeue(self):
		if self.head == -1 and self.tail == -1:
			print('nothin in queue')
			
		elif self.head == self.tail:
			self.head = self.tail = -1
			
		else:
			self.queue[self.head] ='\'Empty\''
			self.head = (self.head+1)%self.n
			print('new head',self.queue[self.head])
					
	def view(self):
		if self.head ==-1 and self.tail==-1:
			print('nothing in queue')
		if self.head == self.tail:
			print(self.queue[self.head])
		else:
			for i in self.queue:
				print(i,end=" ")
			print()
				
o = cq(5)
o.enqueue(1)
o.enqueue(2)
o.enqueue(3)
o.enqueue(4)
o.enqueue(5)

o.view()

o.dequeue()

o.view()

o.dequeue()
o.view()

o.enqueue(6)
o.enqueue(7)

o.view()

o.enqueue(8)

o.dequeue()
o.dequeue()
o.dequeue()
o.dequeue()
o.dequeue()
o.dequeue()

o.enqueue(11)
o.enqueue(12)
o.enqueue(13)
o.enqueue(14)
o.enqueue(15)
o.enqueue(16)

o.view()





		
		