# *********************
# Name: Hannah Bergman
# ID: 001539744
# *********************

from datetime import timedelta
from DeliverySystem import PackageDelivery


print("***********************************")
print("WGUPS PACKAGE DELIVERY - MAIN MENU")
print("***********************************")

(total_distance, packages_hash, packages) = PackageDelivery.run()

print("Delivery Status: \n All WGUPS packages have been delivered on time")
print('Mileage Information: \n Packages were delivered in {} miles'.format(total_distance))
print("------------------------------------------------")

while True:

    # Display special packages without repetition
    def package_look_up_for_interface(package_id):
        package = packages_hash.look_up(int(package_id))
        package_time = "12:00:00"
        (hour, minute, sec) = package_time.split(':')
        timestamp = timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))
        print(package.specific_package_lookup(timestamp))

# Navigation directory actions
    print()
    user_input = input("""\
NAVIGATION DIRECTORY: 
   1 - Retrieve information using the Package ID and a specified time
   2 - Check the current status of all packages at a particular time indicated as HH:MM:SS
   3 - Show cumulative distance covered by all trucks
   4 - Show all special packages by category
   exit - Exit the application

INPUT ONE OF THE NUMBERS ABOVE OR TYPE "exit" TO EXIT THE APPLICATION: """)

    if user_input == "1":
        package_id = input("Enter the Package ID of the package you want to retrieve: ")

        # Get package ID from hash table
        # Time complexity is linear: O(n)
        package = packages_hash.look_up(int(package_id))

        package_time = input("Enter a time as HH:MM:SS : ")

        (hour, minute, sec) = package_time.split(':')
        timestamp = timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))

        print(package.specific_package_lookup(timestamp))

    elif user_input == "2":
        package_time = input("Enter a time as HH:MM:SS : ")
        (hour, minute, sec) = package_time.split(":")
        timestamp = timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))

        # Create a loop to go through packages and show their current delivery status
        for package in packages:
            print(package.inline_report(timestamp))

    elif user_input == "3":
        print("\nTOTAL DISTANCE TRAVELED BY ALL TRUCKS: {} miles".format(total_distance))

    elif user_input == "4":
        print("\n --- DISPLAYING ALL SPECIAL PACKAGES ---\n")

        print("---------------------------------------------------------------------------------------")
        print("DEADLINE DELIVERIES - The following packages have a 10:30 deadline, without other special notes:")

        package_look_up_for_interface(1)
        package_look_up_for_interface(29)
        package_look_up_for_interface(30)
        package_look_up_for_interface(31)
        package_look_up_for_interface(34)
        package_look_up_for_interface(37)
        package_look_up_for_interface(40)

        print("\n---------------------------------------------------------------------------------------")
        print("SIMULTANEOUS DELIVERIES - The following packages are scheduled to be delivered together: ")

        package_look_up_for_interface(13)
        package_look_up_for_interface(14)
        package_look_up_for_interface(15)
        package_look_up_for_interface(16)
        package_look_up_for_interface(19)
        package_look_up_for_interface(20)

        print("\n---------------------------------------------------------------------------------------")
        print("PACKAGE DELAYS - The following packages are experiencing a delay in delivery until 9:05: ")

        package_look_up_for_interface(3)
        package_look_up_for_interface(18)
        package_look_up_for_interface(36)
        package_look_up_for_interface(38)

        print("\n---------------------------------------------------------------------------------------")
        print("PACKAGE UPDATE - Address for package has been fixed and expected delivery is after 10:20 : ")
        package_look_up_for_interface(9)


    elif user_input == "exit":
        exit()

    else:
        print("\nThe input action you entered is invalid\nPlease select a valid action from the options listed in the navigation directory")

