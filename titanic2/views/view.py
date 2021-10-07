from python.titanic2.model.dataset import Dataset
from python.titanic2.model.service import Service


class View(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocessing(train, test)
        print(f'This is Type {type(this.train)}')
        print(f'The head of Train is {this.train.head(2)}')
        print(f'The head of Test is {this.test.head(2)}')

    def preprocessing(self, train, test) -> object:  # ??
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)  # <- (train)=(payload)
        this.test = service.new_model(test)
        return this  # =self.dataset in this


if __name__ == '__main__':
    View().modeling('train.csv', 'test.csv')
