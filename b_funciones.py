import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import pandas as pd
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import cross_val_predict, cross_val_score, cross_validate


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

def imputar_f (df,list_cat):  
    df_c=df[list_cat]
    df_n=df.loc[:,~df.columns.isin(list_cat)]
    imputer_n=SimpleImputer(strategy='median')
    imputer_c=SimpleImputer(strategy='most_frequent')
    imputer_n.fit(df_n)
    imputer_c.fit(df_c)
    X_n=imputer_n.transform(df_n)
    X_c=imputer_c.transform(df_c)
    df_n=pd.DataFrame(X_n,columns=df_n.columns)
    df_c=pd.DataFrame(X_c,columns=df_c.columns)
    df =pd.concat([df_n,df_c],axis=1)
    return df

def convertir_a_tiempo(df):
    # Convertir las columnas a datetime
    for column in df.columns:
        df[column] = pd.to_datetime(df[column], errors='coerce')
    # Formatear las columnas datetime como '%H:%M'
    for column in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[column]):
            df[column] = df[column].dt.strftime('%H:%M')
    return df

# Crear una función para calcular la diferencia en minutos 

def calcular_diferencia(hora1, hora2):
    if pd.notnull(hora1) and pd.notnull(hora2):
        try:
            h1, m1 = map(int, hora1.split(':'))
            h2, m2 = map(int, hora2.split(':'))
            return (h2 * 60 + m2) - (h1 * 60 + m1)  # Cambio en el orden
        except ValueError:
            return None
    else:
        return None
    

def selector(trsh,df):
    selector = VarianceThreshold(threshold=trsh)
    num_fil = pd.DataFrame(selector.fit_transform(df), columns=df.columns[selector.get_support()])
    num2=num_fil
    return num2
    
def scalador(mc_num):
    # MinMaxScaler
    sca = MinMaxScaler()
    # Aplicar el escalado a los datos y convertirlos en un DataFrame
    x_sc = sca.fit_transform(mc_num)
    x_sc_df = pd.DataFrame(x_sc, columns=mc_num.columns)
    return x_sc_df

def medir_modelos(modelos,scoring,X,y,cv):
    metric_modelos=pd.DataFrame()
    for modelo in modelos:
        scores=cross_val_score(modelo,X,y, scoring=scoring, cv=cv )
        pdscores=pd.DataFrame(scores)
        metric_modelos=pd.concat([metric_modelos,pdscores],axis=1)
    metric_modelos.columns=['m1_dt', 'm1_gb', 'm1_rf']
    return metric_modelos