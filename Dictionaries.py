dictionary = {
    "dekho ":" look",
    "na" : "please",
    "Yaar":"hey!dude",
    "bultaoreune":"I'm on fire",
    
}


sentence=("Yaar dekho na (Hindi to English). bultaoreune (Korean to English ) ")
wordList=sentence.split(" ")
print(wordList)

for word in wordList:
    if word in dictionary.keys():
        print(dictionary[word])
    #if word == dictionary[word]

