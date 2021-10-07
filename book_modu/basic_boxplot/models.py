import matplotlib.pyplot as plt
import random
from book_modu.temp_chng_bday import TempChgBday
from book_modu.basic_histo.models import BasicHisto


class BasicBoxplot(object):

    def sorted_random_arr(month: str) -> []:
        arr = []
        [arr.append(random.randint(1, 1000)) for i in range(13)]
        return arr

    # def show_boxplot(arr: []):
    #     plt.boxplot(arr)
    #     plt.show()
    #
    # def show_boxplot_month(month: str):
    #     plt.boxplot(histograms.max_temps(month))
    #     plt.show()
    def show_boxplot(month: str):
        arr = BasicHisto.max_temps(month)
        plt.boxplot(arr)
        plt.show()

    def show_boxplot_all_months():
        # birth = TempChgBday()
        # birth.read_data()
        # arr = birth.data
        # month = [[], [], [], [], [], [], [], [], [], [], [], []]
        #    [month.append((float(i[-1])) for i in arr if i[-1] != '' and i[0].split('-')[1] - 1)]
        # for i in arr:
        #     if i[-1] != '':
        #         month[int(i[0].split('-')[1])-1].append(float(i[-1]))
        # [month[int(i[0].split('-')[1]) - 1].append(float(i[-1])) for i in arr if i[-1] != '']
        arr = []
        [arr.append(BasicHisto.max_temps(str(i + 1)
                                         if len(str(i + 1)) == 2
                                         else str('0' + str(i + 1))))
         for i in range(12)]
        plt.boxplot([i for i in arr])
        plt.show()

    def show_boxplot_per_date(month: str):
        arr = TempChgBday()
        arr.read_data()
        date = []
        # for i in range(31):
        #     day.append([])
        [date.append([]) for i in range(31)]
        [date[int(i[0].split('-')[2]) - 1].append(float(i[-1])) for i in arr.data if
         i[-1] != '' and i[0].split('-')[1] == month]

        #    [day.append(float(j[-1]) for i in arr if j[-1] != '' and j[0].split('-')[1] == '08' and int(j[0].split('-')[2]) - 1]
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 5), dpi=300)
        plt.boxplot(date, showfliers=False)
        plt.show()
