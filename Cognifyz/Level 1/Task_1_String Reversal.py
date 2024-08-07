def String_Reversal(Name):
    Reverse_Name = ''
    for s in reversed(Name):
        Reverse_Name += s
    return (f"The Reversed string is : {Reverse_Name}")
    
Name=input("Enter a String : ")
Name_reverse= String_Reversal(Name)
print(Name_reverse)    

'''
OUTPUT:-

Enter a String : Cognifyz
The Reversed string is : zyfingoC
'''
