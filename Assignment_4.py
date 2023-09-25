import copy

def objects(a):
    # Assume a = [1,2,[3,4,5]]
    # Assign a equal to the variable b that they should have same id address
    b = a

    # Tip: When element in a[2] changes value, c should also change. They shouldn't have same id.
    # Assign a copy of a to the variable c
    c = copy.copy(a)

    # Tip: When element in a[2] changes value, but d doesn't change. They shouldn't have same id.
    # Assign a deep copy of a to the variable d
    d = copy.deepcopy(a)

    # Assign the id of a to the variable id_a
    id_a = id(a)
    
    return b, c, d, id_a

def prime_number(number):
    """
    This is to review interactive loops and if statements
    You need to write for loop to make a list output of the prime number from 2 to the number.
    The range of numbers should not include the number as input.
    Example1:
            Input: number = 10
            Output:[2,3,5,7]
    Example2:
            Input: number = 100
            Output:[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    Example3:
            Input: number = 7
            Output:[2,3,5]
    """

    num = []
    #Write your code here
    q = list(range(2,number))
    num = q[:]
    for i in q:
        for j in q:
            if i!=j:
                if i%j == 0 and i in num:
                    num.remove(i)

    return num
    

def while_loop(number):
    
    """
    This is to review interactive loops and error statements
    At first,  you need to write try statement to check String input,
    If input is not an integer number, output will be String "Error".
    Finally you need to write a while loop to calculate the sum of num, num - 1, num -2,.....,1.
    Example1:
            Input: "3"
            Output: 6
            Explanation: 3 + 2 + 1 = 6
    Example2:
            Input: "Hello"
            Output: "Error"
            Explanation: Checked as a String in try statement, return "Error" with except statement.
    Example3:
            Input: "-1"
            Output: 0
            Explanation: It is an integer but nothing to do in while loop, so return defualt value as 0.
    """
    try:
        inp = int(number)
    except ValueError:
        return "Error"
    else:
        total = 0
        if inp<0:
            return 0
        else:
            while (inp > 0):
                total += inp
                inp -= 1
    return total