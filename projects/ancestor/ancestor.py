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


def earliest_ancestor_v2(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
    queue = []
    queue.append([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while len(queue) > 0:
        path = queue.pop()
        current = path[-1]
        if (len(path) >= max_path_len and current < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = current
            max_path_len = len(path)
        for neighbor in graph.vertices[current]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return earliest_ancestor


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Error: vertex not found")

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
