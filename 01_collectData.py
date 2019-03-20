import matplotlib.pyplot as plt
import pandas_datareader.data as web 

#Collecting Data for Amazon from 17-04-22 to 18-04-22
stock='AAPL'
start='2018-03-19'
end='2019-03-19'

#Instantiating a dataframe (/spreadsheet)
df = web.DataReader(name=stock, data_source='iex', start=start, end=end)

print(df)
df.to_csv("~/Desktop/pynance/{}.csv".format(stock))

#Visualizing collected data with matplotlib
#selecting only 'close'-column
close=df[['close']]
#rename the column with symbol name 
close=close.rename(columns={'close':stock})
#Some naming
ax=close.plot(title=stock)
ax.set_xlabel('date')
ax.set_ylabel('close price')
ax.grid()
plt.show()
