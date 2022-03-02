list1 = [1, 2, 4, 7]
list2 = [7, 4]

res = []
# Iterate in the 1st list 
for idx, m in enumerate(list1): 
    # Iterate in the 2nd list 
    for idx2, n in enumerate(list2): 
        # if there is a match
        if m != n:
            None
        else:
            res.append((idx, idx2)) 

print(res)

def find_matching_index(list1, list2):

    inverse_index = { element: index for index, element in enumerate(list1) }

    return [(index, inverse_index[element])
        for index, element in enumerate(list2) if element in inverse_index]

#find_matching_index([1,2,3], [3,2,1]) # [(0, 2), (1, 1), (2, 0)]
print(find_matching_index(list1, list2))
