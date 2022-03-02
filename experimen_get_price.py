all_items = [{"item":"susu", "harga":50000}, {"item":"daging", "harga":20000},
             {"item":"lampu", "harga":15000},{"item":"masker", "harga":25000},
             {"item":"apel", "harga":30000}]
             
usr_item = ["susu", "masker"]

val = []
for n in range(len(all_items)):
	for m in range(len(usr_item)):
		if usr_item[m] == all_items[n]["item"]:
			val.append(all_items[n]["harga"])
			

print(val)
print(type(val))
		
