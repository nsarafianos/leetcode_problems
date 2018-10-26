from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
	# A brute-force solution is to use a deque for efficient popping
	# and compute the max in each window. 

        if len(nums) == 0:
            return []
        if len(nums) <= k:
            return [max(nums)]
        finish = k
        q = deque(nums[0:finish])

        prev_max = max(q)
        wind = [prev_max]
        while finish < len(nums):
            finish += 1
            q.popleft()
            q.append(nums[finish-1])
            wind.append(max(q))
        return wind


    def maxSlidingWindow_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
	# Key idea: Deque which stores the index of max in each window in the 
	# very first element. No need to to traverse each window to find max any more

        if len(nums) == 0:
            return []
        if k == 0:
            return nums
	
	q, res = deque(), []
	
	# Iterate through first window. Put the index of the max on the very left of the deque
	# If new max shows up pop whatever's left of it. Elements on the right of the max
	# stay as the are
	for i in range(k):
	    while len(q) != 0:
		if nums[i] > nums[q[-1]]:
		    q.pop()
		else:
		    break
	    q.append(i)
	
	# Iterate through rest of elements. If index of max no longer in window pop it
	# Repeat same process with above by checking new element and adding it to the deque
	# Append final max (of last window).
	for i in range(k, len(nums)):
	    res.append(nums[q[0]])
	    if q[0] < i - k + 1:
		q.popleft()
            
	    while len(q) != 0:
		if nums[i] > nums[q[-1]]:
		    q.pop()
		else:
		    break
	    q.append(i)
	res.append(nums[q[0]])
	return res
