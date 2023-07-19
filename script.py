import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = './factory_test_data.csv'
df = pd.read_csv(path)
df = df[(df['Y1']<=1600)]
df = df[~df.astype(str).apply(lambda x: x.str.contains('\[\]').any(), axis=1)]
y1 = pd.to_numeric(df['Y1']).dropna()
y2 = pd.to_numeric(df['Y2'], errors='coerce').dropna()
x5 = pd.to_numeric(df['X5'], errors='coerce').dropna()
x2 = pd.to_numeric(df['X2'], errors='coerce').dropna()
y3 = pd.to_numeric(df['Y3'], errors='coerce').dropna()
y4 = pd.to_numeric(df['Y4'], errors='coerce').dropna()
x3 = pd.to_numeric(df['X3'], errors='coerce').dropna()
x4 = pd.to_numeric(df['X4'], errors='coerce').dropna()
y5 = pd.to_numeric(df['Y5'], errors='coerce').dropna()
xy2 = (y2-x2)
xy3 = (y3-x3)
xy4 = (y4-x4)
xy5 = (y5-x5)

# Line plots of Y variables
plt.plot((y2), label=y2)
plt.plot(x2, label=x2)
plt.plot(y2.mean(), label='mean')
plt.plot(y2.median(), label='median')
plt.plot(y2.mode(), label='mode')
plt.title('2')
plt.legend()
plt.show()

plt.plot((y3),label=y3)
plt.plot(x3, label=x3)
plt.plot(y3.mean(), label='mean')
plt.plot(y3.median(), label='median')
plt.plot(y3.mode(), label='mode')
plt.title('3')
plt.legend()
plt.show()

plt.plot((y4), label=y4)
plt.plot(x4, label=x4)
plt.plot(y4.mean(), label='mean')
plt.plot(y4.median(), label='median')
plt.plot(y4.mode(), label='mode')
plt.title('4')
plt.legend()
plt.show()

plt.plot((y5))
plt.plot(x5, label=x5)
plt.plot(y5.mean(), label='mean')
plt.plot(y5.median(), label='median')
plt.plot(y5.mode(), label='mode')
plt.title('5')
plt.legend()
plt.show()








