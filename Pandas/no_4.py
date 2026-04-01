#convert series to categorical and display
import pandas as pd
s=pd.Series(['apple','banana','apple','orange'])
print(s)
cat_s=s.astype('category')
print(cat_s)