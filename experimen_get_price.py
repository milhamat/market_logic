all_items = [{"item":"susu", "harga":50000}, {"item":"daging", "harga":20000},
             {"item":"lampu", "harga":15000},{"item":"masker", "harga":25000},
             {"item":"apel", "harga":30000}]
             
usr_item = ["lampu", "masker", "susu"]

val = []
#for n in range(len(all_items)): 
#	for m in range(len(usr_item)): 
#		if usr_item[m] == all_items[n]["item"]:
#			val.append(all_items[n]["harga"])

item_1 = ['susu','daging','lampu','masker','apel']
harga = [2000, 5000, 6000, 7000, 8000]

res = []
for idx, m in enumerate(item_1): 
    for idx2, n in enumerate(usr_item): 
        if m != n:
            None
        else:
            res.append((idx, idx2)) 

#print(res)
#print(val)
#print(type(val))
		
def find_matching_index(list1, list2):

    inverse_index = { element: index for index, element in enumerate(list1) }

    return [(index, inverse_index[element])
        for index, element in enumerate(list2) if element in inverse_index]
    
print(find_matching_index(item_1, usr_item))
dat_tup = find_matching_index(item_1, usr_item)
idx = []
for a, b in dat_tup:
	idx.append(b)
print(idx)

for n in idx:
	print(harga[int(n)])
