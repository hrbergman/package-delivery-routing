# *********************
# Name: Hannah Bergman
# ID: 001539744
# *********************

# The Location class used in graph
# Defines variables for location, name, & delivery address
class Location(object):
    def __init__(self, identifier, name, address):
        self.identifier = int(identifier)
        self.name = name
        self.address = address