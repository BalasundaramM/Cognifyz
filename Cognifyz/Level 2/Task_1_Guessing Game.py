import random
Random_number = random.randint(1,100)
print("Guess the number Between 1 and 100 !\n")
while True:
    Guessing_Number = int(input("Enter the Number you Guessed between 1 and 100 : "))
    
    if Guessing_Number == Random_number:
        print(f"\nCongratulations! You Guessed the number {Random_number} Correctly")
        break
    
    elif Guessing_Number > Random_number:
        print("Too High")
    
    else:
        print("Too Low")
        
        
'''
Guess the number Between 1 and 100 !

Enter the Number you Guessed between 1 and 100 : 25
Too High
Enter the Number you Guessed between 1 and 100 : 23
Too Low
Enter the Number you Guessed between 1 and 100 : 24

Congratulations! You Guessed the number 24 Correctly
'''        