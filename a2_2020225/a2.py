# Assignment - 2
# Name - Pallav Singla
# Roll No - 2020225

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters:
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''

	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	'''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

	a=[]
	for i in range(len(records)):
		if (records[i]['first_name']).casefold() == first_name.casefold():
			a.append(records[i]['id'])
		else:
			continue
	return a



def filter_by_last_name(records, last_name):
	'''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

	b=[]
	for i in range(len(records)):
		if (records[i]['last_name']).casefold() == (last_name).casefold():
			b.append(records[i]['id'])
		else:
			continue
	return b




def filter_by_full_name(records, full_name):
	'''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

	c=[]
	for i in range(len(records)):
		if (records[i]['first_name'] + " " + records[i]['last_name']).casefold() == full_name.casefold():
			c.append(records[i]['id'])
		else:
			continue
	return c



def filter_by_age_range(records, min_age, max_age):
	'''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

	d=[]
	for i in range(len(records)):
		if min_age > 0 and min_age <= max_age:
			if (min_age <= records[i]['age'] <= max_age):
				d.append(records[i]['id'])
			else:
				continue
		else:
			continue
	return d



def count_by_gender(records):
	'''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''

	m = 0
	f = 0
	for i in range(len(records)):
		if records[i]['gender'] == 'female':
			f+=1
		else:
			m+=1
	Dict = {"male": m, "female": f}

	return Dict


def filter_by_address(records, address):
	'''
	Description: Filters the person records whose address matches the given address. 

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {} 
				=> All records match this case
			
			Case 2: { "block": "AD", "city": "Delhi" } 
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''

	e = []
	e = address.keys()
	List=[]
	for i in range(len(records)):
		flag = True
		for j in e:
			if j!= 'house_no' and j!= 'pincode':
				if address[j].casefold() != records[i]['address'][j].casefold():
					flag = False
			else:
				if address[j] != records[i]['address'][j]:
					flag = False
		if flag == True:
			List.append({"first_name": records[i]['first_name'], 'last_name': records[i]['last_name']})
	return List


def find_alumni(records, institute_name):
	'''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''

	List2=[]
	for i in range(len(records)):
		for j in range(len(records[i]['education'])):
			if (records[i]['education'][j]["institute"]).casefold() == institute_name.casefold():
				if records[i]['education'][j]['ongoing'] == False:
					List2.append({'first_name':records[i]['first_name'],'last_name':records[i]['last_name'],'percentage':records[i]['education'][j]['percentage']})
				else:
					continue
			else:
				continue
	return List2



def find_topper_of_each_institute(records):
	'''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''


	Dict2 = {}
	Dict3={}
	for i in range(len(records)):
		L = {}
		for j in range(len(records[i]['education'])-1,-1,-1):
			if records[i]['education'][j]['ongoing'] == False :
				if records[i]['education'][j]['institute'] in L:
					continue
				if (records[i]['education'][j]["institute"] not in Dict2):
					L[records[i]['education'][j]["institute"]] = 1
					Dict2[records[i]['education'][j]["institute"]] = [records[i]['id'],records[i]['education'][j]['percentage']]
				elif Dict2[records[i]['education'][j]["institute"]][1] < records[i]['education'][j]['percentage']:
					Dict2[records[i]['education'][j]["institute"]] = [records[i]['id'],records[i]['education'][j]['percentage']]
					L[records[i]['education'][j]["institute"]] = 1


	for k in (Dict2):
		Dict3[k]=Dict2[k][0]

	return Dict3



def find_blood_donors(records, receiver_person_id):
	'''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note: 
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''

	List3 = {}
	if receiver_person_id < 0:
		return List3
	for i in range(len(records)):
		if records[i]['id'] != receiver_person_id:
			if records[receiver_person_id]['blood_group'] == 'A':
				if records[i]['blood_group'] == 'A' or records[i]['blood_group'] =='O':
					List3[records[i]['id']] = records[i]["contacts"]
				else:
					continue
			elif records[receiver_person_id]['blood_group'] == 'B':
				if records[i]['blood_group'] == 'B' or records[i]['blood_group'] =='O':
					List3[records[i]['id']] = records[i]["contacts"]
				else:
					continue
			elif records[receiver_person_id]['blood_group'] == 'AB':
				if records[i]['blood_group'] == 'A' or records[i]['blood_group'] =='B' or records[i]['blood_group'] =='AB' or records[i]['blood_group'] =='O':
					List3[records[i]['id']] = records[i]["contacts"]
				else:
					continue
			elif records[receiver_person_id]['blood_group'] == 'O':
				if records[i]['blood_group'] == 'O':
					List3[records[i]['id']] = records[i]["contacts"]
				else:
					continue

	return List3


def get_common_friends(records, list_of_ids):
	'''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''

	ab = []
	List4 = []
	id_1 = []
	for p in range(len(records)):
		id_1.append(records[p]['id'])
	for j in list_of_ids:
		if j in id_1:
			ab.extend(records[j]["friend_ids"])
		else:
			continue
	for i in ab:
		if ab.count(i)==len(list_of_ids):
			if i not in List4:
				List4.append(i)
		else:
			continue
	return List4



def is_related(records, person_id_1, person_id_2):
	'''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
	'''

	# Alternste Code (if time increase pls run this one)
	# for i in range(len(records)):
	# 	if person_id_1 in records[i]["friend_ids"] and person_id_2 in records[i]["friend_ids"]:
	# 		return True
	# 	elif person_id_1 in records[i]["friend_ids"]:
	# 		for j in records[i]["friend_ids"]:
	# 			if person_id_2 in records[j]["friend_ids"]:
	# 				return True
	# 			else:
	# 				continue
	# 	else:
	# 		continue
	# return False

	List_6 = []
	for i in range(len(records)):
		List_6.extend(records[i]['friend_ids'])
	for j in List_6:
		for k in records[j]['friend_ids']:
			if k not in List_6:
				List_6.append(k)
			else:
				continue

	if person_id_1 == person_id_2:
		return False
	elif person_id_1 in List_6 and person_id_2 in List_6:
		return True
	else:
		return False




def delete_by_id(records, person_id):
	'''
	Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	for i in records:
		if i['id'] == person_id:
			records.remove(i)
		else:
			continue
		for j in records:
			if person_id in j["friend_ids"]:
				j["friend_ids"].remove(person_id)
			else:
				continue

	return records



def add_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	for i in range(len(records)):
		if 0<=person_id < len(records) and 0<=friend_id < len(records) and person_id != friend_id:
			if records[i]['id'] == person_id:
				if friend_id not in records[i]['friend_ids']:
					records[i]['friend_ids'].append(friend_id)
					records[i]['friend_ids'].sort()
			if records[i]['id'] == friend_id:
				if person_id not in records[i]['friend_ids']:
					records[i]['friend_ids'].append(person_id)
					records[i]['friend_ids'].sort()
		else:
			continue

	return records



def remove_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	for i in range(len(records)):
		if person_id!=friend_id:
			if records[i]['id'] == person_id:
				if friend_id in records[i]['friend_ids']:
					records[i]['friend_ids'].remove(friend_id)
			elif records[i]['id'] == friend_id:
				if person_id in records[i]['friend_ids']:
					records[i]['friend_ids'].remove(person_id)
			else:
				continue

	return records



def add_education(records, person_id, institute_name, ongoing, percentage):
	'''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	if ongoing == "False":
		ongoing = False
	elif ongoing == "True":
		ongoing = True
	for i in range(len(records)):
		if records[i]['id'] == person_id:
			if ongoing == False:
				records[i]['education'].append({"institute": institute_name, "ongoing": False, "percentage": percentage})
			else:
				records[i]['education'].append({"institute": institute_name, "ongoing": True})


	return records



