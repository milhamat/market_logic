def extract(data, num):
	list = []
	if num == 1:
		for n in range(len(data)):
			list.append(all_items[n]['item'])
	else:
		for n in range(len(data)):
			list.append(all_items[n]['harga'])
	return list
		
