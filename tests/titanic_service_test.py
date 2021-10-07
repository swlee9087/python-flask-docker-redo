import unittest

from python.titanic.model.titanic_service import TitanicService


class TitanicServiceTest(unittest.TestCase):
    mock = TitanicService()

    def test_new_model(self):
        # print(self.mock.new_model("train"))
        print(self.mock.new_model("test"))

    def create_train(self):
        return self.mock.train.drop('Survived', axis=1)

    def count_survived_dead(self):
        return []

    def create_label(self):

        return None

    def drop_feature(self, *feature):

        return None

    def embarked_nominal(self):
        return None
    def fare_ordinal(self):  # fare=ordinal bc sortable into grps
        return None
    def age_ordinal(self):
        return None
    def title_nominal(self):
        return None
    def gender_nominal(self):
        return None

    def create_k_fold(self):  #
        return None

    def accuracy_by_classifier(self):  #
        return None

if __name__ == '__main__':
    unittest.main()