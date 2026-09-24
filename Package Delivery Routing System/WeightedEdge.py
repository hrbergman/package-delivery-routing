# *********************
# Name: Hannah Bergman
# ID: 001539744
# *********************

# ********************************************************************************************************
# Referenced Webinar 1, "Let's Go Hashing" by Course Instructor, Dr. Cemel Tepe, to create this hash table
# Full citation is included in attached report
# ********************************************************************************************************

# The Edge class used in graph
# Defines variables for location, identifier, & weight
class WeightedEdge(object):
    def __init__(self, location, weight=0.0):
        self.identifier = location.identifier
        self.location = location
        self.weight = weight
