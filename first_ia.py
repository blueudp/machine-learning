import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url, names=['largo sepalo', 'ancho sepalo', 'largo petalo', 'ancho petalo', 'especie'])
features = ['largo sepalo', 'ancho sepalo', 'largo petalo', 'ancho petalo']
print("dataset")
print(df.head())

