def Palindrome_string(Name):
    Reverse_Name = ''
    for s in reversed(Name):
        Reverse_Name += s
    if Reverse_Name == Name:
        return f"The given String {Name} is a Palindrome."
    else:
        return f"The given String {Name} is not a Palindrome."
    
Name=input("Enter a String : ").lower()
Palindrome= Palindrome_string(Name)
print(Palindrome)  

'''
OUTPUT:-

Enter a String : racecar
The given String racecar is a Palindrome.

Enter a String : technology
The given String technology is not a Palindrome.
'''