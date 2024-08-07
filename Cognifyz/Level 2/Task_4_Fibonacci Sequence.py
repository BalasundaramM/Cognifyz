def fibonacci_Sequence(num1,num2,n):
    for i in range(n):
        sum = num1 + num2
        num1=num2
        num2=sum
        print(sum,end =' ')

num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))
n = int(input("Enter the Length of the Fibonacci Sequence : "))
print("The Fibonacci Sequence Numbers are : ")
fibonacci_Sequence(num1,num2,n)

'''
OUTPUT:-

    Enter the First Number : 1
    Enter the Second Number : 2
    Enter the Length of the Fibonacci Sequence : 5
    The Fibonacci Sequence Numbers are : 
    3 5 8 13 21 
'''