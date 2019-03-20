import datetime as dt #for starttimes
import matplotlib.pyplot as plt
from matplotlib import style #for better looking graphs 
import pandas as pd #most popular data analysis library
import pandas_datareader.data as web #for grabbing data from yahoo api
import quandl
style.use('ggplot')

stock = 'GOOG'
start=dt.datetime(2000,1,1)
end= dt.datetime(2018,12,31)
#some typecasting for filename when writing to csv, split returns a list
start_year=str(start).split('-')
end_year=str(end).split('-')

def get_Data(stock, start, end):
        #instantiating dataframe with ticker (stockname) and where we'll get data 
    #you can think of a dataframe as a spreadsheet

    df= web.DataReader([stock], 'yahoo', start, end)
    df=web.get_data_yahoo(stock,start=start,end=end)
    #prints out the first 5 rows of our dataframe by default or more when passed: print(df.head(6))
    print('Got the data of stock '+stock+' for you. Here are the first 5 rows'+df.head())
    return df

def write_csv(stock,start_year, end_year):
          df.to_csv(stock+'_'+start_year[0]+'_to_'+end_year[0]+'.csv')

#datareader puts date as index column. when reading csv files not as default, this solves issue
df=pd.read_csv('GOOG.csv',parse_dates=True, index_col=0)

#Creating a new column for moving averages 
#Moving average: Takes one price and 99 prior day prices creates an average of those so also for
#tomorrow etc
#some kind of smootg out price over time 
#df['100 ma'] = df['Adj Close'].rolling(window=100).mean()




def main():
    #get_Data(stock, start, end)
    #write_csv(start_year,end_year)
    print('All is working')
    
          
          

if __name__ == "__main__":
    main()

