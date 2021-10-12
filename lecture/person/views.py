from lecture.person.models import Person

if __name__ == '__main__':
    persons = []
    while 1:
        print('\n0=exit 1=add 2=print')
        menu = input('Choose 1 option. ')
        if menu == '0':
            break
        elif menu == '1':
            persons.append(Person(input('name '), input('age '), input('address ')))
        elif menu == '2':
            for i in persons:
                i.to_string()
