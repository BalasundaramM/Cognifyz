import sys
def Password_checker(password):
# Create variables to store the count of letters
    num_count= 0
    special= 0
    upper_case = 0
    lower_case = 0
    
    # Check the length of the password 
    if len(password)>=6: 
        
        for i in password: 
            if i.isnumeric():  #check if the given password has the number then the count will increase
                num_count += 1 
                
            elif i.isupper() :
                upper_case += 1
            
            elif i.islower():
                lower_case += 1
            else: 
                special += 1
            
        '''check if the given (number or alphabet or special character) in this any one value was written 
            then it print the password is weak'''
        if( password.isalpha()) or (password.isnumeric()) or (special >=2) :
            print("Your password is weak.")
            sys.exit()
        # check if the given password has upper case greater or equal to 1 lowercase greater or equal to 1
        # and number count is greaterthan or equal to 2 
        # and special character is greater than or equal to 1   
        elif( num_count >=2 and special >=1 and upper_case >=1 and lower_case >= 4):
            '''check if the password is greater than or equal 16 then it prints the password is very strong
            else it is strong'''
            if len(password) >= 10:
                print("Your password is Very strong")
            else:    
                print("Your password is strong")
                sys.exit()

        else: #if the Condition not satisfied then it prints the password is ok
            print("Your password is Ok")                

    else:  # checks if password length is less than 8 then it prints password is too short
        print("your password is too short")
        
password=input("Create Password with minimum 6 characters: ")
Password_checker(password)        

'''
OUTPUT :-
        Create Password with minimum 6 characters: Cognifyz@2024
        Your password is Very strong
            
        Create Password with minimum 6 characters: Cogz@20z      
        Your password is strong  
        
        Create Password with minimum 6 characters: Cognifyz@    
        Your password is Ok
        
        Create Password with minimum 6 characters: Cognifyz     
        Your password is weak.
        
        Create Password with minimum 6 characters: Co@20        
        your password is too short
   
'''