import csv
from datetime import timedelta
from Package import Package
from Location import Location
from HashTable import HashTable
from Graph import Graph
from Truck import Truck

class PackageDelivery(object):

    # Main function - executes the WGUPS package delivery system
    @staticmethod
    def run():
        graph = Graph()
        locations_hash = HashTable(20)
        packages_hash = HashTable(40)

        # Load data from the DistanceName file
        # Fill hash table and graph using location data
        with open("DistanceName.csv") as csvfile:
            distance_name = csv.reader(csvfile)

            # The time it takes the program to loop through the WGUPS location data
            # Time & space complexity: O(n)
            for row in distance_name:
                location = Location(*row)

                # Insert the location data into hash table
                # Time complexity: O(n)
                locations_hash.insert(location.identifier, location)
                locations_hash.insert(location.address, location)

                # Create vertexes on graph from location data
                # Time complexity: O(n)
                graph.add_vertex(location)

        # Package lists for each truck during trips
        all_packages = []
        truck_one_trip_one = []
        truck_two_trip_one = []
        truck_one_trip_two = []

        # Loop through the PackageInformation csv to create the above package lists, sorting by top to bottom priority
        with open("PackageInformation.csv") as csvfile:
            package_info = csv.reader(csvfile)

            for row in package_info:
                package = Package(*(row + [locations_hash.look_up(row[1])]))

                all_packages.append(package)
                packages_hash.insert(package.identifier, package)

                # Separate packages into manually loaded  (note: there is likely a better way to do this via automation)
                # Time complexity: O(1)
                if package.truck_one_trip_one():
                    truck_one_trip_one.append(package)
                if package.truck_two():
                    truck_two_trip_one.append(package)
                if package.truck_one_trip_two():
                    truck_one_trip_two.append(package)

        # Loop through DistanceTable csv
        # Filter data based on location
        # Generate weighted edges between vertexes in the graph
        with open("DistanceTable.csv") as csvfile:
            distance_table = csv.reader(csvfile)

            # Loop through each cell in the DistanceTable
            # Time & space complexity: O(n^2)
            for first_row, row in enumerate(distance_table):
                for second_row, data in enumerate(row):
                    if data != '':
                        # Add weighted edge to graph
                        # Time complexity: O(n)
                        graph.add_weighted_edge(locations_hash.look_up(first_row),
                                                locations_hash.look_up(second_row),
                                                float(data))

        start_time = timedelta(hours=8)
        start_time_truck_2 = timedelta(hours=9, minutes=5)
        start_location = locations_hash.look_up(0)

        # We'll only be using two trucks, with the first truck making two trips
        truck_list = [Truck(1, start_time, start_location), Truck(2, start_time_truck_2, start_location)]
        truck1 = Truck(1, start_time, start_location)
        truck2 = Truck(2, start_time_truck_2, start_location)
        # Creating the schedule of what times the trucks will be on standby ready to leave the hub for their deliveries
        times_to_leave_hub = [timedelta(hours=8), timedelta(hours=9, minutes=5), timedelta(hours=10, minutes=20)]

        # Filter lists by distance
        # Time & space complexity: O(n)
        truck_one_trip_one = sorted(truck_one_trip_one, key=graph.distance_to_deliver(start_location))
        truck_two_trip_one = sorted(truck_two_trip_one, key=graph.distance_to_deliver(start_location))
        truck_one_trip_two = sorted(truck_one_trip_two, key=graph.distance_to_deliver(start_location))

        # Ensure counts start at 0
        count = 0
        first_row = 0

        if first_row <= len(times_to_leave_hub):
            leave_hub_at = times_to_leave_hub[first_row]
            truck1.wait_at_hub(leave_hub_at)
        first_row += 1

        # All packages Truck 1 can fit on their 1st trip
        # Time & space complexity: O(1)
        for package in truck_one_trip_one:
            truck1.add_package(package)
            count += 1

        truck1.delivering_packages_algo(graph, (len(all_packages) - count) > truck1.max)

        # All packages Truck 2 can fit on their 1st trip
        # Time & space complexity: O(1)
        for package in truck_two_trip_one:
            truck2.add_package(package)
            count += 1

        truck2.delivering_packages_algo(graph, (len(all_packages) - count) > truck2.max)

        # All packages Truck 1 can fit on their 2nd trip
        # Time & space complexity: O(1)
        for package in truck_one_trip_two:
            truck1.add_package(package)
            count += 1

        truck1.delivering_packages_algo(graph, (len(all_packages) - count) > truck1.max)

        # Calculate the total distance traveled by both Truck 1 & Truck 2
        def total_distance(truck2):
            return truck1.total_distance + truck2.total_distance
        # Return the total distance
        return [sum(map(total_distance, truck_list)), packages_hash, all_packages]
