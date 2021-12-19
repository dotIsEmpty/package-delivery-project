from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
from distance import get_travel_time
from distance import distance
from distance import get_loc_index
from package import get_package_address
from hash import HashTable
from package import hash_table

#Updates time counter
#Adds travel time of each individual delivery to current time.
#space-time complexity O(1)
def time_after_travel(time,trav_time):
    t = datetime.combine(date.today(),time) + timedelta(minutes=trav_time)
    new_time = t.time()
    return new_time

#Converts input time string to a time object
#space-time complexity O(1)
def conv_str_to_time(search_time):
   conv_format = '%H:%M:%S'
   time_obj = datetime.strptime(search_time, conv_format)
   return time_obj

#Truck 1 being loaded
truck1_first = []
truck1_first.append(10)
truck1_first.append(13)
truck1_first.append(14)
truck1_first.append(15)
truck1_first.append(16)
truck1_first.append(20)
truck1_first.append(21)
truck1_first.append(30)
truck1_first.append(31)
truck1_first.append(32)
truck1_first.append(37)
truck1_first.append(40)
truck1_first.append(2)
truck1_first.append(19)
truck1_first.append(5)
truck1_first.append(7)

#Truck 2 being loaded
truck2_first = []
truck2_first.append(3)
truck2_first.append(6)
truck2_first.append(23)
truck2_first.append(1)
truck2_first.append(11)
truck2_first.append(12)
truck2_first.append(17)
truck2_first.append(18)
truck2_first.append(26)
truck2_first.append(29)
truck2_first.append(22)
truck2_first.append(25)
truck2_first.append(28)
truck2_first.append(34)
truck2_first.append(36)
truck2_first.append(38)

#Truck 1, second trip being loaded
truck1_second = []
truck1_second.append(9)
truck1_second.append(8)
truck1_second.append(24)
truck1_second.append(4)
truck1_second.append(27)
truck1_second.append(33)
truck1_second.append(35)
truck1_second.append(39)

#Mile counters track total miles driven on each trip
t1_first_miles = 0.0
t2_first_miles = 0.0
t1_second_miles = 0.0


from distance import find_shortest_dist
#This creates a list called Route1 which contains all the packages in truck1_first but
#organized according to find_shortest_dist function
route1 = find_shortest_dist(truck1_first)
truck_start1 = time(8,0)
time1 = time(8,0)
#Current location starts at the hub but updates itself at each new delivery location
current_loc1 = '4001 South 700 East'
#t1_curr_indx and t1_last_indx are used later to calculate distance and time spent returning
#to the hub after delivering the last package in route1
t1_curr_indx = get_loc_index('4001 South 700 East')
t1_last_indx = get_loc_index(get_package_address(route1[15]))

#Iterates through the route, "traveling" to the location for each package and
#updating information accordingly.
#space-time complexity O(N)
for i in range(0, len(route1)):
    id = route1[i]
    address1 = get_package_address(id)
    #If the next package address is the same as the current location (i.e. multiple packages go to the same address),
    # no extra time or miles are added to the route.
    if address1 == current_loc1:
        data = hash_table.get(id)

        new_val = 'Delivered'

        data[6] = new_val
        data[7] = str(truck_start1)
        data[8] = str(time1)

        hash_table.update(id, data)
    #Else if the next package address is different from the current location,
    #distance and travel time must be recorded and current location updated to reflect traveling.
    else:

        address_indx = get_loc_index(address1)
        curr_indx = get_loc_index(current_loc1)
        dist_val1 = distance(curr_indx, address_indx)
        travel_time1 = get_travel_time(dist_val1)
        t1_first_miles = t1_first_miles + dist_val1
        temp_time1 = time_after_travel(time1, travel_time1)
        time1 = temp_time1

        current_loc1 = address1

        data = hash_table.get(id)

        new_val = 'Delivered'

        data[6] = new_val
        data[7] = str(truck_start1)
        data[8] = str(time1)

        hash_table.update(id, data)
#Distance between hub and last stop on route
return_dist = distance(t1_curr_indx,t1_last_indx)
#Time spent returning to hub after delivering last package in route
return_trav_time = get_travel_time(return_dist)
#Current time after being updated to reflect returning to hub
return_time = time_after_travel(time1,return_trav_time)
#Return to hub miles added to mile counter
t1_first_miles = t1_first_miles + return_dist
#Time at which truck 1 is reloaded and ready to begin it's second trip
trip2_start_time = return_time


#Same as route1 except does not include a return to hub
route2 = find_shortest_dist(truck2_first)
truck_start2 = time(9,5)
time2 = time(9,5)
current_loc2 = '4001 South 700 East'

for i in range(0, len(route2)):
    id = route2[i]
    address2 = get_package_address(id)
    if address2 == current_loc2:
        data = hash_table.get(id)

        new_val = 'Delivered'

        data[6] = new_val
        data[7] = str(truck_start2)
        data[8] = str(time2)

        hash_table.update(id, data)
    else:
        address_indx = get_loc_index(address2)
        curr_indx = get_loc_index(current_loc2)
        dist_val2 = distance(curr_indx, address_indx)
        travel_time2 = get_travel_time(dist_val2)
        t2_first_miles = t2_first_miles + dist_val2
        temp_time2 = time_after_travel(time2, travel_time2)
        time2 = temp_time2

        current_loc2 = address2

        data = hash_table.get(id)

        new_val = 'Delivered'

        data[6] = new_val
        data[7] = str(truck_start2)
        data[8] = str(time2)

        hash_table.update(id, data)


#same as route2 (No return trip)
route3 = find_shortest_dist(truck1_second)
#Sends package# 9 to the end of the list due to address error delay.
#This allows time for the address correction to come in before delivering package# 9
route3.append(route3.pop(route3.index(9)))
#Truck 1 second trip start time set to first trip return time
truck_start3 = trip2_start_time
time3 = trip2_start_time
current_loc3 = '4001 South 700 East'

for i in range(0, len(route3)):
    id = route3[i]
    address3 = get_package_address(id)
    if address3 == current_loc3:
        data = hash_table.get(id)

        new_val = 'Delivered'

        data[6] = new_val
        data[7] = str(truck_start3)
        data[8] = str(time3)

        hash_table.update(id, data)
    else:
        address_indx = get_loc_index(address3)
        curr_indx = get_loc_index(current_loc3)
        dist_val3 = distance(curr_indx, address_indx)
        travel_time3 = get_travel_time(dist_val3)
        t1_second_miles = t1_second_miles + dist_val3
        temp_time3 = time_after_travel(time3, travel_time3)
        time3 = temp_time3
        # If time is 10:20 or later, package# 9 address can be corrected
        if conv_str_to_time(str(time3)) >= conv_str_to_time('10:20:00'):
            err_data = hash_table.get(9)
            new_val = '410 S State St'
            err_data[1] = new_val
            hash_table.update(9, err_data)
        current_loc3 = address3

        data = hash_table.get(id)

        new_val = 'Delivered'

        data[6] = new_val
        data[7] = str(truck_start3)
        data[8] = str(time3)

        hash_table.update(id, data)