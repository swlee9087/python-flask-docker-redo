import unittest

from python.basic.numpy_lib import NumpyLib


class NumpyLibTest(unittest.TestCase):
    mock = NumpyLib()

    def test_show_numpy(self):
        self.mock.show_numpy()

    def test_numpy_choice(self):
        self.mock.numpy_choice()

    def test_numpy_bubble_chart(self):
        self.mock.numpy_bubble_chart()

    def test_indexing_slicing(self):
        self.mock.indexing_slicing()

    def test_array_one_type(self):
        self.mock.array_one_type()

    def test_np_repeat_list(self):
        self.mock.np_repeat_list()

    def test_np_arange(self):
        self.mock.np_arange()

    def test_np_linspace(self):
        self.mock.np_linspace()

    def test_np_mask(self):
        self.mock.np_mask()

    def test_np_bubble_chart(self):
        self.mock.np_bubble_chart()

if __name__ == '__main__':
    unittest.main()