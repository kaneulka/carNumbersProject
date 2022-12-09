import numpy as np
import pandas as pd
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = pd.read_csv('sortData.csv', encoding = "ISO-8859-1")
#df.set_index('CustomerID', drop=True)
#print(df.head())
#print(df['AverageBuyoutPrice'][0]/df['PurchaseCount'][0])
dfAnilized = pd.DataFrame({'AverageBuyoutPrice': df['AverageBuyoutPrice'],'PurchaseCount': df['PurchaseCount']}, columns=['AverageBuyoutPrice', 'PurchaseCount'])
print(dfAnilized.head())

scaler = MinMaxScaler()
scaler.fit(dfAnilized)
x = scaler.transform(dfAnilized)
pca = PCA(n_components=2)
pca.fit(x)
x_new = pca.transform(x)  

comp1 = x_new[:, 0]
comp2 = x_new[:, 1]
plt.scatter(comp1, comp2)
plt.show()
print(x)