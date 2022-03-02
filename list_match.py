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
