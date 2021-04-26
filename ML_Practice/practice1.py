# Time complexity
"""
Comparison of class functions of Time complexity =>

1 < log n < sqrt n < n < nlog n < n ^ 2 < n ^ 3 < ...  < 2 ^ n < 3 ^ n < ... n ^ n

log0 + log1 + log2 +..... + log(n-1)+ logn = log 1* 2 * 3 *...*n = log n!


Gometric progression :

a + ar + ar^2 + ar^3 +.....+ar^n =     (n)
                                    a(r      -  1)
                                    ----------------
                                        r - 1   


For single recursive function : 
    eg : factorial 

    consider fun factorial have M(n) time complexity

    def factorial(n):
        if n < 0:
            return -1
        elif n == 0:
            return 1
        else:
            return n * factorial(n-1)


    O( factorial(n) ) = O(1) + O( factorial (n-1) )
    M( n ) = O(1) + M( n-1 )

    M(0) = O(1) = 1

    M(n-1) =  1 + M( (n-1) - 1)
    M(n-2) =  1 + M( (n-2) - 1)

    Therefore ,
    M( n ) = O(1) + M( n-1 )
    M( n ) =  1   + 1 + M( (n-1) - 1) 
    M( n ) =  2  + M ( n - 2)
    M( n ) =  2  + 1 + M( (n-2) - 1)
    M( n ) =  3 + M( n - 3 )

    Thus,  = a + M ( n - a)

    when a  =  n , above equation is  =  n + M(0)
    => M(n) = n + 1
    dropping constant 1  =>  n


    Therefore time complexity is O( n )


for multiple recursive function :
    
     eg  : fibo of all numbers 

     def allFib(n):
        for i in range(n):
            print(str(i)+":, " + str(fib(i)))

    def fib(n):   =====================================> O ( 2 ^ n)
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return fib(n-1) + fib(n-2)

    Explaination : 

     considering single fib(n) function  =>
      
              fib(3)
            /       \
      fib(2)        fib(1)   ==========> Time complexity : branches ^ depth 
      /     \          |
   fib(1) fib(0)       1      =========> O ( 2 ^ n)

    considering allFib(n): 

    fib(1)   ->  2 ^ 1
    fib(2)   ->  2 ^ 2
    fib(3)   ->  2 ^ 3
    .
    .
    fib(n)   ->  2 ^ n

    allFib(n) =  2 ^ 1 + 2 ^ 2 + ...........+ 2 ^ n
              = [ 2 ^ (  n + 1 ) - 1 ]- 1 ===================> -1 since no 2 ^ 0 here
              = 2 ^ ( n + 1 ) - 2

    Therefore time complexity is O ( 2 ^ n )


    video 36 ?

    

"""



def sumOfDigits(num):
    assert num >=0  and int(num) == num, 'Sum is of positive integers only'
    if num == 0 :
        return 0
    else :
        return  int(num % 10) + sumOfDigits(num//10)

def superDigit(n, k):
    number = (int)(n * k)
    if number % 10 == number :
        return (int)(number) 
    else :
        return superDigit( sumOfDigits(number) , 1)
    

def powerOfNum(num, k):

    assert k >= 0 and int(k)==k, ' power cannot be negative'

    if k == 0 :
        return  1
     
    else :
        return num * powerOfNum(num, k-1)   


def gcd(a, b):
    while a != b :
        if a > b :
            a = a - b
        else :
            b = b - a
    return a

def gcd_rec(a, b) :
    """
    on basis of euclidean algorithm:
    gcd(48,18) =>
    48/18 = 2 remainder 12
    18/12 = 1 remainder 6
    12/6  = 2 remainder 0

    Therefore answer is 6

    gcd( a, b ) = gcd ( b , a mod b )
    gcd ( a , 0) =  a

    """
    assert int(a) == a and int(b) == b , ' only integer numbers'

    if a < 0 :
        a = -1 * a
    if b < 0 :
        b = -1 * b
    
    if b == 0 :
        return a 

    else : 
        return gcd(b , a % b)


def decToBin(num):
    """
    https://www.youtube.com/watch?v=4caFoQ0eoyg&list=PLWRfwqpR738WmkQCsyFjGd2cke3gVuBpj&index=17
    """
    assert int(num) ==  num , 'must be integer'
    if num == 0:
        return 0
    else :
        return num%2 + 10 * decToBin(num//2)


""" 
print(superDigit('123', 3))
print(sumOfDigits(0))
print(powerOfNum(3,-1))
print(gcd(8,12))
print(gcd_rec( 48 , 18)) 
print(decToBin(13))

"""

#One Dimensional Array

"""
from array import *
arr1 = array('i', [1, 2, 3, 4, 5, 5])
arr2 = array('i', [10, 11])
arr1.insert(2, 8)
print(arr1)

def linearSearch(arr, val):

    for elm in arr :
        if elm == val :
            return "found at index " + str(arr.index(val))
        
    return "not found"
#print(linearSearch(arr1, 3))

arr1.append(6)
arr1.extend(arr2)
tempList = [22, 33]
arr1.fromlist(tempList)
arr1.remove(8)
arr1.pop()
print("updated array " , arr1)
print("index of 22 " , arr1.index(22))
arr1.reverse()
print("reversed array " , arr1)
print(arr1.buffer_info())
print(arr1.count(5))
tempString = arr1.tostring()
intarr = array('i')
intarr.fromstring(tempString)
print(intarr)
print(intarr.tolist())
print(arr1[:-1])




# terminal :
>>> from array import *
>>> arr1 = array("i", [1,2,3])
>>> arr1
array('i', [1, 2, 3])
>>> del arr1[1]
>>> arr1
array('i', [1, 3])
>>> arr1.pop(0)
1
>>> arr1
array('i', [3])
>>> arr1.remove(3)
>>> arr1
array('i')
>>> arr1.insert(0, 22)
>>> arr1[1:]=[23, 34, 55]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign array (not "list") to array slice
>>> arr1.insert(1, 23)
>>> arr1.insert(2, 33)
>>> del arr1[:2]
>>> arr1
array('i', [33])
>>> 



"""




# Two Dimensional Array

"""
5   6   7   8   
9   10  11  12
4   45  16  18

"""
"""
import numpy as np 

twoDArr =  np.array([[5, 6, 7, 8] , [9, 10, 11, 12], [4, 45, 16, 18]])

print(twoDArr)

def access( Array, rowIndex, columnIndex) :
    if rowIndex >= len(Array) or columnIndex >= len(Array[0]) :
        print(" element not found")
    else :
        print(Array[rowIndex][columnIndex])

print(" element at row 2 and index 3 is ", access(twoDArr,  2, 3))

newTwoDArr =  np.insert(twoDArr, 0 , [[1, 2, 3]], axis = 1)
print("new Array with colum inserted at 0 ",  newTwoDArr)

def traverse(Array) :
    for i in range(len(Array)) :
        for j in range(len(Array[0])) :
            print(Array[i][j])
print(traverse(newTwoDArr))

def search(Array, val):
    for i in range(len(Array)) :
        for j in range(len(Array[0])) :
            if Array[i][j] == val :
                return "fount at row index = " + str(i) + " and column index = " + str(j)
    return "not found"

print(search(twoDArr, 12))

newDeletedArr = np.delete(newTwoDArr, 0 , axis = 1)  # returns new array
print(" old array ", newTwoDArr)
print(" delete array ", newDeletedArr)

newDeletedArr = np.append(newDeletedArr,[[99, 98 ,97, 79]] , axis = 0)
print(" append deleted array = ", newDeletedArr)
"""


def average() :
    elm =[]
    while(True):
        inp = input("enter a number")
        if inp == 'done' : break
        elm.append(float(inp))

    return sum(elm)/ len(elm)


#print(average())


import numpy as np
#inpArr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12])

def missingNumber(inpArr):
    
    n = len(inpArr)
    return ((n+1) * (n+2) //2) - sum(inpArr)

#print(missingNumber(inpArr))

#=======WRONG=================
#inpArr = np.array([1, 2 , 0 , 3, 4])
def pairOfInt(inpArr, sumValue):
    pair = {}
    for elm in inpArr:
        if (sumValue - elm) in inpArr:
            pair.append((elm, sumValue-elm)) 
    return pair

#print(pairOfInt(inpArr,5))

inpArr = np.array([22, 3, 77, 20, 1, 30, 44, 19, 21, 5, 9, 88, 54, 99])



def maxProduct(inpArr):
    firstMax = 0
    secondMax = 0

    for i in range(len(inpArr)-1):
        if inpArr[i+1] > inpArr[i]:
            if inpArr[i+1] > firstMax :
                firstMax = inpArr[i+1]
            if inpArr[i] > secondMax:
                secondMax = inpArr[i]
            print("a")
            print(firstMax , secondMax)
        else:
            if inpArr[i] > firstMax :
                firstMax = inpArr[i]
            if inpArr[i+1] > secondMax:
                secondMax = inpArr[i+1]
            print("b")
            print(firstMax, secondMax)
    print("first" , firstMax)
    print("second", secondMax)
    return firstMax * secondMax


def maxProductUsingSort(inpArr):
    inpArr.sort()
    return inpArr[-1] * inpArr[-2]


def maxProductOn(list1):
    # Python program to find second largest
# number in a list

# list of numbers - length of
# list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i]>secondmax and \
        mx != list1[i]:
        secondmax=list1[i]

print("Second highest number is : ",\
    str(secondmax))





print(maxProductOn(inpArr))


