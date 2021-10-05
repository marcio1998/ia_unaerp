# -*- coding: utf-8 -*-
"""perceptron_xor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JVD0729qKzHyuNvEKdwHsD4MkYWmUGJp
"""

i1 = [0,0,1,1]
i2 = [0,1,0,1]
weight_1 = 5
weight_2 = 6
weight_3 = 9
weight_4 = 3
weight_5 = 4
weight_6 = 2
trash_hold = 10
trash_hold_2 = 2
trash_hold_3 = 1
sum1 = []
sum2 = []
sum3 = []
O1 = [] 
O2 = []
O3 = []

for x in range(len(i1)):
  sum1.append(i1[x]*weight_1 + i2[x]*weight_2)
  if sum1[x] > trash_hold:
    O1.append(1)
  else:
    O1.append(0)
print(sum1)
print(O1)

import pandas as pd
df = pd.DataFrame(columns = ['i1', 'i2', 'Sum1', 'O1'])
df['i1'] = i1
df['i2'] = i2
df['Sum1'] = sum
df['O1'] = O1
df

for x in range(len(i1)):
  sum2.append(i1[x]*weight_3 + i2[x]*weight_4)
  if sum2[x] < trash_hold_2:
    O2.append(1)
  else:
    O2.append(0)
print(sum2)
print(O2)

df['Sum2'] = sum2
df['O2'] = O2
df

for x in range(len(i1)):
  sum3.append(O1[x]*weight_5 + O2[x]*weight_6)
  if sum3[x] < trash_hold_3:
    O3.append(1)
  else:
    O3.append(0)
print(sum3)
print(O3)

df['Sum3'] = sum3
df['O3'] = O3
df

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.scatter(sum3,O3)
plt.plot(sum3,O3,c = 'orange', lw = 3)
plt.xlabel('Sum')
plt.ylabel('f(sum)')
plt.title('Percpetron XOR')
plt.show()