import string

def word_occurance(Filename):
    try:
        with open(Filename, "r") as file:
            word_count={}
            
            for Sen in file:
                Sen = Sen.strip().lower()
                Sen = Sen.translate(str.maketrans("","", string.punctuation))
                
                words = Sen.split()
                
                for word in words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count [word] = 1 
            
            sorted_word_count = dict(sorted(word_count.items()))
            
            for word , count in sorted_word_count.items():
                print(f"{word} : {count}")
    
    except FileNotFoundError:
        print(f"Error: File ' {Filename} ' was not found.")
        
Filename = input("Enter the Filename: ")
print("\nThe Words and the Number of Words Presented in the Text file is:-\n")
word_occurance(Filename)

'''
OUTPUT:-

Enter the Filename: c:\\Users\\MIRUDULAA\\Desktop\\Cognifyz\\Level 2\\Task_5_wordcount.txt    

    The Words and the Number of Words Presented in the Text file is:-

    apple : 2
    bitterguard : 1
    carrot : 2
    chilli : 1
    mango : 1
    orange : 2
    papaya : 2
    potato : 2
    strawberry : 1
    turnip : 2
'''