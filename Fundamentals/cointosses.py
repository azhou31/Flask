#def function coin_tosses()
#print "Starting the program..."
# win_heads=0
# win_tails=0
# for x in range(1, 5000):
#     win_tails = win_tails + 1
#     print "Attempt #", x, ": Throwing a coin... It's a head!... Got ", win_heads, " head(s) so far and ", win_tails, "tail(s) so far."


import random
def coin_toss(reps):
    attempt_count = 1
    results = [ [0,'tail'], [0, 'head'] ]
    for x in range(1, reps):
        new_toss = random.randint(0,1)
        results[new_toss][0] += 1
        print "Attempt #", attempt_count, ": Throwing a coin... It's a ", results[new_toss][1], "! Got ", results[1][0], "head(s) so far and", results[0][0], "tail(s) so far"
        attempt_count += 1
coin_toss(5000)
