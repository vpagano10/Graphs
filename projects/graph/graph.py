from util import Stack, Queue


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

    def bft(self, starting_vertex):
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size() > 0:
            current = queue.dequeue()
            print(current)
            visited.add(current)
            for next_vert in self.get_neighbors(current):
                if next_vert not in visited:
                    queue.enqueue(next_vert)
                    visited.add(next_vert)

    def dft(self, starting_vertex):
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            current = stack.pop()
            print(current)
            visited.add(current)
            for next_vert in self.get_neighbors(current):
                if next_vert not in visited:
                    stack.push(next_vert)
                    visited.add(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)
                # base case here is: if a node has no unvisited neighbors, do nothing

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            current = queue.dequeue()
            if current[-1] == destination_vertex:
                return current
            else:
                for next_vert in self.get_neighbors(current[-1]):
                    new_current = list(current)
                    new_current.append(next_vert)
                    queue.enqueue(new_current)
                    # queue.enqueue(current + [next_vert])
        return "Destination Vertex not found"

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            current = stack.pop()
            if current[-1] == destination_vertex:
                return current
            else:
                for next_vert in self.get_neighbors(current[-1]):
                    new_current = list(current)
                    new_current.append(next_vert)
                    stack.push(new_current)
                    # stack.push(current + [next_vert])
        return "Destination Vertex not found"

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        new_path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return new_path
        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                next_vert_path = self.dfs_recursive(
                    next_vert, destination_vertex, visited, new_path)
                if next_vert_path:
                    return next_vert_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
