"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Create an empty queue
        to_visit = Queue()

        # Create an empty set to track visited vertices
        visited = set()

        # Enqueue the starting vertex
        to_visit.enqueue(starting_vertex)

        # While the queue is not empty
        while to_visit.size() > 0:

            # Get the current vertex (dequeue)
            current = to_visit.dequeue()

            # If the current vertex has not been visited
            if current not in visited:
                #Print the current vertex
                print(current)
                #Add the current vertex to the list containing the vertexes that we visited
                visited.add(current)
                #Add the neighbors of the current vertex to the queue to be visited
                for vertex in self.get_neighbors(current):
                    to_visit.enqueue(vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Create an empty stack
        to_visit = Stack()
        # Create an empty set to track visited vertices
        visited = set()

        to_visit.push(starting_vertex)

        while to_visit.size() > 0:

            current = to_visit.pop()

            if current not in visited:
                print(current)
                visited.add(current)

                for vertex in self.get_neighbors(current):
                    to_visit.push(vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # Print the current vertex, in this case the starting vertex on initialization
        print(starting_vertex)

        # On initialization, make an empty set to keep track of what we've visited
        if visited is None:
            visited = set()

        # Add the current vertex to the visited set
        visited.add(starting_vertex)

        # Get the neighbors of the current vertex
        for next_vert in self.get_neighbors(starting_vertex):
            # If the neighboring vertex has not been visited
            if next_vert not in visited:
                # We call the current function recursively with the neighboring vertex as the current one and with an updated visited set
                self.dft_recursive(starting_vertex=next_vert, visited=visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        to_visit = Queue()
        visited = set()

        # Make a list for the final path to the destination vertex
        to_visit.enqueue([starting_vertex])

        while to_visit.size() > 0:

            # Create a current path from the first vertex in the queue
            path = to_visit.dequeue()

            # Set the last node in the currentPath to a variable
            last_vertex = path[-1]

            # If the vertex have not been visited
            if last_vertex not in visited:

                # Add the vertex to the visited set
                visited.add(last_vertex)

                # If the vertex is the destination
                if last_vertex == destination_vertex:
                    # We can return the path to it
                    return path
                # If not, get the neighbors and add the to the queue to be visited
                else:
                    for vertex in self.get_neighbors(last_vertex):
                        to_visit.enqueue(path + [vertex])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        to_visit = Stack()
        visited = set()

        to_visit.push([starting_vertex])

        while to_visit.size() > 0:

            path = to_visit.pop()

            last_vertex = path[-1]

            if last_vertex not in visited:

                visited.add(last_vertex)

                if last_vertex == destination_vertex:
                    return path
                else:
                    for vertex in self.get_neighbors(last_vertex):
                        to_visit.push(path + [vertex])

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # Initializing, create a set containing visited vertices
        if visited is None:
            visited = set()

        # Create a list for the path to the destination vertex
        if path is None:
            path = []

        # If the current vertex has not been visited
        if starting_vertex not in visited:

            # Add the vertex to the path to the destination
            path = path + [starting_vertex]

            # Mark that we've visited the current vertex
            visited.add(starting_vertex)

            # If the current vertex is the destination, return the current path to it
            if starting_vertex == destination_vertex:
                return path

            # If not, we want to get the neighboring vertexes
            else:
                for vertex in self.get_neighbors(starting_vertex):
                    # Set the next path to contain the neighboring vertex and updated visited and path list
                    next_path = self.dfs_recursive(vertex, destination_vertex, visited, path)
                    if next_path:
                        return next_path

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
