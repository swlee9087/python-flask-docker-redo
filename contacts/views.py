from contacts.models import Contacts
from menu.models import Menu

if __name__ == '__main__':
    # ls = ['0-exit', '1-add', '2-print', '3-delete']
    # ls2 = ['exit', 'add', 'print', 'delete']
    # print(menu(ls2))
    # contacts = []
    # while 1:
    #     menu = print_menu(['exit', 'add', 'print', 'delete'])
    #     if menu == 1:
    #         t = Contacts.set_contact()
    #         contacts.append(t)
    #     elif menu == 2:
    #         Contacts.get_contacts(contacts)
    #     elif menu == 3:
    #         Contacts.del_contact(contacts, input('Del Name'))
    #     else:
    #         break

    ls = []
    while 1:
        menu = Menu.print_menu(['exit', 'add', 'print', 'delete', 'edit'])
        if menu == 1:
            t = Contacts.set_contact()
            ls.append(t)
        elif menu == 2:
            for i in ls:
                print({i.get_contact()})
        elif menu == 3:
            Contacts.del_contact(ls, input('Delete Contact'))
            for i, j in enumerate(ls):
                if j.name == Contacts.del_name:
                    del ls[i]
        elif menu == 4:
            pass
        else:
            print('try again')
            break
