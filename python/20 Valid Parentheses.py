"""
https://leetcode.com/problems/valid-parentheses/description/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

用list模拟stack，使用list默认方法append、pop、index完成条件判断，简单高效
"""

class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		if len(s) % 2 == 1: return False

		stack = []
		left = ("(", "[", "{")
		right = (")","]","}")
		zip(left,right)
		for v in s:
			if v in left:
				stack.append(v)
			else:
				if not stack:
					return False
				p = stack.pop()
				if left.index(p) != right.index(v):
					return False
		return len(stack) == 0