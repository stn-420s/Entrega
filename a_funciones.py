import matplotlib.pyplot as plt
import seaborn as sns

def plot_box_plots(dataframe, columns):
    for column in columns:
        dataframe[column].plot(kind='box', figsize=(5, 5))
        plt.title(f'Box Plot of {column}')
        plt.show()

def bp(data_x, data_y, x_label, y_label, title):
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data_x, y=data_y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_category_counts(data, column_name):
    counts = data[column_name].value_counts()
    m = pd.DataFrame({column_name: counts.index, 'Count': counts.values})
    m = m.sort_values(by=column_name)
    sns.barplot(data=m, y=column_name, x='Count')
    plt.show()

def plot_travel_frequency(data, target, xlabel, ylabel, title):
    sns.countplot(x=data, hue=target)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()