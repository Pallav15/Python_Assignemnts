# Name - Pallav Singla
# Roll No - 2020225

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


# Write the code here for creating an interactive program.

import a2

print("*="*24)
print("|" + "!!! WELCOME !!!".center(46) + "|")
print("*="*24)
print("| CODE   |           QUERY                     |")
print("*="*24)

print("""| 1.     |   read_data_from_file               |
| 2.     |   filter_by_first_name              |
| 3.     |   filter_by_last_name               |
| 4.     |   filter_by_full_name               |
| 5.     |   filter_by_age_range               |
| 6.     |   count_by_gender                   |
| 7.     |   filter_by_address                 |
| 8.     |   find_alumni                       |
| 9.     |   find_topper_of_each_institute     |
| 10.    |   find_blood_donors                 |
| 11.    |   get_common_friends                |  
| 12.    |   is_related                        |
| 13.    |   delete_by_id                      |
| 14.    |   add_friend                        |
| 15.    |   remove_friend                     |
| 16.    |   add_education                     |""")
print("*="*24)

records = a2.read_data_from_file()

while True:
    code = int(input("Which query would you like to perform? "))
    if code == -1:
        break
    elif code == 1:
        print(a2.read_data_from_file())

    elif code == 2:
        first_name = input("Enter first_name ").casefold()
        print(a2.filter_by_first_name(records,first_name))

    elif code == 3:
        last_name = input("Enter last_name ").casefold()
        print(a2.filter_by_last_name(records, last_name))

    elif code == 4:
        full_name = input("Enter full_name: ").casefold()
        print(a2.filter_by_full_name(records, full_name))

    elif code == 5:
        min_age = int(input("Enter minimum age: "))
        max_age = int(input("Enter maximum age: "))
        print(a2.filter_by_age_range(records, min_age, max_age))

    elif code == 6:
        print(a2.count_by_gender(records))

    elif code == 7:
        address = {}
        house_no = input("Enter House number: ")
        block = input("Enter Block: ")
        town = input("Enter Town: ")
        city = input("Enter City: ")
        pincode = input("Enter Pincode: ")
        state = input("Enter state: ")

        if house_no != '':
            address['house_no']=int(house_no)
        if block != '':
            address['block']=block
        if town!='':
            address['town']=town
        if city!='':
            address['city']=city
        if pincode!='':
            address['pincode']=int(pincode)
        if state!='':
            address['state']=state
        elif len(address)==0:
            address = {}
        print(a2.filter_by_address(records,address))

    elif code == 8:
        institute_name = input("Enter institute: ")
        print(a2.find_alumni(records, institute_name))

    elif code == 9:
        print(a2.find_topper_of_each_institute(records))

    elif code == 10:
        receiver_person_id = int(input("Enter receiver person id: "))
        print(a2.find_blood_donors(records, receiver_person_id))

    elif code == 11:
        list_of_ids = list(map(int,input("Enter ids for finding common friends: ").split()))
        print(a2.get_common_friends(records, list_of_ids))

    elif code == 12:
        person_id_1 = int(input("Enter person id 1: "))
        person_id_2 = int(input("Enter person id 2: "))
        print(a2.is_related(records, person_id_1, person_id_2))

    elif code == 13:
        person_id = int(input("Enter the person id to remove"))
        print(a2.delete_by_id(records, person_id))

    elif code == 14:
        person_id = int(input("Enter person id: "))
        friend_id = int(input("Enter friend id: "))
        print(a2.add_friend(records, person_id, friend_id))

    elif code == 15:
        person_id = int(input("Enter person id: "))
        friend_id = int(input("Enter friend id: "))
        print(a2.remove_friend(records, person_id, friend_id))

    elif code == 16:
        person_id = int(input("Enter person id: "))
        institute_name = input("Enter institute name: ")
        ongoing = input("Enter status of studying (True or False): ")
        if ongoing == "False":
            percentage = float(input("Enter percentage: "))
            print(a2.add_education(records, person_id, institute_name, ongoing, percentage))
        else:
            print(a2.add_education(records, person_id, institute_name, ongoing, None))




