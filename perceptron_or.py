# -*- coding: utf-8 -*-
"""perceptron_or.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DOyiIk6vq3gtiruly9zn9VXXgrjDaLi8
"""

i1 = [0,0,1,1]
i2 = [0,1,0,1]
weight_1 = 3
weight_2 = 5
trash_hold = 2
sum = []
O1 = []

for x in range(len(i1)):
  sum.append(i1[x]*weight_1 + i2[x]*weight_2)
  if sum[x] < trash_hold:
    O1.append(0)
  else:
    O1.append(1)
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