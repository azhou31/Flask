#PART ONE
# def function draw_stars()
# x=[4,6,1,3,5,7,25]
# for i in range(0, len(x)):
#     print "1" * x[i]

#PART TWO
# def function draw_stars()
x=[4, "Tom", 1, "Michael", 5,7,"Jimmy Smith"]
for i in range(0, len(x)):
    if type(x[i][0]) == str:
        print "x[i].lower()" * x[i][0]
    else:
        print "*" * x[i]