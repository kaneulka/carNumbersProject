import pandas as pd

df = pd.read_csv('data.csv', encoding = "ISO-8859-1")
print(df.head())

dfNew = pd.DataFrame([], columns=['CustomerID', 'AverageBuyoutPrice', 'PurchaseCount'])

customerID_dfColumn = df['CustomerID'].tolist()
customerIDList = []
[customerIDList.append(x) for x in customerID_dfColumn if x not in customerIDList]

for i in customerIDList:
    averageBuyoutPrice = 0
    purchaseCount = 0
    tempDF = df.query('CustomerID == @i').sort_values('InvoiceDate', ascending=False)
    if len(tempDF) == 0:
        continue
    for index, row in tempDF.iterrows():
        averageBuyoutPrice += row['Quantity']*row['UnitPrice']
        purchaseCount += row['Quantity']
    #averageBuyoutPrice = averageBuyoutPrice / purchaseCount
    new_row = {'CustomerID': i, 'AverageBuyoutPrice': averageBuyoutPrice, 'PurchaseCount': purchaseCount}
    dfNew.loc[len(dfNew.index)] = new_row

dfNew.head()
dfNew.to_csv('sortData.csv')