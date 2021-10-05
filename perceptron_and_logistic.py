# -*- coding: utf-8 -*-
"""perceptron_and_logistic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UiT3tLXh-S4feiIlQiTUi5odF1TryjXV
"""

import numpy as np
i1 = [0,0,1,1]
i2 = [0,1,0,1]
weight_1 = 3
weight_2 = 5
t = 6
def trash_hold(sum):
  return 1/(1+np.exp(-10*(sum-t)))
sum = []
O1 = []

for x in range(len(i1)):
  sum.append(i1[x]*weight_1 + i2[x]*weight_2)
  if sum[x] > trash_hold(sum[x]):
    O1.append(1)
  else:
    O1.append(0)
print(sum)
print(O1)

import pandas as pd
df = pd.DataFrame(columns = ['i1', 'i2', 'Sum', 'O1'])
df['i1'] = i1
df['i2'] = i2
df['Sum'] = sum
df['O1'] = O1
df

import matplotlib.pyplot as plt
import seaborn as sns
sum.sort()
sns.set()
plt.scatter(sum,O1)
plt.plot(sum,O1,c = 'orange', lw = 3)
plt.xlabel('Sum')
plt.ylabel('f(sum)')
plt.title('Percpetron AND')
plt.show()