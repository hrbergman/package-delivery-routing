# *********************
# Name: Hannah Bergman
# ID: 001539744
# *********************

from datetime import timedelta

class Truck(object):
    packages_on_truck = 16
    const_speed_of_truck = 18
    seconds_to_hours = 3600

    # Define variables for truck
    def __init__(self, identifier, start_time, start_location):
        self.identifier = identifier
        self.current_time = start_time
        self.start_location = start_location
        self.total_distance = 0
        self.max = self.packages_on_truck
        self.packages = []
        self.locations = set()

    # Use a helper method to find the time at the Hub
    def wait_at_hub(self, timestamp):
        self.current_time = timestamp

    # Add package to package list
    # Time Complexity is linear: O(n), where n represents the number of packages
    def add_package(self, package):
        # If the length of packages is less than the MAX_PACKAGES_PER_TRUCK, add the package to the list
        if len(self.packages) < self.max:
            self.packages.append(package)
            self.locations.add(package.destination)

            # Show that the package is on the truck and at what time
            package.on_truck = True
            package.left_hub_at = self.current_time

    # *********************************************************************************************************************
    # Referenced Webinar 2, "Getting Greedy, who moved my data?" by Course Instructor, Dr. Cemel Tepe, to create this algorithm
    # Full citation is included in attached report
    # *********************************************************************************************************************

    # This application uses a self-adjusting greedy algorithm (delivering_packages_algo).
    # The delivering_packages_algo requires a few parameters, including a city map and a boolean showing whether to return to the hub.
    # The function arranges the package list based on distance from the current location of the truck after it has traveled.
    # Following this action, the package list will be updated according to the new location, and this process will repeat until all packages have been delivered.
    # Time complexity is quadratic: O(n^2), where n represents the number of packages
    def delivering_packages_algo(self, map_of_city, return_to_hub=True):
        current_location = self.start_location
        locations = list(self.locations)

        while self.packages:
            # Sort locations based on distance to the current location
            # Use pop to remove the closest location from the list
            # Time complexity is linear: O(n)
            locations = sorted(locations, key=map_of_city.distance_from(current_location))
            nearest_location = locations.pop(0)

            distance = map_of_city.find_distance_between(current_location, nearest_location)
            time_to_deliver = self.traveling_time(distance)
            delivered_at = self.current_time + timedelta(seconds=time_to_deliver)

            # Finds all packages requiring delivery at the current location
            # Time & Space complexity is linear: O(n)
            packages_at_location = [pack for pack in self.packages if pack.destination.identifier == nearest_location.identifier]
            for package in packages_at_location:

                # Mark package as delivered
                package.delivered_at = delivered_at

                # Remove the delivered package from the list
                # Time complexity is linear: O(n)
                self.packages.remove(package)

            # Update the truck's location, time, and total distance traveled
            current_location = nearest_location
            self.total_distance += distance
            self.current_time = delivered_at

        # If the truck no longer has packages left to deliver, it must return to the Hub
        if return_to_hub:
            distance = map_of_city.find_distance_between(current_location, self.start_location)
            time_to_return = self.traveling_time(distance)

            self.current_time = self.current_time + timedelta(seconds=time_to_return)
            self.total_distance += distance

            # Reset the locations list to empty
            self.locations = set()


    # Calculate traveling time based on distance, speed, and time
    def traveling_time(self, distance):
        return (distance / self.const_speed_of_truck) * self.seconds_to_hours
