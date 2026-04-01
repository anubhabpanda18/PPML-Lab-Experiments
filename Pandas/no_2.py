import pandas as pd
s=pd.Series(['2023-01-01','not a date','2024-05-10'])
#convert to datetime
dt_s=pd.to_datetime(s,errors='coerce')#invalid values->converted to NaT
#filter valid dates like man or nat
valid_dates=dt_s.dropna()
print(valid_dates)