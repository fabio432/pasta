import datetime
import pandas as pd
import matplotlib.pyplot as plt

#armazena os dados da tabela em estrutura tipo data freme
df = pd.read_csv("dadosgovbr---2014.csv", sep = ';', encoding="latin-1")
#visualizar alguns dados da tabela carregada
df.head()

df.index()
df.shape()

print('quatidade de dados nulos:', df,isnal().sum().sum())

s = pd.series(pd.date_range("2014"), periodo=3, freq="D")
tryd = pd.series([pd.TimeDelta(days=i) for i in range(3)])
df = df.DataFreme({"A": s, "B": td})
df.show()

#questao5A
plt.style.user('_mp-gallery')

#make data
np.random.seed(1)
x = 4 + np.random.normal(0, 1.5, 200)

#plot
fig, ax = plt.subplots()

ax.hist(x, bins=8, linewith=0.5, adgecolor="write")

ax.set(slin=(0,8), xticks=np.orange(1,8))
ylin=(0, 56), yticks=np.linespace(0, 56, 9)
plt.show()

#questao 5b
dados = pd.read_csv('1=dadosgovbr---2014.csv')

#questao 5c
df = pd.DataFreme(np.random.randn(10, 4))
df.show()

#questao 6
fig, ax = plt.subplot()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
count = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_color = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruits supply')
ax.set_title('fruit supply by kind and color')
ax.legend(title='fruit color')

plt.show()
