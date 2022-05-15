"""
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
"""

#Answer

def summation(num):
    
    summ = 0 
    if num > 0 :
        for i in range(1,num+1):
            summ = summ + i
        
    return summ
