# -*- coding: utf-8 -*-
"""Gaussian Mixture Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TJ-vD9sxiLL_-5bF9WI360IeJoRT9xgE

#Libraries and Data
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Data Mining for Business in Python 2021/4. Clustering - Gaussian Mixture Model

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

#import dataset
data = pd.read_csv("Country-data.csv")
data.head()
dataset = data.iloc[:, 1:]
dataset.head()

"""# Clustering"""

#Optimal Clusters
n_components = np.arange(1, 10)
models = [GaussianMixture(n,
                          random_state = 1502).fit(dataset)
          for n in n_components]

plt.plot(n_components, [m.bic(dataset) for m in models], label='BIC')
plt.plot(n_components, [m.aic(dataset) for m in models], label='AIC')
plt.legend(loc='best')
plt.xlabel('n_components')

#Gaussian Mixture Model
model = GaussianMixture(n_components = 4,
                        random_state=1502).fit(dataset)

"""#Interpretation"""

#Predicting the cluster per country
cluster = pd.Series(model.predict(dataset))
data["cluster"] = cluster
data.head()

data.loc[data['country'] == "Portugal"]

#Prediction the probabilites of each cluster
probabilities = round(pd.DataFrame(model.predict_proba(dataset)),2)
data = pd.concat([data, probabilities], axis = 1)
data.head()

#cluster interpretation
cluster_details = pd.DataFrame(model.means_,
                        columns = list(dataset.columns))
cluster_details