all_items = [{"item":"susu", "harga":50000}, {"item":"daging", "harga":20000},
             {"item":"lampu", "harga":15000},{"item":"masker", "harga":25000},
             {"item":"apel", "harga":30000}]
             
promotional_items = [{"item":"susu", "harga":50000},
                     {"item":"masker", "harga":25000}]
 
 #print(type(all_items))
#print(all_items[0]["item"])                    
                     
inp = input("input your finding : ")

for n in range(len(all_items)):
	if inp == all_items[n]["item"]:
		print("available with price : ",all_items[n]["harga"])
