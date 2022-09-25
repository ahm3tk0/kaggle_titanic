import pandas as pd
import numpy as np

train_data = pd.read_csv(r'.\data\train.csv')
train_data = train_data.astype(object).replace(np.nan, None)

train_data['title'] = train_data['Name'].str.split(',').str[1].str.split('.').str[0]

train_data_cabin_none = train_data[train_data['Cabin'].isnull()==True]
train_data_cabin_not_none = train_data[train_data['Cabin'].isnull()==False]

cont_cabin = train_data_cabin_none[train_data_cabin_none['Ticket'].isin(train_data_cabin_not_none['Ticket'].tolist())]
cabin_pred = train_data[train_data['Ticket'].isin(cont_cabin['Ticket'].tolist())]

## Titlelar üzerinden çalışan mı değil mi bul
## Ticketlar ve fiyatlar üzerinden ekik cabinleri belirle
## Sib , parch ve embarked düşün bakem (cabin belirleyebiliriz bunlarla)