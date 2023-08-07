import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

data_iris = pd.read_csv('data/iris.data', names=['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width','Species'])
#print(data_iris.head)
#data_iris.describe()

#data_segment = pd.read_csv('/content/drive/MyDrive/ThacSi/HienThiDuLieu/data/data/segment.data', names=['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12','G13','G14','G15','G16','G17','G18','G19','G20'])

data_segment = pd.read_csv('data/segment.data',encoding='utf-8', header=None, sep=' ')
#rint(data_segment.head)
#data_segment.describe()

data_sat = pd.read_csv('data/sat.trn',encoding='utf-8', header=None, sep=' ')
print(data_sat.head)
data_sat.describe()