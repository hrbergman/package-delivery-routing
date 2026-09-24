# *********************
# Name: Hannah Bergman
# ID: 001539744
# *********************

from HashTable import HashTable
from Vertex import Vertex
from WeightedEdge import WeightedEdge

# *********************************************************************************************************************
# Referenced Webinar 2, "Getting Greedy, who moved my data?" by Course Instructor, Dr. Cemel Tepe, to create this graph
# Full citation is included in attached report
# *********************************************************************************************************************

# Space complexity: O(n^2)
class Graph(object):
    def __init__(self):
        self.vertices = HashTable(20)

    # Find vertex that matches the following location
    # Time complexity: O(n)
    def find_vertex(self, location):
        return self.vertices.look_up(location.identifier)

    # Add a 2D weighted edge between 2 vertices
    # Time complexity: O(n)
    def add_weighted_edge(self, origin, destination, weight):
        self.vertices.look_up(origin.identifier).add_edge(WeightedEdge(destination, weight))
        self.vertices.look_up(destination.identifier).add_edge(WeightedEdge(origin, weight))

    # Add a vertex by location and add it to the hash table
    # Time complexity: O(n)
    def add_vertex(self, location):
        self.vertices.insert(location.identifier, Vertex(location))

    # Measure the distance between current location and location of the package requiring delivery
    def distance_to_deliver(self, location):
        def distance_to(package):
            return self.vertices.look_up(location.identifier).distance_to_nearby(package.destination)

        return distance_to

    # Find the distance between vertices
    # Time complexity: O(n)
    def find_distance_between(self, origin, target):
        return self.vertices.look_up(origin.identifier).distance_to_nearby(target)

    # Find the next closest location for the truck to travel to
    def distance_from(self, origin):
        def distance_to(destination):
            return self.vertices.look_up(origin.identifier).distance_to_nearby(destination)

        return distance_to
