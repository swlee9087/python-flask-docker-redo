import pandas as pd


# #matches, gold, silver, bronze, total / summer -winter-combined total

class OlympicMedals:

    def read_wiki(self) -> object:
        df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0, index_col=0)
        print(df)
        return df

    def show_summer(self, df):
        summer = df[1].iloc[:, :5]
        summer.columns = ['Match #', 'Gold', 'Silver', 'Bronze', 'Total']
        return summer.sort_values('Gold', ascending=False)
