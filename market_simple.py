all_items = [{"item":"susu", "harga":50000}, {"item":"daging", "harga":20000},
             {"item":"lampu", "harga":15000},{"item":"masker", "harga":25000},
             {"item":"apel", "harga":30000}]
             
promotional_items = [{"item":"susu", "harga":50000},
                     {"item":"masker", "harga":25000}]
                     

def casier(user_inp):
	try:
		if user_inp.lower() == "all items":
			inp = input("input your order : ").lower()
			for n in range(len(all_items)):
				if inp == all_items[n]["item"]:
					print("available with price : ",all_items[n]["harga"])
				
		
		elif user_inp.lower() == "promotional items":
			inp = input("input your order : ").lower()
			for n in range(len(promotional_items)):
				if inp == promotional_items[n]["item"]:
					print("available with price : ",promotional_items[n]["harga"])
		
		else:
			print("there is no such options !!!")
	except (NameError, ValueError) as err:
		print("your error : ", err)
		
	

init = input("item : ")
casier(init)
