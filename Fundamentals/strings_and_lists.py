#FIND AND REPLACE
words ="It's thanksgiving day. It's my birthday, too!"
print words.find("day")
print words.replace("day", "month")

#MIN AND MAX
values = [4,5,69]
print (min(values))
print (max(values))

#FIRST AND LAST
x = ["hello",4,5,6,3,"world"]
print x[len(x)-1]
print x[0]

#NEW LIST
x=[19,54,6,7,3,98]
x.sort()
print x
first_list = x[:len(x)/2]
second_list = x[len(x)/2:]
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
