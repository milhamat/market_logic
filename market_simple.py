all_items = [{"item":"susu", "harga":50000}, {"item":"daging", "harga":20000},
             {"item":"lampu", "harga":15000},{"item":"masker", "harga":25000},
             {"item":"apel", "harga":30000}]
             
promotional_items = [{"item":"susu", "harga":50000},
                     {"item":"masker", "harga":25000}]
     
item_1 = ['susu','daging','lampu','masker','apel']
item_2 = ['susu', 'masker']                

def casier(user_inp):
	num = []
	usr_item = []
	rm_spc_car = ","
	
	try:
		if user_inp.lower() == "all items":
			inp = input("input your order : ").lower()
			
			for char in rm_spc_car:
				inp = inp.replace(char, "")
				
			order = inp.split()
			print(order)
			
		
		elif user_inp.lower() == "promotional items":
			inp = input("input your order : ").lower()
			
			for char in rm_spc_car:
				inp = inp.replace(char, "")
				
			
			
		else:
			print("there is no such options !!!")
	except (NameError, ValueError) as err:
		print("your error : ", err)
		
	
print("instruction!!")
print("option: ")
print("- all items")
print("- promotional items")
init = input("\nitem : ")
casier(init)
