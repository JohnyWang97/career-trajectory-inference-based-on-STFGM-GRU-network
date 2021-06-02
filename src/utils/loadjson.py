from pandas.io.json import json_normalize
import pandas as pd
import json

data_str = open('/Users/wangjunren/Downloads/prediction_api/src/utils/top_10000_trajectories.json').read()
df = pd.read_json(data_str,orient = 'records')
df.head()