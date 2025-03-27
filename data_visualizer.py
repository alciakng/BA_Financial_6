from matplotlib import ticker
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DataVisualizer:
    def __init__(self):
        self.df = None

    def df_setter(self, df, title, x_label, y_label, x_size, y_size):
        self.df = df
        plt.figure(figsize=(x_size,y_size))
        plt.ticklabel_format(style='plain', axis='y')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        return plt

    def pie(self, plt, legned_title):
        fig = plt.figure(figsize=(8,8))
        fig.set_facecolor('white')

        ax = fig.add_subplot()
        ax.pie(self.df['COUNT'],
            labels=self.df.BIZ_COUNT,
            startangle=0,
            counterclock=False,
            autopct=lambda p :'{:.1f}%'.format(p))

        plt.legend(title=legned_title)
        plt.show()

    def box(self,plt):
        ax = sns.boxplot(x="BTH_SECTION",y="AMT", data=self.df, palette='Set2')
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

        plt.tight_layout()
        plt.show()


    def hist(self, column, bins=10):
        plt.figure(figsize=(8, 4))
        sns.histplot(self.df[column], bins=bins, kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()



    def scatter(self, x, y, hue=None):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=self.df, x=x, y=y, hue=hue)
        plt.title(f'Scatter plot of {y} vs {x}')
        plt.tight_layout()
        plt.show()

    def heatmap_corr(self):
        plt.figure(figsize=(10, 8))
        corr = self.df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.show()