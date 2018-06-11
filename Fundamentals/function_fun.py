#Fun with Functions Assignment

#ODD/EVEN
def function odd_even(1,2000)
for i in range(1,2000):
    if i % 2 == 1:
        print "Number is ", str(i), ". This is an odd number."
    else:
        print "Number is ", str(i), ". This is an even number."

#MULTIPLY
def function multiply(arr,num)
a=[2,4,10,16]
b=multiply(a,5)
    print b
for x in range(len(arr)):
    arr[x]*=num
return arr
# a=[2,4,10,16]
# b=multiply(a,5)
# print b

# #HACKER CHALLENGE
def layered_multiples([2,4,5],3):
new_array = []
for i in arr:
    val_arr=[]
    for x in range(0,i)
        val_arr.append(1)
    new_array.append(val_arr)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x 

# def layered_multiples(arr):
#     print arr
#     new_array = []
#     for x in arr:
#         val_arr = []
#         for i in range(0,x):
#             val_arr.append(1)
#         new_array.append(val_arr)
#     return new_array

# x = layered_multiples(multiply([2,4,5],3))
# print x