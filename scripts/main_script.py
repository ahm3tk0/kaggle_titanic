import pandas as pd

df = pd.read_csv("/Users/fors/Desktop/AFAD Projects/kaggle_titanic/data/train.csv")
df['title'] =df['Name'].str.split(', ').str[1].str.split(' ').str[0].str[:-1]

cabin_pred=[]
df = df.astype(object).where(df.notna(), None)
for index,row in df.iterrows():
    if row['Cabin'] == None:
        df_tmp = df[df['Ticket']==row['Ticket']]
        if df_tmp.Cabin.isnull().sum() != len(df_tmp) and df_tmp.Cabin.isnull().sum() >0:
            df_tmp=df_tmp.loc[df_tmp['Cabin'].notnull()]
            cabin_pred.append({"PassengerId":row["PassengerId"],"cabin_pred":list(df_tmp['Cabin'].unique())[0]})
        else:
            cabin_pred.append({"PassengerId":row["PassengerId"],"cabin_pred":None})
    else:
        cabin_pred.append({"PassengerId":row["PassengerId"],"cabin_pred":row['Cabin']})

df_c = pd.DataFrame(cabin_pred)
df = df.merge(df_c,how='inner',on='PassengerId')