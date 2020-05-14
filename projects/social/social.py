import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        # Creates a bi-directional friendship
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        # Create a new user with a sequential integer ID
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        # Takes a number of users and an average number of friendships as arguments
        # Creates that number of users and a randomly distributed friendships between those users.
        # The number of users must be greater than the average number of friendships. Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(0, num_users):
            self.add_user(f"User: {i+1}")  # i?
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        # Takes a user's user_id as an argument
        # Returns a dictionary containing every user in that user's
        # extended network with the shortest friendship path between them.
        # The key is the friend's ID and the value is the path.
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()
        queue.enqueue([user_id])
        while queue.size() > 0:
            path = queue.dequeue()
            current = path[-1]
            if current not in visited:
                visited[current] = path
                for friend in self.friendships[current]:
                    new_path = list(path)
                    new_path.append(friend)
                    queue.enqueue(new_path)

        return visited


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop()
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add[v2]
        else:
            return "Error: could not find vertex"

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("Friendships", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("Connections", connections)
