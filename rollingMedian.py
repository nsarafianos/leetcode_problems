import heapq
class Solution():
	# Given a stream of numbers compute the running median
	# Key Idea: Use Max Heap for bottom part of numbers and Min Heap for top part. Remember that python's heapq is min-heap so you need to add a minus sign in front. A very nice reference video from HackerRank: https://www.youtube.com/watch?v=VmogG01IjYc
	
    def runningMedian(self, nums):
        lower, higher = [], []
        heapq.heapify(lower)
        heapq.heapify(higher)
        medians = [0] * len(nums)
        for i, n in enumerate(nums):
            self.addNumber(n, lower, higher)
            self.rebalance(lower, higher)
            medians[i] = self.getMedian(lower, higher)
        return medians
		
    def addNumber(self, n, lower, higher):
        if len(lower) == 0 or -n > lower[0]:
            heapq.heappush(lower, -n)
        else:
            heapq.heappush(higher, n)

    def rebalance(self, lower, higher):
        if len(lower) - len(higher) > 1:
            heapq.heappush(higher, -heapq.heappop(lower))
        elif len(higher) - len(lower) > 1:
            heapq.heappush(lower, -heapq.heappop(higher))


    def getMedian(self, lower, higher):
        if len(lower) == len(higher):
            return (-lower[0] + higher[0])/2.
        elif len(lower) > len(higher):
            return -lower[0]
        else:
            return higher[0]
			
			
sol = Solution()
print sol.runningMedian([2,1,5,7,8,10,0, -2, 100])