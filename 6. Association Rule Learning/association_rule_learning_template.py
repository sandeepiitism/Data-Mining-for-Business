# -*- coding: utf-8 -*-
"""Association Rule Learning Template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18BFqyritZWVBZfWhZ3KaAzIgkG1qMopZ

#Libraries and data
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Data Mining for Business in Python 2021/6. Association Rule Learning

pip install mlxtend

import pandas as pd
from mlxtend.frequent_patterns import association_rules, apriori

#import the dataset
dataset = pd.read_csv("groceries.csv")
dataset.head()

"""#Preparing Transactions"""

dataset.shape

#transaction list
transactions = []
for i in range (0, 9834):
    transactions.append([str(dataset.values[i,j])
                         for j  in range (0,22)])
transactions

#Encode the transactions
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_transactions = te.fit_transform(transactions)
df = pd.DataFrame(te_transactions,
                  columns = te.columns_)
df.head()

"""# Association Rule Learning"""

#remove nan column
df = df.drop(columns = ("nan"))

#Association Rule LEarning
model = apriori(df, min_support =0.03, use_colnames = True)
results = association_rules(model, 
                            metric = "confidence", 
                            min_threshold = 0.3)
results.sort_values(by='lift', ascending=False)

#visualization
import matplotlib.pyplot as plt
plt.scatter(results['support'], 
            results['confidence'],
            s = 100,
            color = 'red')
plt.xlabel('support')
plt.ylabel('confidence')
plt.title('Support vs Confidence')
for i, label in enumerate(results.index):
    plt.annotate(label, (results['support'][i], 
                         results['confidence'][i]))
plt.show()