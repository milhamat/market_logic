all_items = [{"item":"susu", "harga":50000}, {"item":"daging", "harga":20000},
             {"item":"lampu", "harga":15000},{"item":"masker", "harga":25000},
             {"item":"apel", "harga":30000}]
             
promotional_items = [{"item":"susu", "harga":50000},
                     {"item":"masker", "harga":25000}]
                     
#print(type(all_items))
#print(all_items[0]["item"])

def casier(user_inp):
	try:
		if user_inp.lower() == "all items":
			inp = input("input your order : ").lower()
			for item in all_items:
				
		
		elif user_inp.lower() == "promotional items":
			inp = input("input your order : ").lower()
		
		else:
			print("there is no such options !!!")
	except err:
		print("your error : ", err)
		
	
		


init = input("item : ")
casier(init)
