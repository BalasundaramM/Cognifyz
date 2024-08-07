def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)/1.8


Temperature =float(input("Enter the Temperature Number : "))
Unit = input("Enter the Unit Measure (C -> Celsius  and  F -> Fahrenheit ) : ") .strip().upper()

if Unit == 'C' :
    convert = celsius_to_fahrenheit(Temperature)
    print(f"The Converted Celsius to Fahrenheit is : {convert:.2f} °F")
    
elif Unit == 'F':
    convert = fahrenheit_to_celsius(Temperature)
    print(f"The Converted Fahrenheit Temperature to Celsius Temperature is : {convert:.2f} °C")
    
else:
    print("please check the Unit Measure ")
        
'''
OUTPUT:-

Enter the Temperature Number : 46
Enter the Unit Measure (C -> Celsius  and  F -> Fahrenheit ) : c
The Converted Celsius to Fahrenheit is : 114.80 °F

Enter the Temperature Number : 114.80
Enter the Unit Measure (C -> Celsius  and  F -> Fahrenheit ) : f
The Converted Fahrenheit Temperature to Celsius Temperature is : 46.00 °C
'''