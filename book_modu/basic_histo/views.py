from book_modu.basic_histo.models import BasicHisto

if __name__ == '__main__':
    # hist_show()
    """ls = show_dice(1000000)
    print(ls)
    dice_hist(ls)"""
    # BasicHisto.show_dice()
    # BasicHisto.dice_hist()
    BasicHisto.max_temps('08')
    BasicHisto.show_hist_about(BasicHisto.max_temps('01'), month='01')
