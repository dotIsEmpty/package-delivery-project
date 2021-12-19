import csv
from package import get_package_address
import truck

#Reads in data from full_loc_distance_table.csv
#then converts data to float values
#space-time complexity O(N^2)
with open('full_loc_distance_table.csv') as csvfile:
    miles_table = []
    for line in csvfile.readlines():
        miles_table.append(line.split('\n')[0].split(','))
    floatDistanceTable = []
    for i in miles_table:
        floatDistanceTable.append([float(j) for j in i])

    #loc_distCSV = csv.reader(csvfile, delimiter=',')
    #loc_distCSV = list(loc_distCSV)

#Reads data from location_names_copy.csv into list names_CSV
#space-time complexity O(N)
with open('location_names_copy.csv') as csv_names:
    names_CSV = csv.reader(csv_names, delimiter=',')
    names_CSV = list(names_CSV)

#Uses index inputs to find distance between two locations from full_loc_distance_table.csv file
#space-time complexity O(N)
def distance(rw,cl):
    di = 0.0
    for row in floatDistanceTable:
        if row[0] == cl:
            rw = rw + 1
            di = row[rw]
            break

    return float(di)

#Takes in an address string, returns its index from location_names_copy.csv
#This index value is used to find the distance between two location indices
#space-time complexity O(N)
def get_loc_index(loc):
    loc_index = 0
    # On each iteration, checks to see if list[2] (the address string) is the same as the address string input.
    for list in names_CSV:
        #If true, loc_index is set to the index of that item in names_CSV list, used later to retrieve distance
        #between two location inputs.
        if list[2] == loc:
            loc_index = int(list[0])
            break

    return loc_index

#takes input of distance to calculate travel time.
#converts from hours to minutes
#space-time complexity O(1)
def get_travel_time(miles):
    mph = 18
    t = miles/mph
    return t*60

#Takes in a trucks package list as input, creates a new list, and sorts packages into the new list
#to create a delivery route using a "greedy" Nearest Neighbor algorithm to find the closest location to each current location.
#space-time complexity O(N^2)
def find_shortest_dist(package_list):
    #Current starts at the hub
    current1 = '4001 South 700 East'

    #Checks if package list is for first trip of truck1.
    if package_list == truck.truck1_first:
        #Creates a copy of package list that can be manipulated without affecting the original list
        temp_list = truck.truck1_first
        #Creates list that will become a sorted "delivery route"
        sorted_list1 = []
        #Starting shortest distance initialized to a number that will be easy to beat
        shortest1 = 25.0
        shortest_found = False
        #Will hold the package id of each current closest package as For Loop searches for the closest.
        p1 = 0

        #space-time complexity O(N)
        while shortest_found == False:
            #After completing the For Loop, the closest address is found.
            #Package id with the closest address is added to the route, and then removed from the package list.
            #Current location is updated to the address of the package, allowing the next closest to be found from
            #this new location.
            #For loop then re-runs on the package list - 1, finding the next closest, etc.
            #This continues until the route (sorted_list) contains all packages on the truck, sorted in order according
            #to the nearest neighbor algorithm.
            #space-time complexity O(N)
            for i in range(0,len(temp_list)-1):
                indx_curr = get_loc_index(current1)
                indx_nxt = get_loc_index(get_package_address(temp_list[i+1]))
                indx_i = get_loc_index(get_package_address(temp_list[i]))

                #Checks whether i + 1 is closer to current location than i.
                if distance(indx_curr,indx_nxt) < distance(indx_curr,indx_i):
                    #Checks whether distance between i + 1 and current location is shorter than the current
                    #shortest distance (shortest1).
                    if distance(indx_curr,indx_nxt) < shortest1:
                        #If both are true, updates shortest1 to new shorter distance and sets variable p1
                        #to be the package id of item i + 1 in the list.
                        shortest1 = distance(indx_curr,indx_nxt)
                        p1 = temp_list[i+1]
                #Checks whether i is closer to current location than i + 1.
                elif distance(indx_curr,indx_nxt) > distance(indx_curr,indx_i):
                    # Checks whether distance between i and current location is shorter than the current
                    # shortest distance (shortest1).
                    if distance(indx_curr,indx_i) < shortest1:
                        # If both are true, updates shortest1 to new shorter distance and sets variable p1
                        # to be the package id of item i in the list.
                        shortest1 = distance(indx_curr,indx_i)
                        p1 = temp_list[i]
                #Else if both i and i + 1 are of equal distance, i + 1 is selected.
                else:
                    # Checks whether distance between i + 1 and current location is shorter than the current
                    # shortest distance (shortest1).
                    if distance(indx_curr, indx_nxt) < shortest1:
                        #If true, updates shortest1 to new shorter distance and sets variable p1
                        # to be the package id of item i + 1 in the list.
                        shortest1 = distance(indx_curr, indx_nxt)
                        p1 = temp_list[i + 1]

            #After For Loop iterates through all packages in the truck, variable p1 will contain the id of the package
            #with a delivery address that is closest to the current location.

            #Package id with closest address is appended to sorted route list.
            sorted_list1.append(p1)
            #Current location is updated to p1 address as package is "delivered".
            current1 = get_package_address(p1)
            del_index = temp_list.index(p1)
            #"Delivered" package is removed from package list copy to avoid being selected again.
            temp_list.pop(del_index)

            #Checks to see if full sorted route - 1 has been determined
            if len(sorted_list1) == 15:
                #If true, while loop is broken.
                shortest_found = True
                #Last remaining package is appended to the route.
                sorted_list1.append(temp_list[0])
                #Final package is removed from package list copy
                temp_list.pop(0)
                #Returns list of packages in a sorted "route".
                return sorted_list1
            #If package list is not yet fully built
            else:
                #Shortest distance is reset
                shortest1 = 25.0
                #p1 variable is reset
                p1 = 0
                #Loop is re-run on all remaining packages to determine the next closest delivery
                #address from the new current location after delivering the last package.
                shortest_found = False

    #Same as truck1_first, but for truck2 package list
    elif package_list == truck.truck2_first:
        temp_list2 = truck.truck2_first
        sorted_list2 = []
        shortest2 = 25.0
        shortest_found = False

        while shortest_found == False:
            for i in range(0,len(temp_list2)-1):
                indx_curr = get_loc_index(current1)
                indx_nxt = get_loc_index(get_package_address(temp_list2[i + 1]))
                indx_i = get_loc_index(get_package_address(temp_list2[i]))

                if distance(indx_curr,indx_nxt) < distance(indx_curr,indx_i):
                    if distance(indx_curr,indx_nxt) < shortest2:
                        shortest2 = distance(indx_curr, indx_nxt)
                        p2 = temp_list2[i + 1]
                elif distance(indx_curr,indx_nxt) > distance(indx_curr,indx_i):
                    if distance(indx_curr,indx_i) < shortest2:
                        shortest2 = distance(indx_curr,indx_i)
                        p2 = temp_list2[i]
                else:
                    if distance(indx_curr, indx_nxt) < shortest2:
                        shortest2 = distance(indx_curr, indx_nxt)
                        p2 = temp_list2[i + 1]

            sorted_list2.append(p2)
            current1 = get_package_address(p2)
            del_index = temp_list2.index(p2)
            temp_list2.pop(del_index)

            if len(sorted_list2) == 15:
                shortest_found = True
                sorted_list2.append(temp_list2[0])
                temp_list2.pop(0)
                return sorted_list2
            else:
                shortest2 = 25.0
                p2 = 0
                shortest_found = False

    #Same as other two routes, except truck1 second trip contains fewer packages (8 instead of 16)
    elif package_list == truck.truck1_second:
        temp_list3 = truck.truck1_second
        sorted_list3 = []
        shortest3 = 25.0
        shortest_found = False

        while shortest_found == False:
            for i in range(0, len(temp_list3) - 1):
                indx_curr = get_loc_index(current1)
                indx_nxt = get_loc_index(get_package_address(temp_list3[i + 1]))
                indx_i = get_loc_index(get_package_address(temp_list3[i]))

                if distance(indx_curr, indx_nxt) < distance(indx_curr, indx_i):
                    if distance(indx_curr, indx_nxt) < shortest3:
                        shortest3 = distance(indx_curr, indx_nxt)
                        p3 = temp_list3[i + 1]
                elif distance(indx_curr, indx_nxt) > distance(indx_curr, indx_i):
                    if distance(indx_curr, indx_i) < shortest3:
                        shortest3 = distance(indx_curr, indx_i)
                        p3 = temp_list3[i]
                else:
                    if distance(indx_curr, indx_nxt) < shortest3:
                        shortest3 = distance(indx_curr, indx_nxt)
                        p3 = temp_list3[i + 1]
            sorted_list3.append(p3)
            current1 = get_package_address(p3)
            del_index = temp_list3.index(p3)
            temp_list3.pop(del_index)

            if len(sorted_list3) == 7:
                shortest_found = True
                sorted_list3.append(temp_list3[0])
                temp_list3.pop(0)
                return sorted_list3
            else:
                shortest3 = 25.0
                p3 = 0
                shortest_found = False