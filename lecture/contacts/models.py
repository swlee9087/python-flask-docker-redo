class Contacts(object):

    def __init__(self, name, phone, email, address):  # inst factor designated
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')

    @staticmethod
    def set_contact(self) -> object:
        return Contacts(input('Name: '), input('Number: '),
                        input('Email; '), input('Address: '))
        # inst on RAM. name/number etc = 0D

    @staticmethod
    def get_contact(ls):  # print directly
        for i in ls:  # i=element 1D, ls=obj 2D
            Contacts(input('Name: '), input('Number: '),
                     input('Email; '), input('Address: '))
            i.to_string()

    @staticmethod
    def del_contact(ls, name):
        for i, j in enumerate(ls):  # i=index bc index needed for data coordinate
            if name == j.name:  # no 'switch' in py, so. i=fixed, j=variable
                del ls[i]

    def print_menu(ls) -> int:
        # t = ' '
        # for i, j in enumerate(ls):
        #     t += str(i) + '-' + j + '\t'
        # return int(input(t))
        strg = ''
        for i, val in enumerate(ls):
            strg += f'{i}-{val}\t'
        return int(input(strg))

    # def main(self):
    #     ls = []
    #     while 1:
    #         menu = self.print_menu(['exit', 'add', 'print', 'delete', 'edit'])
    #         if menu == 1:
    #             t = self.set_contact()
    #             ls.append(t)
    #         elif menu == 2:
    #             for i in ls:
    #                 print({i.get_contact()})
    #         elif menu == 3:
    #             self.del_contact(ls, input('Delete Contact'))
    #             for i, j in enumerate(ls):
    #                 if j.name == self.del_name:
    #                     del ls[i]
    #         elif menu == 4:
    #             pass
    #         else:
    #             print('try again')
    #             break
