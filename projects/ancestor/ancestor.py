# graph represents parents -> children over multiple generations
# data formatted as list of (parent, child) pairs
# each infividual given unique integer identifier

#  10                       oldest: gen1
#  /
# 1   2   4  11             gen2
#  \ /   / \ /
#   3   5   8               gen3
#    \ / \   \
#     6   7   9             youngest: gen4


# return earliest known ancestor - the one at the farthest distance from the input individual
# if 2 inidividuals are return as earliest ancestor, return the one with the lower numeric value
# if input individual has no parent, return -1


# input not empty
# no cycles in input
# no repeated ancestors
# ids always positive
# parents may have any number of children


def earliest_ancestor(ancestors, starting_node):
    queue = []
    queue.append(starting_node)
    visited = set()
    while len(queue) > 0:
        current = queue.pop()
        visited.add(current)
        for ancestor in ancestors:
            if ancestor[1] == current:
                queue.append(ancestor[0])
    if current == starting_node:
        return -1
    else:
        return current

# plan
# BFT/BFS?
# exception = if no ancestors return -1
# make queue
# initiate by putting start in queue
# check if we've seen that person before
# make visit variable
# while we have ppl in queue
# current pop off queue
# for ancestor pair in ancestors
# if there is another ancestor
# add that ancestor to the queue
# repeat
