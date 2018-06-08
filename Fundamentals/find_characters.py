def function findCharacters(vowels)
word_list = ["hello", "world", "my", "name","is","Anna"]
char ='o'
new_list = [ ]
for i in range(0,len(word_list)):
    if word_list[i] == char:
        new_list.append(word_list[i])
        print (new_list)

def function findCharacters(word_list, char)
word_list = ["hello", "world", "my", "name","is","Anna"]
new_list = [ ]
for i in range(0,len(word_list)):
    if word_list.find(char) != -1:
        new_list.append(word_list[i])
        print (new_list)