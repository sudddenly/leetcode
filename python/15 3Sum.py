"""
https://leetcode.com/problems/3sum/description/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.
"""

class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		:runtime: 1218 ms
		"""
		length = len(nums)
		ret = []
		if length < 3: return ret

		nums.sort()
		def find(num, begin, end, target):
			l, r = begin, end
			while l < r:
				if num[l] + num[r] + target == 0:
					ans = []
					ans.append(num[l])
					ans.append(num[r])
					ans.append(target)
					ret.append(ans)
					while l < r and num[l] == num[l + 1]:l += 1
					while l < r and num[r] == num[r - 1]:r -= 1
					l += 1
					r -= 1
				elif num[l] + num[r] + target < 0:l += 1
				else:r -= 1
			return 0

		for i in range(length - 2):
			if i > 0 and nums[i] == nums[i - 1]:
				i +=1
				continue
			tmp = find(nums, i + 1, length - 1, nums[i])
		return ret


