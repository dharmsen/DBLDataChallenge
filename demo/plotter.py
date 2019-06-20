import pandas as pd
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, data):
        self.df = pd.read_csv(data)

    def sent_bar(self):
        plt.figure(figsize=(8, 5))
        self.df['sentiments'].value_counts().plot(kind='bar', rot=0)
        plt.xticks(fontsize=16)
        plt.xlabel('Sentiment', fontsize=17)
        plt.yticks(fontsize=16)
        plt.ylabel('Frequency', fontsize=17)
        plt.title('Sentiment distribution in dataset', weight='bold', fontsize=20)


if __name__ == '__main__':
    pass
    # plotter = Plotter('cleaned_data.csv')
    # plotter.sent_bar()
