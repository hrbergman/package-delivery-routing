# *********************
# Name: Hannah Bergman
# ID: 001539744
# *********************

# ********************************************************************************************************
# Referenced Webinar 1, "Let's Go Hashing" by Course Instructor, Dr. Cemel Tepe, to create this hash table
# Full citation is included in attached report
# ********************************************************************************************************

from HashTable import HashTable

class Vertex(object):
    def __init__(self, location):
        self.edges = HashTable()
        self.value = location

    # Add edge to the Hash Table
    # Time & space complexity are both linear: O(n)
    def add_edge(self, edge):
        self.edges.insert(edge.identifier, edge)

    # Find the distance to nearby vertex
    # Time & space complexity are both linear: O(n)
    def distance_to_nearby(self, location):
        return self.edges.look_up(location.identifier).weight

    # Find edge from the edge ID
    # Time & space complexity are both linear: O(n)
    def find_edge(self, edge_id):
        return self.edges.look_up(edge_id)
