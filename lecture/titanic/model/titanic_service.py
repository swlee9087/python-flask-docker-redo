import numpy as np
import pandas as pd

# 2
from lecture.titanic.model.dataset import Dataset
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier


class TitanicService(object):
    dataset = Dataset()  # constructorrrrr

    def new_model(self, payload: str) -> object:
        """this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)"""
        return pd.read_csv(f"/data/{payload}.csv")

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)  # del "Survived' col from dataset

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:  # data features to omit from set because they are irrelevant as death cause
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:  # QSC -> numbers
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this  # this에 다시 넣어주고 ctrlr로 넘김

    """['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
     'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']"""

    @staticmethod
    def fare_ordinal(this) -> object:  # paid amount correlate to pclass?
        this.train['Fare'] = this.train['Fare'].fillna(1)  # fill blanks
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'],4, labels={1,2,3,4})
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1,2,3,4})
        # qcut() auto divides into range qty as specified
        # bins = [-1,8,15,31,np.inf]  # np.inf = infinite range
        # this.train = this.train.drop(['Fare'])
        # this.test = this.test.drop(['Fare'])
        return this

    @staticmethod
    def title_nominal(this) -> object:  # mr mrs miss master ms -> numbers
        combine = [this.train, this.test]
        title_mapping = {'Mr':1, 'Ms':2, 'Mrs':3, 'Master':4, 'Nobles':5, 'Rare':6}
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)  # vvv specific. expand=False to stop reading further
        for dataset in combine:
            dataset["Title"] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer','Dona','Mme'], 'Rare')
            dataset["Title"] = dataset['Title'].replace(['Mlle'], 'Mr')
            dataset["Title"] = dataset['Title'].replace(['Miss'], 'Ms')
            dataset["Title"] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Nobles')
            dataset['Title'] = dataset['Title'].fillna(0)  # for those without titles
            dataset['Title'] = dataset['Title'].map(title_mapping)
        """this.train = this.train
        this.test = this.test"""
        return this

    @staticmethod
    def gender_nominal(this) -> object:  # mf
        combine = [this.train, this.test]
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Gender'] = dataset['Sex'].map(sex_mapping)
        """this.train = this.train
        this.test = this.test"""
        return this

    @staticmethod
    def age_ordinal(this) -> object:  # qcut() ok but nah. split into age grps. don't combine
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)  # -0.5 so that the are classified into unknown
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown','Baby','Child','Teenager','Student','Young Adult','Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6,
                       'Senior': 7}
        """
        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)  # unlike qcut(0 that divs equally into qrts, cut() divs as bins specified
        test['AgeGroup'] = pd.cut(test['Age'], bins, labels=labels)        
        age_title_mapping = {0: 'Unknown', 1: 'Baby', 2: 'Child', 3: 'Teenager', 4: 'Student', 5: 'Young Adult',
                             6: 'Adult', 7: 'Senior'}
     
        for i in range(len(train['AgeGroup'])):
            if train['AgeGroup'][i] == 'Unknown':
                train['AgeGroup'][i] =age_title_mapping[train['Title'][i]]
        for i in range(len(test['AgeGroup'])):
            if test['AgeGroup'][i] == 'Unknown':
                test['AgeGroup'][i] =age_title_mapping[test['Title'][i]]
        
        
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        this.train = this.train
        this.test = this.test
        """
        for i in train, test:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def create_k_fold() -> object:  # creates model through learning in series
        return KFold(n_splits=10, shuffle=True, random_state=0)  # loop x10

    def accuracy_by_classifier(self, this):  #
        score = cross_val_score(RandomForestClassifier(), this.train, this.label,
                                cv=self.create_k_fold(),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score)*100,2)

