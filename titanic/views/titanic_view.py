
# 3
import pandas as pd

from python.titanic.model.dataset import Dataset
from python.titanic.model.titanic_service import TitanicService
from sklearn.ensemble import RandomForestClassifier


class TitanicView(object):
    dataset = Dataset()
    service = TitanicService()

    def modeling(self):
        """# service = self.service
        print(f'This is Type {type(this.train)}')
        print(f'The head of Train is \n {this.train.head(2)}')
        print(f'The head of Test is \n {this.test.head(2)}')"""
        this = self.preprocessing()
        self.learning(this)
        return this

    def preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")  # 합치기
        this.test = service.new_model("test")
        this.id = this.test['PassengerId']
        this.label = service.create_label(this)  #?
        this.train = service.create_train(this)  #?
        this = service.embarked_nominal(this)
        this = service.fare_ordinal(this)
        this = service.title_nominal(this)
        this = service.gender_nominal(this)
        this = service.age_ordinal(this)
        this = service.drop_feature(this,'Cabin', 'Name', 'Sex','Age','Fare', 'SibSp','Parch','Ticket')
        # self.print_this(this)  # no more need to testprint here
        return this

    def learning(self,this):
        print(f'SKLearn algorithm accuracy : {self.service.accuracy_by_classifier(this)}')

    def submit(self):
        this = self.modeling()
        clf = RandomForestClassifier()
        clf.fit(this.train, this.test)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('../data/submission.csv', index=False)

    @staticmethod  # exactly why though. when X self but this.
    def print_this(this):
        print('*'*100)
        print(f'\nType of Train is {type(this.train)}. '
              f'\nType of Test is {type(this.test)}.\n')
        print('-' * 50)
        print(f'\nTop Row of Train is \n{this.train.head(1)}. '
              f'\nTop Row of Test is \n{this.test.head(1)}.\n')
        print('-' * 50)
        print(f'\nColumns of Train are \n{this.train.columns}. '
              f'\nColumns of Test are \n{this.test.columns}.\n')
        print('-' * 50)
        print(f'\nNull Count of Train is \n{this.train.isnull().sum()}. '
              f'\nNull Count of Test is \n{this.test.isnull().sum()}.\n')
        print('*'*100)
"""
if __name__ == '__main__':
    view = TitanicView()
    view.modeling()
"""