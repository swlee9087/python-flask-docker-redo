import unittest
from admin.sorting.basic.models_oop import *


class TestCalc(unittest.TestCase):

    def test_add(self):
        inst = Calculator(6, 3)
        res = inst.add()
        self.assertEqual(res, 9)

    def test_subtract(self):
        inst = Calculator(6, 3)
        res = inst.subtract()
        self.assertEqual(res, 3)

    def test_multiply(self):
        inst = Calculator(6, 3)
        res = inst.multiply()
        self.assertEqual(res, 18)

    def test_divide(self):
        inst = Calculator(6, 3)
        res = inst.divide()
        self.assertEqual(res, 2)


class TestContacts(unittest.TestCase):
    def test_get_contact(self):
        ls = [Contacts.set_contact('A', "010-1234", "a@abc.com", "City A"),
              Contacts.set_contact('B', "010-2345", "b@abc.com", "City B"),
              Contacts.set_contact('C', "010-3456", "c@abc.com", "City C")]
        ls = Contacts.get_contact(ls)
        self.assertEqual(ls[0].name, 'A')

    def test_del_contact(self):
        ls = [Contacts.set_contact('A', "010-1234", "a@abc.com", "City A"),
              Contacts.set_contact('B', "010-2345", "b@abc.com", "City B"),
              Contacts.set_contact('C', "010-3456", "c@abc.com", "City C")]
        ls = Contacts.del_contact(ls, 'B')
        print([x.to_string() for x in ls])
        self.assertEqual(len(ls), 2)


class TestGrade(unittest.TestCase):
    def test_avg(self):
        grade = Grade('Han', 60, 70, 80)
        # gr = Grade()
        # gr.name = 'Han'
        # gr.kor = 60
        # gr.eng = 70
        # gr.math = 80
        self.assertEqual(grade.name, 'Han')
        self.assertEqual(grade.return_grade(), 'C')


class TestPerson(unittest.TestCase):
    def test_person(self):
        pers = Person("Lee", 31, "Seoul")
        res = pers.to_string()
        print(res)
        # self.assertEqual(pers.name,"Lee")
        # self.assertEqual(pers.age,31)
        # self.assertEqual(pers.address, "Seoul")


if __name__ == '__main__':
    unittest.main()
