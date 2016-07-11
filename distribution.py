# goal is to read in all paths from paths.txt and
# iterate over all possible boards and plot the distribution
# of the possible values.

import matplotlib.pyplot as plt
from itertools import permutations
import seaborn as sns

# flag that, if false, will bypass plotting
run_plot = True

# first lets get a list of all paths

with open("paths.txt") as f:
    paths = [l.strip() for l in f.readlines()] 

# each path is a string representing a path through the 
# square diagram:
# 
# 0 1 2
# 3 4 5
# 6 7 8

# now lets get a list of all possible boards
# 
# since there are 5 values on a board, and no value can
# repeat, there are:
# 9 x 8 x 7 x 6 x 5 = 15120 possible boards
# this function call returns a list of quintuples whose indicies
# corespond to the even tiles in the diagram above,
# i.e. board_index = tuple_index * 2

boards = list(permutations(range(1,10),5))

# first, we need a dict whose keys are the odd tile numbers
# and whose values are the operations from the board.
real_ops = {"1":lambda a,b: a + b, 
       "3":lambda a,b: a - b,
       "5":lambda a,b: a - b,
       "7":lambda a,b: a + b
       }

plus_ops = {"1":lambda a,b: a + b, 
       "3":lambda a,b: a + b,
       "5":lambda a,b: a + b,
       "7":lambda a,b: a + b
       }

minus_ops = {"1":lambda a,b: a - b, 
       "3":lambda a,b: a - b,
       "5":lambda a,b: a - b,
       "7":lambda a,b: a - b
       }

# method that, given a board and a path, returns a value
def calc(board, path,ops):
    # first, lets get a list of values from the path and board
    vals = [board[int(int(i)/2)] for i in path[::2]]
    os = [ops[i] for i in path[1::2]]

    # now we need to loop  over the values in the path and do the operations
    # between the values
    r = vals[0]
    for i,op in enumerate(os):
        r = op(r,vals[i+1])
    return r

# calculate all 3 million-ish board-path combinations
vals = [calc(b,p,minus_ops) for b in boards for p in paths]

buckets = list(range(min(vals),max(vals)+1))
counts = [len([v for v in vals if v == b]) for b in buckets]


# plot the distribution
if run_plot:
    plt.plot(buckets,counts)
    plt.show()

# some general notes for real_ops, i.e. the one corresponding to the actual board: 
# putting it into buckets and counts form, I can do analysis
# much easier.
#
# mean = 5
# median = 5
# mode = 6
# total len = 3024000 (note that this is just 15120 * 200








