from book_modu.temp_chng_bday.models import TempChgBday

if __name__ == '__main__':
    this = TempChgBday()
    this.read_data()
    this.birthday_temps()