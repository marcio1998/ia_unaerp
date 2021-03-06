# -*- coding: utf-8 -*-
"""backpropagtion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mJdvY9Y90x9iPzZULDkPjwbyvpnlfhPC
"""

import pandas as pd
import numpy as np
np.random.seed(1234567)

E1 = [0,0,1,1]
E2 = [0,1,0,1]
saida = [0.0,1.0,1.0,0.0]
tx = 0.0001
erro_inicial = 0.0
I0 = np.zeros(4)
O0 = np.zeros(4)
I1 = np.zeros(4)
O1 = np.zeros(4)
I2 = np.zeros(2)
O2 = np.zeros(2)
w1 = np.random.rand(4,4)
w2 = np.random.rand(4,2)
nw1 = np.zeros((4,4))
nw2 = np.zeros((4,2))
vw1 = np.zeros((4,4))
vw2 = np.zeros((4,2))
d2 = 0.0
d1 = np.zeros(3)

def manipular_peso_trash_hold(matriz):
  if matriz.shape[0] == 2:
    for i in range(matriz.shape[0]):
      for j in range(matriz.shape[1]):
        matriz[i][j] =  (matriz[i][j]*40) -20 
  else:
    for i in range(matriz.shape[0]):
      matriz[i] = (matriz[i]*40)-20

manipular_peso_trash_hold(w1)
manipular_peso_trash_hold(w2)

erro = 1.0
m = 0.0
while erro > tx:
  erro = 0.0
  for x in range(101):
    cs= np.random.randint(3, size=1)
    I0[1] = E1[cs[0]]
    I0[2] = E2[cs[0]]
    I0[3] = 1.0
    O0[1]=I0[1]
    O0[2]=I0[2]
    O0[3]=I0[3]
    I1[1] = O0[1]*w1[1][1]+O0[2]*w1[2][1]+O0[3]*w1[3][1]
    I1[2] = O0[1]*w1[1][2]+O0[2]*w1[2][2]+O0[3]*w1[3][2]
    I1[3] = 1.0
    O1[1]=1.0/(1.0+np.exp(-I1[1]))
    O1[2]=1.0/(1.0+np.exp(-I1[2]))
    O1[3]=I1[3]
    I2[1]=O1[1]*w2[1][1]+O1[2]*w2[2][1]+O1[3]*w2[3][1]
    O2[1]=1.0/(1.0+np.exp(-I2[1]))


    d2=(saida[cs[0]]-O2[1])*O2[1]*(1.0-O2[1])
    d1[1]=O1[1]*(1.0-O1[1])*d2*w2[1][1]
    d1[2]=O1[2]*(1.0-O1[2])*d2*w2[2][1]
    nw2[1][1]= w2[1][1]+0.5*d2*O1[1]+0.5*vw2[1][1]
    vw2[1][1]=nw2[1][1]-w2[1][1]
    w2[1][1]=nw2[1][1]
    nw2[2][1]= w2[2][1]+0.5*d2*O1[2]+0.5*vw2[2][1]
    vw2[2][1]=nw2[2][1]-w2[2][1]
    w2[2][1]=nw2[2][1]
    nw2[3][1]= w2[3][1]+0.5*d2*O1[3]+0.5*vw2[3][1]
    vw2[3][1]=nw2[3][1]-w2[3][1]
    w2[3][1]=nw2[3][1]
    nw1[1][1]= w1[1][1]+0.5*d1[1]*O0[1]+0.5*vw1[1][1]
    vw1[1][1]=nw1[1][1]-w1[1][1]
    w1[1][1]=nw1[1][1]
    nw1[2][1]= w1[2][1]+0.5*d1[1]*O0[2]+0.5*vw1[2][1]
    vw1[2][1]=nw1[2][1]-w1[2][1]
    w1[2][1]=nw1[2][1]
    nw1[3][1]= w1[3][1]+0.5*d1[1]*O0[3]+0.5*vw1[3][1]
    vw1[3][1]=nw1[3][1]-w1[3][1]
    w1[3][1]=nw1[3][1]
    nw1[1][2]= w1[1][2]+0.5*d1[2]*O0[1]+0.5*vw1[1][2]
    vw1[1][2]=nw1[1][2]-w1[1][2]
    w1[1][2]=nw1[1][2]
    nw1[2][2]= w1[2][2]+0.5*d1[2]*O0[2]+0.5*vw1[2][2]
    vw1[2][2]=nw1[2][2]-w1[2][2]
    w1[2][2]=nw1[2][2]
    nw1[3][2]= w1[3][2]+0.5*d1[2]*O0[3]+0.5*vw1[3][2]
    vw1[3][2]=nw1[3][2]-w1[3][2]
    w1[3][2]=nw1[3][2]
    erro+= (saida[cs[0]]-O2[1])*(saida[cs[0]]-O2[1])
  erro = erro/100.0
  m+=1
  print(m,erro)

print(w1)
print(w2)