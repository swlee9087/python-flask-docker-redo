from dataclasses import dataclass


@dataclass
class Calculator(object):
    @property
    def num1(self) -> int:
        return self.num1

    @property
    def num2(self) -> int:
        return self.num2

    @num1.setter
    def num1(self, num1):
        self._num1 = num1

    @num2.setter
    def num2(self, num2):
        self._num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    # @staticmethod
    # def main():
    #     while 1:
    #         num1 = int(input('first number : '))
    #         num2 = int(input('second number : '))
    #         calc = Calculator(num1, num2)
    #         menu = input('0=Exit 1= + 2= - 3= * 4= / \n')
    #         if menu == '0':
    #             break
    #         elif menu == '1':
    #             print('*' * 100)
    #             print(f'{calc.num1}+{calc.num2} = {calc.add()}')
    #             print('*' * 100)
    #             break
    #         elif menu == '2':
    #             print('*' * 100)
    #             print(f'{calc.num1}-{calc.num2} = {calc.subtract()}')
    #             print('*' * 100)
    #             break
    #         elif menu == '3':
    #             print('*' * 100)
    #             print(f'{calc.num1}*{calc.num2} = {calc.multiply()}')
    #             print('*' * 100)
    #             break
    #         elif menu == '4':
    #             print('*' * 100)
    #             print(f'{calc.num1}/{calc.num2} = {calc.divide()}')
    #             print('*' * 100)
    #             break
    #         else:
    #             print('Wrong selected number')
    #         break


@dataclass
class Contacts(object):

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def to_string(self):
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')

    @staticmethod
    def set_contact() -> object:
        return Contacts(input('Name: '), input('Number: '),
                        input('Email; '), input('Address: '))

    @staticmethod
    def get_contact(ls):  # print directly
        for i in ls:  # i=element 1D, ls=obj 2D
            Contacts(input('Name: '), input('Number: '),
                     input('Email; '), input('Address: '))
            i.to_string()
            return ls

    @staticmethod
    def del_contact(ls, name):
        for i, j in enumerate(ls):  # i=index bc index needed for data coordinate
            if name == j.name:  # no 'switch' in py, so. i=fixed, j=variable
                del ls[i]
                return ls

    @staticmethod
    def print_menu(ls) -> int:
        t = ' '
        for i, j in enumerate(ls):
            t += str(i) + '-' + j + '\t'
        return int(input(t))

    # def main():
    #     ls = []
    #     while 1:
    #         menu = print_menu(['exit', 'add', 'print', 'delete', 'edit'])
    #         if menu == 1:
    #             t = set_contact()
    #             ls.append(t)
    #         elif menu == 2:
    #             for i in ls:
    #                 print({i.get_contact()})
    #         elif menu == 3:
    #             del_contact(ls, input('Delete Contact'))
    #             for i, j in enumerate(ls):
    #                 if j.name == del_name:
    #                     del ls[i]
    #         elif menu == 4:
    #             pass
    #         else:
    #             print('try again')
    #             break


@dataclass
class Grade(object):
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def kor(self) -> int:
        return self._kor

    @kor.setter
    def kor(self, kor):
        self._kor = kor

    @property
    def eng(self) -> int:
        return self._eng

    @eng.setter
    def eng(self, eng):
        self._eng = eng

    @property
    def math(self) -> int:
        return self._math

    @math.setter
    def math(self, math):
        self._math = math

    # def __int__(self, name, kor, eng, math):
    #     self.name = name
    #     self.kor = kor
    #     self.eng = eng
    #     self.math = math

    # def addScores(self, score):
    #     self.scores.append(score)

    def sum(self):
        return self.kor+self.eng+self.math

    def avg(self):
        # return sum(self.scores) / len(self.scores)
        return self.sum() / 3

    @staticmethod
    def return_grade(self) -> str:
        avg = self.avg()
        if avg >= 90:
            result = 'A'
        elif avg >= 80:
            result = 'B'
        elif avg >= 70:
            result = 'C'
        elif avg >= 60:
            result = 'D'
        elif avg <= 50:
            result = 'E'
        else:
            result = 'F'
        print(f'{result}')


@dataclass
class Person(object):
    @property
    def name(self) -> str: return self._name

    @name.setter
    def name(self, name): self._name = name

    @property
    def age(self) -> int: return self._age

    @age.setter
    def age(self, age): self._age = age

    @property
    def address(self) -> str: return self._address

    @address.setter
    def address(self, address): self._address = address

    # def __init__(self, name, age, address):
    #     self.name = name
    #     self.age = age
    #     self.address = address

    def to_string(self):  # this is the matrix form to show
        print(f'\n[Personal Info] '
              f'\nName : {self.name}'
              f'\nAge : {self.age}'
              f'\nAddress: {self.address}\n')

# def main():
#     persons = []
#     while 1:
#         print('\n0=exit 1=add 2=print')
#         menu = input('Choose 1 option. ')
#         if menu == '1':
#             persons.append(Person(input('name '), input('age '), input('address ')))
#         elif menu == '2':
#             for i in persons:
#                 i.to_string()
#         elif menu == '0':
#             return
