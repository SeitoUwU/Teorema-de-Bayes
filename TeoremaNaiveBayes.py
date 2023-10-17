import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import colors


plt.rcParams['figure.figsize'] = (16,9)
plt.style. use('ggplot')

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest

df_data = pd.read_csv("~/Documentos/Universidad/Noveno Semestre/Modelos probabilisticos/Teorema-de-Bayes/Datos/comprar_alquilar.csv")
df_data.head()

print(df_data.groupby('comprar').size())

df_data.drop(['comprar'],axis=1).hist()
plt.show()

df_data['gastos']=(df_data['gastos_comunes']+df_data['gastos_otros']+df_data['pago_coche'])
df_data['financiar']=df_data['vivienda']-df_data['ahorros']
df_data.drop(['gastos_comunes','gastos_otros','pago_coche'],axis=1).head(10)

reduced = df_data.drop(['gastos_comunes','gastos_otros','pago_coche'],axis=1)
reduced.describe()
