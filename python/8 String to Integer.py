"""
https://leetcode.com/problems/string-to-integer-atoi/description/
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.
python代码比较简单，不做详细解释了
"""

class Solution(object):
	def myAtoi(self, str):
		"""
		:type str: str
		:rtype: int
		:Runtime: 82 ms
		"""
		if not str  :
			return 0
		str = str.strip()
		if not str  :
			return 0
		number, sign = 0, 1
		if str[0] == '-':
			sign = -1
			str = str[1:]
		elif str[0] == '+':
			sign = 1
			str = str[1:]

		for i in str:
			if i >= '0' and i <='9':
				number = 10*number + ord(i) - ord('0')
			else:
				break

		number = number * sign
		number = number if number < 2147483647 else 2147483647
		number = number if number > -2147483648 else -2147483648
		return number