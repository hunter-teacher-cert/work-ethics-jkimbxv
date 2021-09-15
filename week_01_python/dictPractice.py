#For dictionaries you can write a program that reads a file and uses a
#dictionary to count the number of times each word appears.
#reading in a txt file
f = open("demofile.txt","r") #f is a string of the text file inserted
f = f.read()
fileWords = {}

#detects next words by using spaces.
def findNextWord(text,startLook): #returns index of end of word
    iStart = startLook;
    if (text[startLook] == " "):
        iStart+=1;
    i = iStart;
    while (text[i] != " " and text[i] != "."):
        i+=1
    return i;

#detects if word is repeated
def isItRepeated(hash,word):
    for tableVal in hash:
        if tableVal == word:
            return True;
    return False;


#main part here
#goes thru file and finds next word, adds it to dictionary
iCurr = 0;
while (iCurr < len(f)):
    iEnd = findNextWord(f,iCurr)
    newWord = f[iCurr:iEnd]
    if (isItRepeated(fileWords,newWord)):
        fileWords[newWord] = fileWords[newWord]+1;
    else:
        fileWords[newWord] = 1;
    iCurr = iEnd+1;
print(fileWords)
