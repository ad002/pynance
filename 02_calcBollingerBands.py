import pandas as pd
import matplotlib.pyplot as plt

stock='AMZN'
period=20 #days

#read in CSV file of previously coll. data, use data as index and read
#close as a column 
df=pd.read_csv('~/Desktop/pynance/{}.csv'.format(stock),index_col='date'
, parse_dates=True,usecols=['date','close'], na_values='nan')#treat not
#existing values as 'nan'

#rename the column header with symbol name 
df = df.rename(columns={'close':stock})
df.dropna(inplace=True)

#calculate Simple Moving Average with 20 days window /perdid variable
sma = df.rolling(window=period).mean()

#calculate standard deviation 
rstd = df.rolling(window=period).std()

#calc and rename 
upper_band= sma + 2 * rstd
upper_band= upper_band.rename(columns={stock:'upperBB'})

lower_band= sma - 2 * rstd
lower_band=lower_band.rename(columns={stock:'lowerBB'})

#Plotting
df= df.join(upper_band).join(lower_band)
ax=df.plot(title='{} Price and BB'.format(stock))
#colouring
ax.fill_between(df.index,lower_band['lowerBB'], 
upper_band['upperBB'], color='#ADCCFF', alpha='0.4')
#labelling axes
ax.set_xlabel('date')
ax.set_ylabel('SMA and BB')
ax.grid()
plt.show()

