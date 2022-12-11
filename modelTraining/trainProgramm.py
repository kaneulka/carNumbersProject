import pandas as pd
import numpy as np

train = pd.read_json('modelTraining/Data/train_json.json', orient='index')
valid = pd.read_json('modelTraining/Data/val_json.json', orient='index')

#df_train = pd.melt(train)

print(train.head())
print(valid.head())