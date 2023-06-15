import pandas as pd
import numpy as np

# dic={"name":['rushabh','sandip','pratik','chirag','jinesh','ravi','dhruv','manoj'],
#      "city":['NaN','bhopal','indor','lakhnau','madhyapardesh','ahmedabad','indor','lakhnau'],
#      "marks":[45,66,32,23,54,31,22,56]}

# print(pd.options.display.max_columns)
# pd.options.display.max_rows=1000
# dic=pd.date_range('20021202',periods=10)
# print(dic)
# df=pd.DataFrame(dic)
# print(df)
# print(df.cummax())
# print(df.corr())
# print(df.dropna(subset=['city']))
# newdf=df.fillna(130)
# print(newdf)
# print(newdf.to_string())
# print(df.info())
# df=pd.DataFrame(np.random.rand(65,12))
# prin+t(df.info())
    

# print(df.to_string())
# print(df.loc[[0,1]])
# s=pd.Series(dic,index=['name'])
# print(s)
# print(df.drop_duplicates(subset=['city'],keep=False))
# print(type(df))
# print(df['city'])
# df['marks'][0]=98
# print(df)
# df.loc[0,'marks']=100
# df.iloc[1,2]=200
# print(df)
# print(df.drop(0z))
# df.iloc[:,[0,1]]='sona'
# print(df.drop(['name'],axis=1))
# print(df.drop(['name','marks'],axis=1))
# df.drop([0],inplace=True)
# print(df)

# df.to_csv('detailes_index_false.csv')
# df.to_csv('detailes_noinex.csv',index=False)
# print(df.head(3))
# print(df.tail(3))
# print(df.describe())
# print(pd.read_csv('detailes_noinex.csv'))
# df.index=['r','u','s','h','a','b','h','k']
# print(df)

# df=pd.DataFrame(np.random.randint(10,size=(5,5)))
# df=pd.DataFrame(np.random.rand(5,5))
# df=pd.DataFrame(np.random.choice(['a',1,'b',2],size=(5,5)))
# print(df)
# print(df.iloc[0,1])
# df.iloc[[0,6],[0,1]]='babbu'
# newdf=df
# print(newdf)
# newdf.iloc[0,0]="khatu"
# print(df)
# print(newdf)
# print(df.tail(6))
# df[0][0]=1
# print(df)
# print(df.index)
# print(df.columns)
# print(df.to_numpy())
# print(type(df))
# se=pd.Series(np.random.rand(10))
# print(se)
# print(se.dtypes)
# print(type(se))