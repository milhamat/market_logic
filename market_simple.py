all_items = [{"item":"susu", "harga":50000}, {"item":"daging", "harga":20000},
             {"item":"lampu", "harga":15000},{"item":"masker", "harga":25000},
             {"item":"apel", "harga":30000}]
             
promotional_items = [{"item":"susu", "harga":50000},
                     {"item":"masker", "harga":25000}]
     
item_1 = ['susu','daging','lampu','masker','apel']
item_2 = ['susu', 'masker']                

num = []
usr_item = []
price = []

def get_price():
	val = []
	for n in range(len(all_items)):
		for m in range(len(usr_item)):
			if usr_item[m] == all_items[n]["item"]:
				val.append(all_items[n]["harga"])
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
		print(num[n] + ' ' + usr_item[n] + '-> Rp.',price[n])
		
	

def casier(user_inp):
	global num, usr_item, price
	rm_spc_car = ","
	num = []
	usr_item = []
	price = []
	
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
			rslt = calcu(price)
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
			totl = total(rslt)
			recipt(totl)
				

		else:
			print("there is no such options !!!")
	except (NameError, ValueError) as err:
		print("your error : ", err)
		
	
print("           !!!----------instruction----------!!!")
print("note: type 'all items' or 'promotion items' on the item input ")
print("\noption: ")
print("- all items")
print("- promotional items")
init = input("\nitem : ")
casier(init)
