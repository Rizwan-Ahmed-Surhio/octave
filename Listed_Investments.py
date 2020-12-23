#
#### Install Pandas and Pandas Data Reader if required
# Listed Investments Audit Using Python #####
import pandas as pd
import pandas_datareader as wb

## Setting tehg Dates
start = '2020-6-30'
end  = '2020-6-30'

## Materialiy
materiality = abs(1000)

## Load the CSV file and select symbol column for collecting data
list = pd.read_csv('H:/Udemy/Python for Audit/investments/investments_list.csv')
stocks = (list.symbol)

# creating new an empty data frame that will be used to store values
data = pd.DataFrame()

## Collect data from yahoo finance for all symbols and storing values in data
data = round((wb.DataReader(stocks, 'yahoo', start= start, end = end)['Close']).T,3)

## Renaming the index column heading and values

data.index.names = ['symbol']
data = data['2020-06-30']
data = pd.DataFrame({'symbol':data.index, 'AuditPrices':data.values})

# Storing values into the Audit work paper and saving as csv file at same destination
list['AuditPrices'] = data['AuditPrices']
list['PriceDifference'] = round(list['prices'] - list['AuditPrices'],2)
list['AuditBalanceDifference'] = abs(round(list['PriceDifference'] * list['quantity'],2))
list['Material?'] = ["" if x <=  materiality else 'Material' for x in list['AuditBalanceDifference']]

## Save the file in your desired location
list.to_csv('H:/Udemy/Python for Audit/investments/investments_list.csv')
