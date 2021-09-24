word = str(input("Pleas write a word: "))
reversedWord = ''
for x in range(len(word)-1, -1, -1):
    reversedWord += word[x]
print("The reversed word is: "+reversedWord)
