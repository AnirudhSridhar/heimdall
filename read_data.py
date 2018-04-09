import pandas as pd
from glob import glob
import os

path = 'data/'
all_files = glob(os.path.join(path, '*.json'))
dfs = (pd.read_json(f) for f in all_files)
df = pd.concat(dfs, ignore_index=True)
print (df)
