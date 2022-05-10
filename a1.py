'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions. 

- You MUST complete the functions defined below, except the ones that are already defined. 
'''
code = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
item = ['Tshirt', 'Trousers', 'Scarf', 'Smartphone', 'iPad', 'Laptop', 'Eggs', 'Chocolate', 'Juice', 'Milk']
ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
price = [500, 600, 250, 20000, 30000, 50000, 5, 10, 100, 45]
Apparels = ['Tshirt', 'Trousers', 'Scarf']
Electronics = ['Smartphone', 'iPad', 'Laptop']
Eatables = ['Eggs' , 'Chocolate', 'Juice', 'Milk']
apparels_cost = 0
electronics_cost = 0
eatables_cost = 0
a = 0
e = 0
ea = 0
tco = 0

def show_menu():
	'''
	Description: Prints the menu as shown in the PDF
	
	Parameters: No paramters
	
	Returns: No return value
	'''
	print("="*48)
	print("MY BAZAAR".center(50))
	print("="*48)
	print("Hello! welcome to my grocery store!")
	print("Following are the products available in the shop:")
	print("")
	print("-"*48)
	print("CODE | DESCRPTION |  CATEGORY   | COST (Rs)")
	print("-"*48)
	print("0    | Tshirt     |  Apparels   | 500      ")
	print("1    | Trousers   |  Apparels   | 600      ")
	print("2    | Scarf      |  Apparels   | 250      ")
	print("3    | Smartphone |  Electronics| 20,000   ")
	print("4    | iPad       |  Electronics| 30,000   ")
	print("5    | Laptop     |  Electronics| 50,000   ")
	print("6    | Eggs       |  Eatables   | 5        ")
	print("7    | Chocolate  |  Eatables   | 10       ")
	print("8    | Juice      |  Eatables   | 100      ")
	print("9    | Milk       |  Eatables   | 45       ")
	print("-"*48)
	


def get_regular_input():
	'''
	Description: Takes space separated item codes (only integers allowed). 
	Include appropriate print statements to match the output with the 
	screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i. 
	'''
	print("-"*48)
	print("ENTER ITEMS YOU WISH TO BUY")
	print("-"*48)
	p = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	f = []
	A = list(map(str,input("Enter the item codes (space-separated): ").split()))
	for i in A:
		if i in p:
			f.append(int(i))
		else:
			print("Invalid input")
			continue
	for j in range(0, 10):
		ans[j] = f.count(j)

	return ans



def get_bulk_input():
	'''
	Description: Takes inputs (only integers allowed) from a bulk buyer. 
	For details, refer PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	'''
	print("-"*48)
	print("ENTER ITEM AND QUANTITIES")
	print("-"*48)
	while True:
		try:
			y = list(map(int,input("Enter code and quantity (leave blank to stop): ").split()))
			if y == []:
				print("Your order has been finalized")
				break
			elif y[1]<0 and (y[0]>9 or y[0]<0):
				print("Invalid code and quantity. Try again.")
			elif y[0]<0 or y[0]>9:
				print("Invalid code. Try again.")
			elif y[1]<0:
				print("Invalid quantity. Try again.")
			else:
				print("You added {} {}".format(y[1], item[y[0]]))
				ans[y[0]] += y[1]
		except:
			print("Invalid Input")
			continue
	return ans


def print_order_details(quantities):
	'''
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: No return value
	'''
	print("-"*48)
	print("ORDER DETAILS")
	print("-"*48)
	i=0
	for j in range(len(quantities)):
		if quantities[j] != 0:
			p=price[j] * quantities[j]
			i +=1
			print("[{}] {} x {} = Rs {} * {} = Rs {}".format(i, item[j], quantities[j], price[j], quantities[j], p))
		else:
			continue


def calculate_category_wise_cost(quantities):
	'''
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: A 3-tuple of integers in the following format: 
	(apparels_cost, electronics_cost, eatables_cost)
	'''
	print("-"*48)
	print("CATEGORY_WISE COST")
	print("-"*48)
	global apparels_cost
	global electronics_cost
	global eatables_cost
	for i in range(len(quantities)):
		if item[i] in Apparels:
			apparels_cost += price[i] * quantities[i]
		if item[i] in Electronics:
			electronics_cost += price[i] * quantities[i]
		if item[i] in Eatables:
			eatables_cost += price[i] * quantities[i]

	print("Apparels = Rs {}".format(apparels_cost))
	print("Electronics = Rs {}".format(electronics_cost))
	print("Eatables = Rs {}".format(eatables_cost))

	return (apparels_cost, electronics_cost, eatables_cost)


def get_discount(cost, discount_rate):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the discounted category-wise price, if applicable. 
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	
	Returns: A 3-tuple of integers in the following format: 
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
	'''
	global a
	global e
	global ea
	print("-"*48)
	print("DISCOUNTS")
	print("-"*48)
	if apparels_cost >= 2000:
		dis_on_apparels = get_discount(apparels_cost, 0.1)
		a = apparels_cost - dis_on_apparels
		print("[APPAREL] Rs {} - {} = Rs {}".format(apparels_cost, dis_on_apparels, a))
	else:
		dis_on_apparels = 0
		a = apparels_cost - dis_on_apparels
	if electronics_cost >= 25000:
		dis_on_electronics = get_discount(electronics_cost, 0.1)
		e = electronics_cost - dis_on_electronics
		print("[ELECTRONICS] Rs {} - Rs {} = Rs {}".format(electronics_cost, dis_on_electronics, e))
	else:
		dis_on_electronics = 0
		e = electronics_cost - dis_on_electronics
	if eatables_cost >= 500:
		dis_on_eatables = get_discount(eatables_cost, 0.1)
		ea = eatables_cost - dis_on_eatables
		print("[EATABLES] Rs {} - Rs {} = Rs {}".format(eatables_cost, dis_on_eatables, ea))
	else:
		dis_on_eatables = 0
		ea = eatables_cost - dis_on_eatables
	td = dis_on_apparels + dis_on_electronics + dis_on_eatables
	tc = a + e + ea
	print("")
	print("TOTAL DISCOUNT = Rs {}".format(td))
	print("TOTAL COST = Rs {}".format(tc))

	return (a, e, ea)


def get_tax(cost, tax):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the total cost including taxes.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables' 
	
	Returns: A 2-tuple of integers in the following format: 
	(total_cost_including_tax, total_tax)
	'''
	print("-"*48)
	print("TAX")
	print("-"*48)
	global a
	global e
	global ea
	global tco
	tax_on_apparels = get_tax(a, 0.10)
	print("[APPAREL] Rs {} * {} = Rs {}".format(a, 0.10, tax_on_apparels))
	ta = a + tax_on_apparels
	tax_on_electronics = get_tax(e, 0.15)
	print("[ELECTRONICS] Rs {} * {} = Rs {}".format(e, 0.15, tax_on_electronics))
	te = e + tax_on_electronics
	tax_on_eatables = get_tax(ea, 0.05)
	print("[EATABLES] Rs {} * {} = Rs {}".format(ea, 0.05, tax_on_eatables))
	tea = ea + tax_on_eatables
	tt = tax_on_apparels + tax_on_electronics + tax_on_eatables
	tco = ta + te + tea
	print("")
	print("TOTAL TAX = Rs {}".format(tt))
	print("TOTAL COST = Rs {}".format(tco))

	return (tco, tt)


def apply_coupon_code(total_cost):
	'''
	Description: Takes the coupon code from the user as input (case-sensitive). 
	For details, refer the PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: The total cost (integer) on which the coupon is to be applied.
	
	Returns: A 2-tuple of integers:
	(total_cost_after_coupon_discount, total_coupon_discount)
	'''
	print("-"*48)
	print("COUPON CODE")
	print("-"*48)
	while True:
		discount = 0
		coupon_code = input("Enter coupon code (else leave blank): ")
		if coupon_code == 'HELLE25':
			if total_cost >= 25000:
				discount = 0.25 * total_cost
				if discount > 5000:
					discount = 5000
					print("[HELLE25] min(5000, Rs {} * {}) = Rs {}".format(total_cost, 0.25, discount))
					print("")
					print("TOTAL COUPON DISCOUNT = Rs {}".format(5000))
					print("TOTAL COST = Rs {}".format(total_cost - 5000))
				else:
					print("[HELLE25] min(5000, Rs {} * {}) = Rs {}".format(total_cost, 0.25, discount))
					print("")
					print("TOTAL COUPON DISCOUNT = Rs {}".format(discount))
					print("TOTAL COST = Rs {}".format(total_cost - discount))
			else:
				print("Amount for Discount is Less then 25000")
				discount = 0
			break
		elif coupon_code == 'CHILL50':
			if total_cost >= 50000:
				discount = 0.50 * total_cost
				if discount > 10000:
					discount = 10000
					print("[CHILL50] min(10000, Rs {} * {}) = Rs {}".format(total_cost, 0.50, discount))
					print("")
					print("TOTAL COUPON DISCOUNT = Rs {}".format(10000))
					print("TOTAL COST = Rs {}".format(total_cost - 10000))
				else:
					print("[CHILL50] min(10000, Rs {} * {}) = Rs {}".format(total_cost, 0.50, discount))
					print("")
					print("TOTAL COUPON DISCOUNT = Rs {}".format(discount))
					print("TOTAL COST = Rs {}".format(total_cost - discount))
			else:
				print("Amount for Discount is Less then 50000")
				discount = 0
			break	
		elif len(coupon_code) == 0:
			print("No coupon code applied.")
			print("")
			print("TOTAL COUPON DISCOUNT = Rs 0")
			print("TOTAL COST = Rs {}".format(total_cost))
			break
		else:
			print("Invalid coupon code. Try again.")
			print("")

	m = total_cost - discount
	return (m, discount)



def main():
	'''
	Description: This is the main function. All production level codes usually
	have this function. This function will call the functions you have written
	above to design the logic. You will see how splitting your code into specialised
	functions makes the code easier to read, write and debug. Include appropriate 
	print statements to match the output with the screenshots provided in the PDF.
	
	Parameters: No parameters
	
	Returns: No return value
	'''
	global a
	global e
	global ea
	global tco
	show_menu()
	while True:
		X = input("Would you like to buy in bulk? (y or Y / n or N): ").lower()
		if X == 'y':
			get_bulk_input()
			break
		elif X == 'n':
			get_regular_input()
			break
		else:
			print("Invalid input")
	
	print_order_details(ans)
	calculate_category_wise_cost(ans)
	calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost)
	calculate_tax(a, e, ea)
	apply_coupon_code(tco)

	print("")
	print("Thank you for visiting!")

if __name__ == '__main__':
	main()
