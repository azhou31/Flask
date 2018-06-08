#def function list_type(asfcc):
words =["magical unicorns",19,"hello",98.98,"world"]
newS = " "
sum = 0
sum_str = 0
sum_ind = 0
for value in words(0,len(words)):
    word_item = type(words[i])
    if word_item is str:
        newS = newS + words[i] + " "
        sum_str = sum_str + i
    elif word_item is float:
        sum = sum + words[i]
        sum_index = sum_ind + i
if sum_str == len(words):
    print "You have a string list"
else sum_ind == len(words):
    print "The list you have is of integer type"
else:
    print "You entered a mixed type"