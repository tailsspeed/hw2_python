doc = open("document.txt", "r")
doc_data = doc.read()
#attempt to remove as many common special characters in the document
#assuming pronouns are not removed
doc_list = doc_data.replace('\n', ' ').replace(',', '').replace(':', '').replace('.', ' ').replace(';', '').replace('(', '').replace(')', '').replace('“', '').replace('”', '').split(' ')
#print(doc_list)
list_of_words = [] #list of unique words
list_of_wc = [] #list of word count corresponding to list_of_words

#first, we need to find all the unique words
for i in range(len(doc_list)): #iterate through words from document
    is_unique = True
    for j in range(len(list_of_words)): #check if words are unique
        if doc_list[i] == list_of_words[j]:
            #word is already in list of unique words, increment word count
            is_unique = False
            list_of_wc[j] = list_of_wc[j] + 1
    if is_unique and doc_list[i] != '' and doc_list[i] != ' ':
        #add word to list
        list_of_words.append(doc_list[i])
        list_of_wc.append(1)
        
#now to sort by most frequent words
i = 0; #index 0 of the list
while i < len(list_of_words): #iterate through list of unique words
    j = 0
    while j < len(list_of_words) - i - 1:
        if list_of_wc[j] < list_of_wc[j+1]: #sort by descending order
            #swapping both the word and word count positions
            temp = list_of_wc[j]
            list_of_wc[j] = list_of_wc[j+1]
            list_of_wc[j+1] = temp
            
            temp = list_of_words[j]
            list_of_words[j] = list_of_words[j+1]
            list_of_words[j+1] = temp
        j = j + 1
    i = i + 1

#prelim display
for count in range(len(list_of_words)):
    print(list_of_words[count] + ": " + str(list_of_wc[count]))

        
doc.close()
doc = open("document.txt", "r")
doc_data = doc.read()
#attempt to remove as many common special characters in the document
doc_list = doc_data.replace('\n', ' ').replace(',', '').replace(':', '').replace('.', ' ').replace(';', '').replace('(', '').replace(')', '').replace('“', '').replace('”', '').split(' ')
#print(doc_list)
list_of_words = [] #list of unique words
list_of_wc = [] #list of word count corresponding to list_of_words

#first, we need to find all the unique words
for i in range(len(doc_list)): #iterate through words from document
    is_unique = True
    for j in range(len(list_of_words)): #check if words are unique
        if doc_list[i] == list_of_words[j]:
            #word is already in list of unique words, increment word count
            is_unique = False
            list_of_wc[j] = list_of_wc[j] + 1
    if is_unique and doc_list[i] != '' and doc_list[i] != ' ':
        #add word to list
        list_of_words.append(doc_list[i])
        list_of_wc.append(1)
        
#now to sort by most frequent words
i = 0; #index 0 of the list
while i < len(list_of_words): #iterate through list of unique words
    j = 0
    while j < len(list_of_words) - i - 1:
        if list_of_wc[j] < list_of_wc[j+1]: #sort by descending order
            #swapping both the word and word count positions
            temp = list_of_wc[j]
            list_of_wc[j] = list_of_wc[j+1]
            list_of_wc[j+1] = temp
            
            temp = list_of_words[j]
            list_of_words[j] = list_of_words[j+1]
            list_of_words[j+1] = temp
        j = j + 1
    i = i + 1

#sorting the letters based on ASCII
for k in range(len(list_of_words)):
    for l in range(len(list_of_words) - 1):
        if list_of_wc[l] == list_of_wc[l + 1] and list_of_words[l].lower() > list_of_words[l + 1].lower():
            #comparing the ASCII values of words with the same word count and swapping if necessary
            #swapping both the word and word count positions
            temp = list_of_wc[l]
            list_of_wc[l] = list_of_wc[l+1]
            list_of_wc[l+1] = temp
            
            temp = list_of_words[l]
            list_of_words[l] = list_of_words[l+1]
            list_of_words[l+1] = temp
    

#prelim display
for count in range(5): #changed to display the top 5
    print(list_of_words[count] + ": " + str(list_of_wc[count]))

        
doc.close()
doc = open("document.txt", "r")
doc_data = doc.read()
#attempt to remove as many common special characters in the document
doc_list = doc_data.replace('\n', ' ').replace(',', '').replace(':', '').replace('.', ' ').replace(';', '').replace('(', '').replace(')', '').replace('“', '').replace('”', '').split(' ')
#print(doc_list)
list_of_words = [] #list of unique words
list_of_wc = [] #list of word count corresponding to list_of_words

#first, we need to find all the unique words
for i in range(len(doc_list)): #iterate through words from document
    is_unique = True
    for j in range(len(list_of_words)): #check if words are unique
        if doc_list[i] == list_of_words[j]:
            #word is already in list of unique words, increment word count
            is_unique = False
            list_of_wc[j] = list_of_wc[j] + 1
    if is_unique and doc_list[i] != '' and doc_list[i] != ' ':
        #add word to list 
        list_of_words.append(doc_list[i])
        list_of_wc.append(1)
        
#now to sort by most frequent words
i = 0; #index 0 of the list
while i < len(list_of_words): #iterate through list of unique words
    j = 0
    while j < len(list_of_words) - i - 1:
        if list_of_wc[j] < list_of_wc[j+1]: #sort by descending order
            #swapping both the word and word count positions
            temp = list_of_wc[j]
            list_of_wc[j] = list_of_wc[j+1]
            list_of_wc[j+1] = temp
            
            temp = list_of_words[j]
            list_of_words[j] = list_of_words[j+1]
            list_of_words[j+1] = temp
        j = j + 1
    i = i + 1

#sorting the letters based on ASCII
for k in range(len(list_of_words)):
    for l in range(len(list_of_words) - 1):
        if list_of_wc[l] == list_of_wc[l + 1] and list_of_words[l].lower() > list_of_words[l + 1].lower():
            #comparing the ASCII values of words with the same word count and swapping if necessary
            #swapping both the word and word count positions
            temp = list_of_wc[l]
            list_of_wc[l] = list_of_wc[l+1]
            list_of_wc[l+1] = temp
            
            temp = list_of_words[l]
            list_of_words[l] = list_of_words[l+1]
            list_of_words[l+1] = temp
    

#prelim display
print('') #added new line
for count in range(len(list_of_words)): #changed to display the top 5
    print(list_of_words[count] + ": " + str(list_of_wc[count]))

        
doc.close()
