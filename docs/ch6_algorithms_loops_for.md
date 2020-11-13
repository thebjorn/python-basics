# for-loops

Hvis vi har en liste:

    >>> words = ['mange', 'små', 'ord']
    
skriv ut hvert ord på en egen linje:

    print(words[0])
    print(words[1])
    print(words[2])
    
- [ ] DRY (don't repeat yourself)


    for i in range(3):
        print(words[i])

bedre:        
         
    for i in range(len(words)):
        print(words[i])

best:

    for word in words:
        print(word)
        
