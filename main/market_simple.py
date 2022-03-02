import data as dt
from dataExtract import extract

all_itmB = extract(dt.all_items, 1)
all_itmH = extract(dt.all_items, 2)
promoB = extract(dt.promotional_items, 1)
promoH = extract(dt.promotional_items, 2)
     
item_1 = ['susu','daging','lampu','masker','apel']
item_2 = ['susu', 'masker']                

num = []
usr_item = []
totl_sem = []
price = []

def display_menu():
	print("All Items: ")
	print(all_itmB)
	print(all_itmH,'\n')
	
	print("Promotional Items: ")
	print(promoB)
	print(promoH)


def get_price():
	val = []
	idx = []
	inverse_index = { element: index for index, element in enumerate(all_itmB) }
	dat_tup =  [(index, inverse_index[element]) for index, element in enumerate(usr_item) if element in inverse_index]
	for a, b in dat_tup:
		idx.append(b)
	for n in idx:
		val.append(all_itmH[int(n)])
	return val	
	

def calcu(n):
	result = []
	for i in range(len(num)):
		mult = int(num[i]) * int(price[i])
		result.append(mult)
	return result
	

def total(calc):
	tot = 0
	for n in range(len(calc)):
		tot+=int(calc[n])
	return tot
	

def recipt(total):
	print("\nTotal harga: Rp.", total)
	print("Detail: ")
	for n in range(len(num)):
		print(num[n] + ' ' + usr_item[n] + '-> Rp.',totl_sem[n])
		

def casier(user_inp):
	global num, usr_item, price, totl_sem
	rm_spc_car = ","
	num = []
	usr_item = []
	price = []
	totl_sem = []
	
	try:
		if user_inp.lower() == "all items":
			inp = input("input your order : ").lower()
			
			for char in rm_spc_car:
				inp = inp.replace(char, "")
				
			order = inp.split()
			for n in order:
				if n.isdigit():
					num.append(n)
				elif n in item_1:
					usr_item.append(n)
			
			price = get_price()
			#print(price)
			#print(num)
			rslt = calcu(price)
			totl_sem = rslt
			totl = total(rslt)
			recipt(totl)
			
		
		elif user_inp.lower() == "promotional items":
			inp = input("input your order : ").lower()
			
			for char in rm_spc_car:
				inp = inp.replace(char, "")
				
			order = inp.split()
			for n in order:
				if n.isdigit():
					num.append(n)
				elif n in item_2:
					usr_item.append(n)
			
			price = get_price()
			rslt = calcu(price)
			totl_sem = rslt
			totl = total(rslt)
			recipt(totl)
				

		else:
			print("there is no such options !!!")
	except (NameError, ValueError, IndexError) as err:
		print("\nyour error : ", err)
		
	
print("           !!!----------instruction----------!!!")
print("note: type 'all items' or 'promotion items' on the item input \n")
display_menu()
print("\noption: ")
print("- all items")
print("- promotional items")
init = input("\nuser input : ")
casier(init)
