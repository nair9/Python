
"""
Questons 1:
========================================================================================================
Given an OOP program that is about rectangle, please follow the requests above every function.
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        area = self.width*self.height
        return area
    
    def perimeter(self):
        perimeter = (self.width+self.height)*(2)
        return perimeter
    
    def diagonal(self):
        diagonal = (self.width**2+self.height**2)**(0.5)
        return diagonal
    
    def is_square(self):
        if self.width==self.height:
            return True
        else:
            return False
    
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

"""
Questons 2:
========================================================================================================
Given two strings s and t, determine whether they are isomorphic.
If the characters in s can be replaced according to some mapping relationship to get t, then the two strings are isomorphic.
Each occurrence of a character should map to another character without changing the order of the characters. 
Different characters cannot be mapped to the same character, the same character can only be mapped to the same character, and a character can be mapped to itself.
Example 1:
========================================
Input: s = "egg", t = "add"
Output: true
Example 2:
========================================
Input: s = "foo", t = "bar"
Output: false
Example 3:
========================================
Input: s = "paper", t = "title"
Output: true
"""
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping = {}
    used_chars = set()
    
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        
        if s_char in mapping:
            if mapping[s_char] != t_char:
                return False
        else:
            if t_char in used_chars:
                return False
            mapping[s_char] = t_char
            used_chars.add(t_char)
    
    return True


"""
Questons 3:
========================================================================================================
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
Example 1:
========================================
Input: arr = [2,2,3,4]
Output: 2
Explanation:The only lucky number in the array is 2 , because the value 2 occurs 2 times as well.
Example 2:
========================================
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation:1, 2, and 3 are all lucky numbers, and only the largest 3 among them needs to be returned.
Example 3:
========================================
Input: arr = [2,2,2,3,3]
Output: -1
Explanation:There are no lucky numbers in the array.
Example 4:
========================================
Input: arr = [5]
Output: -1
Example 5:
========================================
Input: arr = [7,7,7,7,7,7,7]
Output: 7
"""
def findLucky(arr):
    op = set(arr)
    lucky_arr = []
    for i in op:
        if arr.count(i)==i:
            lucky_arr.append(i)
    if lucky_arr:
        return(max(lucky_arr))
    else:
        return(-1)

"""
Questons 4:
========================================================================================================
Given an integer array nums, please return the number of numbers whose median is even.
Example 1:
========================================
Input: nums = [12,345,2,6,7896]
Output: 3
Explanation:
12 is 2 digits (even number of digits)
345 is 3 digits (odd number of digits)
2 is 1 digit (odd number of digits)
6 is 1 digit (the number of digits is odd)
7896 is 4 digits (even number of digits)
So only 12 and 7896 are numbers with an even number of digits
Example 2:
========================================
Input: nums = [555,901,482,1771]
Output: 1
Explanation:Only 1771 is a number with an even number of digits.
Example 3:
========================================
Input: nums = [5464,545,12131,15454,112,1,65,457]
Output: 2
Explanation:
Only 5464 and 65 are numbers with an even number of digits.
"""
def findNumbers(nums):
    ctr = 0
    for i in nums:
        if len(str(i))%2==0:
            ctr+=1
    ans = ctr
    return ans
