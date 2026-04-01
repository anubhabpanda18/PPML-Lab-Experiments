import pandas as pd

df1=pd.DataFrame({
    'ID':[1,2,3],
    'NAME':['selena','Annabel','caeso']
})

df2=pd.DataFrame({
    'ID':[2,3,4],
    'AGE':[23,30,34]
})

merged_df=pd.merge(df1,df2,on='ID',how='left')
print(merged_df)