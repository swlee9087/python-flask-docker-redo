import unittest

from matplotlib import pyplot as plt

from python.modu.template.basic_plot import BasicPlot


class BasicPlotTest(unittest.TestCase):
    mock = BasicPlot()

    def test_plot_show(self):
        plt.title("plotting")
        plt.plot([10, 20, 30, 40])  # hence create at least two lists for reference
        plt.show()

    def test_plot_two_list_show(self):
        plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
        plt.show()

    def test_plot_two_list_show2(self):
        plt.title('legend')
        plt.plot([10, 20, 30, 40], label='asc')
        plt.plot([40, 30, 20, 10], label='desc')
        plt.legend()
        plt.show()

    def test_plot_two_list_show3(self):
        plt.title('color')
        plt.plot([10, 20, 30, 40], color='skyblue', label='skyblue')
        plt.plot([40, 30, 20, 10], 'pink', label='pink')
        plt.legend()
        plt.show()

    def test_plot_two_list_show4(self):
        plt.title('linestyle')
        plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='dashed')
        plt.plot([40, 30, 20, 10], color='g', ls=':', label='dotted')
        plt.legend()
        plt.show()

    def test_plot_marker_show(self):
        plt.title('marker')
        plt.plot([10, 20, 30, 40], 'r.', label='circle')
        plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
        plt.legend()
        plt.show()

    def test_show_path(self):
        self.instance.show_path()

if __name__ == '__main__':
    unittest.main()