class Person(object):

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_string(self):  # this is the matrix form to show
        print(f'\n[Personal Info] '
              f'\nName : {self.name}'
              f'\nAge : {self.age}'
              f'\nAddress: {self.address}\n')


def main():
    persons = []
    while 1:
        print('\n0=exit 1=add 2=print')
        menu = input('Choose 1 option. ')
        if menu == '1':
            persons.append(Person(input('name '), input('age '), input('address ')))
        elif menu == '2':
            for i in persons:
                i.to_string()
        elif menu == '0':
            return


if __name__ == '__main__':
    main()
