import random
a=1
b=100
Random_number = random.randint(a,b)
print(f"Guess the number Between {a} and {b} !\n")

while True:
    Guessing_Number = int(input(f"Enter the Number you Guessed between {a} and {b} : "))
    
    if Guessing_Number == Random_number:
        print(f"\nCongratulations! You Guessed the number {Random_number} Correctly")
        break
    
    elif Guessing_Number > Random_number:
        print("Too High")
    
    else:
        print("Too Low")
        
        
'''
Guess the number Between 1 and 100 !

Enter the Number you Guessed between 1 and 100 : 75
Too High
Enter the Number you Guessed between 1 and 100 : 72
Too Low
Enter the Number you Guessed between 1 and 100 : 74

Congratulations! You Guessed the number 74 Correctly
'''        