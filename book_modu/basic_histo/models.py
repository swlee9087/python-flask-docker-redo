import matplotlib.pyplot as plt
import random

from book_modu.temp_chng_bday import TempChgBday

"""def hist_show():
    ls = []
    plt.hist(ls, 'b')
    plt.show()
"""


class BasicHisto(object):

    def show_dice(count):
        """ls2 = [random.randint(1, 6)]
        print(ls2)"""
        ls = []
        [ls.append(random.randint(1, 6)) for i in range(count)]
        return ls

    def dice_hist(ls):
        plt.hist(ls, bins=6)
        plt.show()

    def max_temps(month: str) -> []:
        birth = TempChgBday()
        birth.read_data()
        # [print(i) for i in birth.data]
        arr = []
        [arr.append(float(i[-1])) for i in birth.data if i[-1] != '' and i[0].split('-')[1] == month]
        #    [jan.append(float(i[-1])) for i in birth.data if i[-1] != '' and i[0].split('-')[1] == '01']
        return arr

    def show_hist_about(arr: [], month: str):
        plt.hist(arr, bins=1000, color='r', label=f'{month} Month')
        #    plt.hist(jan, bins=100, color='b', label='Jan')
        plt.legend()
        plt.show()
