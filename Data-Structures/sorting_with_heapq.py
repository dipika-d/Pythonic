import heapq

nums = [-1,2,-3,4,-5,6,-7,8,-9,10]


# convert the list into heap
heap = list(nums)
heapq.heapify(heap)

# heap[0] will always be the smallest number in a heap
# heap[-1] therefore will be the largest number
print(heap)
print('*'*20)
print("Smallest in heap  = ",heap[0])
print('*'*20)
print("Largest in heap = ",heap[-1])

# to pop the smallest item and replace it with the next smallest
# this happens in O(log N) where N is the size of the heap
print(heap)
print('*'*20)
print("Smallest = ",heapq.heappop(heap))
print('*'*20)
print("Next smallest = ",heapq.heappop(heap))
print('*'*20)

# printing the numbers from smallest to largest
print("Printing from smallest to largest \n")
heap = list(nums)
heapq.heapify(heap)

for i in range(len(heap)):
	try:
		print(heapq.heappop(heap))
	except KeyboardInterrupt:
		break