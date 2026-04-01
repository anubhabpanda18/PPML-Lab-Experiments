import pandas as pd
#create dictionary
data={
    'A':[1,2,3],
    'B':[4,5,6]
}
df=pd.DataFrame(data)
df_t=df.T
print("Original DataFrame:",df)
print("Transpose Dataframe :",df_t)