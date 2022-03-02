usr_inp = input("Choose a username: ")
rm_spc_car = ","

for char in rm_spc_car:
	usr_inp = usr_inp.replace(char, "")

print("Your username is: " + usr_inp)
