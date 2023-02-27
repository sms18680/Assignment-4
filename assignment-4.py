# Assignment-4
# Q-1) Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# sample input: 10
# sample output: 35

argument=int(input('enter the number....'))
add = lambda a : a + 25
print(add(argument))
 

# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]

# i = [1,2,3,4,5,6,7]
# a = []
# for i in [1,2,3,4,5,6,7]:
#     a.append(i*3)
# print(a)

nums=(1,2,3,4,5,6,7)
print('original list:', nums)
result= map(lambda x: x + x + x, nums)
print('\nTriple of said list numbers:')
print(list(result))

# def triple(num):
#     return int (num)*3
# result = map(triple, input('Enter the list of int...').split(','))
# print('Triple of all the numbers of entered list of int...',list(result))







#Write a Python program to square the elements of a list using map() function.
#Sample List: [4, 5, 2, 9]
#Square the elements of the list:
#[16, 25, 4, 81]

def square_num(n):
    return n*n
nums = [4,5,2,9]
print('original list:',nums)
result = map(square_num, nums)
print('square the elements of the said list using map():')
print(list(result))

