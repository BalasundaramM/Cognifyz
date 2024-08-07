def Calculator(num1,num2,Operator):
    if Operator == "+":
        result = num1 + num2
    elif Operator == "-":
        result = num1 - num2 
    elif Operator == "*":
        result = num1 * num2 
    elif Operator == "/":
        if num2 != 0:
            result = num1 / num2 
        else:
            print("Number cannot divide by Zero.")
            return
    elif Operator == "%":
        if num2 != 0:
            result = num1 % num2 
        else:
            print("Number cannot divide by Zero.")
            return 
    else:
        print("Invalid Operator")
        return
    
    if result.is_integer():
         print(f"The Result of {num1} {Operator} {num2} is : {int(result)}")
         
    else:
         print(f"The Result of {num1} {Operator} {num2} is : {result}")
         

num1 = float(input("Enter the First Number : "))
num2 = float(input("Enter the Second Number : "))
Operator = input("Enter an Operator (+ , - , * , / , %) :  ")
Calculator(num1,num2,Operator)    


'''
OUTPUT:-

Enter the First Number : 1
Enter the Second Number : 2

Enter an Operator (+ , - , * , / , %) :  +
The Result of 1.0 + 2.0 is : 3

Enter an Operator (+ , - , * , / , %) :  -
The Result of 1.0 - 2.0 is : -1

Enter an Operator (+ , - , * , / , %) :  *
The Result of 1.0 * 2.0 is : 2

Enter an Operator (+ , - , * , / , %) :  /
The Result of 1.0 / 2.0 is : 0.5

Enter an Operator (+ , - , * , / , %) :  %
The Result of 1.0 % 2.0 is : 1
'''