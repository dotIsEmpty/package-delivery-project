import csv
from hash import HashTable
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta

#Reads package data from WGUPS Package File.txt into CSV
#space-time complexity O(N)
with open('WGUPS Package File.txt') as csvfile:
    CSV = csv.reader(csvfile, delimiter=',')
    hash_table = HashTable()

    #Iterates through CSV, creating packages out of the data from each row.
    #space-time complexity O(N)
    for row in CSV:
        id = row[0]
        address = row[1]
        city = row[2]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        deliv_stat = 'At hub'
        start_time = ''
        deliv_time = ''

        #Contains the "value" in the "key/value" pair that will be inserted into the hash table
        h_value = [id,address,city,zip,deadline,weight,deliv_stat,start_time,deliv_time]
        #Uses the packages id to create a unique "key" used to find the "value" in the "key/value" pair
        key = int(id)
        value = h_value
        #Adds "key/value" pair to hash table
        hash_table.add(key,value)


    #Returns hash table
    #space-time complexity O(1)
    def get_hash_table():
        return hash_table

    #Prints entire hash table
    #space-time complexity O(N)
    def show_all():
        for i in range(1, 41):
            print(get_hash_table().get(str(i)))

    #Takes a package id number as an input and returns the corresponding address
    #space-time complexity O(1)
    def get_package_address(package_id):
        data = hash_table.get(package_id)
        addrss = data[1]

        return addrss


