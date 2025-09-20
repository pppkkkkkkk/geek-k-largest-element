import heapq

class Solution:
	def kLargest(self, arr, k):
		# Your code here
		minHeap = []
		
		for i in range(len(arr)):
		    heapq.heappush(minHeap, arr[i])
		    if len(minHeap) > k:
		        heapq.heappop(minHeap)
		
		tmp = []
		while minHeap:
		    tmp.append(heapq.heappop(minHeap))
		    
		ans = []
		for i in range(len(tmp)-1,-1,-1):
		    ans.append(tmp[i])
		return ans