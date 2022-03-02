all_items = [{"item":"susu", "harga":50000}, {"item":"daging", "harga":20000},
             {"item":"lampu", "harga":15000},{"item":"masker", "harga":25000},
             {"item":"apel", "harga":30000}]

item_1 = ['susu','daging','lampu','masker','apel']

num = []
usr_item = []

inp = input("input word : ").split()
lis = inp
#print(lis)

for n in lis:
	if n.isdigit():
		num.append(n)
	elif n in item_1:
		usr_item.append(n)
		
print(num)
print(usr_item)
