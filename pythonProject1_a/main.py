#Name: Josh Brown
#Student ID: 001114722
from package import hash_table
from truck import t1_first_miles
from truck import t2_first_miles
from truck import t1_second_miles

#Totals up all miles from truck1 (both trips) and truck2
total_miles = t1_first_miles + t2_first_miles + t1_second_miles
start = True

while start:
    print('')
    print('All packages were delivered in ', round(total_miles, 2), ' miles.')
    print('')
    print('')
    print('Would you like to: ')
    print('')
    print('a) Search for a package')
    print('b) Update package information')
    print('c) Display all packages')
    print('')
    print('x) Exit')
    print('')
    print('Please answer with "a", "b", or "c", or "x"')
    print('')
    a = input('>>>_')

    if a == 'a':
        print('Do you want to: ')
        print('')
        print('a) Search by ID')
        print('b) Search by TIME')
        print('')
        print('g) Go back')
        print('')
        print('"a", "b", or "g"')
        print('')
        search = input('>>>_')
        if search == 'a':
            print('Enter an ID number: ')
            print('')
            search_id = int(input('>>>_'))
            print('')

            if search_id in range(1, 40):
                print_out = hash_table.get(search_id)

                x_num = ''
                if print_out[7] == '09:05:00':
                    x_num = '2'
                else:
                    x_num = '1'

                print('')
                print('Showing info on package ' + str(search_id) + ':')
                print('')
                print(f"{'ID' : <10}{'Address' : <42}{'Truck #' : <20}{'Deadline' : <15}{'Status' : <15}{'Shipped' : <26}{'Delivered'}")
                print(
                    f"{print_out[0] : <10}{print_out[1] : <42}{x_num : <20}{print_out[4] : <15}{print_out[6] : <15}{'Shipped '}{print_out[7] : <18}{'Delivered '}{print_out[8]}")

        elif search == 'b':
            print('Enter a time (HH:MM:SS)')
            print('')
            search_time = input('>>>_')
            print('')

            from truck import conv_str_to_time
            print(f"{'ID' : <10}{'Address' : <40}{'Truck #' : <20}{'Deadline' : <15}{'Status' : <15}")
            print('')
            #Determines truck number based on what time truck left hub
            #space-time complexity O(N)
            for i in range(1, 41):
                element = hash_table.get(i)
                truck_num = ''
                if element[7] == '09:05:00':
                    truck_num = '2'
                else:
                    truck_num = '1'

                #Checks if element is package 9.
                #space-time complexity O(1)
                if element[0] == 9:
                    #If true, checks if time is after 10:20 am.
                    if conv_str_to_time(search_time) >= conv_str_to_time('10:20:00'):
                        #If true, updates package 9 address with correct information.
                        err_data = hash_table.get(i)
                        correct_address = '410 S State St'
                        err_data[1] = correct_address

                        hash_table.update(i, err_data)
                    #If false, leaves package 9 address the same.
                    else:
                        err_data = hash_table.get(i)
                        correct_address = '300 State St'
                        err_data[1] = correct_address

                        hash_table.update(i, err_data)

                if conv_str_to_time(search_time) < conv_str_to_time(element[7]):
                    print(f"{element[0] : <10}{element[1] : <40}{truck_num : <20}{element[4] : <15}{'At Hub' : <15}")
                elif conv_str_to_time(search_time) >= conv_str_to_time(element[7]) and conv_str_to_time(search_time) < conv_str_to_time(element[8]):
                    print(f"{element[0] : <10}{element[1] : <40}{truck_num : <20}{element[4] : <15}{'En Route' : <15}")
                elif conv_str_to_time(search_time) >= conv_str_to_time(element[8]):
                    print(f"{element[0] : <10}{element[1] : <40}{truck_num : <20}{element[4] : <15}{'Delivered At ' : <15}{element[8]}")
                else:
                    print('Something must have gone wrong')
                    start = True
        elif search == 'g':
            start = True

    elif a == 'b':
        print('Enter ID of package you want to update: ')
        print('')
        package_num = input('>>>_')
        print('')
        old_data = hash_table.get(package_num)

        print('Which would you like to change?')
        print('')
        print('1: Destination Address')
        print('2: Destination City')
        print('3: Destination Zip Code')
        print('4: Delivery Deadline')
        print('5: Package Weight')
        print('')
        print('g: Go back')
        print('')
        print('Enter an option')
        print('')
        option = int(input('>>>_'))
        print('')

        if option == 1:
            print('Enter the new city, or "x" to cancel')
            print('')
            new_data = input(str('>>>_'))
            print('')
            if new_data == 'x':
                print('Action Canceled')
                check = hash_table.get(package_num)
                print(check)
            else:
                old_data[1] = new_data
                hash_table.update(package_num, old_data)

                check = hash_table.get(package_num)
                print(check)
        elif option == 2:
            print('Enter the new city, or "x" to cancel')
            print('')
            new_data = input(str('>>>_'))
            print('')
            if new_data == 'x':
                print('Action Canceled')
                check = hash_table.get(package_num)
                print(check)
            else:
                old_data[2] = new_data
                hash_table.update(package_num, old_data)

                check = hash_table.get(package_num)
                print(check)
        elif option == 3:
            print('Enter the new city, or "x" to cancel')
            print('')
            new_data = input(str('>>>_'))
            print('')
            if new_data == 'x':
                print('Action Canceled')
                check = hash_table.get(package_num)
                print(check)
            else:
                old_data[3] = new_data
                hash_table.update(package_num, old_data)

                check = hash_table.get(package_num)
                print(check)
        elif option == 4:
            print('Enter the new city, or "x" to cancel')
            print('')
            new_data = input(str('>>>_'))
            print('')
            if new_data == 'x':
                print('Action Canceled')
                check = hash_table.get(package_num)
                print(check)
            else:
                old_data[4] = new_data
                hash_table.update(package_num, old_data)

                check = hash_table.get(package_num)
                print(check)
        elif option == 5:
            print('Enter the new city, or "x" to cancel')
            print('')
            new_data = input(str('>>>_'))
            print('')
            if new_data == 'x':
                print('Action Canceled')
                check = hash_table.get(package_num)
                print(check)
            else:
                old_data[5] = new_data
                hash_table.update(package_num, old_data)

                check = hash_table.get(package_num)
                print(check)
        elif option == 'g':
            start = True

        else:
            print("I'm sorry, that's not a valid option.")
            start = True
    elif a == 'c':
        print('Showing all packages: ')
        print('')
        print(f"{'ID' : <10}{'Address' : <40}{'Truck #' : <20}{'Deadline' : <15}{'Status' : <15}{'Shipped' : <26}{'Delivered':}")
        print('')
        for i in range(1, 41):
            element = hash_table.get(i)
            t_num = ''
            if element[7] == '09:05:00':
                t_num = '2'
            else:
                t_num = '1'
            print(f"{element[0] : <10}{element[1] : <40}{t_num : <20}{element[4] : <15}{element[6] : <15}{'Shipped '}{element[7] : <18}{'Delivered '}{element[8]}")
    elif a == 'x':
        exit()
    else:
        print("Input must be 'a', 'b', 'c', or 'x'")

    print('')
    print('Would you like to continue?')
    print('')
    print('y/n')
    print('')
    answer = input('>>>_')
    print('')

    if answer == 'y':
        start = True
    elif answer == 'n':
        start = False
        exit()
