import data as dt
from Market import market
from dataExtract import extract

all_itmB = extract(dt.all_items, 1)
all_itmH = extract(dt.all_items, 2)
promoB = extract(dt.promotional_items, 1)
promoH = extract(dt.promotional_items, 2)

print("           !!!----------instruction----------!!!")
print("note: type 'all items' or 'promotion items' on the item input ")
print("\noption: ")
print("- all items")
print("- promotional items")
init = input("\nitem : ")
#print(init)
#market.casier(init)
mrk = market(init)
print(mrk.user_inp)
#mrk.casier()