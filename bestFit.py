import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# title = str(input('Enter The Graph Title: '))
y_label = str(input('Enter Name of y-axis: '))
x_label = str(input('Enter Name of x-axis: '))

df = pd.DataFrame()

x = [float(x_val) for x_val in input('Enter x values: ').split()]
y = [float(y_val) for y_val in input('Enter y values: ').split()]

df[x_label] = x
df[y_label] = y

# print(df)

sns.regplot(df[x_label],df[y_label])
plt.show()

a = df.describe()

print(a)