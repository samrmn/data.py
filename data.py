import pandas as pd

data = pd.read_csv('C:\\Users\\Samuel\\Desktop\\zerodata\\houseEnergyConsum_1995to2018(1).csv', sep=',', encoding= 'unicode_escape' , decimal='.')

data =  data.stack().str.replace(',','.').unstack()  #replaces decimalcommas with dots

filter = pd.isnull(data) #finds empty data

print(filter)

data_replace = data.fillna(data.groupby(['1995', '2000','2017','2018'], as_index=False).mean())  #fills up the missing data with the mean of the row

print(data)