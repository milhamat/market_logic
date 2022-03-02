class market:


    def __init__(self, user_inp):
        self.user_inp = ''
        self.item_1 = ['susu', 'daging', 'lampu', 'masker', 'apel']
        self.item_2 = ['susu', 'masker']
        self.num = []
        self.usr_item = []
        self.totl_sem = []
        self.price = []


    def get_price(self):
        val = []
        idx = []
        inverse_index = {element: index for index, element in enumerate(all_itmB)}
        dat_tup = [(index, inverse_index[element]) for index, element in enumerate(usr_item) if
                   element in inverse_index]
        for a, b in dat_tup:
            idx.append(b)
        for n in idx:
            val.append(all_itmH[int(n)])
        return val


    def calcu(self, n):
        result = []
        for i in range(len(num)):
            mult = int(self.num[i]) * int(self.price[i])
            result.append(mult)
        return result


    def total(self, calc):
        tot = 0
        for n in range(len(calc)):
            tot += int(calc[n])
        return tot


    def recipt(self, total):
        print("\nTotal harga: Rp.", total)
        print("Detail: ")
        for n in range(len(self.num)):
            print(self.num[n] + ' ' + self.usr_item[n] + '-> Rp.', self.totl_sem[n])


    def casier(self):
        global num, usr_item, price, totl_sem
        rm_spc_car = ","
        num = []
        usr_item = []
        price = []
        totl_sem = []

        try:
            if self.user_inp.lower() == "all items":
                inp = input("input your order : ").lower()

                for char in rm_spc_car:
                    inp = inp.replace(char, "")

                order = inp.split()
                for n in order:
                    if n.isdigit():
                        num.append(n)
                    elif n in item_1:
                        usr_item.append(n)

                price = get_price()
                print(price)
                print(num)
                rslt = calcu(price)
                totl_sem = rslt
                totl = total(rslt)
                recipt(totl)


            elif self.user_inp.lower() == "promotional items":
                inp = input("input your order : ").lower()

                for char in rm_spc_car:
                    inp = inp.replace(char, "")

                order = inp.split()
                for n in order:
                    if n.isdigit():
                        num.append(n)
                    elif n in item_2:
                        usr_item.append(n)

                price = get_price()
                rslt = calcu(price)
                totl_sem = rslt
                totl = total(rslt)
                recipt(totl)

            else:
                print("there is no such options !!!")
        except (NameError, ValueError) as err:
            print("your error : ", err)