
word = input("Enter the word: ")
words = word.split()
pig_latin = ""

if len(words)>1:
    print("Please Type only one word at a time.")
elif len(words)==0:
    print("Please type something..")
else:
    for i in word:
        if i.isnumeric():
            print("No numbers allowed in the word")
            pig_latin=" "
            break
        else: 
            first_letter = word[0]
            rest_letters = word[1:]
            if first_letter in ('a', 'e', 'i', 'o', 'u'):
                pig_latin = word+'ay'
                    
            else:
                pig_latin = f"{rest_letters}{first_letter}ay"

print(pig_latin)