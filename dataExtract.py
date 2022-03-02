def extract(data, num):
	list1 = []
	if num == 1:
		for n in range(len(data)):
			list1.append(data[n]['item'])
	else:
		for n in range(len(data)):
			list1.append(data[n]['harga'])
	return list1


