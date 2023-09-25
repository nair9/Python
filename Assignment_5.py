"""
QUESTION 1:
========================================================================================================
Give a list of numbers, write a function to find the maximum number in the list.
Note: For the purpose of this problem, we define empty list will return None.

NOTE: DO NOT USE "MAX" KEYWORD. WRITE algorithm using loop. 

Example 1:
========================================
Input: [10, 5, 20, 15, 25]
Output: 25
Example 2:
========================================
Input:[10,10,10]
Output: 10
Example 3:
========================================
Input: []
Output: None
"""

def find_maximum(numbers):
    if numbers:    
        op = 0
        for i in numbers:
            if i > op:
                op = i
    else:
        op = None
    return op



"""
QUESTION 2: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
Example 1:
========================================
Input: 0
Output: ['']
Example 2:
========================================
Input: 1
Output: ['()']
Example 3:
========================================
Input: 2
Output: ['(())', '()()']
Example 4:
========================================
Input: 3
Output: ['((()))', '(()())', '(())()', '()(())', '()()()'])
"""

def generateParenthesis(n):
    def combination(ans, cur, open_count, close_count, max_count):
        if len(cur) == max_count * 2:
            ans.append(cur)
            return
        if open_count < max_count:
            combination(ans, cur + '(', open_count + 1, close_count, max_count)
        if close_count < open_count:
            combination(ans, cur + ')', open_count, close_count + 1, max_count)
        
    ans = []
    combination(ans, '', 0, 0, n)
    return ans



"""
QUESTION 3: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true

Explanation:
After removing non-alphanumeric charactors and ignoring cases, the input is:  amanaplanacanalPanama
which reads the same as backward and forward, so it is true.

Example 2:
=========================================
Input: "race a car"
Output: false
Write a function named isPalindrome that takes a string as an input and returns a bool as an output.

Explanation:
After removing non-alphanumeric charactors and ignoring cases, the input is:  raceacar
which does not read the same as backward and forward, so it is false.
"""

def isPalindrome(x):

    import re
    inp = (re.sub('\W+','',x)).lower()
    inp1 = list(inp)
    inp2 = inp1[:]
    inp2.reverse()
    
    return (inp1 == inp2)
    
